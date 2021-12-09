from django.urls import path
from AppFamiliar import views

urlpatterns = [
    path('admin/', admin.site)
    path('inicio', views.inicio()),
    
]