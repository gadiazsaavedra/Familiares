from django.urls import path
from AppFamiliar import views

urlpatterns = [
    
    path('inicio', views.inicio, name='INICIO'),
    path('jugadores', views.jugadores, name='JUGADORES'),
    
]