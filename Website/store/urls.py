# © 2020 Liran Smadja (First Real-World Project) ©

from django.urls import path
from django.conf.urls import url


from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
path('shop/<int:pk>/reviews', views.shopReviews, name= 'shop-reviews'),
path('hot-deals/', views.hotDeals, name= 'hotDeals'),
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
path('admin-panel/inbox/', views.adminMessages, name='admin-messages'),
path('admin-panel/inbox/<int:pk>', views.adminMessageReview, name='admin-message-review'),
path('admin-panel/inbox/<int:pk>/delete', views.adminMessageDelete, name='admin-message-delete'),
path("admin-panel/", views.adminPanel, name="admin-panel"),
path('admin-panel/product/<int:pk>/delete/', views.DeleteProduct, name='delete-product'),
path('admin-panel/product/add/', views.addProduct, name='add-product'),
path('admin-panel/users/', views.userList, name='user-list'),
path('admin-panel/users/add', views.addUser, name='add-user'),
path('admin-panel/users/<int:pk>/review', views.reviewUser, name='review-user'),
path('admin-panel/users/<int:pk>/delete/', views.DeleteUser, name='delete-user'),
path('checkout/', views.checkout, name='checkout'),
path('update_item/', views.updateItem, name='update-item'),
path('update_wishlist/', views.updateWishlist, name='update-wishlist'),
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
path('admin-panel/coupons', views.coupons, name='coupons'),
path('profile/coupons/', views.sellerCoupons, name='seller-coupons'),
path('profile/coupons/<int:pk>/delete', views.sellerCouponDelete, name='seller-coupons-delete'),
path('profile/coupons/add', views.sellerAddCoupon, name='seller-coupons-add'),
path('contactus/', views.contactUs, name='contact-site'),
path('search/', views.searchPage, name='search-page'),
path('shop/<int:pk>', views.sellerShop, name='seller-shop'),
path('shop/<int:pk>/rate', views.sellerStoreRate, name='seller-shop-rate'),
path('profile/my-shops/', views.buyerShopList, name='buyer-shop-list'),
path('profile/my-shops/<int:pk>/delete/', views.buyerDeleteShop, name='buyer-delete-from-shop-list'),
path('order/<str:pk>/success', views.orderCompleted, name='order-completed'),
path('profile/my-orders/', views.buyerOrderList, name='buyer-order-list'),
path('profile/my-sales/', views.sellerSales, name='seller-sales'),
path('admin-panel/transactions/', views.adminTransactions, name='admin-transactions'),
path('admin-panel/settings/', views.adminSettings, name='admin-settings'),
path('admin-panel/activity-logs/', views.adminActivityLogs, name='admin-activity-logs'),
path('category/<str:pk>/', views.categories, name='categoties'),
path('unauthorized', views.unauthorized, name='unauthorized'),
path('best-sellers', views.bestSellersPage, name='best-sellers-page'),


#path('charts', views.charts, name='charts'),


url(r'chat/$', views.all_rooms, name="all_rooms"),
url(r'chat/token/$', views.token, name="token"),
url(r'chat/rooms/(?P<slug>[-\w]+)/$', views.room_detail, name="room_detail"),
url(r'^export/csv/orderExcel', views.orderExcel, name='orderExcel'),
url(r'^export/csv/expansesExcel', views.expansesExcel, name='expansesExcel'),



]
handler404 = 'store.views.error_404_view'

# © 2020 Liran Smadja (First Real-World Project) ©