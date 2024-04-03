from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm

def home(request):
    return render(request, 'home.html')

def create_new_car (request):
    #Save new car in database
    if(request.method == 'POST'):
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form=CarForm()
    return render(request,'create_car.html',{'form':form}) 
    

def get_all_cars(request):
    #show all cars
    cars = {
        'cars': Car.objects.all()
    }
    return render(request, 'cars.html', cars)

def get_one_car(request):
    if(request.method == "POST"):
        car_id = request.POST.get('car_id')
        try:
            car = Car.objects.get(car_id=car_id)
            return render(request, 'find_car.html', {'car': car})
        except Car.DoesNotExist:
            error_message = "Car not found with the provided ID."
            return render(request, 'find_car.html', {'error_message': error_message})
    else:
        return render(request, 'find_car.html')


def update_car(request, car_id):
    if request.method == "POST":
        car = Car.objects.get(car_id=car_id)
        form = CarForm(request.POST, instance=car)

        if form.is_valid():
            form.save()
            return redirect('cars')
        else:
            form = CarForm(instance=car)

    return render(request, "cars.html", {'form': form})

def delete_car(request, car_id):
    if request.method == "POST":
        try:
            car = Car.objects.get(pk=car_id)
            car.delete()
            all_cars = Car.objects.all()
            return render(request, 'cars.html', {'cars': all_cars})
        except Car.DoesNotExist:
            error_message = "Car not found with the provided ID."
            return render(request, 'cars.html', {'error_message': error_message})
        except Exception as e:
            context = {"Error": "Cannot delete this car! " + str(e)}
            return render(request, 'cars.html', context)
    else:
        cars = Car.objects.all()
        return render(request, 'cars.html', {'cars': cars})

