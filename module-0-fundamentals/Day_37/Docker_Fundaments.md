🐳 DÍA 37: MÓDULO 0 - Docker: Conceptos base, Instalación y CLI (El Fin del "En Mi Máquina Sí Funciona")
📦 Dependencias del Módulo:

Entorno: VS Code + Terminal Linux / Windows PowerShell.
Herramientas: Docker Desktop instalado y ejecutándose (el ícono de la ballena debe estar verde en tu barra de tareas).

📖 FASE 1: TEORÍA
El problema clásico de la programación es: "En mi máquina sí funciona, pero en el servidor de producción no". Esto pasa porque tu máquina tiene Python 3.10, Windows y ciertas versiones de librerías, y el servidor tiene Ubuntu, Python 3.8 y le faltan dependencias.

Docker resuelve esto empaquetando tu código Y todo su entorno (sistema operativo base, librerías, configuraciones) dentro de una caja sellada llamada Contenedor. Si el contenedor corre en tu laptop, correrá exactamente igual en el servidor de AWS de producción, garantizado.


DOCUMENTACIÓN OFICIAL
🔗 Doc Oficial: Docker Overview / Docker CLI Reference


🎯 El Propósito
Estandarización y Portabilidad. En lugar de instalar bases de datos, lenguajes y librerías directamente en tu sistema operativo y ensuciarlo, descargas un "Contenedor" que ya trae todo configurado, lo usas, y cuando terminas lo borras sin dejar rastro en tu computadora.


🔑 Puntos Clave: Imágenes, Contenedores y Puertos

Imagen (Image): Es el "molde" o la "receta" de solo lectura. Es el CD de instalación. Pesa megabytes o gigabytes. (Ejemplo: La imagen oficial de postgres o nginx). o es como una plantilla inmutable que contiene todo lo necesario para ejecutar una aplicación: el código, las dependencias, librerías, variables de entorno y configuraciones.
Piensa en ella como una foto congelada del sistema en un estado específico.


Contenedor (Container): Es la imagen "cobrando vida". Es el programa ejecutándose. Puedes arrancar 5 contenedores idénticos a partir de 1 sola imagen. Es la instancia en ejecución de una imagen. Cuando lanzas una imagen, se convierte en un contenedor que corre de manera aislada en tu máquina.


Port Mapping (Mapeo de Puertos): Un contenedor es una computadora aislada. Si arranco un servidor web dentro de Docker en el puerto 80, mi computadora (Host) no lo ve. Debo "mapear" el puerto usando -p 8080:80 (El puerto 8080 de mi laptop apunta al 80 del contenedor).

Detached Mode (-d): Corre el contenedor en segundo plano. Si no usas -d, el contenedor secuestrará tu terminal y, si la cierras o presionas Ctrl+C, el contenedor morirá.


⚠️ Buenas y Malas Prácticas
✅ Buena Práctica: Tratar a los contenedores como entidades efímeras (desechables). Si un contenedor de Django falla, no entras a arreglarlo por dentro modificando archivos manuales; lo matas, arreglas el código original, y levantas un contenedor nuevo.

❌ Mala Práctica: Empezar a usar Docker sin mapear correctamente los puertos, creando contenedores "fantasma" que están corriendo consumiendo memoria pero a los que no puedes acceder desde tu navegador.



💻 Implementación Oficial (Comandos Core)
# 1. Verificar que Docker está corriendo
docker --version

# 2. Descargar una imagen y correrla (El hola mundo oficial)
docker run hello-world

# 3. Listar contenedores corriendo ACTUALMENTE
docker ps

# 4. Listar TODOS los contenedores (corriendo, apagados, fallidos)
docker ps -a

# 5- Crear un contenedor a partir de una imagen y mapearlo al puerto
docker run -d -p 8080:80 nginx

# 6. Apagar un contenedor suavemente (necesitas su ID o Nombre)
docker stop <ID_DEL_CONTENEDOR>

