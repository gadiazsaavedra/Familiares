from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Presentacion de los inteh")