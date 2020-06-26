from django.contrib import admin
from django.urls import path
from covid import views                                     # !!!

urlpatterns = [
    path('', views.home, name='home'),
    path('covid_chart',
         views.covid, name='covid_chart'),
]