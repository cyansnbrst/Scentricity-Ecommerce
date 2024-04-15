from django.contrib.auth.models import User
from django.db import models
from store.models import Product


class Order(models.Model):
    """
    Represents an order placed by a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"Order №{self.id}"

    def save(self, *args, **kwargs):
        """
        Overrides the save method to convert total amount from cents to dollars before saving.
        """
        if self.total != 0:
            self.total /= 100
        super().save(*args, **kwargs)
