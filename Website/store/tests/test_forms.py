from django.test import SimpleTestCase, TestCase
from store.forms import *

class TestForms(TestCase):

    def test_addCoupon_form_valid_Data(self):
        form = addCoupon(data = {
            'Seller': 1,
            'code': '1',
            'discount_amount': 4,
            'title': 'ok',
            'status': True
                                }
        )

        self.assertTrue(form.is_valid())

    def test_addCoupon_form_no_Data(self):
        form = addCoupon(data={})

        self.assertFalse(form.is_valid())


    def test_mainMessage_form_valid_Data(self):
        form = mainMessageForm(data = {
            'title': 'hello',
            'main_message': 'texty',
            'status': True,
            'time': '01/01/2021'
                                }
        )

        self.assertTrue(form.is_valid())

    def test_mainMessage_form_no_Data(self):
        form = mainMessageForm(data={})

        self.assertFalse(form.is_valid())

    def test_PromotedProductsForm_form_valid_Data(self):
        form = PromotedProductsForm(data = {
            'banner': '123',
            'slideshow': '123',
            'popup': '123',
                                }
        )

        self.assertTrue(form.is_valid())

    def test_PromotedProductsForm_form_no_Data(self):
        form = PromotedProductsForm(data={})

        self.assertFalse(form.is_valid())



    def test_ContactSellerForm_form_valid_Data(self):
        form = ContactSellerForm(data = {
            'User': 11,
            'title': 'ok',
            'first_name': 'ok',
            'last_name': 'ok',
            'email': 'ok@ok.com',
            'receiver': 11,
            'body_text': 'null'
                                }
        )

        self.assertTrue(form.is_valid())

    def test_ContactSellerForm_form_no_Data(self):
        form = ContactSellerForm(data={})

        self.assertFalse(form.is_valid())

    def test_ContactBuyerForm_form_valid_Data(self):
        form = ContactBuyerForm(data = {
            'User': 11,
            'title': 'ok',
            'first_name': 'ok',
            'last_name': 'ok',
            'email': 'ok@ok.com',
            'receiver': 11,
            'body_text': 'null'
                                }
        )

        self.assertTrue(form.is_valid())

    def test_ContactBuyerForm_form_no_Data(self):
        form = ContactBuyerForm(data={})

        self.assertFalse(form.is_valid())


    def test_UpdateSellerForm_form_valid_Data(self):
        form = UpdateSellerForm(data = {
            'store_name': 'one',
            'store_category': 'Others',
            'store_description': 'ok',
            'profile_image': 'null',
            'background_image': 'null',
                                }
        )

        self.assertTrue(form.is_valid())

    def test_UpdateSellerForm_form_no_Data(self):
        form = UpdateSellerForm(data={ })

        self.assertFalse(form.is_valid())

    def test_UpdateUserForm_form_valid_Data(self):
        form = UpdateUserForm(data = {
            'username': 'JU7bjnbnfds',
            'email': 'JU7bjnbnfds@none.com',
            'password1': '90J!K89j@98KNnjc',
            'password2': '90J!K89j@98KNnjc',
            'first_name': 'null',
            'last_name': 'null'
                                }
        )

        self.assertTrue(form.is_valid())

    def test_UpdateUserForm_form_no_Data(self):
        form = UpdateUserForm(data={ })

        self.assertFalse(form.is_valid())

    def test_UpdateShippingForm_form_valid_Data(self):
        form = UpdateShippingForm(data = {
            'User_id': 11,
            'address': 'noland U',
            'city': 'noland F',
            'country': 'IL',
            'zipcode': '00000',
            'phone': '000-0000000',
                                }
        )

        self.assertTrue(not form.is_valid())

    def test_UpdateShippingForm_form_no_Data(self):
        form = UpdateShippingForm(data={ })

        self.assertFalse(form.is_valid())

    def test_UpdateProductForm_form_valid_Data(self):
        form = UpdateProductForm(data = {
            'Seller_id': 1,
            'product_name': 'nothing',
            'product_description': 'nothing F',
            'price': 10,
            'quantity': 100,
            'discount': 16,
            'category': 'Others',
            'status': True,
            'image1': 'null',
            'image2': 'null',
            'image3': 'null',
            'advertise': 'Banner'
                                }
        )

        self.assertTrue(form.is_valid())

    def test_UpdateProductForm_form_no_Data(self):
        form = UpdateProductForm(data={ })

        self.assertFalse(form.is_valid())

    def test_addProductForm_form_valid_Data(self):
        form = addProductForm(data = {
            'Seller': 1,
            'product_name': 'nothing',
            'product_description': 'nothing F',
            'price': 10,
            'quantity': 100,
            'discount': 16,
            'category': 'Others',
            'status': True,
            'image1': 'null',
            'image2': 'null',
            'image3': 'null',
            'advertise': 'Banner'
                                }
        )

        self.assertTrue(form.is_valid())

    def test_addProductForm_form_no_Data(self):
        form = addProductForm(data={ })

        self.assertFalse(form.is_valid())

    def test_UserRegisterForm_form_valid_Data(self):
        form = UserRegisterForm(data = {
            'username': 'JU7bjnbnfds',
            'email': 'JU7bjnbnfds@none.com',
            'password1': '90J!K89j@98KNnjc',
            'password2': '90J!K89j@98KNnjc',
            'first_name': 'null',
            'last_name': 'null',
            'is_superuser': True,
                                }
        )

        self.assertTrue(form.is_valid())

    def test_UserRegisterForm_form_no_Data(self):
        form = UserRegisterForm(data={ })

        self.assertFalse(form.is_valid())

    def test_UserLoginForm_form_valid_Data(self):
        form = UserLoginForm(data = {
            'username': 'randomuser',
            'password': 'v7eRBmXLV6bvtwL',

                                }
        )

        self.assertTrue(not form.is_valid())

    def test_UserLoginForm_form_no_Data(self):
        form = UserLoginForm(data={ })

        self.assertFalse(form.is_valid())

    def test_contactSiteForm_form_valid_Data(self):
        form = contactSiteForm(data = {
            'title': 'nothing',
            'body_text': 'nothing',
            'first_name': 'nothing',
            'last_name': 'nothing',
            'email': 'nothingcx@nothing.com',
            'image': 'null',
            'message_category': 'Exploits',
                                }
        )

        self.assertTrue(form.is_valid())

    def test_contactSiteForm_form_no_Data(self):
        form = contactSiteForm(data={ })

        self.assertFalse(form.is_valid())

    def test_productRatingForm_form_valid_Data(self):
        form = productRatingForm(data = {
            'Product': 50374,
            'rating': 3,
            'name': 'nothing',
            'email': 'nothing@nothing.com',
            'Description': 'nothingcx@nothing.com',
            'image': 'null',
                                }
        )

        self.assertTrue(form.is_valid())

    def test_productRatingForm_form_no_Data(self):
        form = productRatingForm(data={ })

        self.assertFalse(form.is_valid())

    def test_storeRatingForm_form_valid_Data(self):
        form = storeRatingForm(data = {
            'Seller': 1,
            'rating': 3,
            'name': 'nothing',
            'email': 'nothing@nothing.com',
            'Description': 'nothingcx@nothing.com',
                                }
        )

        self.assertTrue(form.is_valid())

    def test_storeRatingForm_form_no_Data(self):
        form = storeRatingForm(data={ })

        self.assertFalse(form.is_valid())

    def test_myShopListForm_form_valid_Data(self):
        form = myShopListForm(data = {
            'User': 11,
            'store_name': 'hello land',
            'image': 'null',
            'store': 1,
                                }
        )

        self.assertTrue(not form.is_valid())

    def test_myShopListForm_form_no_Data(self):
        form = myShopListForm(data={ })

        self.assertFalse(form.is_valid())

    def test_transactionForm_form_valid_Data(self):
        form = transactionForm(data = {
            'transaction_id': '71FA477C5336AA850D083747',
            'complete': False,
            'Buyer': 1,
            'total': 17.99,
            'pickup': True
                                }
        )

        self.assertTrue(form.is_valid())

    def test_transactionForm_form_no_Data(self):
        form = transactionForm(data={ })

        self.assertFalse(form.is_valid())


