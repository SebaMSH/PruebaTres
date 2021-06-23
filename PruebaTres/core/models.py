from django.db import models

# Create your models here.
class Proveedores(models.Model):
    idProveedor = models.IntegerField(primary_key=True, verbose_name="Id de Proveedor")
    Nombre = models.CharField(max_length=100, verbose_name="Nombre Proveedor")
    

    def __str__(self):
        return self.patente