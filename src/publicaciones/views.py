from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from publicaciones.models import Publicaciones, Comentario
from django.views.generic import ListView, CreateView, UpdateView , DeleteView, DetailView
from .forms import CrearPublicacionForm , ComentarioForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import SuperusuarioAutorMixin, ColaboradorMixin
from django.core.exceptions import PermissionDenied




# View que renderiza las publicaciones
class VerPublicaciones(ListView):
    model = Publicaciones
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'posteos'


    def get_queryset(self):
        consulta_anterior = super().get_queryset()
        return consulta_anterior.order_by('fecha')


#View que crea posteos nuevos
class Postear(ColaboradorMixin, LoginRequiredMixin, CreateView):
    model = Publicaciones
    template_name = 'publicaciones/postear.html'
    form_class = CrearPublicacionForm

    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    
    def form_valid(self, form):
        f = form.save(commit=False) # le paro el carro para que no guarde todavia
        f.creador_id = self.request.user.id
        return super().form_valid(f)
               


#View que actualiza una publicacion ya existente

class EditarPost(SuperusuarioAutorMixin, LoginRequiredMixin, UpdateView):
    model = Publicaciones
    template_name = 'publicaciones/editar-post.html'
    form_class = CrearPublicacionForm

    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    

# View que elimina un posteo
class EliminarPost(SuperusuarioAutorMixin, LoginRequiredMixin, DeleteView):
    template_name = 'publicaciones/eliminar-post.html'
    model = Publicaciones

    def get_success_url(self):
        return reverse('publicaciones:publicaciones')


# View para ver mas

class PostDetalle(DetailView):
    template_name = 'publicaciones/detalle-post.html'
    model = Publicaciones
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formulario_comentario'] = ComentarioForm()
        return context
    
    def post(self, request, *args, **kwargs):

        if not self.request.user.is_authenticated:
            return redirect('usuarios:login')

        publicacion = self.get_object()
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor_id = self.request.user.id
            comentario.post = publicacion
            comentario.save()
            return super().get(request)
        else:
            return super().get(request)
        

# View que borra comentarios

class BorrarComertarioView(SuperusuarioAutorMixin, LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'publicaciones/borrar-comentario.html'

    def get_success_url(self):
        return reverse('publicaciones:detalle-post', args = [self.object.post.id])


          
