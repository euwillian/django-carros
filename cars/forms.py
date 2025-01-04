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

    def clean_value(self):
        # Django entende que essa é a forma de validação clean_nome_do_campo
        value = self.cleaned_data.get('value') # captura o valor que o usuário informou no form
        if value < 5000:
            self.add_error('value', "Erro: Valor mínimo do carro deve ser de R$ 5.000,00.")
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 2000:
            self.add_error('factory_year', 'Erro: ano de fabricação mínimo deve ser acima de 2000.')
        return factory_year
    
    # def clean_photo(self):
    #     Este trecho não é mais obrigatório pois, alteramos diretamente o models.py para não aceitar null na foto.
    #     photo = self.cleaned_data.get('photo')
        
    #     if photo is None:
    #         self.add_error('photo', "Erro: Não é possível gravar sem uma foto!")
    #     return photo