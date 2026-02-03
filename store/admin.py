from django.contrib import admin
from .models import Product, Customer, Cart, CartItem,Collection

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Collection)
