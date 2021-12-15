from django import forms
import datetime

class AbuelosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.CharField(max_length=40)
    
class 