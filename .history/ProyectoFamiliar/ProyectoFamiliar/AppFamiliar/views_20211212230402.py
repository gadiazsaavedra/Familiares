from django.shortcuts import render
from django.http import HttpResponse
from AppFamiliar.models import Abuelos, Conyuge
from AppFamiliar.forms import AbuelosFormulario

def busquedaConyuge(request):
    return render(request, 'AppFamiliar/busquedaConyuge.html')

def buscar(request):
    #if request.GET["nombre"]:
        #nombre = request.GET['nombre']
        #conyuge = Conyuge.objects.filter(nombre__icontains=nombre)
    
        #return render(request, 'AppFamiliar/resultadoBusqueda.html', {'conyuge': conyuge, 'nombre': nombre})
    #else:
        respuesta = "Porfa ingresar un nombre"
    respuesta 
    return HttpResponse(respuesta)
# Create your views here.
def  abuelosFormulario(request):
    if request.method == 'POST':
        miFormulario = AbuelosFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                abuelos = Abuelos(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'])               
                abuelos.save()
                return render(request, 'AppFamiliar/inicio.html')
    else:
        miFormulario = AbuelosFormulario()
        
        
    return render(request, 'AppFamiliar/abuelosFormulario.html', {'miFormulario': miFormulario})

def inicio(request):
    return render(request, 'AppFamiliar/inicio.html')

def hijos(request):
    return render(request, 'AppFamiliar/hijos.html')

def conyuge(request):
    return render(request, 'AppFamiliar/conyuge.html')

    