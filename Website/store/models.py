# © 2020 Liran Smadja (First Real-World Project) ©
from django.db import models
from django.contrib.auth.admin import User
from datetime import timezone
from django_countries.fields import CountryField
from django_ckeditor_5.fields import CKEditor5Field
import random
import secrets
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



MessageSubject = (
    ('Fraud' , 'Fraud'),
    ('Bugs' , 'Bugs'),
    ('Exploits' , 'Exploits'),
    ('Business' , 'Business'),
    ('General' , 'General'),
    ('Collaborations' , 'Collaborations'),
    ('Jobs' , 'Jobs'),
)

Product_Advertise = (
    ('Not Promoted' , 'Not Promoted'),
    ('Banner' , 'Banner'),
    ('Pop Up' , 'Pop Up'),
    ('Main Slidebar' , 'Main Slidebar'),
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
    id = models.ForeignKey(User, name='User', on_delete=models.CASCADE)
    address = models.CharField(name= 'address', max_length=200)
    city = models.CharField(name='city', max_length=100)
    zipcode = models.CharField(name='zipcode', max_length=7)
    country= CountryField()
    phone = models.CharField(name='phone', max_length=10)

    def __str__(self):
        return self.address

class Seller(models.Model):
    user = models.OneToOneField(User, name = "User", on_delete=models.CASCADE)
    store_name = models.CharField(name='store_name', max_length=200, default='null')
    store_category = models.CharField(name='store_category', choices=Product_Categories, max_length=100, default='Others')
    profile_image = models.ImageField(name = 'profile_image', null=True, blank=True, default='null')
    background_image = models.ImageField(name = 'background_image',null=True, blank=True, default='null')
    followers = models.IntegerField(name= 'followers', default = random.randint(500, 99999))
    store_description = models.TextField(name='store_description', max_length=2000, default='null')

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
    advertise = models.CharField(name='advertise', choices=Product_Advertise, max_length=100, default = 'Not Promoted')

    def __str__(self):
        return self.product_name


class Order(models.Model):
    Buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(name = 'complete', default=False)
    transaction_id = models.CharField(max_length=50, default=secrets.token_hex(nbytes=10).upper())
    pickup = models.BooleanField(name='pickup', default=False)
    total = models.FloatField(name='total', max_length=10, default=0.0)

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
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property  # Make function behave like attribute (of class) and not function
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class wishlist(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    buyer = models.ForeignKey(Buyer, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

class Expenses(models.Model):
    expanse_name = models.CharField(name= 'expanse_name', max_length=200, default='null')
    startDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(default=0, null=True, blank=True)

class myShopList(models.Model):
    user = models.ForeignKey(User, name="User", on_delete=models.CASCADE)
    store_name = models.CharField(name= 'store_name', max_length=200, default='null')
    image = models.CharField(name = 'image', null=True, blank=True, default='null', max_length=500)
    store_id = models.OneToOneField(Seller, name="store", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.product_name

class Coupons(models.Model):
    Seller = models.ForeignKey(Seller, name = "Seller", on_delete=models.CASCADE)
    code = models.CharField(name = 'code', max_length=50)
    discount_amount = models.FloatField(name='discount_amount', default=0)
    title = models.CharField(name = 'title', max_length=200, default='null')
    status = models.CharField(name='status', choices=Product_Disable_Enable, max_length=100, default = 'Not Active')

    def __str__(self):
        return self.title

class contactSite(models.Model):
    time = models.DateTimeField(name = 'time', auto_now_add=True, blank=True)
    title = models.CharField(name= 'title', max_length=200, default='null')
    body_text = CKEditor5Field('body_text', config_name='extends', default='null')
    first_name = models.CharField(name='first_name', max_length=200, default='null')
    last_name = models.CharField(name='last_name', max_length=200, default='null')
    email = models.EmailField(name='email', max_length=200, default='null')
    status = models.BooleanField(name='read_or_not', default=False)
    image = models.ImageField(name='image', null=True, blank=True, default='null')
    message_category = models.CharField(name='message_category', choices=MessageSubject, max_length=100, default='General')


    def __str__(self):
        return self.title

class productRating(models.Model):
    Product = models.ForeignKey(Product, name="Product", on_delete=models.CASCADE)
    time = models.DateTimeField(name='time', auto_now_add=True, blank=True)
    rating = models.CharField(name='rating', max_length=100, default='1')
    name = models.CharField(name='name', max_length=200, default='null')
    email = models.EmailField(name='email', max_length=200, default='null')
    Description = CKEditor5Field('Description', config_name='extends', default='null')
    randomImageNumber = models.IntegerField(name='randomImageNumber', default=random.randint(1, 4))
    image = models.ImageField(name='image', null=True, blank=True, default='null')

class mainMessage(models.Model):
    main_message = models.CharField(name='main_message', max_length=1000, default='null')
    status = models.BooleanField(name='status', default=False)
    title = models.CharField(name='title', max_length=100, default='null')
    time = models.DateTimeField(name='time')


    def __str__(self):
        return self.rating

class storeRating(models.Model):
    seller = models.ForeignKey(Seller, name="Seller", on_delete=models.CASCADE)
    time = models.DateTimeField(name='time', auto_now_add=True, blank=True)
    rating = models.CharField(name='rating', max_length=100, default='1')
    name = models.CharField(name='name', max_length=200, default='null')
    email = models.EmailField(name='email', max_length=200, default='null')
    Description = CKEditor5Field('Description', config_name='extends', default='null')
    randomImageNumber = models.IntegerField(name='randomImageNumber', default=random.randint(1, 4))


    def __str__(self):
        return self.rating

class PromotedProducts(models.Model):
    banner = models.CharField(name='banner', max_length=10)
    slideshow = models.CharField(name='slideshow', max_length=10)
    popup = models.CharField(name='popup', max_length=10)
    unique_save = models.IntegerField(name='unique_save', default=999)

# © 2020 Liran Smadja (First Real-World Project) ©