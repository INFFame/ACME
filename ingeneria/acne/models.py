from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="ID categoria")
    nombreCategoria = models.CharField(max_length=50 , verbose_name="Nombre categoria")

    def __str__(self):
        return self.nombreCategoria
    
class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10, verbose_name="Codigo")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    precio = models.IntegerField(verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    imagen = models.ImageField(upload_to="productos", null=True, blank=True, verbose_name="Imagen")

    def __str__(self):
        return self.nombre
    
class Contenido(models.Model):
    idContenido = models.IntegerField(primary_key=True, verbose_name="ID contenido")
    nombreContenido = models.CharField(max_length=50 , verbose_name="Nombre producto")
    stock = models.IntegerField(default=0, verbose_name="Stock Prod")

    def __str__(self):
        return self.nombreContenido
    
