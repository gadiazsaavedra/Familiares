from django.http import HttpResponse
from datetime import datetime

def saludo(request):
    return HttpResponse("<h1><center>Presentacion de los integrantes de la familia</center></h1><br><br><h2>Luis<br>Juan<br>Pedro</h2><br>")

def relacion(request):
    return HttpResponse("<h1><center>La relacion de parentesco de en la familia</center></h1><br><br><h2>Luis<br>Juan<br>Pedro<br><br><br>Son hermanos<br></h2><br>")

def dia(request):
    fecha = datetime.now()
    return HttpResponse("<h1><center>Que a la fecha : {fecha} estan todos vivos</center></h1>".format(fecha=fecha))

def apellido(request, ape):
    return HttpResponse("<h1><center>Podemos anunciar que esta familia de {ape}</center></h1>".format(ape=ape))