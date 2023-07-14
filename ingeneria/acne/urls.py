from django.urls import path
from .views import index,formulario,login

urlpatterns = [
    path('', index, name="index"),
    path('formulario/', formulario, name="formulario"),
    path('login/', login, name="login"),
]