from django.contrib import admin
from cars.models import Car, Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin):
    # Cabeçalho
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    # Seção de busca
    search_fields = ('model', 'brand__name')

    """Em Django, os dois underscores (__) no campo brand__name no atributo 
    search_fields são usados para acessar atributos de um modelo relacionado por 
    meio de lookup notation."""

    """Tupla com um único elemento: Em Python, para criar uma tupla com um único elemento, 
    é necessário incluir uma vírgula no final, como em ('model',). 
    Caso contrário, o Python tratará os parênteses apenas como agrupamento de expressão e 
    interpretará 'model' como uma string, não uma tupla."""


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
