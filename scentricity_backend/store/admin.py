from django.contrib import admin
from django.core.exceptions import ValidationError

from .models import Category, Brand, Property, Product, ProductProperty


class ProductPropertyInline(admin.TabularInline):
    model = ProductProperty
    readonly_fields = ['value_as_type']
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'property_type')
    verbose_name_plural = "Properties"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'quantity', 'category', 'get_is_active')

    def get_is_active(self, obj):
        return obj.is_active

    get_is_active.short_description = 'Active'

    inlines = [
        ProductPropertyInline,
    ]

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValidationError as e:
            print("error")
            error_message = ', '.join(e.messages)
            self.message_user(request, f"Validation Error: {error_message}", level='ERROR')

        obj.save()
