from django.urls import path
from AppFamiliar import views

urlpatterns = [
    
    path('inicio', views.inicio, name),
    path('jugadores', views.jugadores),
    
]