from django import forms

class AbuelosEstadioFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    capacidad = forms.IntegerField()
    direccion = forms.CharField(max_length=100)
    ciudad = forms.CharField(max_length=100)
    pais = forms.CharField(max_length=100)
    anio = forms.IntegerField()
    imagen = forms.ImageField()