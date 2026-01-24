from django.urls import path
from .views import  ProductViewSet,CollectionViewSet,ReviewViewSet,CartViewSet,CartItemViewSet,CustomerViewSet,ProductImageViewSet

from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='product-list')
router.register('collections', CollectionViewSet)
router.register('carts', CartViewSet, basename='cart-list')
router.register('customer', CustomerViewSet)

# Nested product reviews
product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='product-reviews')
product_router.register('images',ProductImageViewSet,basename='product-images')

# Nested cart items
carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart_pk')
carts_router.register('items', CartItemViewSet, basename='cart-item-list')

urlpatterns = router.urls + product_router.urls + carts_router.urls

# urlpatterns = [
#     path('products/', ProductViewSet.as_view()),
#     path('collections/', CollectionList.as_view()),
#     # path('products/<int:pk>/', ProductDetail.as_view()),
    
#     path('collections/<int:pk>/', CollectionDetail.as_view(), name='collection-details'),
# ]
