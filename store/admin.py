from django.contrib import admin
from .models import Product, Customer, Cart, CartItem

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartItem)