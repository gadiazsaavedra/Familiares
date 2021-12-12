from django import forms

class AbuelosFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    direccion = forms.CharField(required=True)
    ciudad = forms.CharField(max_length=100)
    pais = forms.CharField(max_length=100)
    anio = forms.IntegerField()
    imagen = forms.ImageField()