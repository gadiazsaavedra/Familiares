from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request, 'AppFamiliar/inicio.html')

def jugadores(request):
    return render(request, 'AppFamiliar/jugadores.html')

def  estadio
    