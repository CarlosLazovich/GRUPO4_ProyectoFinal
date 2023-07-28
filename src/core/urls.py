from django.urls import path, include
from core import views  


urlpatterns = [
    path('', views.indexView, name = 'index'),
    path('contacto/', views.contactoView, name = 'contacto'),
    path('quienes-somos/', views.quienesSomosView, name = 'quienes-somos'),

    # includes
    path('publicaciones/', include('publicaciones.urls')),
    path('usuarios/', include('usuarios.urls')),
]

