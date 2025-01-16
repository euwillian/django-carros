from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Essa herança já está pronta
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='fk_car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    photo = models.ImageField(upload_to='cars/', blank=False, null=False)
    bio = models.TextField(blank=True, null=True, max_length=120)

    # tem dependencia da biblioteca Python -m install Pillow (manipular imagens)

    def __str__(self):
        """Funcao padrao de Model que retorna "Car object (1)", subscrevemos"""
        return self.model


class CarInventory(models.Model):
    id = models.AutoField(primary_key=True)
    # não é necessário criar o campo ID, o django cria automático
    cars_count = models.IntegerField(blank=False, null=False)   
    cars_value = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-id']
        # Dessa forma ao buscar no banco de dados irá ordenar de forma decrescente (usando o menos -)
    
    
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'
    