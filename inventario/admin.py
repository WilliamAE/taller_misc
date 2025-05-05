from django.contrib import admin
from .models import Producto, Categoria, Valor, Cantidad

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Valor)
admin.site.register(Cantidad)
