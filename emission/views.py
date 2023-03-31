from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Year, Country, TotalEmission, PerCapitaEmission#, Source
import json

# Create your views here.
def index(request):
    years=Year.objects.all()
    countries=Country.objects.all()
    #for the 2 drop down filters
    return render(request, 'emission/index.html')#, {'years':years, 'countries':countries})

# def country_list(request):
#   countries=Country.objects.all()
#   return render(request, 'emission/country.html',{'countries':countries})

# def year(request):
#     years=Year.objects.all()
#     return render(request, 'emission/search.html', {'years':years} )

def total(request):
    totalemissions = TotalEmission.objects.all()
    #for dropdown search bar
    years=Year.objects.all()
    countries=Country.objects.all()

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Create a Paginator object that contains the totalemissions
    paginator = Paginator(totalemissions, 26) # Show 10 totalemissions per page

    try:
        # Get the Page object for the current page number
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer, show the first page
        page_obj = paginator.get_page(1)
    except EmptyPage:
        # If page_number is out of range (e.g. 9999), show the last page
        page_obj = paginator.get_page(paginator.num_pages)

        # Render table template by default
    return render(request, 'emission/total.html', {'page_obj': page_obj, 'years': years, 'countries': countries})



def per_capita(request, format=None):
    percapitaemissions = PerCapitaEmission.objects.all()
    # for dropdown search bar
    years=Year.objects.all()
    countries=Country.objects.all()

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Create a Paginator object that contains the percapitaemissions
    paginator = Paginator(percapitaemissions, 26) # Show 10 percapitaemissions per page

    try:
        # Get the Page object for the current page number
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer, show the first page
        page_obj = paginator.get_page(1)
    except EmptyPage:
        # If page_number is out of range (e.g. 9999), show the last page
        page_obj = paginator.get_page(paginator.num_pages)

        # Render table template by default
    return render(request, 'emission/per_capita.html', {'page_obj': page_obj, 'format': format, 'years': years, 'countries': countries})


def totalfilter(request):
    # # Get all the total emissions
    # total_emissions = TotalEmission.objects.all()

    # # Get all the years and countries for the dropdowns
    # all_years = Year.objects.all()
    # all_countries = Country.objects.all()

    # # Get the filters from the request
    # selected_country = request.POST.getlist('cfilter')
    # selected_year = request.POST.getlist('yfilter')

    # # Filter the total emissions based on the selected filters
    # if selected_country and selected_year:
    #     total_emissions_filtered = TotalEmission.objects.filter(country__in=selected_country, year__in=selected_year)
    # elif selected_country:
    #     total_emissions_filtered = TotalEmission.objects.filter(country__in=selected_country)
    # elif selected_year:
    #     total_emissions_filtered = TotalEmission.objects.filter(year__in=selected_year)
    # else:
    #     total_emissions_filtered = total_emissions

    # return render(request, 'emission/total_filter.html', {'total_emissions_filtered': total_emissions_filtered, 'all_years': all_years, 'all_countries': all_countries})
    # #to do: add error handkling to check this is a post request
    # if request.method != "POST":
    #     return render(request, 'emission/total.html', {'page_obj': page_obj, 'format': format, 'years': years, 'countries': countries})

    totalemission = TotalEmission.objects.all()
    #for drowpdown search bar
    years=Year.objects.all()
    countries=Country.objects.all()
    c=request.POST.get('cfilter')
    y=request.POST.get('yfilter')
    # print('my country info: ',c,request)
    # print('my year info: ',y,request)
    if c==None:
        totalemi = TotalEmission.objects.filter(year=y)
    elif y==None:
        totalemi = TotalEmission.objects.filter(country=c)
    else:
        totalemi = TotalEmission.objects.filter(country=c).filter(year=y)

    
    return render(request, 'emission/total_filter.html', {'totalemi': totalemi, 'format': format, 'years': years, 'countries': countries, 'totalemi': totalemi})






def search_matierial(request):
    countries=Country.objects.all()
    matierial=""
    country_id=""
    if request.method=='POST':
        matierial=request.POST.get("matierial")
        country_id=request.POST.get("country_id")
        country=Country.objects.filter(id=country_id)
        sources=TotalEmission.objects.filter(country_id=country_id)#Countrywise filter for Total Emissions
        sources_pc=PerCapitaEmission.objects.filter(country_id=country_id)#Countrywise filter for PerCapita Emissions
        sources_temp=[]
        sources_temp_pc=[]
        #Two functions are used to filter out a column for respective datas
        if matierial=='Total':
            for source in sources:
                sources_temp.append(source.total)
                country=source.country
        elif matierial=='Coal':
            for source in sources:
                sources_temp.append(source.coal)
        elif  matierial=='Oil':
            for source in sources:
                sources_temp.append(source.oil)
        elif  matierial=='Gas':
            for source in sources:
                sources_temp.append(source.gas)
        elif  matierial=='Cement':
            for source in sources:
                sources_temp.append(source.cement)
        elif  matierial=='Flaring':
            for source in sources:
                sources_temp.append(source.flaring)

        if matierial=='Total':
            for source_pc in sources_pc:
                sources_temp_pc.append(source_pc.percapita)
                country=source_pc.country
        elif matierial=='Coal':
            for source_pc in sources_pc:
                sources_temp_pc.append(source_pc.coal)
        elif  matierial=='Oil':
            for source_pc in sources_pc:
                sources_temp_pc.append(source_pc.oil)
        elif  matierial=='Gas':
            for source_pc in sources_pc:
                sources_temp_pc.append(source_pc.gas)
        elif  matierial=='Cement':
            for source_pc in sources_pc:
                sources_temp_pc.append(source_pc.cement)
        elif  matierial=='Flaring':
            for source_pc in sources_pc:
                sources_temp_pc.append(source_pc.flaring)          

        sources_list = json.dumps(sources_temp)#Converting python object to JSON object to be passed to UI
        sources_list_pc = json.dumps(sources_temp_pc)
        return render(request, 'emission/totalemission_graph.html',{'sources_list':sources_list,'country':country,'sources_list_pc':sources_list_pc,'countries':countries})

    return render(request, 'emission/totalemission_graph.html',{'countries':countries})

def percapitafilter(request, format=None):
    #to do: add error handkling to check this is a post request
    if request.method != "POST":
        return render(request, 'emission/per_capita.html', {'page_obj': page_obj, 'format': format, 'years': years, 'countries': countries})

    percapitaemissions = PerCapitaEmission.objects.all()
    #for drowpdown search bar
    years=Year.objects.all()
    countries=Country.objects.all()
    c=request.POST.get('cfilter')
    y=request.POST.get('yfilter')
    # print('my country info: ',c,request)
    # print('my year info: ',y,request)
    if c==None:
        percapitaemi = PerCapitaEmission.objects.filter(year=y)
    elif y==None:
        percapitaemi = PerCapitaEmission.objects.filter(country=c)
    else:
        percapitaemi = PerCapitaEmission.objects.filter(country=c).filter(year=y)

    
    return render(request, 'emission/per_capita_filter.html', {'percapitaemi': percapitaemi, 'format': format, 'years': years, 'countries': countries, 'percapitaemi': percapitaemi})



