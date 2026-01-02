from django.urls import path
from .views import  CollectionDetail,CollectionList,ProductViewSet

urlpatterns = [
    path('products/', ProductViewSet.as_view()),
    path('collections/', CollectionList.as_view()),
    # path('products/<int:pk>/', ProductDetail.as_view()),
    
    path('collections/<int:pk>/', CollectionDetail.as_view(), name='collection-details'),
]
