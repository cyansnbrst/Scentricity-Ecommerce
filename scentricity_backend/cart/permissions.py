from rest_framework.permissions import BasePermission, SAFE_METHODS


class CartPermission(BasePermission):
    def has_object_permission (self, request, view, obj):
        return bool(
            obj.user == request.user
        )

class CartItemPermission(BasePermission):
    def has_object_permission (self, request, view, obj):
        return bool(
            obj.cart.user == request.user
        )