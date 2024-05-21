from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from cart.models import Cart, CartItem
from cart.serializers import CartSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from tests.utils import ProductTestDataMixin


class CartAPITestCase(APITestCase, ProductTestDataMixin):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.product1, *_ = self.create_test_data()

    def test_get_cart(self):
        url = reverse('cart')
        print(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_item_to_cart(self):
        url = reverse('cart-action', args=['add', self.product1.id])
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quantity'], 1)

        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quantity'], 2)

        cart = Cart.objects.get(user=self.user)
        cart_item = CartItem.objects.get(cart=cart, product=self.product1)
        self.assertEqual(cart_item.quantity, 2)

    def test_delete_item_from_cart(self):
        cart = Cart.objects.create(user=self.user)
        cart_item = CartItem.objects.create(cart=cart, product=self.product1)

        url = reverse('cart-item-delete', args=[self.product1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(CartItem.DoesNotExist):
            CartItem.objects.get(cart=cart, product=self.product1)
