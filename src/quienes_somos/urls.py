from django.urls import path
from quienes_somos import views

app_name = 'quienes-somos'

urlpatterns = [
    path('quienes-somos/', views.quienesSomosView, name= 'quienes-somos'),
]

