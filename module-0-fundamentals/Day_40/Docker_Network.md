🐳 DÍA 40: MÓDULO 0 - Docker Networking (Telepatía entre Contenedores)

📦 Dependencias del Módulo:
Entorno: VS Code + Terminal.
Herramientas: Docker Desktop activo.


📖 FASE 1: TEORÍA

Imagina que levantas un contenedor con Django (Backend) y otro contenedor con PostgreSQL (Base de datos). 
Están en la misma computadora, pero por defecto, los contenedores están sordos y ciegos. Viven en prisiones aisladas y 
no saben que el otro existe.

Para que Django pueda guardar datos en PostgreSQL, debemos conectarlos al mismo "Switch de red virtual". Esto se hace creando una Docker Network.

La magia suprema de Docker Networks es el DNS Automático. Si metes dos contenedores en la misma red personalizada, no necesitas saber qué dirección IP tienen. Pueden hablarse simplemente usando el nombre del contenedor.


DOCUMENTACIÓN OFICIAL
🔗 Doc Oficial: Docker container networking

🎯 El Propósito
Aislamiento y Comunicación. Permitir que tu aplicación web (Django/React) hable con tu base de datos de forma segura, 
sin exponer la base de datos al internet público.


🔑 Puntos Clave: Redes Bridge
Red por Defecto (Default Bridge): Cuando haces docker run sin especificar red, caen aquí. Pueden hablar por IP, pero NO por nombre. Es una mala práctica depender de esto.

Red Personalizada (Custom Bridge): Tú la creas (docker network create). Los contenedores aquí adentro activan un servidor DNS interno. Si tu base de datos se llama mi_postgres, Django se conecta apuntando al host mi_postgres en lugar de una IP como 172.17.0.2.

Seguridad: Si metes Nginx y Postgres en la misma red interna, Nginx puede ver a Postgres. Pero el mundo exterior (Internet) solo podrá ver a Nginx si tú mapeas su puerto (-p 80:80). Postgres queda oculto y seguro.


⚠️ Buenas y Malas Prácticas
✅ Buena Práctica: Crear una red dedicada por proyecto (ej. agencia_network) y meter ahí solo los contenedores de ese proyecto.

❌ Mala Práctica: Intentar que el contenedor de Django se conecte a Postgres apuntando a localhost. Para un contenedor, localhost es el interior de sí mismo. Nunca encontrará a Postgres ahí.


💻 Implementación Oficial 

# 1. Crear una red personalizada (Tipo bridge por defecto)
docker network create mi_red_proyecto

# 2. Listar las redes que existen en tu Docker
docker network ls

# 3. Levantar un contenedor DENTRO de esa red
docker run -d --name db_server --network mi_red_proyecto postgres

# 4. Inspeccionar la red para ver quiénes están conectados a ella
docker network inspect mi_red_proyecto

# 5. Borrar una red (debe estar vacía primero o sea eliminar el contenedor)
docker network rm mi_red_proyecto



💻 FASE 2: PRÁCTICA DIARIA
(Instrucción: Sigue los pasos en tu terminal. Usaremos comandos de "ping" para probar la conectividad).


⚙️ Ejercicio 1: Implementación - Lógica Base (Creando el Cableado Virtual)
# Contexto: Vas a desplegar la nueva infraestructura de la Agencia Flow. Necesitas 
# una red privada para que tus servidores hablen entre sí.
#
# Requisitos Ejecutables:
# 1. Ejecuta el comando para crear una nueva red llamada `flow_network`.
# 2. Ejecuta el comando para listar todas las redes y verifica que `flow_network` aparezca.
# Pega aquí el output exacto (la tabla) que te devolvió el comando `docker network ls`.

# --- TU OUTPUT DE CONSOLA AQUÍ ---
1- docker network create flow_network
2- docker network ls
3- resultado:
NETWORK ID     NAME           DRIVER    SCOPE
d52ab594f9c9   bridge         bridge    local
f410133f0583   flow_network   bridge    local
c33b756feabe   host           host      local
b5909f898338   none           null      local


