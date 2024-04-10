from django.shortcuts import render
from AppEntrega.models import *
from AppEntrega.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required




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

                return render(request, "AppEntrega/inicio.html", {"mensaje":f"Bienvenido {user}!"})
            
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

@login_required
def agregarAvatar(request):

    if request.method == "POST":

        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user)

            nuevo_avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])

            nuevo_avatar.save()

            return render(request, "AppEntrega/inicio.html")
        
    else:

        form = AvatarForm()

    return render(request, "AppEntrega/agregarAvatar.html", {"formulario":form})

#Logout
@login_required
def cerrar_sesion(request):
    logout(request)
    return render(request,"AppEntrega/inicio.html", {"mensaje":"Has cerrado sesión"})

@login_required
def editarUsuario(request):

    usuario = request.user

    if request.method == "POST":

        form = EditarUsuario(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "AppEntrega/inicio.html")
        
    else:

        form = EditarUsuario(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
        })

    return render(request, "AppEntrega/editarPerfil.html", {"formulario":form, "usuario":usuario})
  



def inicio(request):
    return render(request, "AppEntrega/inicio.html")

def About(request):
    return render(request, "AppEntrega/about.html")

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
    

def eliminarSugerencia(request, nombreSugerencia):

    sugerencia = AddReceta.objects.get(nombre=nombreSugerencia)
    sugerencia.delete()

    sugerencias = AddReceta.objects.all()

    contexto = {"Recetas sugeridas":sugerencias}

    return render(request, "AppEntrega/elimnarSugerencias.html", contexto)

def editarSugerencia(request, nombreSugerencia):

    sugerencia = AddReceta.objects.get(nombre=nombreSugerencia)

    if request.method == "POST":

        miFormulario = RecetasForm(request.POST)

        if miFormulario.is_valid():

            info = miFormulario.cleaned_data

            sugerencia.nombre = info["nombre"]
            sugerencia.nombre_receta = info["nombre_receta"]
            sugerencia.sabor = info["sabor"]
            sugerencia.cant_pasos = info["cant_pasos"]
            sugerencia.dificultad = info["dificultad"]
            sugerencia.descripcion = info["descripcion"]

            sugerencia.save()

            return render(request, "AppEntrega/inicio.html")
        
    else:

        miFormulario = RecetasForm(initial={"nombre":sugerencia.nombre, "nombre_receta":sugerencia.nombre_receta, "sabor":sugerencia.sabor,
        "cant_pasos":sugerencia.cant_pasos, "dificultad":sugerencia.dificultad, "descripcion":sugerencia.descripcion})

    return render(request, "AppEntrega/editarSugerencias.html", {"miFormulario":miFormulario, "nombre":nombreSugerencia})    


#Recetas
    
def ver_recetas(request):
    return render(request, "AppEntrega/Recetas.html")


