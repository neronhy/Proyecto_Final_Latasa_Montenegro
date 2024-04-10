from django.urls import path
from AppEntrega.views import *
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path("", inicio, name="inicio"),    
    path("login/", inicio_sesion, name="LOGIN"),
    path("recetas/", ver_recetas, name="Recetas"),
    path("registro/", registro, name="REGISTRO"),
    path("logout/", cerrar_sesion, name="Logout"),
    path("personalizarPerfil/", agregarAvatar, name="Avatar"),
    path("editarPerfil/", editarUsuario, name="EditarUsuario"),
    path("about/", About, name="about"),

    #CRUD DE RECETAS
    path("sugerencias/", sugerir, name="Hacer Sugerencia"),
    path("mis_sugerencias/", mis_sugerencias, name="Mis Sugerencias"),
    path("editarSugerencias/<nombreSugerencia>/", editarSugerencia, name="EditarSugerencia"),
    path("eliminarSugerencias/<nombreSugerencia>/", eliminarSugerencia, name="EliminarSugerencia"),


    #CRUD DE CONSULTAS
    path("crearConsulta/", crear_consulta, name="Crear mi Consulta"),
    path("verConsulta/", mi_consulta, name="Ver mi Consulta"),


]
