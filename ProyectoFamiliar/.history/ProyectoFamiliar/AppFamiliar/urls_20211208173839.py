from django.urls import path
from AppFamiliar import views

urlpatterns = [
    path('admin/', admin)
    path('inicio', views.inicio()),
    
]