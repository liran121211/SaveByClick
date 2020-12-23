# © 2020 Liran Smadja (First Real-World Project) ©
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, forms
from .models import shippingAdd, Product, Seller, contactSeller, contactBuyer, Coupons , contactSite, productRating, storeRating, myShopList, Order

class addCoupon(forms.ModelForm):
    class Meta:
        model = Coupons
        fields = ['Seller', 'code' , 'discount_amount', 'title', 'status']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'discount_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select()
        }

class ContactSellerForm(forms.ModelForm):
    class Meta:
        model = contactSeller
        fields = ['User', 'title' , 'body_text', 'first_name', 'last_name', 'email', 'receiver']
        widgets = {
            'User': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ContactBuyerForm(forms.ModelForm):
    class Meta:
        model = contactBuyer
        fields = ['User', 'title' , 'body_text', 'first_name', 'last_name', 'email', 'receiver']
        widgets = {
            'User': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UpdateSellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['store_name', 'store_category' , 'store_description', 'profile_image', 'background_image']
        widgets = {
            'store_name': forms.TextInput(attrs={'class': 'form-control'}),
            'store_description': forms.TextInput(attrs={'class': 'form-control'}),
            'store_category': forms.Select(attrs={'class': 'form-control'}),
        }

class UpdateUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UpdateShippingForm(forms.ModelForm):
    class Meta:
        model = shippingAdd
        fields = [ 'address', 'city', 'country','zipcode', 'phone']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [ 'product_name', 'product_description', 'price','quantity', 'discount', 'category', 'status' ,'image1', 'image2', 'image3', 'advertise']
        widgets = {
           'product_name' : forms.TextInput(attrs={'class': 'form-control'}),
           'price': forms.NumberInput(attrs={'class': 'form-control'}),
           'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
           'discount': forms.NumberInput(attrs={'class': 'form-control'}),
           'category': forms.Select(attrs={'class': 'form-control'}),
           'status': forms.Select(attrs={'class': 'form-control'}),
           'advertise': forms.Select(attrs={'class': 'form-control'}),
       }

class addProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Seller', 'product_name', 'product_description', 'price','quantity', 'discount', 'category', 'status' ,'image1', 'image2', 'image3', 'advertise']
        widgets = {
           'product_name' : forms.TextInput(attrs={'class': 'form-control'}),
           'Seller': forms.TextInput(attrs={'class': 'form-control'}),
           'price': forms.NumberInput(attrs={'class': 'form-control'}),
           'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
           'discount': forms.NumberInput(attrs={'class': 'form-control'}),
           'category': forms.Select(attrs={'class': 'form-control'}),
           'status': forms.Select(attrs={'class': 'form-control'}),
           'advertise': forms.Select(attrs={'class': 'form-control'}),
       }

Account_Type=[ ('True','Seller'), ('False','Buyer') ]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    is_superuser = forms.ChoiceField(choices=Account_Type, widget=forms.RadioSelect())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'is_superuser']
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_superuser': forms.Select()
        }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class contactSiteForm(forms.ModelForm):
    class Meta:
        model = contactSite
        fields = ['title', 'body_text', 'first_name', 'last_name','email', 'image', 'message_category' ]
        widgets = {
           'title' : forms.TextInput(attrs={'class': 'form-control'}),
           'first_name': forms.TextInput(attrs={'class': 'form-control'}),
           'last_name': forms.TextInput(attrs={'class': 'form-control'}),
           'last_name': forms.TextInput(attrs={'class': 'form-control'}),
           'email': forms.TextInput(attrs={'class': 'form-control'}),
           'message_category': forms.Select(attrs={'class': 'form-control'}),
       }

Product_Stars = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]


class productRatingForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=Product_Stars, widget=forms.RadioSelect())
    class Meta:
        model = productRating
        fields = ['Product', 'rating', 'name', 'email', 'Description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:500px' }),
            'email': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:500px' }),
            'Product': forms.HiddenInput()
        }

class storeRatingForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=Product_Stars, widget=forms.RadioSelect())
    class Meta:
        model = storeRating
        fields = ['Seller', 'rating', 'name', 'email', 'Description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:500px' }),
            'email': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:500px' }),
            'Seller': forms.HiddenInput()
        }

class myShopListForm(forms.ModelForm):
    class Meta:
        model = myShopList
        fields = ['User', 'store_name', 'image', 'store']
        widgets = {
            'User': forms.HiddenInput(),
            'store_name': forms.HiddenInput(),
            'image': forms.HiddenInput(),
            'store': forms.HiddenInput()
        }


Delivery_Type=[ ('True','Store Pickup'), ('False','Israel Post') ]

class transactionForm(forms.ModelForm):
    pickup = forms.ChoiceField(choices=Delivery_Type, widget=forms.RadioSelect())
    class Meta:
        model = Order
        fields = ['pickup', 'complete', 'Buyer', 'transaction_id', 'total']
        widgets = {
            'transaction_id': forms.HiddenInput(),
            'complete': forms.HiddenInput(),
            'Buyer': forms.HiddenInput(),
            'total': forms.HiddenInput(),
        }

# © 2020 Liran Smadja (First Real-World Project) ©