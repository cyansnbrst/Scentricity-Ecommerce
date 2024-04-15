from rest_framework import serializers
from .models import ProductProperty, Product, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class ProductPropertySerializer(serializers.ModelSerializer):
    property_name = serializers.StringRelatedField()

    class Meta:
        model = ProductProperty
        fields = ['property_name', 'value_as_type']


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    properties = ProductPropertySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'brand', 'price', 'quantity', 'properties', 'image']

