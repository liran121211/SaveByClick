from django.db import models
from django.contrib.auth.admin import User
from datetime import timezone
import random
from django_countries.fields import CountryField
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

class lastLogin(models.Model):
    user = models.ForeignKey(User, name="User", on_delete=models.CASCADE)
    time = models.DateTimeField(name = 'time', auto_now_add=True, blank=True)
    logout = models.BooleanField(name='logout', default = False)
    ip = models.CharField(name= 'ip', max_length=20, default='null')



class Buyer(models.Model):
    user = models.OneToOneField(User, name = "User", on_delete=models.CASCADE)
    name = models.CharField(name = 'name', max_length=50)
    permissionLevel = models.IntegerField(name= "permission_Level", default = 4)

    def __str__(self):
        return self.name

class shippingAdd(models.Model):
    id = models.ForeignKey(User, name='shipping', on_delete=models.CASCADE)
    address = models.CharField(name= 'address', max_length=200)
    city = models.CharField(name='city', max_length=100)
    zipcode = models.CharField(name='zipcode', max_length=7)
    country= CountryField()
    phone = models.CharField(name='phone', max_length=10)

    def __str__(self):
        return self.address

class Seller(models.Model):
    user = models.OneToOneField(User, name = "User", on_delete=models.CASCADE)
    name = models.CharField(name='name', max_length=50)
    store_name = models.CharField(name='store_name', max_length=200)

    def __str__(self):
        return self.name

Product_Categories = (
    ('Motors', 'Motors'),
    ('Books, Movies & Music', 'Books, Movies & Music'),
    ('Electronics', 'Electronics'),
    ('Collectibles & Art', 'Collectibles & Art'),
    ('Fashion', 'Fashion'),
    ('Home & Garden', 'Home & Garden'),
    ('Sporting Goods', 'Sporting Goods'),
    ('Toys & Hobbies', 'Toys & Hobbies'),
    ('Business & Industrial', 'Business & Industrial'),
    ('Health & Beauty', 'Health & Beauty'),
    ('Others', 'Others'),
)
Product_Disable_Enable = (
    ('False' , 'Not Active'),
    ('True' , 'Active'),
)

class Product(models.Model):
    seller = models.ForeignKey(Seller, name = "Seller", on_delete=models.CASCADE)
    product_name = models.CharField(name='product_name', max_length=200, default='null' )
    product_description = CKEditor5Field('product_description', config_name='extends', default='null')
    price = models.FloatField(name='price', max_length=10, default=0.0)
    quantity = models.IntegerField(name='quantity', default=0.0)
    rating = models.FloatField(name='rating', default=0.0)
    image1 = models.ImageField(null=True, blank=True, default='null')
    image2 = models.ImageField(null=True, blank=True, default='null')
    image3 = models.ImageField(null=True, blank=True, default='null')
    discount = models.FloatField(name='discount', max_length=10, default=0.0)
    category = models.CharField(name='category', choices=Product_Categories, max_length=100, default='Others')
    status = models.CharField(name='status', choices=Product_Disable_Enable, default = 'Not Active' , max_length=10)
    def __str__(self):
        return self.product_name

