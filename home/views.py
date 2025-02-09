from django.shortcuts import render
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse


# Create your views here.
# def home(request):
#     return render(request, 'home.html')  # Cambiado a 'index.html'

# def perfil(request):
#     # Puedes agregar información del perfil del usuario aquí si lo deseas
#     return render(request, 'perfil.html')  # Asegúrate de tener un template llamado 'perfil.html'

def home(request):
    return render(request, 'home/home.html')  # Asegúrate de que la plantilla esté en esta ruta

def perfil(request):
    return render(request, 'home/perfil.html')  # La plantilla para el perfil


def logout_view(request):
    logout(request)  # Cerrar sesión
    return redirect('/')