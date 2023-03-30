from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Year, Country, TotalEmission, PerCapitaEmission, Source

# Create your views here.
def index(request):
    years=Year.objects.all()
    countries=Country.objects.all()
    #for the 2 drop down filters
    return render(request, 'emission/index.html', {'years':years, 'countries':countries})

def country_list(request):
  countries=Country.objects.all()
  return render(request, 'emission/country.html',{'countries':countries})

def year(request):
    years=Year.objects.all()
    return render(request, 'emission/search.html', {'years':years} )

def total(request, format=None):
    totalemissions = TotalEmission.objects.all()
    years=Year.objects.all()
    countries=Country.objects.all()

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
        def totalemission_chart (request,country):
            country = request.GET.get('country')
            country_emissions = country_emissions.objects.filter(
                country = country_list).first()                    

        # Render chart template
        return render(request, 'emission/totalemission_chart.html', {'totalemissions': totalemissions, 'format': format})
    else:
        # Render table template by default
        return render(request, 'emission/total.html', {'page_obj': page_obj, 'format': format, 'years': years, 'countries': countries})






#def totalemission(request):
  #totalemissions=TotalEmission.objects.all()
  #return render(request, 'emission/totalemission.html',{'totalemissions':totalemissions})

def per_capita(request, format=None):
    percapitaemissions = PerCapitaEmission.objects.all()

    # Get the year from the request's GET parameters
    year = request.GET.get('year')

    # Filter the per capita emissions by year, if year is provided
    if year:
        year_emissions = percapitaemissions.filter(year=year)
    else:
        # Retrieve per capita emissions for the latest year
        latest_year = PerCapitaEmission.objects.latest('year').year
        year_emissions = percapitaemissions.filter(year=latest_year)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Create a Paginator object that contains the percapitaemissions
    paginator = Paginator(percapitaemissions, 10) # Show 10 percapitaemissions per page

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
        # Create a list of countries and their per capita emissions for the selected year
        country_emissions = []
        for emission in year_emissions:
            country_emissions.append((emission.country.country_name, emission.percapita))
        # Render map template
        return render(request, 'emission/per_capita_map.html', {'country_emissions': country_emissions, 'format': format})
    elif format == 'chart':
        # Render chart template
        return render(request, 'emission/per_capita_chart.html', {'percapitaemissions': percapitaemissions, 'format': format})
    else:
        # Render table template by default
        return render(request, 'emission/per_capita.html', {'page_obj': page_obj, 'format': format, 'percapitaemissions': percapitaemissions})



#def percapitaemission(request):
  #percapitaemissions=PerCapitaEmission.objects.all()
  #return render(request, 'emission/percapitaemission.html',{'percapitaemissions':percapitaemissions})

def source(request):
  sources=Source.objects.all()
  return render(request, 'emission/source.html',{'sources':sources})


def totalfilter(request, format=None):
    totalemissions = TotalEmission.objects.all()
    years=Year.objects.all()
    countries=Country.objects.all()

    # Get the year from the request's GET parameters
    year = request.GET.get('year')

    # Filter the total emissions by year, if year is provided
    if year:
        year_emissions = totalemissions.filter(year=year)
    else:
        # Retrieve total emissions for the latest year
        latest_year = TotalEmission.objects.latest('year').year
        year_emissions = totalemissions.filter(year=latest_year)
    
    if request.method=='POST':
        c=request.POST.get('cfilter')
        print('my country info: ',c,request)
        totalemi = TotalEmission.objects.filter(country=c)


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
    
    return render(request, 'emission/total_filter.html', {'page_obj': totalemi, 'format': format, 'years': years, 'countries': countries})


    # if format == 'map':
    #     # Create a list of countries and their total emissions for the selected year
    #     country_emissions = []
    #     for emission in year_emissions:
    #         country_emissions.append((emission.country.country_name, emission.total))
    #     # Render map template
    #     return render(request, 'emission/totalemission_map.html', {'country_emissions': country_emissions, 'format': format})
    # elif format == 'chart':
    #     def totalemission_chart (request,country):
    #         country = request.GET.get('country')
    #         country_emissions = country_emissions.objects.filter(
    #             country = country_list).first()                    

    #     # Render chart template
    #     return render(request, 'emission/totalemission_chart.html', {'totalemissions': totalemissions, 'format': format})
    # else:
    #     # Render table template by default
    #     return render(request, 'emission/total_filter.html', {'page_obj': page_obj, 'format': format, 'years': years, 'countries': countries})
