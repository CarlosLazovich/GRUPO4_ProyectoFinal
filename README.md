# Proyecto Final - BLOG VIAJERO
Comision 7 - Grupo 4

En el siguiente repositorio presentamos una aplicación web utilizando el framework Django y aplicando los conocimientos que fuimos adquiriendo durante el curso. Esta aplicación web es de tipo BLOG con la tematica de TURISMO/VIAJES.

<img src="./portada.png" width="700">

## Caracteristicas 🛠️

- **Desarrollada con Django:** Utilizamos el framework Django para crear una aplicación robusta y fácil de mantener.
- **Secciones Bien Organizadas:** Presentamos diversas secciones para ofrecer una experiencia de usuario completa, incluyendo:

    - **Home:** La página de inicio donde los usuarios pueden obtener una visión general de las últimas publicaciones, links generales.
    - **Publicaciones:** Lista todas las publicaciones y permite a los visitantes filtrarlas según sus intereses.
    - **Quienes Somos:** Un espacio dedicado para contar al equipo detrás del BLOG VIAJERO.
    - **Contacto:** Facilitamos el contacto directo con nuestro equipo para cualquier consulta.
    - **Registro, Login y Logout:** Implementamos un sistema de registro y autenticación de usuarios para mejorar la experiencia personalizada.
- **Interacción de Usuarios:** En la pagina se puede comentar, dar "Me Gusta". El colaborador puede administrar las publicaciones...


## Comenzando 🚀

_Para obtener una copia del proyecto funcionando en tu PC de manera local para propósitos de desarrollo y pruebas, seguí las instrucciones_


### Pre-requisitos 📋

_Antes de iniciar, es recomendable generar un entorno virtual de trabajo donde instalaremos las dependencias necesarias para que el proyecto funcione. Para ello, abrimos el CMD y nos dirigimos a la carpeta donde queremos guardar el entorno virtual y ejecutamos el siguiente comando:_


```
virtualenv nombre-entorno

```
_Una vez creado es necesario activarlo para ello ejecutamos la siguiente linea (en Windows):_


```
nombre_del_entorno\Scripts\activate.bat

```

_Ya contamos con un entorno virtual activado en el cual podemos instalar todas las dependencias para correr nuestro proyecto._


_Luego, con el entorno activado, no dirigimos a la carpeta donde se encuentra el archivo requirements.txt y ejecuta el siguiente comando en la consola._

```
pip install -r requirements.txt

```
_Este comando instalará en nuestro entorno, todo lo necesario para que el proyecto funcione funciona correctamente._

### SETTINGS 🔧

Luego tenes que crear un archivo de configuraciones en la carpeta proyecto/settings/ y llamala "local.py", donde debes indicar las credenciales de tu base de datos como se muestra a continuacion.

```
from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'databaseName',
        'USER': 'databaseUser',
        'PASSWORD': 'databasePassword',
        'HOST': 'localhost',
        'PORT': 'portNumber',
    }
}

```


## Construido con 🛠️

_Las herramientas utilizadas para el desarrollo fueron:_

* [Django](https://www.djangoproject.com/) Framework web
* [Python](https://www.python.org/) Del lado del servidor (backend)
* [Bootstrap](https://getbootstrap.com/) Framework web para el desarrollo frontend (HTML, CSS, JavaScript)
* [MySql](https://www.mysql.com/) - Sistema de gestión de bases de datos.



## Autores ✒️

- **Carlos Lazovich** - [CarlosLazovich](https://github.com/CarlosLazovich)
- **Victoria Martin** - [viccmartin](https://github.com/viccmartin)
- **Diego Saavedra** - [Dieg0saave06](https://github.com/Dieg0saave06)
- **Giuliano Rossi** - [RossiGiuliano](https://github.com/RossiGiuliano)
- **Dario Chacon** - [darioalej](https://github.com/darioalej)
