from rest_framework import serializers
from myapi.models import Products

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Products
        field = [
            'name',
            'price',
            'description',
            'category',
            'image'
        ]