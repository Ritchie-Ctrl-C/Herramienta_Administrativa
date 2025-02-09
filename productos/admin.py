from django.contrib import admin
from .models import Producto,Categoria
# ---------------------------------------
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_filter = ("nombre",)

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre',"stock","puntaje","creado_en")
    list_filter = ("nombre","stock")
    search_fields = ("nombre",)


# ---------------------------------------
# Register your models here.
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductosAdmin)
 