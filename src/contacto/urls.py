from django.urls import path
from .views import ContactanosView, mensaje_enviado



app_name = 'contacto'

urlpatterns = [
    path('enviar-mensaje/', ContactanosView.as_view(), name = 'enviar-mensaje'),
    path('mensaje-enviado/', mensaje_enviado, name='mensaje-enviado')
]