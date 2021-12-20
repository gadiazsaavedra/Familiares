from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class AbuelosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.CharField(max_length=40)
    
class PrimoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.IntegerField()
    profesional = forms.BooleanField()
    fechaDeNacimiento = forms.DateField()
    
class HijoFormulario(forms.Form):
    apellido = forms.CharField(max_length=40)
    numero = forms.IntegerField()
    esBueno = forms.BooleanField()