from django.shortcuts import render
from django.http import HttpResponse
from AppFamiliar.models import Estadio
from AppFamiliar.forms import EstadioFormulario

def 
# Create your views here.
def inicio(request):
    return render(request, 'AppFamiliar/inicio.html')

def jugadores(request):
    return render(request, 'AppFamiliar/jugadores.html')

def estadioFormulario(request):
    if request.method == 'POST':
        miFormulario = EstadioFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            miFormulario.save()
        return HttpResponse(
            f"Nombre: {nombre} Capacidad: {capacidad} Ubicacion: {ubicacion}"
        )

    return render(request, 'AppFamiliar/estadioFormulario.html')
    