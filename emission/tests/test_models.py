from django.test import TestCase, Client
from emission.models import Country, TotalEmission, PerCapitaEmission, Source, Year
from django.urls import reverse

class YearModelTestCase(TestCase):
    def setUp(self):
        self.year = Year.objects.create(year=2020)
    
    def test_year_creation(self):
        self.assertTrue(isinstance(self.year, Year))
        self.assertEqual(self.year.year, 2020)
    
    def test_year_str_representation(self):
        self.assertEqual(str(self.year), '2020')


class CountryModelTestCase(TestCase):
    def test_country_creation(self):

        country = Country.objects.create(country_name="Testland")
        
        self.assertIsInstance(country, Country)
        self.assertEqual(country.country_name, "Testland")

class TotalEmissionModelTestCase(TestCase):
    def setUp(self):

        self.country = Country.objects.create(country_name="Testland")

    def test_total_emission_creation(self):

        total_emission = TotalEmission.objects.create(
            country=self.country,
            year=2021,
            total=4.728559,
            coal=0.331439,
            oil=3.217576,
            gas=0.131178,
            cement=1.048179,
            flaring=0.021278
        )


        self.assertIsInstance(total_emission, TotalEmission)
        self.assertEqual(total_emission.country, self.country)
        self.assertEqual(total_emission.year, 2021)
        self.assertEqual(total_emission.total, 4.728559)
        self.assertEqual(total_emission.coal, 0.331439)
        self.assertEqual(total_emission.oil, 3.217576)
        self.assertEqual(total_emission.gas, 0.131178)
        self.assertEqual(total_emission.cement, 1.048179)
        self.assertEqual(total_emission.flaring, 0.021278)

class PerCapitaEmissionModelTestCase(TestCase):
    def setUp(self):

        self.country = Country.objects.create(country_name="Testland")

    def test_percapita_emission_creation(self):

        percapita_emission = PerCapitaEmission.objects.create(
            country=self.country,
            year=2021,
            percapita=10.0,
            coal=2.0,
            oil=3.0,
            gas=4.0,
            cement=1.0,
            flaring=0.5
        )


        self.assertIsInstance(percapita_emission, PerCapitaEmission)
        self.assertEqual(percapita_emission.country, self.country)
        self.assertEqual(percapita_emission.year, 2021)
        self.assertEqual(percapita_emission.percapita, 10.0)
        self.assertEqual(percapita_emission.coal, 2.0)
        self.assertEqual(percapita_emission.oil, 3.0)
        self.assertEqual(percapita_emission.gas, 4.0)
        self.assertEqual(percapita_emission.cement, 1.0)
        self.assertEqual(percapita_emission.flaring, 0.5)

class SourceModelTestCase(TestCase):
    def test_source_creation(self):

        source = Source.objects.create(
            coal="CDIAC 2022",
            oil="CDIAC 2022",
            gas="CDIAC 2022",
            cement="CDIAC 2022",
            flaring="Andrew cement",
            year=2012
        )


        self.assertIsInstance(source, Source)
        self.assertEqual(source.coal, "CDIAC 2022")
        self.assertEqual(source.oil, "CDIAC 2022")
        self.assertEqual(source.gas, "CDIAC 2022")
        self.assertEqual(source.cement, "CDIAC 2022")
        self.assertEqual(source.flaring, "Andrew cement")
