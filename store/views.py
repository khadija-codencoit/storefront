from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count,Max,Min
from django.db.models import Q, F
from .models import Product, Collection
from .serializers import ProductSerializer,CollectionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status


class CollectionDetail(APIView):
    def get(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        serializer = CollectionSerializer(collection, context={'request': request})
        return Response(serializer.data)

class ProductList(APIView):
    def get(self, request):
        if request.method == 'GET':
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many = True, context = {'request':request})
            return Response(serializer.data)
    
    def post(self,request):
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class ProductDetail(APIView):
    def get(self,request,id):
        product = get_object_or_404(Product,pk=id)
        serializer = ProductSerializer(product,context={'request': request})
        return Response(serializer.data)
   
    def put(self,request,id):
        product = get_object_or_404(Product,pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,id):
        product = get_object_or_404(Product,pk=id)
        if product.orderitems.count() > 0:
            return Response({'error':'Product cant delete'})
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
