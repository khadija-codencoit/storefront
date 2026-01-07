from rest_framework import serializers
from decimal import Decimal
from .models import Product,Collection,Review,Cart

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title']

class ProductSerializer(serializers.ModelSerializer):
  
    price_with_tax = serializers.SerializerMethodField()
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name='collection-detail'
    )
    class Meta:
        model = Product
        # Field names must match your model
        fields = ['id', 'title', 'description', 'slug', 'unit_price', 'inventory', 'last_update', 'collection', 'price_with_tax']

    def get_price_with_tax(self, product):
        return product.unit_price * Decimal(1.1)

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'created_at']
    
    def create(self,validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id = product_id, **validated_data)
        