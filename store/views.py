from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count,Max,Min
from django.db.models import Q, F
from .models import Product, Collection
from .serializers import ProductSerializer,CollectionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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
        
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_serializer_context(self):
        return {'request':self.request}

    def delete(self,request,id):
        collection = get_object_or_404(Collection,pk=id)
        if collection.orderitems.count() > 0:
            return Response({'error':'collection cant delete'})
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





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
