from django.db import models

# Create your models here.

class Clientes(models.Model):
    
    Id_Cliente = models.CharField(primary_key=True, max_length=6)
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Fecha_Nac = models.CharField(max_length=100)
    Edad = models.IntegerField()
    Telefono = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Nombres