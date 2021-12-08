from django.http import HttpResponse

def saludo(request):
    return HttpResponse("<h1><centerPresentacion de los integrantes de la familia</h1><br><br><h2>Luis<br>Juan<br>Pedro</h2><br>")

def relacion(request):
    return HttpResponse("La relacion de parentesco de en la familia<br><br>Luis<br>Juan<br>Pedro<br>Son hermanos<br>")