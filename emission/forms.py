from django import forms
from .models import Country, TotalEmission, PerCapitaEmission, Source

# YEAR_CHOICES=[1996,1997,1998,1999,2000,2001,2002,2003,2004.2005,2006,2007,2008,2009,2010,2011,2012,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]

class EmissionForm(forms.ModelForm):
  Country=forms.CharField(max_length=50)
  Year=forms.IntegerField(max_length=4)
  # Type=forms.
  # Sector=forms.CharField()

  class Meta:
    model = TotalEmission
    fields=('Country', 'Year',)