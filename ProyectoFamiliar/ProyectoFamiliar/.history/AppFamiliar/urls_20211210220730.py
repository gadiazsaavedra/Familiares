from django.urls import path
from AppFamiliar import views

urlpatterns = [
    
    path('inicio', views.inicio, name='Inicio'),
    path('hijos', views.hijos, name='Hijos'),
    path('conyuge', views.conyuge, name='Conyuge'),
    path('abuelosFormulario', views.abuelosFormulario, name='AbuelosFormulario'),
    path('busquedaConyuge', views.busquedaConyuge, name='BusquedaConyugeEquipo'),
    path('buscar/', views.buscar)
]