from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('user/', views.userPanel, name= 'userPanel'),
    path('products/', views.Products, name='products'),
    path('checkout/', views.Checkout, name='checkout'),
    path('register/', views.RegisterPage, name='register'),
]