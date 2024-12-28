from django import forms
from cars.models import Brand, Car


# class CarForm(forms.Form):
#     # Jeito trabalhoso de fazer
#     model = forms.CharField(max_length=200)
#     brand = forms.ModelChoiceField(Brand.objects.all())  # chave estrangeira, irá fazer uma consulta para trazer
#     factory_year = forms.IntegerField()
#     model_year = forms.IntegerField()
#     plate = forms.CharField(max_length=10)
#     value = forms.DecimalField(max_digits=10, decimal_places=2)
#     photo = forms.ImageField()

#     def save(self):
#         car = Car(
#             model=self.cleaned_data['model'],
#             brand=self.cleaned_data['brand'],
#             factory_year=self.cleaned_data['factory_year'],
#             model_year=self.cleaned_data['model_year'],
#             plate=self.cleaned_data['plate'],
#             value=self.cleaned_data['value'],
#             photo=self.cleaned_data['photo'],
#         )
#         car.save()
#         return car


class CarModelForm(forms.ModelForm):
    # Formulário avançado que linka com a tabela do banco de dados
    class Meta:
        model = Car
        fields = '__all__' #dunder all, irá considerar todos os campos do Model car
    