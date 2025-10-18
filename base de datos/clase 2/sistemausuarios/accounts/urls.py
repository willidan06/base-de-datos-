from django.urls import path
from . import api
urlpatterns = [
    path('pokemons/<int:user_id>/', api.get_pokemons, name='get_pokemons'),
    path('pokemons/', api.get_allpokemons, name='get_allpokemons'),
    path('pokemons/create/', api.create_pokemon, name='create_pokemon'),
    path('pokemons/update/<int:pokemon_id>', api.update_pokemon, name='update_pokemon'),
    path('pokemons/delete/<int:pokemon_id>', api.delete_pokemon, name='delete_pokemon'),
]
