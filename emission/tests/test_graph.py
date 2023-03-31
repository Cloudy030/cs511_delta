from django.test import TestCase, Client
from django.urls import reverse

class TestEmissionPage(TestCase):
    def setUp(self):
        self.client = Client()

    def test_emission_page_chart(self):


        response = self.client.get(reverse('search_matierial'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<canvas id="myChart"></canvas>')
        self.assertContains(response, 'var chart_type')
        self.assertContains(response, 'var sources_list')
        self.assertContains(response, 'var sources_list_pc')
        self.assertContains(response, 'var country')