# 7. Borrar un contenedor definitivamente (debe estar apagado primero)
docker rm <ID_DEL_CONTENEDOR>

# 8. Forzar la eliminacion de una imagen
docker rmi -f 8541484afbc9

# 9. Forzar la eliminacion de un contenedor
docker rm -f 8541484afbc9

# comandos de inspeccion y estado
docker ps            # Lista contenedores en ejecución
docker ps -a         # Lista todos los contenedores (incluidos detenidos)
docker images        # Muestra las imágenes descargadas
docker logs <ID>     # Muestra los logs de un contenedor
docker inspect <ID>  # Información detallada de un contenedor o imagen

## Crear y ejecutar
docker run hello-world              # Prueba instalación de Docker
docker run -d -p 8080:80 nginx      # Crea contenedor en segundo plano con Nginx
docker run -d --name redis-server -p 6379:6379 redis   # Descargar la imagen oficial y correr Redis en segundo plano
docker run -it ubuntu bash          # Contenedor interactivo con Ubuntu
docker exec -it <ID> bash           # Ejecuta comandos dentro de un contenedor

## Control de contenedores
docker stop <ID>        # Detiene un contenedor
docker start <ID>       # Inicia un contenedor detenido
docker restart <ID>     # Reinicia un contenedor
docker rm <ID>          # Elimina un contenedor

## Gestión de imágenes
docker pull nginx             # Descarga una imagen desde Docker Hub
docker build -t mi_app .      # Construye una imagen desde un Dockerfile
docker rmi <ID>               # Elimina una imagen
docker tag mi_app:latest repo/mi_app:v1   # Etiqueta una imagen
docker push repo/mi_app:v1    # Sube una imagen a un repositorio

## Volúmenes y redes
docker volume ls              # Lista volúmenes
docker volume rm <nombre>     # Elimina un volumen
docker network ls             # Lista redes
docker network create mi_red  # Crea una red personalizada




## Ubuntu** | Base para desarrollo y pruebas 
docker run -it ubuntu bash |

## Alpine** | Imagen mínima y ligera para apps rápidas  
docker run -it alpine sh |

## Nginx** | Servidor web y proxy inverso | 
docker run -d --name nginx -p 8080:80 nginx |

## MySQL** | Base de datos relacional | 
docker run -d --name mysql -e MYSQL_ROOT_PASSWORD=1234 -p 3306:3306 mysql |

## Postgres** | Base de datos avanzada | 
docker run -d --name postgres -e POSTGRES_PASSWORD=1234 -p 5432:5432 postgres |

## Node.js** | Entorno de ejecución para JavaScript |
 docker run -it --name nodeapp -v $(pwd):/app -w /app node node |

## Python** | Lenguaje de programación versátil | 
docker run -it --name pyapp python python |

## Redis** | Almacenamiento en memoria para cache y colas |
docker run -d --name redis -p 6379:6379 redis |

## httpd (Apache)** | Servidor web clásico | 
docker run -d --name apache -p 8081:80 httpd |

## Jenkins** | Integración continua y automatización | 
docker run -d --name jenkins -p 8082:8080 jenkins |


💻 FASE 2: PRÁCTICA DIARIA
(Instrucción: Ejecuta estos comandos en tu terminal. Necesitas internet para descargar las imágenes).


⚙️ Ejercicio 1: Implementación - Lógica Base (El Hola Mundo)
# Contexto: Es tu primer día con Docker. Necesitas comprobar que el motor (Engine) 
# funciona correctamente y puede comunicarse con el registro central de internet (Docker Hub).
#
# Requisitos Ejecutables:
# 1. Asegúrate de tener Docker Desktop abierto.
# 2. Abre tu terminal y ejecuta: docker run hello-world
# 3. Docker buscará la imagen localmente, no la encontrará, la descargará de internet y la ejecutará.
# 4. Pega aquí la frase en inglés que te imprime en la consola diciendo que tu instalación "parece funcionar correctamente".

