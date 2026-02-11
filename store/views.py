from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count,Max,Min
from django.db.models import Q, F
from .models import Product, Collection,Review,Cart,Customer,ProductImage
from .permission import *
from .serializers import ProductSerializer,CollectionSerializer,ReviewSerializer,CartSerializer,CartItemSerializer,CustomerSerializer,ProductImageSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from .pagination import *
from .filters import ProductFilter



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['title', 'description']
    ordering_fields = ['unit_price']
    permission_classes = [IsAdminOrReadOnly]

   

    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     collection_id = self.request.query_params.get('collection_id')

    #     if collection_id is not None:
    #         queryset = queryset.filter(collection_id = collection_id)
    #     return queryset


    def get_serializer_context(self):
        return {'request':self.request}

    
    def destroy(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)

        if product.orderitems.count() > 0:
            return Response(
                {'error': 'Product can’t be deleted'},
                status=status.HTTP_400_BAD_REQUEST
            )

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        product_id = self.kwargs.get("product_pk")
        return ProductImage.objects.filter(product_id=product_id)

    def get_serializer_context(self):
        return {'product_id': self.kwargs.get("product_pk")}




class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id= self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}



class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated]


    def get_serializer_context(self):
        return {'request':self.request}

    def delete(self,request,id):
        collection = get_object_or_404(Collection,pk=id)
        if collection.orderitems.count() > 0:
            return Response({'error':'collection cant delete'})
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin,GenericViewSet):
    queryset = Cart.objects.all().prefetch_related('item')
    serializer_class = CartSerializer

class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        cart_id = self.kwargs.get('cart_pk')  
        return CartItem.objects.filter(cart_id=cart_id)


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class =  CustomerSerializer

# ==========Generic APIView===============


# class ProductList(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def get_serializer_context(self):
#         return {'request':self.request}
    
#     def delete(self,request,id):
#         product = get_object_or_404(Product,pk=id)
#         if product.orderitems.count() > 0:
#             return Response({'error':'Product cant delete'})
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ProductDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
#     def delete(self,request,id):
#         product = get_object_or_404(Product,pk=id)
#         if product.orderitems.count() > 0:
#             return Response({'error':'Product cant delete'})
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CollectionList(ListCreateAPIView):
#     queryset = Collection.objects.all()
#     serializer_class = CollectionSerializer

#     def get_serializer_context(self):
#         return {'request':self.request}





# ==============APIView===============

# class ProductList(APIView):
#     def get(self, request):
#         if request.method == 'GET':
#             queryset = Product.objects.all()
#             serializer = ProductSerializer(queryset, many = True, context = {'request':request})
#             return Response(serializer.data)
    
#     def post(self,request):
#         serializer = ProductSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
# class ProductDetail(APIView):
#     def get(self,request,id):
#         product = get_object_or_404(Product,pk=id)
#         serializer = ProductSerializer(product,context={'request': request})
#         return Response(serializer.data)
   
#     def put(self,request,id):
#         product = get_object_or_404(Product,pk=id)
#         serializer = ProductSerializer(product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self,request,id):
#         product = get_object_or_404(Product,pk=id)
#         if product.orderitems.count() > 0:
#             return Response({'error':'Product cant delete'})
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
