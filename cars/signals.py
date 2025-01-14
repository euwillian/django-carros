from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    # Função antes de salvar o carro
    # sender => quem está enviado o este evento para o signal, no caso nosso model car
    # Irá monitorar dentro da tabela Car (Sender), eventos pre save
    print("*** PRE SAVE (antes de salvar) ***")
    if instance.value > 50000:
        print("Enviando email para o dono: boss@python.com")
    
    

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    # Função após salvar o carro
    print("*** PRE POST (apos salvar) ***")    
    print(instance)
    
    
@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    # Função antes de excluir um carro
    print("*** PRE DELETE (antes de excluir) ***")   
    print(instance)
    
    

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    # Função após excluir um carro
    print("*** PRE DELETE (após excluir) ***")       
    print(instance)