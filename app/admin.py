from django.contrib import admin
from .models import Marca, UserComplex, Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "marca"]
    search_fields = ["nombre"]
    list_filter = ["marca", "nuevo"]

class userComplexList(admin.ModelAdmin):
    list_display = ["nombre","apellidos","correo","status","tipoUsuario","fechaCreacion"]
    search_fields = ["nombre","correo"]


admin.site.register(Marca)
admin.site.register(UserComplex, userComplexList)
admin.site.register(Producto, ProductoAdmin)