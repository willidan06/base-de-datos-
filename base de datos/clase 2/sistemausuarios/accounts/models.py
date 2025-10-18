from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.user.username} ({self.role})"

class Pokemon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pokemons', null=True, blank=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    nivel = models.IntegerField()

class Habilidades(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habilidades', null=True, blank=True)
    habilidad = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.habilidad}: {self.descripcion}"
