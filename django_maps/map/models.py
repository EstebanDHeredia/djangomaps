from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nombre de sucursal")
    address = models.CharField(max_length=250, verbose_name="Dirección")
    lat = models.FloatField(verbose_name="Latitud")
    lng = models.FloatField(verbose_name="Longitud")

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"
        ordering = ['name']

    def __str__(self) -> str:       
        return self.name

class client(models.Model):
    name = models.CharField(max_length=250, verbose_name="Nombre")
    address = models.CharField(max_length=250, verbose_name="Dirección")
    lat = models.FloatField(verbose_name="Latitud")
    lng = models.FloatField(verbose_name="Longitud")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['name']

    def __str__(self) -> str:
        return self.name