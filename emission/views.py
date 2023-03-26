from django.shortcuts import render
from .models import Country, TotalEmission, PerCapitaEmission, Source

# Create your views here.
def index(request):
    return render(request, 'emission/index.html')

def country_list(request):
  countries=Country.objects.all()
  return render(request, 'emission/country.html',{'countries':countries})

def total(request):
    return render(request, 'emission/total.html')

def totalemission(request, format=None):
    totalemissions = TotalEmission.objects.all()

    if format == 'map':
        # Render map template
        return render(request, 'emission/totalemission_map.html', {'totalemissions': totalemissions, 'format': format})
    elif format == 'chart':
        # Render chart template
        return render(request, 'emission/totalemission_chart.html', {'totalemissions': totalemissions, 'format': format})
    else:
        # Render table template by default
        return render(request, 'emission/totalemission.html', {'totalemissions': totalemissions, 'format': format})


#def totalemission(request):
  #totalemissions=TotalEmission.objects.all()
  #return render(request, 'emission/totalemission.html',{'totalemissions':totalemissions})

def percapitaemission(request):
  percapitaemissions=PerCapitaEmission.objects.all()
  return render(request, 'emission/percapitaemission.html',{'percapitaemissions':percapitaemissions})

def source(request):
  sources=Source.objects.all()
  return render(request, 'emission/source.html',{'sources':sources})