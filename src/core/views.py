from django.shortcuts import render


# view que renderiza la pagina de inicio
def indexView(request):
    return render(request, 'index.html', {})

def contactoView(request):
    return render(request, 'contacto/contacto.html', {})

def quienesSomosView(request):
    return render(request, 'contacto/quienes-somos.html', {})
