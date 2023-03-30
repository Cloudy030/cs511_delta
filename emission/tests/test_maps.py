from django.test import TestCase, Client
from emission.models import PerCapitaEmission, TotalEmission, Country

class PerCapitaMapTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        aruba = Country.objects.create(country_name='Aruba')
        PerCapitaEmission.objects.create(country=aruba, year=2002, percapita=2.43656, coal=0.0, oil=2.43656, gas=0.0, cement=0.0, flaring=0.0)

    def tearDown(self):
        PerCapitaEmission.objects.all().delete()
        Country.objects.all().delete()

    def test_map_page(self):
        response = self.client.get('/per_capita/map/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Search by year")
        self.assertContains(response, "map")


class TotalMapTest(TestCase):

    def setUp(self):
        self.client = Client()
        bahamas = Country.objects.create(country_name='Bahamas')
        TotalEmission.objects.create(country=bahamas, year=2006, total=1.853984, coal=0.007328, oil=1.846656, gas=0.0, cement=0.0, flaring=0.0)

    def tearDown(self):
        TotalEmission.objects.all().delete()
        Country.objects.all().delete()

    def test_map_page(self):
        response = self.client.get('/total/map/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Search by year")
        self.assertContains(response, "map")










#TotalEmission.objects.create(country=Bahamas, year=2006, total=1.853984, coal=0.007328, oil=1.846656, gas=0.0, cement=0.0, flaring=0.0)

#PerCapitaEmission.objects.create(country=Aruba, year=2002, percapita=2.43656, coal=0.0, oil=2.43656, gas=0.0, cement=0.0, flaring=0.0)