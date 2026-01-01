from rest_framework import serializers
from decimal import Decimal
from .models import Product,Collection

class CollectionSerializer(serializers.Serializer):
    class Meta:
        model = Collection
        fields = ['id','title']

class ProductSerializer(serializers.ModelSerializer):
  
    price_with_tax = serializers.SerializerMethodField()
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name="collection-details"
    )

    class Meta:
        model = Product
        # Field names must match your model
        fields = ['id', 'title', 'description', 'slug', 'unit_price', 'inventory', 'last_update', 'collection', 'price_with_tax']

    def get_price_with_tax(self, product):
        return product.unit_price * Decimal(1.1)
