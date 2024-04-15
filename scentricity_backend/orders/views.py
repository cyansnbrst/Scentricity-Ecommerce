import stripe
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings

from cart.models import Cart
from orders.models import Order
from orders.serializers import OrderSerializer


class OrderAPIView(APIView):
    """
    A view to retrieve orders for the current user.

    * Requires authentication.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Retrieves orders for the current user.

        Returns:
            Response: Serialized order data with appropriate status.
        """
        try:
            user_id = self.request.user.id
            user_orders = Order.objects.filter(user=user_id)
            serializer = OrderSerializer(user_orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({"error": "No orders found for this user"}, status=status.HTTP_404_NOT_FOUND)


class StripeWebhookHandler(APIView):
    """
    A view to handle Stripe webhook events.
    """

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        """
        Dispatch method for the view.

        Ensures the view is exempt from CSRF validation.
        """
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        """
        Handle POST requests from Stripe webhook.

        Returns:
            Response: Success response if the event is handled successfully.
        """
        try:
            sig_header = request.headers.get('Stripe-Signature')
            payload = request.body
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_ENDPOINT_SECRET
            )
        except (ValueError, stripe.error.SignatureVerificationError) as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            metadata = session['metadata']

            user_id = metadata.get('user_id')
            total = session['amount_total']
            try:
                Order.objects.create(user_id=user_id, total=total)
                Cart.objects.get(user=user_id).delete()
            except Cart.DoesNotExist:
                pass

            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_200_OK)
