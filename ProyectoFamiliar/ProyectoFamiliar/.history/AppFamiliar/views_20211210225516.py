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
        
    return HttpResponse(respuesta)
# Create your views here.
def  abuelosFormulario(request):
    if request.method == 'POST':
        miFormulario = AbuelosFormulario(request.POST)
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                abuelosInsta = Abuelos(direccion=informacion['direccion'], anio=informacion['anio'], nombre=informacion['nombre'], telefono=informacion['telefono'])                
                abuelosInsta.save()
                return render(request, 'AppFamiliar/')
        return HttpResponse("Nombre: " + nombre + " Capacidad: " + capacidad + " Ubicacion: " + ubicacion)
    return render(request, 'AppFamiliar/estadioFormulario.html')


def inicio(request):
    return render(request, 'AppFamiliar/inicio.html')

def jugadores(request):
    return render(request, 'AppFamiliar/jugadores.html')

    