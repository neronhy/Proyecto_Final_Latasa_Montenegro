from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Usuario(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    edad = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido} / Edad: {self.edad}"
    

class AddReceta(models.Model):
    nombre = models.CharField(max_length=60)
    nombre_receta = models.CharField(max_length=60, default="")
    sabor = models.CharField(max_length=60)
    cant_pasos = models.IntegerField()
    dificultad = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=240, default='DEFAULT VALUE', blank=True, null=True)

    def __str__(self):
        return f"Nombre de la receta: {self.nombre} / Sabor: {self.sabor} / Cantidad de pasos: {self.cant_pasos} / Dificultad: {self.dificultad}"

class Consulta(models.Model):
    nombre = models.CharField(max_length=60)
    email = models.EmailField()
    consulta = models.CharField(max_length=60)

    def __str__(self):
        return f"Nombre: {self.nombre} / {self.email}"


class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
