from django.db import models
from django.contrib.auth.models import AbstractUser



class Usuario(AbstractUser):
    telefono = models.CharField(max_length=255)
    domicilio = models.CharField(max_length=255, blank=True, null=True)
    es_colaborador = models.BooleanField(default=False)
    es_visitante = models.BooleanField(default=True)
    es_miembro = models.BooleanField(default=False)
    imagen_perfil = models.ImageField(upload_to='imagenes_perfil', null=True, blank=True)
