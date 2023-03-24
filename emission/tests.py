# test for models
from django.test import TestCase
from .models import Country, TotalEmission, PerCapitaEmission, Source

class CountryModelTestCase(TestCase):
    def test_country_creation(self):
        # Create a new Country instance
        country = Country.objects.create(country_name="Testland")
        
        # Check if the Country instance has been successfully created and saved to the database
        self.assertIsInstance(country, Country)
        self.assertEqual(country.country_name, "Testland")

class TotalEmissionModelTestCase(TestCase):
    def setUp(self):
        # Create a Country instance before the test starts to be used in other tests
        self.country = Country.objects.create(country_name="Testland")

    def test_total_emission_creation(self):
        # Create a TotalEmission instance using the Country instance already created
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

        # Check if the TotalEmission instance has been successfully created and saved to the database
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
        # Create a Country instance before the test starts to be used in other tests
        self.country = Country.objects.create(country_name="Testland")

    def test_percapita_emission_creation(self):
        # Create a PerCapitaEmission instance using the Country instance already created
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

        # Check if the PerCapitaEmission instance has been successfully created and saved to the database
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
        # Create a new Source instance
        source = Source.objects.create(
            coal="CDIAC 2022",
            oil="CDIAC 2022",
            gas="CDIAC 2022",
            cement="CDIAC 2022",
            flaring="Andrew cement"
        )

        # Check if the Source instance has been successfully created and saved to the database
        self.assertIsInstance(source, Source)
        self.assertEqual(source.coal, "CDIAC 2022")
        self.assertEqual(source.oil, "CDIAC 2022")
        self.assertEqual(source.gas, "CDIAC 2022")
        self.assertEqual(source.cement, "CDIAC 2022")
        self.assertEqual(source.flaring, "Andrew cement")

