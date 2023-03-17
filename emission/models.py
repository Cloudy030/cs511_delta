from django.conf import settings
from django.db import models

# Create your models here.

class Country(models.Model):
  countryName=models.TextField()
  countryCode=models.TextField()

  def __str__(self):
    return f'{self.countryName}, {self.countryCode}'
