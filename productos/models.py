from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)
    # con CharField  podemos indicar cuanto texto queremos en ese campo 
    # maximo un string de 255 caracterees el maximo lo decides tu
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje= models.FloatField()
    # CASCADE:  eliminar el producto
    # PROTECT: lanza un error
    # RESTRICT: solo elimina si no existen productos
    # SET_NULL: actualiza a valor nulo
    # SET_DEFAULT: asigna valor por defecto
    categoria = models.ForeignKey(
        Categoria,
          on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='productos',default=1)
    
    # foreignkey para crear una relacion del producto en una categora en espesiofico


    creado_en = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nombre