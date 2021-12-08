from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Presentacion de los integrantes de la familia<br><br>Luis<br>Juan<br>Pedro<br>")

def relacion(request):
    return HttpResponse("Presentacion de los integrantes de la familia<br><br>Luis<br>Juan<br>Pedro<br>")