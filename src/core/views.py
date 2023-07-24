from django.shortcuts import render


# view que renderiza la pagina de inicio
def indexView(request):
    return render(request, 'index.html', {})
