from django.contrib.auth.password_validation import password_changed
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from AppFamiliar.models import Abuelos, Conyuge, Primo, Hijo, Padres
from AppFamiliar.forms import AbuelosFormulario, PrimoFormulario, HijoFormulario, UserRegisterForm
#Para el login 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


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

def hijoFormulario(request):
    if request.method == 'POST':
        miFormulario = HijoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                hij = Hijo(
                    apellido=informacion['apellido'],
                    numero=informacion['numero'],
                    esBueno=informacion['esBueno'])               
                hij.save()
                return render(request, 'AppFamiliar/inicio.html')
    else:
            miFormulario = HijoFormulario()
    return render(request, 'AppFamiliar/hijoFormulario.html',{"miFormulario":miFormulario})

def inicio(request):
    return render(request, 'AppFamiliar/inicio.html')

def hijo(request):
    return render(request, 'AppFamiliar/hijo.html')

def conyuge(request):
    return render(request, 'AppFamiliar/conyuge.html')

from django.views.generic import ListView

from django.views.generic.detail import DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView

#from django.urls import reverse_lazy

#Leer --- nos da todos los cursos
class PadresList(ListView):
    
    model = Padres
    template_name = "AppFamiliarCoder/cursos_list.html"
    
#Detalle - SUPER Leer - Buscar!!!!!
class CursoDetalle(DetailView):
    
    model = Curso
    template_name = "AppCoder/curso_detalle.html"
    
#Crear elementos
class CursoCreacion(CreateView):
    
    model = Curso
    success_url = "../curso/list"
    fields = ["nombre", "camada", "esNoche"]
    
#modificar!!!!!!!!!!!  
class CursoUpdate(UpdateView):
    
    model = Curso
    success_url = "../curso/list"
    fields = ["nombre", "camada", "esNoche"]
  
#Borrar   
class CursoDelete(DeleteView):
    
    model = Curso
    success_url = "../curso/list"
    
    

def login_request(request):

    if request.method =="POST":

        form = AuthenticationForm(request, data = request.POST)

        if not form.is_valid():
            return render(
                request,
                "AppCoder/inicio.html",
                {"mensaje": "FORMULARIO erroneo"},
            )

                        
                        
                

        usuario = form.cleaned_data.get("username")
        contra = form.cleaned_data.get("password")

        user = authenticate(username=usuario, password = contra)

        if user is not None:

            login(request, user)

            return render(request, "AppCoder/inicio.html", {"mensaje":f"BIENVENIDO, {usuario}!!!!"})

        else:
            
            return render(
                request,
                "AppCoder/inicio.html",
                {"mensaje": "DATOS MALOS :(!!!!"},
            )

                            

    form = AuthenticationForm()  #Formulario sin nada para hacer el login

    return render(request, "AppCoder/login.html", {"form":form} )


def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            
            form = UserRegisterForm(request.POST)
            
            if form.is_valid():

                  username = form.cleaned_data['username']
                  
                  
                  form.save()
                  
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":f"{username} Creado :)"})

      else:
            #form = UserCreationForm()     
            
              
            form = UserRegisterForm()     

      return render(request,"AppCoder/register.html" ,  {"form":form})
