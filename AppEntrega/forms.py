from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    email = forms.EmailField()
    edad = forms.IntegerField()
    
class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]




class ConsulForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    email = forms.EmailField()
    consulta = forms.CharField(max_length=240)

class RecetasForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    nombre_receta = forms.CharField(max_length=60)
    sabor = forms.CharField(max_length=60)
    cant_pasos = forms.IntegerField()
    dificultad = forms.CharField(max_length=60)
    descripcion = forms.CharField(max_length=240)