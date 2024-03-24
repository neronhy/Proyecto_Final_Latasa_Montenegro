from django.shortcuts import render
from AppEntrega.models import *
from AppEntrega.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate


# Create your views here.

# Inicio:

def inicio_sesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            passw = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = passw)

            if user:

                login(request, user)

                return render(request, "AppEntrega/inicio.html", {"mensaje":f"Bienvenido {user}"})
            
        else:

            return render(request, "AppEntrega/inicio.html", {"mensaje":"Datos incorrectos."})
        
    else:

        form = AuthenticationForm()

    return render(request, "AppEntrega/login.html", {"formulario":form})
        
def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            usuario = form.cleaned_data["username"]
            form.save()
            return render(request, "AppEntrega/inicio.html", {"mensaje":f"Usuario creado existosamente."})
        
    else:

        form = UsuarioRegistro()

    return render(request, "AppEntrega/registro.html", {"formulario":form})








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
