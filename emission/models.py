from django.conf import settings
from django.db import models

# Create your models here.

class Country(models.Model):
  country_name=models.TextField()
  country_code=models.TextField()

  def __str__(self):
    return f'{self.countryName}, {self.countryCode}'

class TotalEmission(models.Model):
  country_code=models.ForeignKey('emission.Country', on_delete=models.CASCADE, related_name='totalemission')
  year=models.IntegerField()
  total=models.FloatField()
  coal=models.FloatField()
  oil=models.FloatField()
  gas=models.FloatField()
  cement=models.FloatField()
  flaring=models.FloatField()


  def __str__(self):
    return f'{self.country_code}, {self.year}, {self.total}, {self.coal}, {self.oil}, {self.gas}, {self.cement}, {self.flaring}, {self.percapita}'

class PerCapitaEmission(models.Model):
  country_code=models.ForeignKey('emission.Country', on_delete=models.CASCADE, related_name='percapitaemission')
  year=models.IntegerField()
  percapita=models.FloatField()  
  coal=models.FloatField()
  oil=models.FloatField()
  gas=models.FloatField()
  cement=models.FloatField()
  flaring=models.FloatField()

  def __str__(self):
    return f'{self.country_code}, {self.year}, {self.total}, {self.coal}, {self.oil}, {self.gas}, {self.cement}, {self.flaring}'

class Source(models.Model):
  coal=models.TextField()
  oil=models.TextField()
  gas=models.TextField()
  cement=models.TextField()
  flaring=models.TextField()