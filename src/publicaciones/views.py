from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from publicaciones.models import Publicaciones, Comentario, Categoria
from django.views.generic import ListView, CreateView, UpdateView , DeleteView, DetailView
from .forms import CrearPublicacionForm , ComentarioForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import SuperusuarioAutorMixin, ColaboradorMixin, VisitanteMixin, MiembroMixin
from django.core.exceptions import PermissionDenied




# View que renderiza las publicaciones
class VerPublicaciones(ListView, VisitanteMixin):
    model = Publicaciones
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'posteos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all
        return context


    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtrando por categoria
        categoria_seleccionada = self.request.GET.get('categoria')
        if categoria_seleccionada:
            queryset = queryset.filter(categoria = categoria_seleccionada)


        # Ordenando por distintos criterios
        orden = self.request.GET.get('orderby')
        if orden:
            if orden == 'fecha_asc':
                queryset = queryset.order_by('fecha')
            elif orden == 'fecha_desc':
                queryset = queryset.order_by('-fecha')
            elif orden == 'alf_asc':
                queryset = queryset.order_by('titulo')
            elif orden == 'alf_desc':
                queryset = queryset.order_by('-titulo')              


        return queryset


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

class PostDetalle(DetailView, MiembroMixin, VisitanteMixin):
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

class BorrarComertarioView(SuperusuarioAutorMixin, MiembroMixin, LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'publicaciones/borrar-comentario.html'

    def get_success_url(self):
        return reverse('publicaciones:detalle-post', args = [self.object.post.id])
    

def me_gusta(request):
    if request.method == 'POST':
        publicacion_id = request.POST.get('publicacion_id')
        publicacion = get_object_or_404(Publicaciones, id = publicacion_id)
        usuario = request.user

        if publicacion.meGusta.filter(id=usuario.id).exists():
            publicacion.meGusta.remove(usuario)
        else:
            publicacion.meGusta.add(usuario)

    return redirect('publicaciones:publicaciones')        



          
