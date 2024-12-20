from django.shortcuts import render
from cars.models import Car 
# importa meu model

def cars_views(request):
    # cars = Car.objects.filter(brand=2)
    # cars = Car.objects.filter(brand__name="Fiat")
    cars = Car.objects.filter(model__contains="f")
    # Campo__função
    # cars = Car.object.all()
    # retonar um QuerySet
    # select * from cars, seria basicamente essa sintaxe
    # ao verificar no navegador e olhar no terminal é apresentado um QuerySet
    
    return render(
        request=request, 
        template_name='cars.html', 
        context= {'cars': cars }
        )
