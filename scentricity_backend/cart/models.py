from django.contrib.auth.models import User
from django.db import models

from store.models import Product


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def total_price(self):
        """
        Calculates the total price of the entire cart.

        Returns:
            float: The total price of the cart.
        """
        total = 0
        for item in self.items.all():
            total += item.quantity * item.product.price
        return total

    def get_items(self):
        """
        Retrieves all items in the cart.

        Returns:
            QuerySet: A queryset containing all items in the cart.
        """
        return self.items.all()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        """
        Calculates the subtotal price of items of one type in the cart.

        Returns:
            float: The subtotal price of the item type.
        """
        return self.quantity * self.product.price

    class Meta:
        ordering = ['-added']

    def __str__(self):
        """
        Returns a string representation of the CartItem.

        Returns:
            str: A string representation of the CartItem.
        """
        return f"{self.quantity} {self.product.name} in cart №{self.cart.id}"
