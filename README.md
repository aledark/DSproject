# Aplicación en Flask basado en un tutorial de FreeCodeCamp

Este README.md consta de las siguientes secciones:

* [Descripción de las etapas](#descripcion-de-las-etapas)

* [Requerimientos](#requerimientos) **Esta sección es la primera que debe leer** si desea seguir paso a paso lo que se encuentra en este repositorio. Esta sección brinda los elementos para preparar su entorno y llevar a cabo todas las etapas descritas en este repositorio.

## Descripcion de las etapas 

El código de este repositorio se basa en la información provista por el tutorial que se presenta en [este video](https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=91s).
El video se siguió detenidamente y la forma de mostrar el desarrollo del aplicativo es a través de etapas y cada etapa estará en un *branch* de este repositorio.
El *branch* uno es la primera etapa y de allí en adelante hasta llegar a la versión "final".

### Etapa 01 

[Enlace a etapa 01](https://github.com/josanabr/flask-introduction/tree/etapa-01).

En esta etapa se ha creado un directorio llamado `app` y en su interior se encuentra el archivo [`app.py`](app/app.py) el cual tiene la lógica de la aplicación.
Por lo pronto es un código sencillo que muestra como se construyen *web services* con Flask.

### Etapa 02

[Enlace a etapa 02](https://github.com/josanabr/flask-introduction/tree/etapa-02).

En el archivo [`app.py`](app/app.py) se ha modificado la función `index()` de modo que ahora se utiliza el método `render_template` de Flask para mostrar una página HTML en lugar de que la función retorne una sencilla cadena de caracteres.

### Etapa 03

[Enlace a etapa 03](https://github.com/josanabr/flask-introduction/tree/etapa-03).

En esta etapa se hace una modificación importante al archivo [`index.html`](app/templates/index.html) de modo que ahora se usará un archivo HTML ([`base.html`](app/templates/base.html)) como plantilla para cualquier otro archivo HTML en la aplicación.

### Etapa 04 

[Enlace a etapa 04](https://github.com/josanabr/flask-introduction/tree/etapa-04).

En esta etapa se adiciona una hoja de estilos [`main.css`](app/static/css/main.css) la cual se usa en el archivo [`base.html`](app/templates/base.html).

### Etapa 05 

[Enlace a etapa 05](https://github.com/josanabr/flask-introduction/tree/etapa-05).

En esta etapa se modifica el archivo [`app.py`](app/app.py) y se incluye la definición de un objeto `Todo` el cual será el tipo de dato que se almacenará en la base de datos.

### Etapa 06 

[Enlace a etapa 06](https://github.com/josanabr/flask-introduction/tree/etapa-06).

En esta etapa se modifica el archivo [`index.html`](app/templates/index.html) de modo que se tendrá una tabla que permitirá mostrar las tareas que están pendientes por ser realizadas.

### Etapa 07 

[Enlace a etapa 07](https://github.com/josanabr/flask-introduction/tree/etapa-07).

En esta etapa el decorador de la función `index()`, en el archivo [`app.py`](app/app.py), cambia y ahora tiene la posibilidad de aceptar los métodos `POST` y `GET` del protocolo HTTP. 
El archivo [`index.html`](app/templates/index.html) ahora incluye un formulario el cual permite que se adicione una tarea a la aplicación.

### Etapa 08

[Enlace a etapa 08](https://github.com/josanabr/flask-introduction/tree/etapa-08).

En esta etapa ya se comenzará a acceder a información a la base de datos. 
La base de datos para efectos de este demo es la base de datos SQLite. 
Para crear la base de datos se deben ejecutar los siguientes comandos desde la terminal y desde el directorio donde se encuentra el archivo `app.py`:

```
python3
```

En este momento se encuentra en un intérprete de comandos de Python 3. 
ejecute las siguientes instrucciones:

```
from app import db
db.create_all()
exit()
```

Esto creará un archivo en el directorio donde está el archivo `app.py` llamado `todo.db`. 

En esta etapa se ha modificado la función `index()`, en el archivo [`app.py`](app/app.py), de modo que ahora se reciben las peticiones del método `POST`, se procesan los datos enviados y estos se almacenan en base de datos.
El archivo [`index.html`](app/templates/index.html) ahora llena la tabla con datos tomados de la base de datos.

### Etapa 09

[Enlace a etapa 09](https://github.com/josanabr/flask-introduction/tree/etapa-09).

En esta etapa se hace una modificación importante de la hoja de estilos [`main.css`](app/static/css/main.css).

### Etapa 10

[Enlace a etapa 10](https://github.com/josanabr/flask-introduction/tree/etapa-10).

En esta etapa se adiciona un nuevo método y un nuevo *end-point* al archivo [`app.py`](app/app.py) de modo que se posibilita el borrado de tareas en la base de datos.
Así mismo, se modifica el archivo [`index.html`](app/templates/index.html) de modo que se habilita en la referencia `Delete` el borrado de una tarea en particular.

### Etapa 11

[Enlace a etapa 11](https://github.com/josanabr/flask-introduction/tree/etapa-11).

En esta etapa se posibilita la actualización de registros en la base de datos.
Se modifica el archivo [`app.py`](app/app.py) de modo que se adiciona el método `update` y el *end-point* `update` en la aplicaión. 

Se habilita en la página HTML [`index.html`](app/templates/index.html) la referencia a `Update` de modo que ahora se puede actualizar la información de una tarea. 
Para actualizar dicha información se crea una nueva página HTML llamada [`update.html`](app/templates/update.html) en la cual hay un formulario que contiene la información de la tarea que se desea actualizar.

En la página [`index.html`](app/templates/index.html) se hace una validación de modo que si no hay tareas pendientes se muestre un mensaje como el siguiente: `There are no tasks. Create one below!`.

### Etapa 12

[Enlace a etapa 12](https://github.com/josanabr/flask-introduction/tree/etapa-12).

En esta etapa se habilita el acceso a uno de los *end-points* para que el acceso se haga a través de la línea de comando con herramientas como `curl`. 

La función `index` localizada en el archivo [`app.py`](app/app.py) y con *end-point* `/` fue la que se modificó. 

Una vez modificada, la forma de acceder desde la línea de comandos es:

```
curl -X POST -d '{"content": "leer libro"}' -H "Content-Type: application/json" http://localhost:5000/
```

### Etapa 13

[Enlace a etapa 13](https://github.com/josanabr/flask-introduction/tree/etapa-13).

En esta etapa se contenerizará la aplicación. 

A través de la tecnología de Docker se llevará a cabo la creación de una imagen de contenedor la cual contiene todos los insumos para que corra la aplicación.

En este directorio se encuentra el archivo [`Dockerfile`](app/Dockerfile) el cual permite la creación de la imagen de contenedor.
Se ejecuta el siguiente comando:

```
docker image build -t app.py .
```

Para ejecutar el contenedor recien creado,

```
docker container run  --rm -d -p 5000:5000 --name app.py app.py
```

### Etapa 14

A continuación se presenta como llevar a cabo la ejecución del contenedor descrito en la [etapa 13](#etapa-13) a través del comando `docker-compose`.

Primero se debe instalar la herramienta. 
`docker-compose` se debe instalar en sistemas tipo Linux pues en otros ambientes como Mac o Windows este viene integrado en ambientes como Docker Desktop.

La instalación de `docker-compose` en Linux se logra a través de este comando:

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose
```

Para tener una versión posiblemente más actualizada visitar [este enlace](https://docs.docker.com/compose/install/).

Una vez el `docker-compose` se encuentre disponible se puede lanzar la ejecución del contenedo a través de este comando:

```
docker-compose up
```

El insumo de este comando es el archivo [`docker-compose.yml`](app/docker-compose.yml).


---

## Requerimientos

Este tutorial se llevó a cabo bajo un ambiente Ubuntu Linux 20.04.
Además de requerir [Python 3](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu) es necesario tener instalados `python3-pip` y `python3-virtualenv`. 
Para instalar este software se debe ejecutar el siguiente comando:

```
sudo apt update && sudo apt -y install python3-pip python3-virtualenv
```

Clonar este repositorio

```
git clone https://github.com/josanabr/flask-introduction
```

Una vez se termina la clonación de este repositorio, se genera un directorio llamado `flask-introduction`. 
Ingresar al directorio `flask-introduction`.

Ejecutar los siguientes comandos:

```
virtualenv env
source env/bin/activate
```

Se instala en este contexto las siguientes librerías de Python:

```
pip3 install flask flask-sqlalchemy
```

