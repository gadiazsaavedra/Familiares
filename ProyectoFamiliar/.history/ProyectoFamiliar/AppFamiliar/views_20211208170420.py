from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return HttpResponse("<h1>Bienvenido a la pagina principal</h1>")