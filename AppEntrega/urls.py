from django.urls import path
from AppEntrega.views import *
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path("", inicio, name="inicio"),    
    path("login/", inicio_sesion, name="LOGIN"),
    path("usuario/", ver_user, name="Ver mi Usuario"),
    path("recetas/", ver_recetas, name="Recetas"),
    path("registro/", registro, name="REGISTRO"),
    path("logout/", LogoutView.as_view(template_name="AppEntrega/logout.html"), name="Logout"),

    #CRUD DE RECETAS
    path("sugerencias/", sugerir, name="Hacer Sugerencia"),
    path("mis_sugerencias/", mis_sugerencias, name="Mis Sugerencias"),


    #CRUD DE CONSULTAS
    path("crearConsulta/", crear_consulta, name="Crear mi Consulta"),
    path("verConsulta/", mi_consulta, name="Ver mi Consulta"),


]
