from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.homePage, name='home'),
    path('profile/', views.userPanel, name= 'userPanel'),
    path('update-info/', views.userUpdateInfo, name= 'user-update-info'),
    path("update-shipping/", views.userUpdateShipping, name="update-shipping"),
    #path('products/', views.Products, name='products'),
    path('register/', views.RegisterPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("logoutnow/", views.logoutPage, name="logout_with_log"),
    path('product/<int:pk>/', views.productDetails, name='product-details'),
    path('admin-panel/product/<int:pk>/review/', views.reviewProduct, name='review-product'),
    path('admin-panel/product-list/', views.productList, name='product-list'),
    path("admin-panel/", views.adminPanel, name="admin-panel"),
    path('admin-panel/product/<int:pk>/delete/', views.DeleteProduct, name='delete-product'),
    path('admin-panel/product/add/', views.addProduct, name='add-product'),
    path('admin-panel/users/', views.userList, name='user-list'),
    path('admin-panel/users/add', views.addUser, name='add-user'),
    path('admin-panel/users/<int:pk>/review', views.reviewUser, name='review-user'),
    path('admin-panel/users/<int:pk>/delete/', views.DeleteUser, name='delete-user'),
    path('checkout/', views.Checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update-item'),
    path('cart/', views.cart, name='cart')


]
handler404 = 'store.views.error_404_view'