from django.shortcuts import render
from django.http import HttpResponse
from AppFamiliar.models import Abuelos, Conyuge, Primo, Hijo
from AppFamiliar.forms import AbuelosFormulario, PrimoFormulario, HijoFormulario


def editarHijo(request, numero_para_editar):
    hijo = Hijo.objects.get(numero=numero_para_editar)
    if request.method == 'POST':
        miFormulario = HijoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                hijo.apellido = informacion['apellido']
                hijo.numero = informacion['numero']
                hijo.esBueno = informacion['esBueno']
                hijo.save()
                return render(request, 'AppFamiliar/inicio.html')
    else:
        miFormulario = HijoFormulario(initial={'apellido': hijo.apellido, 'numero': hijo.numero, 'esBueno': hijo.esBueno})
        
        
    return render(request, 'AppFamiliar/editarHijo.html', {'miFormulario': miFormulario,"numero_para_editar": numero_para_editar})

def eliminarHijo(request, numero_para_borrar):
    hijoQueQuieroBorrar = Hijo.objects.get(numero=numero_para_borrar)
    hijoQueQuieroBorrar.delete()
    hijos = Hijo.objects.all()
    return render(request, 'AppFamiliar/leerHijos.html', {'hijos': hijos})

def leerHijos(request):
    hijos = Hijo.objects.all()
    dir = {"hijos": hijos}
    return render(request, 'AppFamiliar/leerHijos.html', dir)

def busquedaConyuge(request):
    return render(request, 'AppFamiliar/busquedaConyuge.html')

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        conyuge = Conyuge.objects.filter(nombre__icontains=nombre)
    
        return render(request, 'AppFamiliar/resultadoBusqueda.html', {'conyuge': conyuge, 'nombre': nombre})
    else:
        respuesta = "Porfa ingresar un nombre"
        #respuesta = f"Estoy buscando la conyuge de nombre : {request.GET['nombre']}"
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

def  primoFormulario(request):
    if request.method == 'POST':
        miFormulario = PrimoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                prim = Primo(nombre=informacion['nombre'], apellido=informacion['apellido'], dni=informacion['dni'], profesional=informacion['profesional'], fechaDeNacimiento=informacion['fechaDeNacimiento'])               
                prim.save()
                return render(request, 'AppFamiliar/inicio.html')
    else:
        miFormulario = PrimoFormulario()
        
        
    return render(request, 'AppFamiliar/primoFormulario.html', {'miFormulario': miFormulario})

def hijoFormulario()

def inicio(request):
    return render(request, 'AppFamiliar/inicio.html')

def hijo(request):
    return render(request, 'AppFamiliar/hijo.html')

def conyuge(request):
    return render(request, 'AppFamiliar/conyuge.html')

    