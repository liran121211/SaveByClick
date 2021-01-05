from django.test import TestCase, Client
from django.urls import reverse
from store.models import *


class TestViews(TestCase):

 def test_bestSellersPage_GET(self):
  client = Client()

  response = client.get(reverse('best-sellers-page'))

  self.assertEqual(response.status_code, 200)
  self.assertTemplateUsed(response, 'best_sellers_page.html')



# © 2020 Liran Smadja (First Real-World Project) ©



