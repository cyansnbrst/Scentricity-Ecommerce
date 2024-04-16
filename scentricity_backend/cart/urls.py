from django.urls import path

from cart.views import CartAPIView, CartItemAPIView

urlpatterns = [
    path('', CartAPIView.as_view(), name='cart'),
    path('change/<str:action>/<int:product_id>/', CartItemAPIView.as_view(), name='cart-action'),
    path('delete/<int:product_id>/', CartItemAPIView.as_view(), name='cart-item-delete')
]
