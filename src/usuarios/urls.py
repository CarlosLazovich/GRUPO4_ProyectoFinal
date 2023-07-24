from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistroView

app_name = 'usuarios'

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'usuarios/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = 'usuarios:login'), name = 'logout'),
    path('registrarse/', RegistroView.as_view(), name='registrarse')
]
