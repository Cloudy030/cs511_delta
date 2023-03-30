from django.test import TestCase
from django.urls import reverse
from emission.models import TotalEmission

class TestViews(TestCase):

    def test_homepage(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Global fossil CO2 emissions")




    

