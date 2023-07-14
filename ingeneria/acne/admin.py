from django.contrib import admin
from .models import Categoria,Producto,Contenido

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display =  ["nombre","precio","stock","categoria"]
    list_editable =["precio"]
    search_fields =["nombre"]
    list_filter = ["stock"]
    list_per_page = 5

class ContenidoAdmin(admin.ModelAdmin):
    list_display =  ["nombreContenido","stock"]
    list_editable =["stock"]
    search_fields =["nombreContenido"]
    list_per_page = 5

admin.site.register(Categoria)
admin.site.register(Contenido,ContenidoAdmin)
admin.site.register(Producto,ProductoAdmin)
