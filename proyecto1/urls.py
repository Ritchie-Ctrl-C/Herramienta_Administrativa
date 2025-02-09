"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from productos.views import register_login,logout_view,formulario,eliminar_producto
from home.views import perfil# Importamos la vista


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register_login, name='login'),#pendiente
    path('home/', include('home.urls')), #app
    path ('productos/', include('productos.urls')),#app
    path('perfil/', perfil, name='perfil'),
    path('logout/', logout_view, name='logout'),
    path('formulario/<int:id>/', formulario, name='editar_producto'),
    path('eliminar/<int:id>/', eliminar_producto, name='eliminar_producto'),

    

]
