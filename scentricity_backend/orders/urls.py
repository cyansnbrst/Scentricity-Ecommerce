from django.urls import path

from orders.views import StripeWebhookHandler, OrderAPIView

urlpatterns = [
    path('order_info_stripe_webhook/', StripeWebhookHandler.as_view()),
    path('my_orders/', OrderAPIView.as_view()),
]