from django.db import models

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
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
