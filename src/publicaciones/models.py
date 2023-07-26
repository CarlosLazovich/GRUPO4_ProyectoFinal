from django.db import models
from usuarios.models import Usuario



# Esta clase crea una tabla para guardar las categorias
class Categoria(models.Model):
    nombre = models.CharField(max_length= 255)

    def __str__(self):
        return self.nombre





# Clase crea una tabla para las publicaciones
class Publicaciones(models.Model):
    fecha = models.DateField(auto_now_add = True)
    update = models.DateField(auto_now=True)
    titulo = models.CharField(max_length = 255)
    post = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, related_name= 'posteos', null= True) 
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='posteos_usuario')
    meGusta = models.ManyToManyField(Usuario, related_name='publicaciones_gustadas', blank=True)

    def __str__(self):
        return self.titulo
        

class Comentario(models.Model):
    texto = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Publicaciones, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='comentarios')


    def __str__(self):
        return self.post.titulo + '-' + self.autor.first_name

