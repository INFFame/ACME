from django.urls import path
from .views import index,formulario,login,cajas,contacto,nosotros

urlpatterns = [
    path('', index, name="index"),
    path('formulario/', formulario, name="formulario"),
    path('login/', login, name="login"),
    path('cajas/<int:codigo>', cajas, name="cajas"),
    path('contacto/', contacto, name="contacto"),
    path('nosotros/', nosotros, name="nosotros"),
]