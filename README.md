# Vagrant + Docker Swarm

En la raiz de este repositorio se encuentran los archivos que permiten el despliegue de la herramienta Docker Swarm sobre un cluster de máquinas virtuales.

Para llevar a cabo el despliegue de este cluster se necesitan las siguientes herramientas instaladas en su computador (adicional se indica la versión donde fueron probados estos scripts y el comando para validar la disponibilidad de la herramienta en su sistema):

<table>
<tr>
<td> <b> Herramienta </b> </td>
<td> <b> Versión </b> </td>
<td> <b> Comando validación </b> </td>
</tr>
<tr>
<td> Vagrant </td>
<td> 2.2.16 </td>
<td> <code>vagrant --version</code> </td>
</tr>
<tr>
<td> VirtualBox </td>
<td> 6.1.22r144080 </td>
<td> <code>VBoxManage --version</code> </td>
</tr>
</table>

Una vez clonado este repositorio en su máquina, ingrese al directorio `DSproject` y ejecute el comando `vagrant up`.
Al ejecutar este comando se comenzará el proceso de creación de tres máquinas virtuales que serán aprovisionadas con el orquestador Docker Swarm.

Una vez aprovisionadas se puede ingresar al nodo `manager` a través del comando `vagrant ssh manager`

# Despliegue

Una vez dentro del nodo `manager`, ingrese a la carpeta `DSproject/app` y ejecute los siguientes comandos:

* `docker service create --name registry --publish published=5000,target=5000 registry:2`
* `docker-compose push`
* `docker stack deploy --compose-file docker-compose.yml stackdemo`

Comprueba que se está ejecutando con `docker stack services stackdemo`. Una vez que esté funcionando, debería ver 1/1 en REPLICAS para ambos servicios.

Finalmente, puedes probar la aplicación con curl: `curl -X POST -d "{ \"content\": \"Sustentar el proyecto!!\"}" -H "Content-Type: application/json" http://address-of-the-node:8000/`

# Baja la aplicación

Para terminar los servicios, ejecute los siguientes comandos:

* `docker stack rm stackdemo`
* `docker service rm registry`

Si sólo está probando en una máquina local y quiere sacar su motor Docker del modo de enjambre, utilice `docker swarm leave --force`
