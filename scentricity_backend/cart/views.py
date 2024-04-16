from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from cart.models import Cart, CartItem
from cart.permissions import CartPermission, CartItemPermission
from cart.serializers import CartSerializer, CartItemSerializer
from store.models import Product


class CartAPIView(APIView):
    """
    A view to display the current user's cart.

    * Requires authentication.
    """
    permission_classes = [IsAuthenticated, CartPermission]

    def get(self, request):
        """
        Retrieve the current user's cart.

        Returns:
            Response: Serialized cart data with appropriate status.
        """
        try:
            user = self.request.user
            user_cart, created = Cart.objects.get_or_create(user=user)
            response_status = status.HTTP_200_OK if not created else status.HTTP_201_CREATED
            return Response(CartSerializer(user_cart).data, status=response_status)
        except Cart.DoesNotExist:
            return Response({"error": "Cart does not exist"}, status=status.HTTP_404_NOT_FOUND)


class CartItemAPIView(APIView):
    """
    A view to add, delete, or modify items in the cart.

    * Handles operations such as adding or deleting items from the cart.
    """
    permission_classes = [IsAuthenticated, CartItemPermission]

    @staticmethod
    def handle_resource_not_found():
        """
        Handle cases when requested resources are not found.

        Returns:
            Response: Error response with appropriate status.
        """
        return Response({"error": "Resource does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, action, product_id):
        """
        Add or delete items from the cart.

        Args:
            request: HTTP request object.
            action (str): Action to perform ('add' or 'delete').
            product_id (int): ID of the product to add or delete.

        Returns:
            Response: Serialized cart item data with appropriate status.
        """
        try:
            if action not in ["add", "delete"]:
                return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)

            user = request.user
            user_cart, _ = Cart.objects.get_or_create(user=user)
            product = Product.active.get(id=product_id)
            item_in_cart, item_created = CartItem.objects.get_or_create(cart=user_cart, product=product)

            if not item_created:
                if action == "add":
                    item_in_cart.quantity += 1
                elif action == "delete":
                    if item_in_cart.quantity - 1 > 0:
                        item_in_cart.quantity -= 1

            try:
                item_in_cart.save()
                serialized_item = CartItemSerializer(item_in_cart)
                return Response(serialized_item.data, status=status.HTTP_200_OK)
            except IntegrityError:
                return Response({"error": "Failed to save cart item"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except (Product.DoesNotExist, Cart.DoesNotExist, CartItem.DoesNotExist):
            return self.handle_resource_not_found()

    def delete(self, request, product_id):
        """
        Delete an item from the cart.

        Args:
            request: HTTP request object.
            product_id (int): ID of the product to delete from the cart.

        Returns:
            Response: Success response with appropriate status or error response if the item is not found.
        """
        try:
            user_id = self.request.user.id
            user_cart = Cart.objects.get(user=user_id)
            product = Product.objects.get(id=product_id)
            try:
                item_in_cart = CartItem.objects.get(cart=user_cart, product=product)
                item_in_cart.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except CartItem.DoesNotExist:
                return Response({"error": "Item does not exist in cart"}, status=status.HTTP_404_NOT_FOUND)
        except (Cart.DoesNotExist, Product.DoesNotExist):
            return self.handle_resource_not_found()
