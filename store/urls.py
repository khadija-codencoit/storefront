from django.urls import path
from .views import ProductList, ProductDetail, CollectionDetail

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('products/<int:id>/', ProductDetail.as_view()),
    
    path('collections/<int:pk>/', CollectionDetail.as_view(), name='collection-details'),
]
