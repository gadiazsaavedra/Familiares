from django.urls import path
from AppFamiliar import views
from 

urlpatterns = [
    
    path('inicio', views.inicio, name='Inicio'),
    path('hijos', views.hijos, name='Hijos'),
    path('conyuge', views.conyuge, name='Conyuge'),
    path('abuelosFormulario', views.abuelosFormulario, name='AbuelosFormularios'),
    path('busquedaConyuge', views.busquedaConyuge, name='BusquedaConyuge'),
    path('buscar/', views.buscar),
    path('primoFormulario', views.primoFormulario, name='PrimoFormulario'),
    
    
    path('hijoFormulario', views.hijoFormulario, name='HijoFormulario'),
    path('leerHijos', views.leerHijos, name="LeerHijos"),
    path('eliminarHijo/<numero_para_borrar>/', views.eliminarHijo, name="EliminarHijo"),
    path('editarHijo/<numero_para_editar>/', views.editarHijo, name="EditarHijo"),

#PARA CLASES BASADAS EN VISTAS
    path('padre/list', views.PadreList.as_view(), name='List'),
    
    path(r'^(?P<pk>\d+)$', views.PadreDetalle.as_view(), name='Detail'),
    
    
    
    path(r'^nuevo$', views.PadreCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.PadreUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.PadreDelete.as_view(), name='Delete'),
    
    
    
    #Clase 23 LOGIN
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),

]