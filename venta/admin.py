from django.contrib import admin
from .models import *

# Register your models here.

class ClienteAdmin (admin.ModelAdmin):
    list_display = ['rut' , 'nombre', 'telefono']
    list_filter = ['nombre' , 'telefono']

class ProductoAdmin (admin.ModelAdmin):
    fieldsets = (('Descripcion', {'fields': ('idd', 'nombre',)}) , ('Variable', {'fields': ('precio', 'stock' )}), )


class ProductoInLine(admin.TabularInline):
    model = Producto

class ProveedoresFilt(admin.ModelAdmin):
    list_display = ['rut', 'nombre' , 'direccion', 'telefono']
    list_display_links = ['rut' , 'nombre'] 
    list_filter = ['nombre']
    inlines = [ProductoInLine, ]

class VentaAdmin(admin.ModelAdmin): 
    list_display = ['fecha', 'cliente', 'Descc']
    list_display_links = ['fecha' , 'cliente', ]
    actions = ['desc']
 
    def descuentoo(self,request,queryset):
        return queryset.update(descuento = True)

class CategoriaAdmin (admin.ModelAdmin):
    list_display = ['idd' , 'nombre', 'descripcion']

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Proveedores,ProveedoresFilt)
admin.site.register(Venta,VentaAdmin)
admin.site.register(Direccion)
