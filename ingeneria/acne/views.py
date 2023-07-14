from django.shortcuts import render, redirect,get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.

def index(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    
    return render(request, 'app/index.html', data)

def formulario(request):
   
    return render(request, 'app/formulario.html', )

def login(request):
    return render(request, 'app/login.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')

def cajas(request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    return render(request, 'app/cajas.html', {'producto': producto})
def agregar_producto(request):

    data ={
        'form': ProductoForm()
    }
    if request.method == 'POST':
        stock = ProductoForm (data=request.POST, files=request.FILES)
        if stock.is_valid():
            stock.save()
            messages.success(request, "Se agregó correctamente") 
        else:
            data["form"] = stock

    return render(request, 'app/producto/agregar.html',data)  
def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity':productos,
        'paginator': paginator
    }
    return render(request, 'app/producto/listar.html', data)

def modificar_producto(request, id):
    producto = get_object_or_404(Producto, codigo=id)  
    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        stock = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if stock.is_valid():
            stock.save()
            messages.success(request, "modificado correctamente")
            return redirect(to=listar_productos)
        data['form'] = stock

    return render(request, 'app/producto/modificar.html', data)  
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, codigo=id)  
    producto.delete()
    messages.success(request, "eliminado correctamente")
    return redirect(to="listar_productos")  
