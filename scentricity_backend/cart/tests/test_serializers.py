from django.test import TestCase
from cart.serializers import CartSerializer, CartItemSerializer
from tests.utils import CartTestDataMixin


class CartSerializerTestCase(TestCase, CartTestDataMixin):
    def setUp(self):
        self.user, self.cart, \
            self.cart_item1, self.cart_item2, self.cart_item3, self.cart_item4 = self.create_cart_test_data()

    def test_cart_serializer(self):
        serializer = CartSerializer(instance=self.cart)
        serialized_data = serializer.data

        expected_total_price = self.cart.total_price()

        expected_data = {
            'user': self.user.id,
            'total_price': expected_total_price,
            'items': [
                {
                    'product': self.cart_item4.product.id,
                    'quantity': self.cart_item4.quantity,
                    'subtotal': self.cart_item4.subtotal()
                },
                {
                    'product': self.cart_item3.product.id,
                    'quantity': self.cart_item3.quantity,
                    'subtotal': self.cart_item3.subtotal()
                },
                {
                    'product': self.cart_item2.product.id,
                    'quantity': self.cart_item2.quantity,
                    'subtotal': self.cart_item2.subtotal()
                },
                {
                    'product': self.cart_item1.product.id,
                    'quantity': self.cart_item1.quantity,
                    'subtotal': self.cart_item1.subtotal()
                }
            ]
        }

        self.assertEqual(serialized_data, expected_data)


class CartItemSerializerTestCase(TestCase, CartTestDataMixin):
    def setUp(self):
        self.user, self.cart, \
            self.cart_item1, self.cart_item2, self.cart_item3, self.cart_item4 = self.create_cart_test_data()

    def test_cart_item_serializer(self):
        serializer = CartItemSerializer(instance=self.cart_item1)
        serialized_data = serializer.data

        expected_data = {
            'product': self.cart_item1.product.id,
            'quantity': self.cart_item1.quantity,
            'subtotal': self.cart_item1.subtotal()
        }

        self.assertEqual(serialized_data, expected_data)
