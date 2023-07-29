from django.urls import path, include
from core import views 



urlpatterns = [
    path('', views.indexView, name = 'index'),
    

    # includes
    path('publicaciones/', include('publicaciones.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('contacto/', include('contacto.urls')),
    path('quienes-somos/', include('quienes_somos.urls')),   
]

