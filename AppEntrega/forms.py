from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    email = forms.EmailField()
    edad = forms.IntegerField()


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