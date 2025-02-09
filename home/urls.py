from django.urls import path
from .views import home, perfil

app_name = 'home'  # Esto es opcional pero recomendado

urlpatterns = [
    path('', home, name='home'),
    path('perfil/', perfil, name='perfil'),
]