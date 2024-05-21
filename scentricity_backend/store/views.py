from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ReadOnlyModelViewSet

from store.models import Product
from store.serializers import ProductSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    """
    A viewset for viewing products. Read-only.
    Modifying products is restricted and can only be performed via the Django administration interface.
    """
    queryset = Product.active.all()
    serializer_class = ProductSerializer

    # Define filter backends
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]
    filterset_fields = ['brand', 'category']

    # Define permissions
    permission_classes = [IsAuthenticatedOrReadOnly]
