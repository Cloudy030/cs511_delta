from django.test import TestCase, Client
from django.urls import reverse
from emission.models import Year, Country, PerCapitaEmission, TotalEmission

class TestFilterSearchBarPer(TestCase):
    def setUp(self):
        self.client = Client()
        self.year1 = Year.objects.create(year=2020)
        self.year2 = Year.objects.create(year=2021)
        self.country1 = Country.objects.create(country_name='USA')
        self.country2 = Country.objects.create(country_name='China')
        self.emission1 = PerCapitaEmission.objects.create(country=self.country1,year=2019, percapita=15.730884,coal=3.202695, oil=7.055616, gas=5.007181, cement=0.122326, flaring=0.264367)
        self.emission2 = PerCapitaEmission.objects.create(country=self.country1,year=2019, percapita=15.730884,coal=3.202695, oil=7.055616, gas=5.007181, cement=0.122326, flaring=0.264367)
        self.emission3 = PerCapitaEmission.objects.create(country=self.country2,year=2020, percapita=7.68895,coal=5.337608, oil=1.14232, gas=0.482747, cement=0.602298, flaring=0.003592)

    def test_filter_search_bar(self):
        response = self.client.post(reverse('percapitafilter'), {'yfilter': 2020, 'cfilter': self.country1.id})
        response = self.client.post(reverse('percapitafilter'), {'yfilter': 2020, 'cfilter': self.country2.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "USA")
        self.assertContains(response, "China")


class TestFilterSearchBarTotal(TestCase):
    def setUp(self):
        self.client = Client()
        self.year1 = Year.objects.create(year=2000)
        self.year2 = Year.objects.create(year=2001)
        self.country1 = Country.objects.create(country_name='Albania')
        self.country2 = Country.objects.create(country_name='Afghanistan')
        self.emission1 = TotalEmission.objects.create(country=self.country1,year=2000, total=3.024926,coal=0.069531, oil=0.069531, gas=0.021957, cement=0.093637, flaring=0.0)
        self.emission2 = TotalEmission.objects.create(country=self.country1,year=2000, total=3.024926,coal=0.069531, oil=0.069531, gas=0.021957, cement=0.093637, flaring=0.0)
        self.emission3 = TotalEmission.objects.create(country=self.country2,year=2001, total=1.069098,coal=0.069616, oil=0.762112, gas=0.208848, cement=0.006538, flaring=0.021984)

    def test_filter_search_bar(self):
        response = self.client.post(reverse('totalfilter'), {'yfilter': 2000, 'cfilter': self.country1.id})
        response = self.client.post(reverse('totalfilter'), {'yfilter': 2001, 'cfilter': self.country2.id})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Albania")
        self.assertContains(response, "Afghanistan")






















