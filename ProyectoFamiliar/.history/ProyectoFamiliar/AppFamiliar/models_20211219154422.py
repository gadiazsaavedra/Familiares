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
        return f"Padres: {self.nombre} APELLIDO: {self.apellido} TELEFONO: {self.telefono} DIRECCION: {self.direccion} CORREO: {self.correo} FECHA_NACIMIENTO: {self.fecha_nacimiento} PARENTESCO: {self.parentesco}"
    
class Hijo(models.Model):
    apellido = models.CharField(max_length=50)
    nu = models.CharField(max_length=50)
    esIntelligente = models.BooleanField(default=False)
    
class Conyuge(models.Model):
    nombre = models.CharField(max_length=50)
    casada = models.BooleanField(default=False)
    
class Abuelos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    def __str__(self):
        return f"Abuelos: {self.nombre} APELLIDO: {self.apellido} EDAD: {self.edad}"
    
class Primo(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    profesional = models.BooleanField()
    fechaDeNacimiento = models.DateField()
    
    #def __str__(self):
        #return f"Primo: {self.nombre} APELLIDO: {self.apellido} DNI: {self.dni} PROFESIONAL: {self.profesional} FECHA_NACIMIENTO: {self.fechaDeNacimiento}"
