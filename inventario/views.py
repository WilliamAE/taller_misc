from rest_framework import viewsets
from .models import Categoria, Producto, Inventario, Movimiento
from .serializers import CategoriaSerializer, ProductoSerializer,InventarioSerializer, MovimientoSerializer
from rest_framework.response import Response
from rest_framework import status

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    

class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer

    def perform_create(self, serializer):
        movimiento = serializer.save()
        inventario, created = Inventario.objects.get_or_create(producto=movimiento.producto)
        
        if movimiento.tipo == 'ENTRADA':
            inventario.cantidad_disponible += movimiento.cantidad
        elif movimiento.tipo == 'SALIDA':
            if inventario.cantidad_disponible >= movimiento.cantidad:
                inventario.cantidad_disponible -= movimiento.cantidad
            else:
                raise serializer.ValidationError("No hay suficiente inventario para esta salida.")
        
        inventario.save()
