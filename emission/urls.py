from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('country_list', views.country_list, name='country_list'),
    path('totalemission', views.totalemission, name='totalemission'),
    path('percapitaemission', views.percapitaemission, name='percapitaemission'),
    path('source', views.source, name='source'),
]