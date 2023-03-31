from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):
    
    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Charting")
        
    def test_per_capita_view(self):
        url = reverse('per_capita')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Per Capita CO2 Emissions Across the World")
        
    def test_total_view(self):
        url = reverse('total')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Annual CO2 emissions")



    

