from django.db import models

# Create your models here.

class Producto(models.Model):
    idd= models.IntegerField()
    nombre = models.CharField(max_length = 50, null=False)
    precio = models.CharField(max_length = 50, null=False)
    stock = models.IntegerField(default = 0)
    provedor = models.ForeignKey("Proveedores", related_name='+',  on_delete=models.CASCADE,null = False,)
    categoria = models.ForeignKey("Categoria", related_name='+',  on_delete=models.CASCADE,null = False,)

    def __str__(self):
        return self.nombre
        
class Categoria(models.Model):
    idd= models.IntegerField(default = 0)
    nombre = models.CharField(max_length = 50, null=False)
    descripcion = models.CharField(max_length = 50, null=False)
    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    calle = models.CharField(max_length = 50, null=False)
    numero = models.CharField(max_length = 50, null=False)
    comuna = models.CharField(max_length = 50, null=False)
    ciudad = models.CharField(max_length = 50, null=False)
    def __str__(self):
        return self.calle + ", " + self.ciudad

class Proveedores(models.Model):
    nombre = models.CharField(max_length = 50, null=False)
    web = models.CharField(max_length = 50, null=False)
    rut = models.CharField(max_length = 50, null=False)
    telefono = models.CharField(max_length = 50, null=False)
    direccion = models.ForeignKey("Direccion", related_name='+',  on_delete=models.CASCADE,null = False,)
    def __str__(self):
        return self.nombre

class Venta(models.Model):
    idd = models.IntegerField()
    fecha = models.CharField(max_length = 50)
    montofinal = models.CharField(max_length = 50, null=False)
    descuento = models.BooleanField(default = 0)
    cliente = models.ForeignKey("Cliente", related_name='+',  on_delete=models.CASCADE, null = False,)
    def Descc(self):
        return self.descuento
    Descc.boolean = descuento
    Descc.short_description = 'Tiene Descuento'
    def __str__(self):
        return self.fecha 

class Cliente(models.Model):
    nombre = models.CharField(max_length = 50, null=False)
    rut = models.CharField(max_length = 50, null=False)
    telefono = models.CharField(max_length = 50, null=False)
    direccion = models.ForeignKey("Direccion", related_name='+',  on_delete=models.CASCADE,null = False,)
    def __str__(self):
        return self.nombre