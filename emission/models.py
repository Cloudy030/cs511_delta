try:
  from django.conf import settings
  from django.db import models
except ImportError as error:
  print("Error importing Module: ", error)

# Create your models here.
class Year(models.Model):
    year=models.IntegerField()
     
    def __str__(self):
      return f'{self.year}'

class Country(models.Model):
  # model for Country with only the country name form country.csv with automated generated id
  id=models.BigAutoField(primary_key=True)
  country_name=models.TextField()
  # country_code=models.TextField()

  def __str__(self):
    return f'{self.country_name}'
    # ', {self.country_code}'


class TotalEmission(models.Model):
  # model for total emission table from GCB2022v27_MtCO2_flat.csv
  # with country name as the foreign key with the Country class
  # with automated generated id
  # and other fields year, total emission of the country in the year, coal emission of the country in the year,
  # oil emission of the country in the year, gas emission of the country in the year, 
  # cement emission of the country in the year and flaring emission of the country in the year
  id=models.BigAutoField(primary_key=True)
  country=models.ForeignKey('Country', on_delete=models.CASCADE, null=True)
  year=models.IntegerField()
  total=models.FloatField()
  coal=models.FloatField()
  oil=models.FloatField()
  gas=models.FloatField()
  cement=models.FloatField()
  flaring=models.FloatField()


  def __str__(self):
    return f'{self.country}, {self.year}, {self.total}, {self.coal}, {self.oil}, {self.gas}, {self.cement}, {self.flaring}'

class PerCapitaEmission(models.Model):
  # model for per capita emission table from GCB2022v27_percapita_flat.csv
  # with country name as the foreign key with the Country class
  # with automated generated id
  # and other fields year, per capita emission of the country in the year, per capita coal emission of the country in the year,
  # per capita oil emission of the country in the year, per capita gas emission of the country in the year, 
  # per capita cement emission of the country in the year and per capita flaring emission of the country in the year
  id=models.BigAutoField(primary_key=True)
  country=models.ForeignKey('Country', on_delete=models.CASCADE, null=True)
  year=models.IntegerField()
  percapita=models.FloatField()  
  coal=models.FloatField()
  oil=models.FloatField()
  gas=models.FloatField()
  cement=models.FloatField()
  flaring=models.FloatField()

  def __str__(self):
    return f'{self.country}, {self.year}, {self.percapita}, {self.coal}, {self.oil}, {self.gas}, {self.cement}, {self.flaring}'

# class Source(models.Model):
#   # model for sources table from GCB2022v27_sources_flat.csv
#   # with country name as the foreign key with the Country class
#   # with automated generated id
#   # and other fields year, sources for the data:
#   # total emission of the country in the year, coal emission of the country in the year,
#   # oil emission of the country in the year, gas emission of the country in the year, 
#   # cement emission of the country in the year and flaring emission of the country in the year
#   id=models.BigAutoField(primary_key=True)
#   country=models.ForeignKey('Country', on_delete=models.CASCADE, null=True)
#   year=models.IntegerField()
#   coal=models.TextField()
#   oil=models.TextField()
#   gas=models.TextField()
#   cement=models.TextField()
#   flaring=models.TextField()