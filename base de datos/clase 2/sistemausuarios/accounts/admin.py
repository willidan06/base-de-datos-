from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Profile, Pokemon, Habilidades

User = get_user_model()

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email')

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'nivel')
    list_filter = ('tipo',)
    search_fields = ('nombre',)

@admin.register(Habilidades)
class habilidadesAdmin(admin.ModelAdmin):
    list_display = ('habilidad', 'descripcion')
    search_fields = ('habilidad',)
