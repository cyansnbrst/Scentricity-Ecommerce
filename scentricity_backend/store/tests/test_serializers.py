from django.test import TestCase
from store.models import Brand, Category
from store.serializers import ProductSerializer, CategorySerializer, BrandSerializer
from tests.utils import ProductTestDataMixin


class ProductSerializerTestCase(TestCase, ProductTestDataMixin):
    def setUp(self):
        self.product1, self.product2, self.product3, self.product4 = self.create_test_data()

    def test_product_serializer(self):
        serializer = ProductSerializer([self.product1, self.product2, self.product3, self.product4], many=True)
        serialized_data = serializer.data
        expected_data = [
            {
                'id': self.product1.id,
                'name': 'Perfume 1',
                'category': {'id': self.product1.category.id, 'name': self.product1.category.name},
                'brand': {'id': self.product1.brand.id, 'name': self.product1.brand.name},
                'price': '50.00',
                'quantity': 50,
                'properties': [],
                'image': '/media/None.jpeg'
            },
            {
                'id': self.product2.id,
                'name': 'Perfume 2',
                'category': {'id': self.product2.category.id, 'name': self.product2.category.name},
                'brand': {'id': self.product2.brand.id, 'name': self.product2.brand.name},
                'price': '45.00',
                'quantity': 40,
                'properties': [],
                'image': '/media/None.jpeg'
            },
            {
                'id': self.product3.id,
                'name': 'Candle 1',
                'category': {'id': self.product3.category.id, 'name': self.product3.category.name},
                'brand': {'id': self.product3.brand.id, 'name': self.product3.brand.name},
                'price': '50.00',
                'quantity': 60,
                'properties': [],
                'image': '/media/None.jpeg'
            },
            {
                'id': self.product4.id,
                'name': 'Candle 2',
                'category': {'id': self.product4.category.id, 'name': self.product4.category.name},
                'brand': {'id': self.product4.brand.id, 'name': self.product4.brand.name},
                'price': '55.00',
                'quantity': 30,
                'properties': [],
                'image': '/media/None.jpeg'
            }
        ]

        self.assertEqual(serialized_data, expected_data)


class CategorySerializerTestCase(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name='Perfumes')
        self.category2 = Category.objects.create(name='Candles')

    def test_category_serializer(self):
        serializer = CategorySerializer([self.category1, self.category2], many=True)
        serialized_data = serializer.data

        expected_data = [
            {
                'id': self.category1.id,
                'name': 'Perfumes'
            },
            {
                'id': self.category2.id,
                'name': 'Candles'
            }
        ]

        self.assertEqual(serialized_data, expected_data)


class BrandSerializerTestCase(TestCase):
    def setUp(self):
        self.brand1 = Brand.objects.create(name='Brand A')
        self.brand2 = Brand.objects.create(name='Brand B')

    def test_brand_serializer(self):
        serializer = BrandSerializer([self.brand1, self.brand2], many=True)
        serialized_data = serializer.data

        expected_data = [
            {
                'id': self.brand1.id,
                'name': 'Brand A'
            },
            {
                'id': self.brand2.id,
                'name': 'Brand B'
            }
        ]

        self.assertEqual(serialized_data, expected_data)
