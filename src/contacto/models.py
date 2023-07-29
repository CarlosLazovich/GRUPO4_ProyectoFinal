from django.db import models
from usuarios.models import Usuario

class Contacto(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, related_name='contacto', null=True)

    def __str__(self):
        return self.asunto