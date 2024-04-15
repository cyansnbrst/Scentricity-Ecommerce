from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from store.serializers import ProductSerializer
from tests.utils import ProductTestDataMixin


class ProductApiTestCase(APITestCase, ProductTestDataMixin):
    def setUp(self):
        self.product1, self.product2, self.product3, self.product4 = self.create_test_data()

    def test_get_products(self):
        url = reverse('product-list')
        response = self.client.get(url)

        serializer_context = {'request': response.wsgi_request}
        serializer = ProductSerializer([self.product1, self.product2, self.product3, self.product4], many=True,
                                       context=serializer_context)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


    def test_get_single_product(self):
        product_url = reverse('product-detail', args=[self.product1.pk])
        response = self.client.get(product_url)

        serializer_context = {'request': response.wsgi_request}
        serializer = ProductSerializer(self.product1, context=serializer_context)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
