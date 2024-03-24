from django.contrib import admin
from django.urls import path
from app_create_cars import views

urlpatterns = [
    #rote, view adm and reference name
    #cars.com/
    path('', views.home,  name='home'),
    #car.com/cars-list
    path('cars-list', views.cars, name='cars_list'),
]