# --- TU OUTPUT DE CONSOLA AQUÍ ---
1- busque como instalar docker desktop
2- instale el wsl de windows con wsl --install en powershell
3- verifque la virtualizacion y si estaba activa
4- reinicie mi equipo
5- corri en powershell docker run hello-world
6- resultado: 
docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete
d5e71e642bf5: Download complete
Digest: sha256:5dd0d3e6e255913fc30f90b9f2b1d359cc2cbdb48090cc4b65f1676e203243cc
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash



🚀 Ejercicio 2: Implementación - Escenario Real (Levantando un Servidor en 1 Segundo)
# Contexto: Un cliente te pide que le muestres cómo se ve un servidor web moderno.
# Hacer esto de la forma tradicional te tomaría 20 minutos (instalar Nginx, configurar red, etc).
# Con Docker, toma 1 segundo y no ensucias tu máquina.
#
# Requisitos Ejecutables:
# 1. Ejecuta el siguiente comando para arrancar un servidor web oficial de nginx en 
#    segundo plano (-d) y mapeando el puerto 8080 de tu PC al 80 del contenedor:
#    docker run -d -p 8080:80 nginx
# 2. Abre tu navegador web y entra a: http://localhost:8080 (Deberías ver "Welcome to nginx!").
# 3. Ejecuta `docker ps` en tu terminal.
# Pega aquí la línea exacta del output que te devolvió `docker ps` (donde se ven el ID y los puertos).

# --- TU OUTPUT DE 'docker ps' AQUÍ ---
1- docker run -d -p 8080:80 nginx # Nota: este comando lo que hace es descargar la imagen ngnix, ponerla a correr en el contenedor, mapea el puerto que se necesita y los mando a segundo plano.
2- Instalacion completa y welcome to nginx correctamente
3-  CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS         
                            NAMES
77eebd1eb91a   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   priceless_cori


🚀 Ejercicio 3: Implementación - Escenario Real (Limpieza del Cuarto de Máquinas)
# Contexto: Ya le mostraste la página web al cliente. Ahora necesitas apagar ese servidor 
# NGINX y destruirlo para que no siga consumiendo memoria RAM en tu computadora.
#
# Requisitos Ejecutables:
# 1. Usando el ID del contenedor que obtuviste en el ejercicio 2 (solo necesitas los 
#    primeros 3 o 4 caracteres del ID), ejecuta el comando para detenerlo suavemente.
# 2. Ahora que está apagado, ejecuta el comando para borrar/remover el contenedor de tu sistema.
# 3. Verifica que ya no existe ejecutando `docker ps -a`.
# Escribe los 2 comandos exactos que usaste para apagarlo y borrarlo.

# --- TUS COMANDOS AQUÍ ---
1- docker ps -a : 77eebd1eb91a # quise usar el comando para irme acostumbrando
2- docker stop 77eebd1eb91a = 
CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS                      PORTS     NAMES
77eebd1eb91a   nginx         "/docker-entrypoint.…"   8 minutes ago   Exited (0) 12 seconds ago
3- docker rm 77eebd1eb91a
4- docker ps -a


🐛 Ejercicio 4: Lectura de Código y Debugging (El Servidor Secuestrado)
# Contexto: Un Junior en la Agencia Flow necesita correr una base de datos Redis súper rápido.
# Ejecuta este comando en su terminal: docker run -p 6379:6379 redis
#
# Inmediatamente su terminal empieza a llenarse de logs de Redis (dibujando un logo gigante).
# El Junior intenta escribir comandos nuevos en esa misma terminal (como 'ls' o 'docker ps'), 
# pero la terminal no responde, está "atrapada" por Redis. Él presiona Ctrl+C para recuperar 
# su consola, y al hacerlo, la base de datos se apaga y el sistema se cae.
#
# Pregunta Debugging: ¿Qué bandera/parámetro exacto (de solo 2 caracteres) olvidó agregar el 
# Junior en su comando `docker run` para que el contenedor corriera como un proceso fantasma 
# sin secuestrarle la consola?

