from django.urls import path

from cart.views import CartAPIView, CartItemAPIView

urlpatterns = [
    path('', CartAPIView.as_view()),
    path('change/<str:action>/<int:product_id>/', CartItemAPIView.as_view()),
    path('delete/<int:product_id>/', CartItemAPIView.as_view())
]
