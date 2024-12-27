from django import forms
from cars.models import Brand


class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all()) # chave estrangeira, irá fazer uma consulta para trazer
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.DecimalField(max_digits=10, decimal_places=2)
    photo = forms.ImageField()

