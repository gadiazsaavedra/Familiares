from django.shortcuts import render
from django.http import HttpResponse
from AppFamiliar.models import Abuelos, Conyuge
from AppFamiliar.forms import AbuelosFormulario

def busquedaConyuge(request):
    return render(request, 'AppFamiliar/busquedaConyuge.html')

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        conyuge = Conyuge.objects.filter(nombre__icontains=nombre)
    
        return render(request, 'AppFamiliar/resultadoBusqueda.html', {'conyuge': conyuge, 'nombre': nombre})
    else:
        respuesta = "Porfa ingresar un nombre"
        
        
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
    