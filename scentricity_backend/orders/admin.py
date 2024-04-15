from django.contrib import admin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_order_id', 'user', 'total', 'created')

    def get_order_id(self, obj):
        return str(obj)

    get_order_id.short_description = 'ID'
