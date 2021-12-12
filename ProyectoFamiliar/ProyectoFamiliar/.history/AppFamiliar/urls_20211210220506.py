from django.urls import path
from AppFamiliar import views

urlpatterns = [
    
    path('inicio', views.inicio, name='Inicio'),
    path('hijos', views.hijos, name='Hijos'),
    path('conyuge', views.conyuge, name='Conyuge'),
    path('estadioFormulario', views.estadioFormulario, name='EstadioFormulario'),
    path('busquedaEquipo', views.busquedaEquipo, name='BusquedaEquipo'),
    path('buscar/', views.buscar)
]