from . import models 
from django.forms import ModelForm
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'stock', 'puntaje','categoria']

  