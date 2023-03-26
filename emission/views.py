from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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

    # Get the year from the request's GET parameters
    year = request.GET.get('year')

    # Filter the total emissions by year, if year is provided
    if year:
        year_emissions = totalemissions.filter(year=year)
    else:
        # Retrieve total emissions for the latest year
        latest_year = TotalEmission.objects.latest('year').year
        year_emissions = totalemissions.filter(year=latest_year)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Create a Paginator object that contains the totalemissions
    paginator = Paginator(totalemissions, 10) # Show 10 totalemissions per page

    try:
        # Get the Page object for the current page number
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer, show the first page
        page_obj = paginator.get_page(1)
    except EmptyPage:
        # If page_number is out of range (e.g. 9999), show the last page
        page_obj = paginator.get_page(paginator.num_pages)

    if format == 'map':
        # Create a list of countries and their total emissions for the selected year
        country_emissions = []
        for emission in year_emissions:
            country_emissions.append((emission.country.country_name, emission.total))
        # Render map template
        return render(request, 'emission/totalemission_map.html', {'country_emissions': country_emissions, 'format': format})
    elif format == 'chart':
        # Render chart template
        return render(request, 'emission/totalemission_chart.html', {'totalemissions': totalemissions, 'format': format})
    else:
        # Render table template by default
        return render(request, 'emission/totalemission.html', {'page_obj': page_obj, 'format': format})



#def totalemission(request):
  #totalemissions=TotalEmission.objects.all()
  #return render(request, 'emission/totalemission.html',{'totalemissions':totalemissions})

def percapitaemission(request):
  percapitaemissions=PerCapitaEmission.objects.all()
  return render(request, 'emission/percapitaemission.html',{'percapitaemissions':percapitaemissions})

def source(request):
  sources=Source.objects.all()
  return render(request, 'emission/source.html',{'sources':sources})