from django.test import SimpleTestCase
from django.urls import reverse, resolve
from store.views import *
class TestUrls(SimpleTestCase):

#reverse(viewname, urlconf=None, args=None, kwargs=None, current_app=None)
# resolve(path, urlconf=None)

#The resolve() function can be used for resolving URL paths to the corresponding view functions
#If you need to use something similar to the url template tag in your code
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func,homePage) #check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/') # check if url redirect to url as the function is [.views] declared

    def test_shop_reviews_url_is_resolved(self):
        url = reverse('shop-reviews', args=['1'])
        self.assertEqual(resolve(url).func,shopReviews) #check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/shop/1/reviews') # check if url redirect to url as the function is [.views] declared

    def test_hotDeals_url_is_resolved(self):
        url = reverse('hotDeals')
        self.assertEqual(resolve(url).func,hotDeals) #check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/hot-deals/') # check if url redirect to url as the function is [.views] declared


    def test_userPanel_url_is_resolved(self):
        url = reverse('userPanel')
        self.assertEqual(resolve(url).func, userPanel)  # check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/profile/')  # check if url redirect to url as the function is [.views] declared


    def test_userUpdateInfo_url_is_resolved(self):
        url = reverse('user-update-info')
        self.assertEqual(resolve(url).func, userUpdateInfo)  # check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/update-info/')  # check if url redirect to url as the function is [.views] declared


    def test_userUpdateShipping_url_is_resolved(self):
        url = reverse('update-shipping')
        self.assertEqual(resolve(url).func, userUpdateShipping)  # check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/update-shipping/')  # check if url redirect to url as the function is [.views] declared


    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func,RegisterPage) #check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/register/') # check if url redirect to url as the function is [.views] declared

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func,loginPage) #check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/login/') # check if url redirect to url as the function is [.views] declared

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertURLEqual(url, '/logout/') # check if url redirect to url as the function is [.views] declared


    def test_logout_with_log_url_is_resolved(self):
        url = reverse('logout_with_log')
        self.assertEqual(resolve(url).func, logoutPage)  # check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/logoutnow/')  # check if url redirect to url as the function is [.views] declared


    def test_product_details_url_is_resolved(self):
        url = reverse('product-details', args=['50385'])
        self.assertEqual(resolve(url).func, productDetails)  # check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/product/50385/')  # check if url redirect to url as the function is [.views] declared


    def test_review_product_url_is_resolved(self):
        url = reverse('review-product', args= ['50385'])
        self.assertEqual(resolve(url).func, reviewProduct)  # check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/admin-panel/product/50385/review/')  # check if url redirect to url as the function is [.views] declared


    def test_productList_url_is_resolved(self):
        url = reverse('product-list')
        self.assertEqual(resolve(url).func,productList) #check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/admin-panel/product-list/') # check if url redirect to url as the function is [.views] declared

    def test_adminMessages_reviews_url_is_resolved(self):
        url = reverse('admin-messages')
        self.assertEqual(resolve(url).func,adminMessages) #check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/admin-panel/inbox/') # check if url redirect to url as the function is [.views] declared

    def test_adminMessageDelete_url_is_resolved(self):
        url = reverse('admin-message-delete', args = ['1'])
        self.assertEqual(resolve(url).func,adminMessageDelete) #check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/admin-panel/inbox/1/delete') # check if url redirect to url as the function is [.views] declared


    def test_adminPanel_url_is_resolved(self):
        url = reverse('admin-panel')
        self.assertEqual(resolve(url).func, adminPanel)  # check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/admin-panel/')  # check if url redirect to url as the function is [.views] declared


    def test_DeleteProduct_url_is_resolved(self):
        url = reverse('delete-product', args=['50417'])
        self.assertEqual(resolve(url).func, DeleteProduct)  # check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/admin-panel/product/50417/delete/')  # check if url redirect to url as the function is [.views] declared


    def test_addProduct_url_is_resolved(self):
        url = reverse('add-product')
        self.assertEqual(resolve(url).func, addProduct)  # check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/admin-panel/product/add/')  # check if url redirect to url as the function is [.views] declared


    def test_userList_url_is_resolved(self):
        url = reverse('user-list')
        self.assertEqual(resolve(url).func,userList) #check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/admin-panel/users/') # check if url redirect to url as the function is [.views] declared

    def test_addUser_url_is_resolved(self):
        url = reverse('add-user')
        self.assertEqual(resolve(url).func,addUser) #check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/admin-panel/users/add') # check if url redirect to url as the function is [.views] declared

    def test_reviewUser_url_is_resolved(self):
        url = reverse('review-user', args = ['11'])
        self.assertEqual(resolve(url).func, reviewUser)  # check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/admin-panel/users/11/review') # check if url redirect to url as the function is [.views] declared


    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)  # check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/checkout/')  # check if url redirect to url as the function is [.views] declared


    def test_updateItem_url_is_resolved(self):
        url = reverse('update-item')
        self.assertEqual(resolve(url).func, updateItem)  # check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/update_item/')  # check if url redirect to url as the function is [.views] declared


    def test_updateWishlist_url_is_resolved(self):
        url = reverse('update-wishlist')
        self.assertEqual(resolve(url).func, updateWishlist)  # check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/update_wishlist/')  # check if url redirect to url as the function is [.views] declared

    def test_cart_url_is_resolved(self):
        url = reverse('cart')
        self.assertEqual(resolve(url).func, cart)  # check if [path] is match to this [.views] function
        self.assertURLEqual(url, '/cart/')  # check if url redirect to url as the function is [.views] declared


    def test_faq_url_is_resolved(self):
         url = reverse('faq')
         self.assertEqual(resolve(url).func, faq)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/faq/')  # check if url redirect to url as the function is [.views] declared

    def test_SellerProducts_url_is_resolved(self):
         url = reverse('my-products')
         self.assertEqual(resolve(url).func, SellerProducts)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/profile/my-products/')  # check if url redirect to url as the function is [.views] declared


    def test_sellerReviewProduct_url_is_resolved(self):
         url = reverse('seller-review-products', args=['50393'])
         self.assertEqual(resolve(url).func, sellerReviewProduct)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url,'/profile/my-products/50393/review')  # check if url redirect to url as the function is [.views] declared

    def test_wishlist_url_is_resolved(self):
         url = reverse('wishlist')
         self.assertEqual(resolve(url).func, wish_list)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/wishlist/')  # check if url redirect to url as the function is [.views] declared

    def test_SellerDeleteProduct_url_is_resolved(self):
         url = reverse('seller-delete-product', args=['50385'])
         self.assertEqual(resolve(url).func, SellerDeleteProduct)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url,'/profile/my-products/50385/delete/')  # check if url redirect to url as the function is [.views] declared

    def test_sellerAddProduct_url_is_resolved(self):
         url = reverse('seller-add-product')
         self.assertEqual(resolve(url).func, sellerAddProduct)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/profile/my-products/add/')  # check if url redirect to url as the function is [.views] declared


    def test_sellerContact_url_is_resolved(self):
         url = reverse('seller-contact', args=['11'])
         self.assertEqual(resolve(url).func, sellerContact)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url,'/seller/11/contact/')  # check if url redirect to url as the function is [.views] declared

    def test_userMessages_url_is_resolved(self):
         url = reverse('user-messages')
         self.assertEqual(resolve(url).func, userMessages)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/profile/inbox/')  # check if url redirect to url as the function is [.views] declared

    def test_userMessageReview_url_is_resolved(self):
         url = reverse('user-message-review', args=['11'])
         self.assertEqual(resolve(url).func, userMessageReview)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url,'/profile/inbox/11')  # check if url redirect to url as the function is [.views] declared

    def test_sellerMessageDelete_url_is_resolved(self):
         url = reverse('seller-delete-message', args=['10'])
         self.assertEqual(resolve(url).func, sellerMessageDelete)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url,'/profile/inbox/10/delete/seller')  # check if url redirect to url as the function is [.views] declared

    def test_BuyerMessageDelete_url_is_resolved(self):
         url = reverse('buyer-delete-message', args=['10'])
         self.assertEqual(resolve(url).func, BuyerMessageDelete)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/profile/inbox/10/delete/buyer')  # check if url redirect to url as the function is [.views] declared

    def test_coupons_url_is_resolved(self):
         url = reverse('coupons')
         self.assertEqual(resolve(url).func, coupons)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/admin-panel/coupons')  # check if url redirect to url as the function is [.views] declared

    def test_sellerCoupons_url_is_resolved(self):
         url = reverse('seller-coupons')
         self.assertEqual(resolve(url).func, sellerCoupons)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/profile/coupons/')  # check if url redirect to url as the function is [.views] declared

    def test_sellerCouponDelete_url_is_resolved(self):
         url = reverse('seller-coupons-delete', args=['11'])
         self.assertEqual(resolve(url).func, sellerCouponDelete)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/profile/coupons/11/delete')  # check if url redirect to url as the function is [.views] declared

    def test_sellerAddCoupon_url_is_resolved(self):
         url = reverse('seller-coupons-add')
         self.assertEqual(resolve(url).func, sellerAddCoupon)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/profile/coupons/add')  # check if url redirect to url as the function is [.views] declared

    def test_contactUs_url_is_resolved(self):
         url = reverse('contact-site')
         self.assertEqual(resolve(url).func, contactUs)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/contactus/')  # check if url redirect to url as the function is [.views] declared

    def test_searchPage_url_is_resolved(self):
         url = reverse('search-page')
         self.assertEqual(resolve(url).func, searchPage)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/search/')  # check if url redirect to url as the function is [.views] declared

    def test_sellerShop_url_is_resolved(self):
         url = reverse('seller-shop', args=['11'])
         self.assertEqual(resolve(url).func, sellerShop)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/shop/11')  # check if url redirect to url as the function is [.views] declared

    def test_sellerStoreRate_url_is_resolved(self):
         url = reverse('seller-shop-rate', args=['11'])
         self.assertEqual(resolve(url).func, sellerStoreRate)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/shop/11/rate')  # check if url redirect to url as the function is [.views] declared

    def test_buyerShopList_url_is_resolved(self):
         url = reverse('buyer-shop-list')
         self.assertEqual(resolve(url).func, buyerShopList)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/profile/my-shops/')  # check if url redirect to url as the function is [.views] declared

    def test_buyerDeleteShop_url_is_resolved(self):
         url = reverse('buyer-delete-from-shop-list', args=['10'])
         self.assertEqual(resolve(url).func, buyerDeleteShop)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/profile/my-shops/10/delete/')  # check if url redirect to url as the function is [.views] declared

    def test_orderCompleted_url_is_resolved(self):
         url = reverse('order-completed', args=['41D39170A37554E50054F331'])
         self.assertEqual(resolve(url).func, orderCompleted)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/order/41D39170A37554E50054F331/success')  # check if url redirect to url as the function is [.views] declared

    def test_buyerOrderList_url_is_resolved(self):
         url = reverse('buyer-order-list')
         self.assertEqual(resolve(url).func, buyerOrderList)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/profile/my-orders/')  # check if url redirect to url as the function is [.views] declared

    def test_sellerSales_url_is_resolved(self):
         url = reverse('seller-sales')
         self.assertEqual(resolve(url).func, sellerSales)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/profile/my-sales/')  # check if url redirect to url as the function is [.views] declared

    def test_adminTransactions_url_is_resolved(self):
         url = reverse('admin-transactions')
         self.assertEqual(resolve(url).func, adminTransactions)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/admin-panel/transactions/')  # check if url redirect to url as the function is [.views] declared

    def test_adminSettings_url_is_resolved(self):
         url = reverse('admin-settings')
         self.assertEqual(resolve(url).func, adminSettings)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/admin-panel/settings/')  # check if url redirect to url as the function is [.views] declared

    def test_unauthorizeed_url_is_resolved(self):
         url = reverse('unauthorized')
         self.assertEqual(resolve(url).func, unauthorized)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/unauthorized')  # check if url redirect to url as the function is [.views] declared

    def test_bestSellersPage_url_is_resolved(self):
         url = reverse('best-sellers-page')
         self.assertEqual(resolve(url).func, bestSellersPage)  # check if [path] is match to this [.views] function
         self.assertURLEqual(url, '/best-sellers')  # check if url redirect to url as the function is [.views] declared
