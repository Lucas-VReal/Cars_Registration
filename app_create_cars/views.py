from django.shortcuts import render
from .models import Car

def home(request):
    return render(request, 'cars/home.html')
def cars (request):
    #Save new car in database
    new_car = Car()
    new_car.car_name = request.POST.get('name')
    new_car.car_year = request.POST.get('year')
    new_car.save()
    #show all cars
    cars = {
        'cars': Car.objects.all()
    }
    return render(request, 'cars/cars.html', cars)