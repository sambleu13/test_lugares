from django.db import models

# Create your models here.
class Lugar(models.Model):
    #id_nombre = models.IntegerField(primary_key=)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    #id_direccion = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Direccion(models.Model):
    sitio = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    calle = models.CharField(max_length=200)
    numero = models.IntegerField() #0 es S/N
    codigo_postal = models.IntegerField()
    colonia = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
