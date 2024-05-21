from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
import stripe
from cart.models import Cart


class CreateCheckoutSession(APIView):
    """
    A view for creating a checkout session for the current user.

    * Requires authentication.
    """
    permission_classes = [IsAuthenticated]
    FRONTEND_DOMAIN = "http://176.109.99.199:8080:8080/#/checkout"

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        """
        Dispatch method for the view.

        Ensures the view is exempt from CSRF validation.
        """
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        """
        Handle POST requests.

        Creates a checkout session for the current user.

        Args:
            request (HttpRequest): The request object.

        Returns:
            Response: The response object containing the checkout session URL or error message.
        """
        try:
            user_id = self.request.user.id
            metadata = {'user_id': user_id}

            user_cart = Cart.objects.get(user=user_id)
            items = user_cart.get_items()

            line_items = []
            for item in items:
                line_items.append({
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(item.product.price * 100),
                        'product_data': {
                            'name': item.product.name,
                        },
                    },
                    'quantity': item.quantity,
                })

            stripe.api_key = settings.STRIPE_SECRET_KEY
            checkout_session = stripe.checkout.Session.create(
                line_items=line_items,
                mode='payment',
                success_url=self.FRONTEND_DOMAIN + '?success=true',
                cancel_url=self.FRONTEND_DOMAIN + '?canceled=true',
                metadata=metadata,
            )

            return Response({"url": checkout_session.url})

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
