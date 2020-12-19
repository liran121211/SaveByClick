from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, forms
from .models import shippingAdd, Product


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
        fields = [ 'product_name', 'product_description', 'price','quantity', 'discount', 'category', 'status' ,'image1', 'image2', 'image3' ]
        widgets = {
           'product_name' : forms.TextInput(attrs={'class': 'form-control'}),
           'price': forms.NumberInput(attrs={'class': 'form-control'}),
           'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
           'discount': forms.NumberInput(attrs={'class': 'form-control'}),
           'category': forms.Select(attrs={'class': 'form-control'}),
           'status': forms.Select(attrs={'class': 'form-control'}),
       }

class addProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Seller', 'product_name', 'product_description', 'price','quantity', 'discount', 'category', 'status' ,'image1', 'image2', 'image3' ]
        widgets = {
           'product_name' : forms.TextInput(attrs={'class': 'form-control'}),
           'Seller': forms.TextInput(attrs={'class': 'form-control'}),
           'price': forms.NumberInput(attrs={'class': 'form-control'}),
           'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
           'discount': forms.NumberInput(attrs={'class': 'form-control'}),
           'category': forms.Select(attrs={'class': 'form-control'}),
           'status': forms.Select(attrs={'class': 'form-control'}),
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
