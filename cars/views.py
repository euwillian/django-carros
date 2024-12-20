from django.shortcuts import render
from cars.models import Car 
# importa meu model

def cars_views(request):
    cars = Car.objects.filter(brand=2)
    print(cars)
    # retonar um QuerySet
    # select * from cars, seria basicamente essa sintaxe
    # ao verificar no navegador e olhar no terminal é apresentado um QuerySet
    
    return render(
        request=request, 
        template_name='cars.html', 
        context= {'cars': cars }
        )
