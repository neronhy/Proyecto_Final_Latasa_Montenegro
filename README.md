# Tercera Preentrega-Latasa Montenegro

## Pagina Web de Recetas MILM

Esta es una pagina web en desarrollo con el objetivo de permitir que usuarios puedan buscar recetas de cocina casera en un solo sitio, con sus ingredientes, pasos y dificultad. La idea es que a medida que entren usuarios y hagan uso de la pagina vayan agregando sugerencias para asi poder compartir una gran variedad de recetas.

### Requerimientos

Tener instalado Django para asi poder ejecutar las lineas de codigo sin que surjan posibles errores.

1- Para crear la base de datos donde haremos la instalacion ejecute el siguiente comando:

*Windows*
```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```

*MacOS*
```bash
  python3 manage.py makemigrations
```
```bash
  python3 manage.py migrate
```

2- Ejecutar el siguiente codigo para que el servidor se pueda visualizar en una pagina del navegador que prefieran.
```bash
  python manage.py runserver
```

*MacOS*
```bash
  python3 manage.py runserver
```

3- Para poder ingresar a la pagina desde el navegador ingrese el siguiente url en su barra de busqueda:
```bash
  localhost:8000/
```

Le aparecera una lista con 2 opciones, una bajo el nombre de Admin y la otra con el nombre de la App de la pagina.

### Admin

Para poder acceder a la App de Admin tendra que introducir el siguiente url:
```bash
  localhost:8000/admin
```

La pagina le pedira que ingrese un usuario y una contraseña para loguearse, los datos que necesita son los siguientes:

_user_: JoaquinAdmin

_password_: mcfnaf123

### App Recetas MILM
Para poder acceder a la App de Recetas MILM tendra que introducir el siguiente url:
```bash
  localhost:8000/AppEntrega/
```
Desde la misma pagina podra navegar entre los distintos apartados haciendo click en los botones que aparence en la parte superior. Tambien podra testear algunas de las funciones de esta App en sus apartados correspondientes, por ejemplo: hacer una consulta, una sugerencia, registrar su usuario, entre otros.

Si por alguna razon no puede ingresar a los apartados mediante los botones puede ingresar los correspondientes urls:

_inicio_
```bash
  localhost:8000/AppEntrega/
```

_registrarse_:
```bash
  localhost:8000/AppEntrega/registrarse/
```

_ver usuarios_:
```bash
  localhost:8000/AppEntrega/usuario/
```

_crear consulta_:
```bash
  localhost:8000/AppEntrega/crearConsulta/
```

_ver consultas_:
```bash
  localhost:8000/AppEntrega/verConsultas/
```

_sugerencias_:
```bash
  localhost:8000/AppEntrega/sugerencias/
```

_mis sugerencias_:
```bash
  localhost:8000/AppEntrega/mis_sugerencias/
```

### IMPORTANTE
La pagina aun esta siendo desarrollada y por eso apartados como el de "Recetas" no tienen contenido cuando haces click en las fotos, todas las funciones que esperamos agregar seran añadidas a medida que se desarrolle la pagina.


