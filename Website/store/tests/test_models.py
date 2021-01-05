from django.test import TestCase
from store.models import *
from django.db import models
from django.contrib.auth.admin import User
from datetime import timezone
from django_countries.fields import CountryField
from django_ckeditor_5.fields import CKEditor5Field
import random
import secrets

class TestModels(TestCase):

    def test_User_Table(self):
        user_info = User.objects.filter(id=11).first()
        self.assertTrue(isinstance(user_info, User))
        self.assertIsNotNone(user_info)
        self.assertTrue(user_info.is_active)

    def test_Buyer_Table(self):
        buyer_info = Buyer.objects.filter(id=1).first()
        self.assertTrue(isinstance(buyer_info, Buyer))
        self.assertIsNotNone(buyer_info)
        self.assertEqual(buyer_info.id, 1)

    def test_Seller_Table(self):
        seller_info = Seller.objects.filter(id=1).first()
        self.assertTrue(isinstance(seller_info, Seller))
        self.assertIsNotNone(seller_info)
        self.assertEqual(seller_info.id, 1)

    def test_lastLogin_Table(self):
        lastLogin_info = lastLogin.objects.filter(id=9).first()
        self.assertTrue(isinstance(lastLogin_info, lastLogin))
        self.assertIsNotNone(lastLogin_info)
        self.assertEqual(lastLogin_info.id, 9)

    def test_contactSeller_Table(self):
        contactseller_info = contactSeller.objects.filter(id=3).first()
        self.assertTrue(isinstance(contactseller_info, contactSeller))
        self.assertIsNotNone(contactseller_info)
        self.assertEqual(contactseller_info.email, 'snow@man.info')

    def test_contactBuyer_Table(self):
        contactbuyer_info = contactBuyer.objects.filter(id=11).first()
        self.assertTrue(isinstance(contactbuyer_info, contactBuyer))
        self.assertIsNotNone(contactbuyer_info)
        self.assertEqual(contactbuyer_info.email, 'test@ac.sce.ac.il')

    def test_Order_Table(self):
        order_info = Order.objects.filter(id=105).first()
        self.assertTrue(isinstance(order_info, Order))
        self.assertIsNotNone(order_info)
        self.assertEqual(order_info.transaction_id, '465054931F282FC126204911')

    def test_Product_Table(self):
        product_info = Product.objects.filter(id=50398).first()
        self.assertTrue(isinstance(product_info, Product))
        self.assertIsNotNone(product_info)
        self.assertEqual(product_info.price, 51.95)

    def test_shippingAdd_Table(self):
        shippingadd_info = shippingAdd.objects.filter(id=72666).first()
        self.assertTrue(isinstance(shippingadd_info, shippingAdd))
        self.assertIsNotNone(shippingadd_info)
        self.assertEqual(shippingadd_info.country, 'DE')

    def test_wishlist_Table(self):
        wishlist_info = wishlist.objects.filter(id=50).first()
        self.assertTrue(isinstance(wishlist_info, wishlist))
        self.assertIsNotNone(wishlist_info)
        self.assertEqual(wishlist_info.buyer_id, 2)

    def test_Expenses_Table(self):
        expenses_info = Expenses.objects.filter(id=5).first()
        self.assertTrue(isinstance(expenses_info, Expenses))
        self.assertIsNotNone(expenses_info)
        self.assertEqual(expenses_info.expanse_name, 'Technical Webiste Maintenance')

    def test_myShopList_Table(self):
        myshoplist_info = myShopList.objects.filter(id=5).first()
        self.assertTrue(isinstance(myshoplist_info, myShopList))
        self.assertIsNotNone(myshoplist_info)
        self.assertEqual(myshoplist_info.store_id, 1)

    def test_Coupons_Table(self):
        coupons_info = Coupons.objects.filter(id=3).first()
        self.assertTrue(isinstance(coupons_info, Coupons))
        self.assertIsNotNone(coupons_info)
        self.assertEqual(coupons_info.code, 'B434GHG8AWN')

    def test_contactSite_Table(self):
        contactsite_info = contactSite.objects.filter(id=7).first()
        self.assertTrue(isinstance(contactsite_info, contactSite))
        self.assertIsNotNone(contactsite_info)
        self.assertEqual(contactsite_info.message_category, 'Collaborations')

    def test_productRating_Table(self):
        productrating_info = productRating.objects.filter(id=16).first()
        self.assertTrue(isinstance(productrating_info, productRating))
        self.assertIsNotNone(productrating_info)
        self.assertEqual(productrating_info.Description, 'The watch is advertised as water resistant and able to take this watch in the pool and able to submerge the watch up to five feet for 30 minutes. My wife went swimming and the watch no longer works. I called Samsung warranty and they said the water lock setting must be turned on and they are not responsible for water damage. Nowhere on the website or documentation provided with the watch does it say that the feature must be turned on. Also if water damage voids the warranty, how can they claim that the watch can be submerged in water? ')

    def test_mainMessage_Table(self):
        mainmessage_info = mainMessage.objects.filter(id=7).first()
        self.assertTrue(isinstance(mainmessage_info, mainMessage))
        self.assertIsNotNone(mainmessage_info)
        self.assertEqual(mainmessage_info.status, True)

    def test_storeRating_Table(self):
        storerating_info = storeRating.objects.filter(id=3).first()
        self.assertTrue(isinstance(storerating_info, storeRating))
        self.assertIsNotNone(storerating_info)
        self.assertEqual(storerating_info.Description, 'Nothing yet...')

    def test_PromotedProducts_Table(self):
        promotedproducts_info = PromotedProducts.objects.filter(id=1).first()
        self.assertTrue(isinstance(promotedproducts_info, PromotedProducts))
        self.assertIsNotNone(promotedproducts_info)
        self.assertEqual(promotedproducts_info.banner, '50384')