from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Presentacion de los integrantes de la familia<br><br>Lorem100")
