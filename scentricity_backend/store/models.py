from django.core.validators import MinValueValidator
from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    """
    Represents a product category.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Brand(models.Model):
    """
    Represents a product brand.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Property(models.Model):
    """
    Represents a product property.
    """
    name = models.CharField(max_length=255)
    STRING = 'string'
    INTEGER = 'integer'
    BOOLEAN = 'bool'
    PROPERTY_TYPES = [
        (STRING, 'String'),
        (INTEGER, 'Integer'),
        (BOOLEAN, 'Boolean'),
    ]
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES, default=STRING)

    def __str__(self):
        return self.name


class ActiveManager(models.Manager):
    """
    Manager for active products.
    """

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Product(models.Model):
    """
    Represents a product.
    """
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2,
                                validators=[
                                    MinValueValidator(0)
                                ])
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="products/", default="None")
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    active = ActiveManager()

    class Meta:
        ordering = ['-created']

    # def clean(self):
    #     """
    #     Validates the product instance.
    #     """
    #     if self.quantity < 0:
    #         raise ValidationError("Quantity cannot be negative.")
    #     if self.price < 0:
    #         raise ValidationError("Price cannot be negative.")

    def save(self, *args, **kwargs):
        if self.quantity == 0:
            self.is_active = False
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} by {self.brand}"


class ProductProperty(models.Model):
    """
    Represents a property of a product.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="properties")
    property_name = models.ForeignKey(Property, on_delete=models.CASCADE)
    value = models.CharField(null=True, blank=True)

    @property
    def value_as_type(self):
        """
        Converts property value to appropriate type.
        """
        property_type = self.property_name.property_type
        type_converters = {
            Property.STRING: str,
            Property.INTEGER: int,
            Property.BOOLEAN: bool,
        }
        converter = type_converters.get(property_type)
        return converter(self.value)

    def __str__(self):
        return f"{self.product.name} - {self.property_name.name}: {self.value_as_type}"
