from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
from django.views.generic import ListView, CreateView

# importa meu model, forms, views etc

# def cars_views(request):
#     search = request.GET.get('search')
#     # captura a request digitada na url: /cars/?search=Fox

#     # cars = Car.objects.filter(brand=2)
#     # cars = Car.objects.filter(brand__name="Fiat")
#     cars = Car.objects.filter(model__icontains=search).order_by('model') if search else Car.objects.all().order_by(
#         '-model')
#     # Campo__função
#     # cars = Car.object.all()
#     # retonar um QuerySet
#     # select * from cars, seria basicamente essa sintaxe
#     # ao verificar no navegador e olhar no terminal é apresentado um QuerySet

#     return render(
#         request=request,
#         template_name='cars.html',
#         context={'cars': cars}
#     )
# acima está a forma "antiga"

# class CarsView(View):
    
#     def get(self, request):

#         search = request.GET.get('search')
#         cars = Car.objects.filter(model__icontains=search).order_by('model') if search else Car.objects.all().order_by(
#         '-model')
        
#         return render(
#         request=request,
#         template_name='cars.html',
#         context={'cars': cars}
#     )
# Para ficar mais específico foi feita a melhoria abaixo:

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'    
    
    def get_queryset(self):
        search = self.request.GET.get('search', '').strip()
        cars = super().get_queryset().order_by('model')
#       super().get_queryset() chama a implementação padrão do ListView para obter todos os objetos do modelo Car.
#       O .order_by('model') organiza os carros por ordem crescente do campo model
#       É necessário pois, por padrão sempre a busca do django faz .all()        

        if search:
            cars = cars.filter(model__icontains=search)
        
        return cars
    
# def new_car_view(request):
#     if request.method == "POST":
#         # envia o formulário para enviar ao banco de dados
#         # irá capturar os dados e arquivos enviados via POST
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         # print(new_car_form.data)
#         if new_car_form.is_valid():
#             # verifica se os dados são válidos
#             new_car_form.save()
#             return redirect('cars_list')
#     else:
#         # retorna a página padrão, para o usuário preencher
#         new_car_form = CarModelForm()

#     return render(
#         request=request,
#         template_name='new_car.html',
#         context={'new_car_form': new_car_form})


# class NewCarView(View):
    
#     def get(self, request):
#         new_car_form = CarModelForm()
#         return render(
#             request=request,
#             template_name='new_car.html',
#             context={'new_car_form': new_car_form})
        
        
#     def post(self, request):
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#         return render(
#             request=request,
#             template_name='new_car.html',
#             context={'new_car_form': new_car_form})    
        
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars_list/'
    # no caso do render que usava new_car_form lá no html, basta trocar por form.as_table 
    # caso contrário é necessário personalizar       