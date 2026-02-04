from rest_framework import serializers
from decimal import Decimal
from .models import Product,Collection,Review,Cart,CartItem,Customer,ProductImage

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'images']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return ProductImage.objects.create(product_id=product_id, **validated_data)

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True,read_only = True)
    price_with_tax = serializers.SerializerMethodField()
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name='collection-detail'
    )
    class Meta:
        model = Product
        # Field names must match your model
        fields = ['id', 'title', 'description', 'slug', 'unit_price', 'inventory',
         'last_update', 'collection', 'price_with_tax','images']

    def get_price_with_tax(self, product):
        return product.unit_price * Decimal(1.1)
    

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','unit_price']

class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    class Meta:
        model = CartItem
        fields = ['id','product','quantity']

class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    item = CartItemSerializer(many=True, required=False)

    class Meta:
        model = Cart
        fields = ['id', 'item']

    def create(self, validated_data):
        items_data = validated_data.pop('item', [])
        cart = Cart.objects.create(**validated_data)
        for item_data in items_data:
            CartItem.objects.create(cart=cart, **item_data)
        return cart


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'created_at']
    
    def create(self,validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id = product_id, **validated_data)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','email','phone']