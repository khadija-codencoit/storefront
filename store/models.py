from django.db import models
from uuid import uuid4

# Create your models here.


class Promotion(models.Model):
    description = models.TextField()
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    class Meta():
        ordering = ['title']



class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True,null=True, )
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True)
    promotions = models.ManyToManyField(Promotion, blank=True)

    def __str__(self):
        return self.title
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='store/images')

class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
   

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Use DateTimeField instead of DateField for timestamps

    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = [['cart','product']]