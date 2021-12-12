from django.shortcuts import render
from django.http import HttpResponse
from django
# Create your views here.
def inicio(request):
    return render(request, 'AppFamiliar/inicio.html')

def jugadores(request):
    return render(request, 'AppFamiliar/jugadores.html')

def  estadioFormulario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        capacidad = request.POST.get('capacidad')
        ubicacion = request.POST.get('ubicacion')
        return HttpResponse("Nombre: " + nombre + " Capacidad: " + capacidad + " Ubicacion: " + ubicacion)
    return render(request, 'AppFamiliar/estadioFormulario.html')
    