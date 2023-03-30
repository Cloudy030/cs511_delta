from django.test import TestCase
from django.urls import reverse
from emission.models import PerCapitaEmission, Country, TotalEmission

class PerCapitaEmissionTableTest(TestCase):
    def setUp(self):
   

        self.country = Country.objects.create(country_name="Afghanistan")


        self.percapitaemission = PerCapitaEmission.objects.create(
            country=self.country,
            year=2021,
            percapita=0.296119,
            coal=0.104828,
            oil=0.185029,
            gas=0.185029,
            cement=0.000306,
            flaring=0.0
        )

    def test_table_data_display(self):

        response = self.client.get(reverse('per_capita'))
        self.assertEqual(response.status_code, 200)


        self.assertContains(response, "Afghanistan")
        self.assertContains(response, "2021")
        self.assertContains(response, "0.296119")
        self.assertContains(response, "0.104828")
        self.assertContains(response, "0.185029")
        self.assertContains(response, "0.185029")
        self.assertContains(response, "0.000306")
        self.assertContains(response, "0.0")

class TotalEmissionTableTest(TestCase):
    def setUp(self):
   
  
        self.country = Country.objects.create(country_name="Albania")
        self.totalemission = TotalEmission.objects.create(
            country=self.country,
            year=2015,
            total=4.712137,
            coal=0.322432,
            oil=3.337904,
            gas=0.062288,
            cement=0.954113,
            flaring=0.0354
        )

    def test_table_data_display2(self):

        response = self.client.get(reverse('total'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Albania")
        self.assertContains(response, "2015")
        self.assertContains(response, "4.712137")
        self.assertContains(response, "0.322432")
        self.assertContains(response, "3.337904")
        self.assertContains(response, "0.062288")
        self.assertContains(response, "0.954113")
        self.assertContains(response, "0.0354")



