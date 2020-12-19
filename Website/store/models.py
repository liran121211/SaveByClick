from django.db import models
from django.contrib.auth.admin import User
from datetime import timezone
import random
from django_countries.fields import CountryField
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

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

class Room(models.Model):
    """Represents chat rooms that users can join"""
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)

    def __str__(self):
        """Returns human-readable representation of the model instance."""
        return self.name



class lastLogin(models.Model):
    user = models.ForeignKey(User, name="User", on_delete=models.CASCADE)
    time = models.DateTimeField(name = 'time', auto_now_add=True, blank=True)
    logout = models.BooleanField(name='logout', default = False)
    ip = models.CharField(name= 'ip', max_length=20, default='null')

class contactSeller(models.Model):
    user = models.ForeignKey(User, name="User", on_delete=models.CASCADE)
    time = models.DateTimeField(name = 'time', auto_now_add=True, blank=True)
    title = models.CharField(name= 'title', max_length=200, default='null')
    body_text = CKEditor5Field('product_description', config_name='extends', default='null')
    first_name = models.CharField(name='first_name', max_length=200, default='null')
    last_name = models.CharField(name='last_name', max_length=200, default='null')
    email = models.EmailField(name='email', max_length=200, default='null')
    status = models.BooleanField(name='read_or_not', default=False)
    receiver = models.IntegerField(name='receiver',  default=0)

    def __str__(self):
        return self.receiver

class contactBuyer(models.Model):
    user = models.ForeignKey(User, name="User", on_delete=models.CASCADE)
    time = models.DateTimeField(name='time', auto_now_add=True, blank=True)
    title = models.CharField(name='title', max_length=200, default='null')
    body_text = CKEditor5Field('product_description', config_name='extends', default='null')
    first_name = models.CharField(name='first_name', max_length=200, default='null')
    last_name = models.CharField(name='last_name', max_length=200, default='null')
    email = models.EmailField(name='email', max_length=200, default='null')
    status = models.BooleanField(name='read_or_not', default=False)
    receiver = models.IntegerField(name='receiver', default=0)

    def __str__(self):
        return self.receiver

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
    store_name = models.CharField(name='store_name', max_length=200)
    store_category = models.CharField(name='store_category', choices=Product_Categories, max_length=100, default='Others')

    def __str__(self):
        return self.store_name


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
    views = models.IntegerField(name='views', default=0)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    Buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property # Make function behave like attribute (of class) and not function
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property # Make function behave like attribute (of class) and not function
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property  # Make function behave like attribute (of class) and not function
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class wishlist(models.Model):
    user = models.ForeignKey(User, name="User", on_delete=models.CASCADE)
    store_name = models.CharField(name= 'store_name', max_length=200, default='null')
    product_name = models.CharField(name='product_name',max_length=200, default=0)
    price = models.FloatField(name='price', max_length=20, default=0.0)
    image = models.ImageField(null=True, blank=True, default='null')
    stock = models.IntegerField(name="stock", default=0)

    def __str__(self):
        return self.product_name

class Coupons(models.Model):
    Seller = models.ForeignKey(Seller, name = "Seller", on_delete=models.CASCADE)
    code = models.CharField(name = 'code', max_length=50)
    discount_amount = models.FloatField(name='discount_amount', default=0)
    title = models.CharField(name = 'title', max_length=200, default='null')
    status = models.BooleanField(name='status', default=False)
    status = models.CharField(name='status', choices=Product_Disable_Enable, max_length=100, default = 'Not Active')

    def __str__(self):
        return self.title