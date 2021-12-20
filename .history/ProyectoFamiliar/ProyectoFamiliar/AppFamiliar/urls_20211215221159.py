from django.urls import path
from AppFamiliar import views

urlpatterns = [
    
    path('inicio', views.inicio, name='Inicio'),
    path('hijo', views.hijos, name='Hijos'),
    path('conyuge', views.conyuge, name='Conyuge'),
    path('abuelosFormulario', views.abuelosFormulario, name='AbuelosFormularios'),
    path('busquedaConyuge', views.busquedaConyuge, name='BusquedaConyuge'),
    path('buscar/', views.buscar),
    path('primoFormulario', views.primoFormulario, name='PrimoFormulario'),
    
    
    path('hijoFormulario', views.hijoFormulario, name="HijoFormulario"),
    path('leerHijos', views.leerHijos, name="LeerHijos"),
    path('eliminarHijo/<numero_para_borrar>/', views.eliminarHijo, name="EliminarHijo"),
    path('editarHijo/<numero_para_editar>/', views.editarHijo, name="EditarHijo"),

]