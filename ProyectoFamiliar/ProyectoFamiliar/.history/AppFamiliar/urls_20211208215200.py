from django.urls import path
from AppFamiliar import views

urlpatterns = [
    
    path('inicio', views.inicio, name='Ini'),
    path('jugadores', views.jugadores, name='JUGADORES'),
    
]