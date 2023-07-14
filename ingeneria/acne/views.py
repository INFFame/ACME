from django.shortcuts import render
from .models import Producto


# Create your views here.

def index(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/index.html',data)

def formulario(request):
    data = {
        'form' :ProductoForm()
    }
    return render(request, 'app/formulario.html', data)

def login(request):
    return render(request, 'app/login.html')