from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum


# @receiver(pre_save, sender=Car)
# def car_pre_save(sender, instance, **kwargs):
#     # Função antes de salvar o carro
#     # sender => quem está enviado o este evento para o signal, no caso nosso model car
#     # Irá monitorar dentro da tabela Car (Sender), eventos pre save
#     print("*** PRE SAVE (antes de salvar) ***")
#     if instance.value > 50000:
#         print("Enviando email para o dono: boss@python.com")

def car_inventory_update():
    # Função de update do veículo
    cars_count = Car.objects.all().count()
    # irá retornar a quantidade de registros no banco de dados
    cars_value = Car.objects.aggregate(
        total_value=SUM('value')
    )['total_value']
    # Irá somar todos os valores do campo value, se não colocar ['total_value'] retorna um dict
    
    CarInventory.objects.create(cars_count=cars_count, cars_value=cars_value)
    # Insert no banco de dados -> persistir
    

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    # Função após salvar o carro
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    # Função após excluir um carro
    car_inventory_update()
    

# @receiver(pre_delete, sender=Car)
# def car_pre_delete(sender, instance, **kwargs):
#     # Função antes de excluir um carro
#     print("*** PRE DELETE (antes de excluir) ***")   
#     print(instance)