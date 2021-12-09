from django.db import models

# Create your models here.
class Padres(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    parentesco = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
class Hijos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    
class Conyuge(models.Model):
    nombre = models.CharField(max_length=50)
    casada = models.BooleanCharField(max_length=50)