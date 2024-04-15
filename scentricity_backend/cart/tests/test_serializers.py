from django.contrib.auth.models import User
from django.test import TestCase
from cart.models import Cart, CartItem, Product
from cart.serializers import CartItemSerializer, CartSerializer


class CartItemSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.product = Product.objects.create(name='Test Product', price=10.00, quantity=20)
        self.cart_item = CartItem.objects.create(product=self.product, quantity=2)

    def test_cart_item_serializer(self):
        serializer = CartItemSerializer(self.cart_item)
        serialized_data = serializer.data

        expected_data = {
            'product': self.product.id,
            'quantity': 2,
            'subtotal': '20.00'
        }

        self.assertEqual(serialized_data, expected_data)


class CartSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.product = Product.objects.create(name='Test Product', price=10.00, quantity=20)
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=2)

    def test_cart_serializer(self):
        serializer = CartSerializer(self.cart)
        serialized_data = serializer.data

        expected_data = {
            'user': self.user.id,
            'total_price': '20.00',
            'items': [
                {
                    'product': self.product.id,
                    'quantity': 2,
                    'subtotal': '20.00'
                }
            ]
        }

        self.assertEqual(serialized_data, expected_data)
