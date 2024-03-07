from django.urls import path
from AppEntrega.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("registrarse/", registrar, name="Registrar"),
    path("usuario/", ver_user, name="Ver mi Usuario"),
    path("crearConsulta/", crear_consulta, name="Crear mi Consulta"),
    path("verConsulta/", mi_consulta, name="Ver mi Consulta"),
    path("recetas/", ver_recetas, name="Recetas"),
    path("sugerencias/", sugerir, name="Hacer Sugerencia"),
    path("mis_sugerencias/", mis_sugerencias, name="Mis Sugerencias"),
]