🚀 Ejercicio 2: Implementación - Escenario Real (Levantando los Servidores)
# Contexto: Vamos a encender dos servidores usando imágenes ligeras de Linux (Alpine) 
# y los conectaremos a tu nueva red.
#
# Requisitos Ejecutables:
# 1. Levanta el primer contenedor llamado 'servidor_web':
#    docker run -d --name servidor_web --network flow_network alpine sleep infinity
# 2. Levanta el segundo contenedor llamado 'base_datos':
#    docker run -d --name base_datos --network flow_network alpine sleep infinity
# 3. Usa el comando de inspección de red (`docker network inspect flow_network`).
# Pega aquí solo la sección del archivo JSON (output) que dice "Containers", donde se ve 
# que ambos servidores están conectados a tu red.

# --- TU OUTPUT DE CONSOLA (JSON) AQUÍ ---
1- docker run -d --name server_web --network flow_network alpine sleep infinity
2- docker run -d --name base_datos --network flow_network alpine sleep infinity
3- docker network inspect flow_network
4- "Containers": {
            "0604ec6ea4a5b2ed15159c9d170c826966213e977ed73d5d67dd2204d8d48b0e": {
                "Name": "base_datos",
                "EndpointID": "52f9ff8cca29958feaa130a0dc9eec378855dba6c5a3b7fa030623da00be06d4",        
                "MacAddress": "86:96:dd:32:8b:66",
                "IPv4Address": "172.18.0.3/16",
                "IPv6Address": ""
            },
            "678db77a7ecd64ec0487a9f5f97b05e4490bfeacde9786305cbbec9cca236aaa": {
                "Name": "server_web",
                "EndpointID": "1662d6c2fe8c74b8bfd18db70630c04e1f8b1c08a5d1aaca37757169e64bdcdf",        
                "MacAddress": "d2:ef:5e:cd:7e:fa",
                "IPv4Address": "172.18.0.2/16",
                "IPv6Address": ""
            }
}


🚀 Ejercicio 3: Implementación - Escenario Real (Probando la Telepatía DNS)
# Contexto: Estás dentro del 'servidor_web' y necesitas enviarle un paquete de datos 
# a la 'base_datos'. ¡Vamos a probar la resolución DNS automática!
#
# Requisitos Ejecutables:
# 1. Abre una terminal interactiva DENTRO del servidor web:
#    docker exec -it servidor_web sh
# 2. Haz un ping a la base de datos usando SU NOMBRE, no su IP:
#    ping -c 3 base_datos
# 3. Sal del contenedor con `exit`.
# 4. Limpia todo: Borra ambos contenedores (docker rm -f servidor_web base_datos) y borra la red.
# Pega aquí el resultado exitoso del 'ping'. Observa cómo Docker tradujo mágicamente 
# el nombre 'base_datos' a una dirección IP interna.

# --- TU OUTPUT DEL PING AQUÍ ---
1- docker star server_web
2- docker start base_datos
3- docker exect -it server_web sh
-4 ping -c 3 base_datos: ping -c 3 base_datos
PING base_datos (172.18.0.2): 56 data bytes
64 bytes from 172.18.0.2: seq=0 ttl=64 time=0.994 ms
64 bytes from 172.18.0.2: seq=1 ttl=64 time=0.087 ms
64 bytes from 172.18.0.2: seq=2 ttl=64 time=0.117 ms
5- exit 
6- docker stop server_web base_datos
7- docker rm -f server_web base_datos
8- docker network ls 
9- NETWORK ID     NAME                   DRIVER    SCOPE
7d9950947a56   bridge                 bridge    local
f410133f0583   flow_network           bridge    local
10- docker network rm flow_network


