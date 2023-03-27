from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('country_list', views.country_list, name='country_list'),
    path('totalemission', views.totalemission, name='totalemission'),
    path('total/', views.total, name='total'),
    path('total/map/', views.totalemission, {'format': 'map'}, name='totalemission_map'),
    path('per_capita/', views.per_capita, name='per_capita'),
    path('per_capita/map/', views.percapitaemission, {'format': 'map'}, name='per_capita_map'),
    path('per_capita/chart/', views.percapitaemission, {'format': 'chart'}, name='per_capita_chart'),
    path('percapitaemission', views.percapitaemission, name='percapitaemission'),
    path('source', views.source, name='source'),
]