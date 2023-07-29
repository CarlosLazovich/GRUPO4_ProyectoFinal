from django import forms
from .models import Publicaciones, Comentario

class CrearPublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicaciones
        fields = ('categoria', 'titulo', 'post', 'imagen_publicacion')
        labels = {
            'titulo' : '',
            'post' : '',
            'categoria': 'SELECCIONAR CATEGORIA',
        }

        widgets = {
            'titulo' : forms.TextInput(attrs= {'placeholder' : 'TITULO'}),
            'post' : forms.TextInput(attrs= {'placeholder' : 'TEXTO'})
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        labels = {
            'texto' : '',
        }
        widgets = {
            'texto' : forms.TextInput(attrs= {'placeholder' : 'Deja tu comentario'}),
        }