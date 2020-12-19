from django.urls import path
from django.conf.urls import url


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
path('cart/', views.cart, name='cart'),
path('faq/', views.faq, name='faq'),
path('profile/my-products/', views.SellerProducts, name='my-products'),
path('profile/my-products/<int:pk>/review', views.sellerReviewProduct, name='seller-review-products'),
path('wishlist/', views.wish_list, name='wishlist'),
path('profile/my-products/<int:pk>/delete/', views.SellerDeleteProduct, name='seller-delete-product'),
path('profile/my-products/add/', views.sellerAddProduct, name='seller-add-product'),
path('seller/<int:pk>/contact/', views.sellerContact, name='seller-contact'),
path('profile/inbox/', views.userMessages, name='user-messages'),
path('profile/inbox/<int:pk>', views.userMessageReview, name='user-message-review'),
path('profile/inbox/<int:pk>/delete/seller', views.sellerMessageDelete, name='seller-delete-message'),
path('profile/inbox/<int:pk>/delete/buyer', views.BuyerMessageDelete, name='buyer-delete-message'),
path('category/motors', views.categoryMotors, name='category-motors'),
path('admin-panel/coupons', views.coupons, name='coupons'),
path('profile/coupons/', views.sellerCoupons, name='seller-coupons'),
path('profile/coupons/<int:pk>/delete', views.sellerCouponDelete, name='seller-coupons-delete'),
path('profile/coupons/add', views.sellerAddCoupon, name='seller-coupons-add'),

url(r'chat/$', views.all_rooms, name="all_rooms"),
url(r'chat/token/$', views.token, name="token"),
url(r'chat/rooms/(?P<slug>[-\w]+)/$', views.room_detail, name="room_detail"),


    path('', views.homePage, name='home')


]
handler404 = 'store.views.error_404_view'