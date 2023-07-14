from django.urls import path
from .views import index,formulario,login,cajas,contacto,nosotros,agregar_producto,\
listar_productos,modificar_producto,eliminar_producto

urlpatterns = [
    path('', index, name="index"),
    path('formulario/', formulario, name="formulario"),
    path('login/', login, name="login"),
    path('cajas/<int:codigo>', cajas, name="cajas"),
    path('contacto/', contacto, name="contacto"),
    path('nosotros/', nosotros, name="nosotros"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<int:id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<int:id>/', eliminar_producto, name="eliminar_producto"),

]