# --- TU EXPLICACIÓN Y CORRECCIÓN AQUÍ ---
Primeramente ese comando no es que este malo, si no que simple y sencillamemente le falta un parametro importante que es el -d ya que es muy importante, que es y es hace, en docker el parametro -d o Detached Mode manda a segundo plano los contenedores cuando  se estan corriendo, esto es importante porque si no el contenedor correra en primer plano y obstaculizara nuestro trabajo como DEV.


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA
❓ Pregunta Teórica 1:
¿Cuál es la diferencia fundamental en consumo de recursos (RAM y Disco) entre una Máquina Virtual tradicional (como la que usas en VirtualBox para correr Windows Server) y un Contenedor de Docker? (Pista: Piensa en el "Sistema Operativo Huésped" / Guest OS).
La diferencia fundamental es que un server en virtual box consume mas recursos( ram y espacio) porque cada virtualizacion ocupa un sistema completo haciendolo mas pesado y a su vez le demanda mas recursos a la laptop, en cambio en un contenedor de docker comparte kernel con el host y solo utiliza lo necesario ya que cuando una VM ocupa 2 de ram con docker solo se ocupa 400 mb.


❓ Pregunta Teórica 2:
Explicamos que en el comando docker run -p 8080:80 nginx, el parámetro -p es el Mapeo de Puertos (Port Mapping). Si tienes tu laptop conectada al Wi-Fi de un cliente y tu IP local es 192.168.1.50, ¿qué dirección exacta y puerto debe escribir el cliente en el navegador de su teléfono celular para ver el NGINX que corre dentro de tu Docker? Justifica el porqué.
Esto se explica de una manera sencilla 8080 es el host o puerto de mi laptop, toda peticion que le llegue a ese puerto la laptop lo va redirigir al 80 que seria el contenedor nginx, como no se esta accediendo al contenedor desde la laptop la direccion que el cliente tiene que poner es http://192.168.1.50:8080 en donde la ip 192.168.1.50 es el host y todo peticion que venga de ahi lo va aredirigir al 8080 que es el puerto de la laptop y asu vez este lo dirige al contenedor 80.

Nota; Hice el ensayo de esta pregunta en mi casa, corri el contenedor docker con docker run -d -p 8080:80 nginx, 
despues abri powershell y utilice el comando ipconfig para conocer la ip de mi laptop(192.168.0.204), luego desde mi celular puse la direccion web http://192.168.0.204:8080 y efectivamente desde mi celular tuve un welcome to nginx.


🗣️ Prueba de Feynman (Explicación):
Escenario: Un cliente dueño de un supermercado no entiende qué es Docker y por qué le dices que "empaquetarás" su sistema de inventario.
Explícale el concepto usando la analogía de los contenedores de transporte en los barcos mercantes en APM Terminals (Moín, Limón).
(Pista: Antes, llevar arena, muebles o líquidos requería barcos con compartimentos distintos y si cambiabas de barco había que reconstruir los cuartos; ahora, no importa qué lleves por dentro, la grúa del puerto siempre agarra la misma caja de metal estándar y todos los barcos/puertos del mundo saben cómo manejarla).
Docker vino a solucionar un problema cotidiano en el mundo de las apps el cual es en mi pc funciona pero en el tuyo no, de forma sencilla esto es como antes se ocupaba un barco especifico para X carga, ahora gracias a los contenedores estandar, todo se empaqueta o se alista y se introduce en el contenedor ya sea material a granel empacado en bolsa, carros de lujo, muebles, comida etc... luego se sella el contenedor y se coloca en el barco de una manera estandar gracias a la grua o en palabras tecnicas docker run -d -p 8080:80 nginx.