🐛 Ejercicio 4: Lectura de Código y Debugging (El Error de Localhost)
# Contexto: Un desarrollador Junior configura su aplicación de Python (Django) en un contenedor.
# La base de datos (PostgreSQL) corre en otro contenedor llamado `db_postgres`. Ambos están en 
# la misma `docker network`.
#
# El Junior te muestra su archivo de configuración de Django, que dice:
# DATABASES = {
#     'HOST': 'localhost',
#     'PORT': '5432'
# }
#
# Al arrancar, Django tira un error: "Connection refused on port 5432".
# El Junior dice: "¡Pero si mi base de datos está corriendo perfecto en el puerto 5432!".
#
# Pregunta Debugging: Explícale al Junior por qué poner `localhost` no funciona cuando 
# el código corre adentro de Docker. ¿Qué palabra EXACATA debe escribir en la variable 
# 'HOST' para que Django encuentre a PostgreSQL exitosamente gracias a la red que crearon?

# --- TU EXPLICACIÓN AQUÍ ---
Poner local host no funciona porque dentro de un contenedor, localhost se refiere al propio contenedor, no al contenedor de la base de datos. Para que Django pueda conectarse a PostgreSQL, debe usar el nombre del contenedor de la base de datos como 'HOST'. En este caso, debe cambiar 'HOST' a 'db_postgres' (el nombre del contenedor de PostgreSQL) para que la conexión funcione correctamente gracias a la red Docker que los conecta.



🧠 FASE 3: CONSOLIDACIÓN TEÓRICA
❓ Pregunta Teórica 1:
Si levanto mi base de datos con docker run --network flow_network postgres (Nota: NO le puse mapeo de puertos -p 5432:5432), ¿podrá un contenedor Django que también esté dentro de flow_network conectarse a esa base de datos? Justifica la diferencia entre conectividad interna (Docker Network) y conectividad externa (Port Mapping).

El mappeo externo o port mapping (-p 5432:5432) expone el puerto de la base de datos al mundo exterior, permitiendo que cualquier aplicación fuera de Docker pueda conectarse a ella. Sin embargo, cuando ambos contenedores (Django y PostgreSQL) están en la misma Docker Network (flow_network), pueden comunicarse directamente entre sí usando sus nombres de contenedor sin necesidad de exponer puertos al exterior. Esto proporciona un nivel adicional de seguridad, ya que la base de datos no es accesible desde fuera del entorno Docker, reduciendo el riesgo de ataques externos.


❓ Pregunta Teórica 2:
¿Por qué es una ventaja de seguridad masiva el hecho de que el DNS de Docker solo resuelva nombres (traduzca nombres a IPs) dentro de las redes personalizadas, aislando esos servidores del resto de tu computadora y del internet público?
Es un nivel de seguridad muy recoemdable porque al mantener la resolución de nombres y la comunicación entre contenedores dentro de una red personalizada, se evita que servicios sensibles (como bases de datos) sean accesibles desde el exterior. Esto significa que incluso si alguien intenta acceder a tu máquina desde internet, no podrá llegar a esos contenedores internos, ya que no están expuestos a la red pública. Además, al usar nombres de contenedor en lugar de direcciones IP, se reduce la posibilidad de errores de configuración y se facilita la gestión de los servicios dentro del entorno Docker.


🗣️ Prueba de Feynman (Explicación):
Escenario: Tienes que explicarle a un Junior cómo funciona una Docker Network.
Explícale el concepto usando la analogía de una oficina cerrada (La red), empleados con gafetes con su nombre (Contenedores) y el intercomunicador de la oficina (Resolución DNS).
La creacion de una docker network con el coamndo docker create network flow_network es como construir una oficina cerrada donde solo los empleados (contenedores) que tienen un gafete con su nombre pueden entrar y comunicarse entre sí. Cada empleado tiene un intercomunicador (DNS interno) que les permite llamarse por su nombre en lugar de recordar números de teléfono (direcciones IP). Esto significa que si un empleado quiere hablar con otro, simplemente dice el nombre del otro empleado y el intercomunicador se encarga de conectarlos, sin que nadie más fuera de la oficina pueda escucharlos o intervenir.