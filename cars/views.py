from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm
# importa meu model, forms, views etc

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


def new_car_view(request):
    
    if request.method == "POST":
        # envia o formulário para enviar ao banco de dados
        # irá capturar os dados e arquivos enviados via POST
        new_car_form = CarForm(request.POST, request.FILES)
        # print(new_car_form.data)
        if new_car_form.is_valid():
            # verifica se os dados são válidos
            new_car_form.save()
            return redirect('cars_list')
    else:
        # retorna a página padrão, para o usuário preencher
        new_car_form = CarForm()
        
    return render(
        request=request,
        template_name='new_car.html', 
        context={'new_car_form': new_car_form})
    
    