import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
# login y register
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# ---------------------------------------------------------
from .forms import ProductoForm
from .models import Producto
# ------------------------------

# Create your views here.



# def index(request):
#     producto = Producto.objects.all()

#     return render(
#         request,
#         "index.html",
#         context={"productos":producto}
#     )
def index(request):
    # Mostrar solo los productos del usuario logueado
    productos = Producto.objects.filter(usuario=request.user)
    return render(request, 'index.html', {'productos': productos})

def detalle(request, producto_id):
    producto =get_object_or_404(Producto,id=producto_id)
    # producto = Producto.objects.get(id=producto_id)


    return render(
        request,
        "detalle.html",
        context={"producto":producto})


# validacion , agregar , actgualizar 
def formulario(request, id=None):
    producto = None
    form = ProductoForm()

    # 🔹 Búsqueda de producto por ID en el formulario
    if request.method == 'GET' and 'buscar_id' in request.GET:
        buscar_id = request.GET.get('buscar_id')
        if buscar_id:
            producto = Producto.objects.filter(id=buscar_id,usuario=request.user).first()
            if producto:
                return redirect('productos:editar_producto', id=producto.id)  # 🔥 Redirige a edición

    # 🔹 Si se está editando (ID en la URL)
    if id:
        producto = get_object_or_404(Producto, id=id,usuario=request.user)
        form = ProductoForm(instance=producto)

    # 🔹 Guardar producto (crear o actualizar)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user  # Asignamos el usuario logueado al producto
            producto.save()
            return redirect('productos:index')# Redirigir al índice

    return render(request, 'formulario.html', {'form': form, 'producto': producto})


# 🔥 Vista para eliminar un producto
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id, usuario=request.user)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos:index')  # Redirigir al índice
    return render(request, 'eliminar.html', {'producto': producto})





def damefecha(request):
    fecha_actual=datetime.datetime.now()

    return render(
        request,
        "fecha.html",
        context= {"fecha_actual":fecha_actual}
        
    )


# inicio de secion y registro
def register_login(request):
    if request.user.is_authenticated:
        return redirect('/home')  # Si el usuario ya está logueado, redirigir a productos
    
    if request.method == "POST":
        if "register" in request.POST:  # Si el usuario se está registrando
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            
            if User.objects.filter(username=username).exists():
                messages.error(request, "El usuario ya existe")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)  # Iniciar sesión automáticamente después de registrarse
                return redirect("/home")  # Redirigir a productos después del registro
        
        elif "login" in request.POST:  # Si el usuario está iniciando sesión
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/home")  # Redirigir a productos después de iniciar sesión
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
    
    return render(request, "register_login.html")




def logout_view(request):
    logout(request)  # Cerrar sesión
    return redirect('/')