from django.shortcuts import render
from django.http import HttpResponse
from AppFamiliar.models import Abuelos, Conyuge
from AppFamiliar.forms import AbuelosFormulario

def busquedaConyuge(request):
    return render(request, 'AppFamiliar/busquedaConyuge.html')

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        conyuge = Conyuge.objects.filter(nombre=nombre)
    respuesta = f"Estoy buscando"
    return render(request, 'AppFamiliar/buscar.html')
# Create your views here.
def inicio(request):
    return render(request, 'AppFamiliar/inicio.html')

def jugadores(request):
    return render(request, 'AppFamiliar/jugadores.html')

def  estadioFormulario(request):
    if request.method == 'POST':
        miFormulario = EstadioFormulario(request.POST)
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                
                miFormulario.save()
        return HttpResponse("Nombre: " + nombre + " Capacidad: " + capacidad + " Ubicacion: " + ubicacion)
    return render(request, 'AppFamiliar/estadioFormulario.html')
    