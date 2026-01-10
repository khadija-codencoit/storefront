from django.urls import path
from .views import  ProductViewSet,CollectionViewSet,ReviewViewSet,CartViewSet

from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('products',ProductViewSet,basename = 'product-list')
router.register('collections',CollectionViewSet)
router.register('carts',CartViewSet,basename='cart-list')

product_router = routers.NestedDefaultRouter(router,'products', lookup = 'product')
product_router.register('reviews',ReviewViewSet, basename = 'product-reviews')

urlpatterns = router.urls + product_router.urls

# urlpatterns = [
#     path('products/', ProductViewSet.as_view()),
#     path('collections/', CollectionList.as_view()),
#     # path('products/<int:pk>/', ProductDetail.as_view()),
    
#     path('collections/<int:pk>/', CollectionDetail.as_view(), name='collection-details'),
# ]
