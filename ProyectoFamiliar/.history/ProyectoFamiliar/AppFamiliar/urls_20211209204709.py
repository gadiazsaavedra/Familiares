from django.urls import path
from AppFamiliar import views

urlpatterns = [
    
    path('inicio', views.inicio, name='Inicio'),
    path('jugadores', views.jugadores, name='Jugadores'),
    path('equipos', views.equipos, name='Equipos'),
    path
    
]