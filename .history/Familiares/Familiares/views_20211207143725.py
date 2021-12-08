from django.http import HttpResponse

def saludo(request):
    return HttpResponse("<h1><center>Presentacion de los integrantes de la familia</center></h1><br><br><h2>Luis<br>Juan<br>Pedro</h2><br>")

def relacion(request):
    return HttpResponse("<h1><center>La relacion de parentesco de en la familia</center></h1><br><br><h2>Luis<br>Juan<br>Pedro<br>Son hermanos<br></")