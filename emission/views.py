from django.shortcuts import render
from .models import Country, TotalEmission, PerCapitaEmission, Source

# Create your views here.
def index(request):
    return render(request, 'emission/index.html')

def country_list(request):
  countries=Country.objects.all()
  return render(request, 'emission/country.html',{'countries':countries})

def totalemission(request):
  totalemissions=TotalEmission.objects.all()
  return render(request, 'emission/totalemission.html',{'totalemissions':totalemissions})

def percapitaemission(request):
  percapitaemissions=PerCapitaEmission.objects.all()
  return render(request, 'emission/percapitaemission.html',{'percapitaemissions':percapitaemissions})

def source(request):
  sources=Source.objects.all()
  return render(request, 'emission/source.html',{'sources':sources})