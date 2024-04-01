from django.shortcuts import render
from .models import Car
from .forms import CarForm

def home(request):
    return render(request, 'cars/home.html')
def create_new_car (request):
    #Save new car in database
    new_car = Car()
    new_car.car_name = request.POST.get('name')
    new_car.car_year = request.POST.get('year')
    new_car.save()

def get_all_cars(request):
    #show all cars
    cars = {
        'cars': Car.objects.all()
    }
    return render(request, 'cars/cars.html', cars)

def get_one_car(request):
    if(request.method == "POST"):
        id = request.POST.get('id')
        requested_car = Car.objects.filter(id = id)

        if requested_car.exists():
            car = requested_car.first
            return render(request, 'find_car.html', {'car' : car})
        else:
            error_message = "No users found using the given parameters"
            return render(request, 'find_car.html',  {'error': error_message})
    return render(request,'find_car.html')


def update_car (request):
    if (request.method=="POST") :

        id = int(request.POST['hidden-input'])

        car = Car.objects.get(pk=id)
        if(car.exists()): 
            car.car_name = request.POST["name"]
            car.car_year = request.POST["year"]

            car.save()

            return render(request, 'update_car.html', {'car': car})
        else:
            context = {"Error":"Car does not exist"}
            return render(request,"update_car.html",context)
            
    return render(request,"update_car.html", {})

def delete_car (request):
    if (request.method== "POST") :
        id = int(request.POST['deleteId'] )
        car = Car.objects.get(pk=id)
        
        try:
          car.delete()
          all_cars = Car.objects.all()
          return render(request, 'cars.html',{'cars':all_cars})
        except Exception as e:
           context={"Error":"Cannot delete this car!"+ str(e)}
           return render(request,'cars.html',context)    
    cars = Car.objects.all();
    return render(request,'cars.html',{"cars":cars})