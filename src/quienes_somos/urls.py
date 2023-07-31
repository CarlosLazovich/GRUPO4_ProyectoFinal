from django.urls import path
from quienes_somos import views

app_name = 'quienes-somos'

urlpatterns = [
    path('', views.quienesSomosView, name= 'quienes-somos'),
]

