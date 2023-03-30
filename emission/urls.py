from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('country_list', views.country_list, name='country_list'),
path('total/', views.total, name='total'),
path('total/map/', views.total, {'format': 'map'}, name='totalemission_map'),
path('total/chart/', views.total, {'format': 'chart'}, name='totalemission_chart'),
path('per_capita/', views.per_capita, name='per_capita'),
path('per_capita/map/', views.per_capita, {'format': 'map'}, name='per_capita_map'),
path('per_capita/chart/', views.per_capita, {'format': 'chart'}, name='per_capita_chart'),
path('source', views.source, name='source'),
path('year', views.year, name='year'),

   
]