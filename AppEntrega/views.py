from django.shortcuts import render
from AppEntrega.models import *
from AppEntrega.forms import *

# Create your views here.

# Inicio:

def inicio(request):
    return render(request, "AppEntrega/inicio.html")

def registrar(request):

    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            new_user = Usuario(nombre = info["nombre"],
                               apellido = info["apellido"],
                               email = info["email"],
                               edad = info["edad"]
            )
        new_user.save()
        return render(request, "AppEntrega/inicio.html")
    else:
        formulario = UsuarioForm()

    return render(request, "AppEntrega/registrarse.html", {"formulario":formulario})


def ver_user(request):
    buscar = request.GET.get("nombre","")
    if buscar == "":
        return render(request, "AppEntrega/verUser.html")
    else:
        result = Usuario.objects.filter(nombre__icontains=buscar)
        return render(request, "AppEntrega/verUser.html", {"result":result})



#consultas

def crear_consulta(request):

    if request.method == "POST":
        formulario = ConsulForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            new_consul = Consulta(nombre = info["nombre"],
                                  email = info["email"],
                                  consulta = info["consulta"]
            )
        new_consul.save()
        return render(request, "AppEntrega/inicio.html")
    else:
        formulario = ConsulForm()
    
    return render(request, "AppEntrega/crearConsulta.html", {"formulario":formulario})

def mi_consulta(request):
    buscar = request.GET.get("nombre","")
    if buscar == "":
        return render(request, "AppEntrega/verConsulta.html")
    else:
        result = Consulta.objects.filter(nombre__icontains=buscar)
        return render(request, "AppEntrega/verConsulta.html", {"result":result})
    


#Sugerencias
    
def sugerir(request):
    if request.method == "POST":
        formulario = RecetasForm(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            new_recipe = AddReceta(nombre = info["nombre"],
                                  nombre_receta = info["nombre_receta"],
                                  sabor = info["sabor"],
                                  cant_pasos = info["cant_pasos"],
                                  dificultad = info["dificultad"],
                                  descripcion = info["descripcion"]
            )
        new_recipe.save()
        return render(request, "AppEntrega/inicio.html")
    else:
        formulario = RecetasForm()
    
    return render(request, "AppEntrega/Sugerencias.html", {"formulario":formulario})

def mis_sugerencias(request):
    buscar = request.GET.get("nombre","")
    if buscar == "":
        return render(request, "AppEntrega/mis_sugerencias.html")
    else:
        result = AddReceta.objects.filter(nombre__icontains=buscar)
        return render(request, "AppEntrega/mis_sugerencias.html", {"result":result})
    
#Recetas
    
def ver_recetas(request):
    return render(request, "AppEntrega/Recetas.html")
