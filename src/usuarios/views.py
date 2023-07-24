from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import RegistrarseForm
from django.urls import reverse
from django.contrib.auth import login


# Vista basada en clases que crea un usuario
class RegistroView(CreateView):
    model = Usuario
    template_name = 'usuarios/registro.html'
    form_class = RegistrarseForm

    def get_success_url(self):
        return reverse('index')


    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response
        
