from django.contrib import admin
from django.urls import path
from app_create_cars.views import *

urlpatterns = [
    #rote, view adm and reference name
    #cars.com/
    path('', home,  name='home'),
    #Get All Cars
    #car.com/cars-list
    path('cars-list', get_all_cars, name='cars'),
    #Get One Car
    #car.com/find_car
    path('find-a-car/', get_one_car, name="find_car"),
    #Create a new car
    #car.com/add-new-car
    path('add-new-car/', create_new_car, name='add_car'),
    #Update a car
    #car.com/update-car/id
    path('update-car/<int:pk>/', update_car, name='update_car'),
    #Delete a car
    #car.car/delete-car/id
    path('delete-car/<int:pk>', delete_car, name='delete_car'),
]