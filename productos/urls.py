from django.urls import path
from . import views


app_name = 'productos'

urlpatterns = [
    path('',views.index, name='index'),

    # ----------------url para editar actualizar y borrar ----------------
    path('formulario',views.formulario, name='formulario'),
    path('formulario/<int:id>/', views.formulario, name='editar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    # -----------------------------------------------------------------------

    path('<int:producto_id>', views.detalle, name='detalle'),

    path ('fecha/',views.damefecha, name='fecha'),

    path('register_login/', views.register_login, name='register_login'),

    path('logout/', views.logout_view, name='logout'),

]