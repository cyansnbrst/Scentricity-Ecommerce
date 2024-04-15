from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from store.views import ProductViewSet

router = SimpleRouter()
router.register(r'products', ProductViewSet)

base_api_url = 'api/v1/'
urlpatterns = [
    path('admin/', admin.site.urls),

    # Djoser auth urls
    path(base_api_url + 'auth/', include('djoser.urls')),
    path(base_api_url + 'auth/', include('djoser.urls.authtoken')),

    # Business urls
    path(base_api_url + 'cart/', include('cart.urls')),
    path(base_api_url + 'payment/', include('payments.urls')),
    path(base_api_url + 'order/', include('orders.urls')),
    path(base_api_url, include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
