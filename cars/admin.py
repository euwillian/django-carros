from django.contrib import admin
from cars.models import Car

class CarAdmin(admin.ModelAdmin):
    # Cabeçalho
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    # Seção de busca
    search_fields = ('model', 'brand')
    
    """Tupla com um único elemento: Em Python, para criar uma tupla com um único elemento, 
    é necessário incluir uma vírgula no final, como em ('model',). 
    Caso contrário, o Python tratará os parênteses apenas como agrupamento de expressão e 
    interpretará 'model' como uma string, não uma tupla."""
    
admin.site.register(Car, CarAdmin)
