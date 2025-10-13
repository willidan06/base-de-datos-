from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Pokemon, Profile, Habilidades

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_pokemon(sender, instance, created, **kwargs):
    if created:
        # Aquí puedes personalizar los valores iniciales del Pokémon
        Pokemon.objects.create(nombre='Pikachu', tipo='Eléctrico', nivel=5, user=instance)

@receiver(post_save, sender=User)
def create_habilidades(sender, instance, created, **kwargs):
    if created:
        Habilidades.objects.create(habilidad='Impactrueno', descripcion='Un ataque eléctrico poderoso', user=instance)
