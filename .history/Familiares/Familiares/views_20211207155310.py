from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
def saludo(request):
    return HttpResponse("<h1><center><br><br>Presentacion de los integrantes de la familia</center></h1><br><br><h2>Luis<br>Juan<br>Pedro</h2><br>")

def relacion(request):
    return HttpResponse("<h1><center><br><br>La relacion de parentesco de en la familia</center></h1><br><br><h2>Luis<br>Juan<br>Pedro<br><br><br>Son hermanos<br></h2><br>")

def dia(request):
    fecha = datetime.now()
    return HttpResponse("<h1><center><br><br>Que a la fecha : {fecha} estan todos vivos</center></h1>".format(fecha=fecha))

def apellido(request, ape):
    return HttpResponse("<h1><center><br><br>Podemos anunciar que esta familia se <br><br>apellida  {ape}</center></h1>".format(ape=ape))

def antiguedad(request, edad):
    anio = datetime.now().year
    antiguedad = anio - edad
    return HttpResponse("<h1><center><br><br>Esta familia tiene origen en el año {antiguedad} </center></h1>".format(antiguedad=antiguedad))

def template1(request):
    html1 = open("C:/Users/gdiaz/OneDrive/GOOGLE DRIVE/Gustavo/Curso programacion/Coder House/ProyectoFamiliares/Familiares/Familiares/plantillas/template1.html")
    plantilla = Template(html1.read())
    html1.close()
    contexto1 = Context()