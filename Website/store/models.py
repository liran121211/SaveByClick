from django.db import models
from django.contrib.auth.admin import User
from datetime import timezone
import random
# Create your models here.

class Buyer(models.Model):
    user = models.ForeignKey(User, name = "User", on_delete=models.CASCADE)
    name = models.CharField(name = 'name', max_length=50)
    permissionLevel = models.IntegerField(name= "permission_Level", default = 4)

    def __str__(self):
        return self.name


class Seller(models.Model):
    user = models.ForeignKey(User, name = "User", on_delete=models.CASCADE)
    name = models.CharField(name='name', max_length=50)
    permissionLevel = models.IntegerField(name= "permission_Level", default = 4)

    def __str__(self):
        return self.name

class Products(models.Model):
    id = models.CharField(name='id', primary_key = True,default=random.randint(1000,99999), max_length=10)
    seller = models.ForeignKey(Seller, name = "Seller", on_delete=models.CASCADE)
    product_name = models.CharField(name='product_name', max_length=200)
    product_description = models.CharField(name='product_description', max_length=500)
    price = models.FloatField(name='price', max_length=10, default=0)
    quantity = models.IntegerField(name='quantity', default=0)
    rating = models.IntegerField(name='rating', default=0)
    def __str__(self):
        return self.product_name
