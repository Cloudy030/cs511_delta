from django.conf import settings
from django.db import models

# Create your models here.

class Country(models.Model):
  id=models.BigAutoField(primary_key=True)
  country_name=models.TextField()
  country_code=models.TextField()

  def __str__(self):
    return f'{self.country_name}, {self.country_code}'

class TotalEmission(models.Model):
  id=models.BigAutoField(primary_key=True)
  # country_id=models.IntegerField()
  # ('emission.Country', on_delete=models.CASCADE, related_name='totalemission123')
  year=models.IntegerField()
  total=models.FloatField()
  coal=models.FloatField()
  oil=models.FloatField()
  gas=models.FloatField()
  cement=models.FloatField()
  flaring=models.FloatField()


  def __str__(self):
    return f'{self.year}, {self.total}, {self.coal}, {self.oil}, {self.gas}, {self.cement}, {self.flaring}'

class PerCapitaEmission(models.Model):
  id=models.BigAutoField(primary_key=True)
  # country_id=models.ForeignKey('emission.Country', on_delete=models.CASCADE, related_name='percapitaemission')
  year=models.IntegerField()
  percapita=models.FloatField()  
  coal=models.FloatField()
  oil=models.FloatField()
  gas=models.FloatField()
  cement=models.FloatField()
  flaring=models.FloatField()

  def __str__(self):
    return f'{self.year}, {self.percapita}, {self.coal}, {self.oil}, {self.gas}, {self.cement}, {self.flaring}'

class Source(models.Model):
  id=models.BigAutoField(primary_key=True)
  coal=models.TextField()
  oil=models.TextField()
  gas=models.TextField()
  cement=models.TextField()
  flaring=models.TextField()