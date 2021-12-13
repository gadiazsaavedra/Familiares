from django import forms

class AbuelosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    direccion = forms.CharField(max)
    ciudad = forms.CharField(max_length=40)