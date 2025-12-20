from decimal import Decimal
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    price_tax = serializers.SerializerMethodField()

    def get_price_tax(self, product):
        return product.price * Decimal('0.10')