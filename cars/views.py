from django.shortcuts import render
from cars.models import Car 
# importa meu model

def cars_views(request):
    search = request.GET.get('search')
    # captura a request digitada na url: /cars/?search=Fox
    
    # cars = Car.objects.filter(brand=2)
    # cars = Car.objects.filter(brand__name="Fiat")
    cars = Car.objects.filter(model__icontains=search).order_by('model') if search else Car.objects.all().order_by('-model')
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
