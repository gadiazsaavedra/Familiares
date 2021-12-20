from django.urls import path
from AppFamiliar import views

urlpatterns = [
    
    path('inicio', views.inicio, name='Inicio'),
    path('hijos', views.hijos, name='Hijos'),
    path('conyuge', views.conyuge, name='Conyuge'),
    path('abuelosFormulario', views.abuelosFormulario, name='AbuelosFormularios'),
    path('busquedaConyuge', views.busquedaConyuge, name='BusquedaConyuge'),
    path('buscar/', views.buscar),
    path('primoFormulario', views.primoFormulario, name='PrimoFormulario'),
    
    
    path('hijoFormulario', views.hijoFormulario, name="HijoFormulario"),
    path('leerHijosJugadores', views.leerJugadores, name="LeerJugadores"),
    path('eliminarJugador/<numero_para_borrar>/', views.eliminarJugador, name="EliminarJugador"),
    path('editarJugador/<numero_para_editar>/', views.editarJugador, name="EditarJugador"),

]