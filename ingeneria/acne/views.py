from django.shortcuts import render, get_object_or_404
from .models import Producto



# Create your views here.

def index(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    
    return render(request, 'app/index.html', data)

def formulario(request):
    data = {
        'form' :ProductoForm()
    }
    return render(request, 'app/formulario.html', data)

def login(request):
    return render(request, 'app/login.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')

def cajas(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    return render(request, 'app/cajas.html', {'producto': producto})

