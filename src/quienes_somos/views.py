from django.shortcuts import render
from django.urls import reverse

def quienesSomosView(request):
    return render(request, 'contacto/quienes-somos.html', {})

    





