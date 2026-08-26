🐳 DÍA 39: MÓDULO 0 - Docker Volumes (La Memoria Inmortal)

📦 Dependencias del Módulo:
Entorno: VS Code + Terminal.
Herramientas: Docker Desktop activo.

📖 FASE 1: TEORÍA
La primera regla que aprendimos es que los contenedores son "efímeros" (desechables). Esto es genial para servidores web (Nginx) o tu código Python, pero es una pesadilla para las Bases de Datos (PostgreSQL, MySQL). No puedes desechar un contenedor y perder las facturas de tus clientes.

La solución de Docker se llama Volúmenes (Volumes). Un volumen es como conectar un "Disco Duro Externo" (USB) a tu contenedor. Si el contenedor explota, muere o lo borras, los datos siguen seguros en el volumen. Cuando creas un contenedor nuevo, simplemente le conectas ese mismo "Disco Duro Externo" y la base de datos vuelve a la vida como si nada hubiera pasado.



DOCUMENTACIÓN OFICIAL
🔗 Doc Oficial: Manage data in Docker (Volumes)

🎯 El Propósito
Garantizar la Persistencia de Datos. Separar el ciclo de vida del contenedor (que puede morir en cualquier momento) del ciclo de vida de los datos (que deben ser eternos).



🔑 Puntos Clave: Tipos de Almacenamiento
Named Volumes (Volúmenes Nombrados): Docker crea una carpeta secreta y protegida en tu disco duro físico, la bautiza con un nombre (ej. mi_db_volumen) y la administra por ti. (El estándar de oro para bases de datos).

Bind Mounts (Montajes de Enlace): Tú eliges una carpeta específica de tu computadora (ej. C:\Users\Eric\Proyecto) y se la "inyectas" al contenedor. Ideal para desarrollo: si editas un archivo Python en VS Code, el contenedor ve el cambio instantáneamente sin necesidad de reconstruir la imagen.

El parámetro -v: Se usa al hacer docker run para montar el volumen. La sintaxis es -v origen:destino_dentro_del_contenedor.



⚠️ Buenas y Malas Prácticas
✅ Buena Práctica: Usar siempre Named Volumes para bases de datos en producción.

❌ Mala Práctica: Levantar un contenedor de PostgreSQL para un cliente sin asignarle un volumen. El día que reinicies el servidor, la empresa perderá toda su información.



💻 Implementación Oficial (Comandos Core)
# 1. Crear un volumen nombrado administrado por Docker
docker volume create mi_super_volumen

# 2. Ver la lista de volúmenes que existen en tu máquina
docker volume ls

# 3. Correr un contenedor inyectándole el volumen recién creado
# (-v nombre_volumen:/ruta/dentro/del/contenedor)
docker run -d --name mi_app -v mi_super_volumen:/app/datos ubuntu sleep infinity

# 4. Inspeccionar un volumen para saber dónde guarda físicamente los datos Docker
docker volume inspect mi_super_volumen

# 5. Borrar un volumen (peligroso, borras los datos)
docker volume rm mi_super_volumen

# 6. Comando para abrir la terminal interactiva del contenedor
docker exec -it <nombre_o_ID> bash




💻 FASE 2: PRÁCTICA DIARIA
(Instrucción: Sigue los pasos en tu terminal. Usaremos la imagen oficial de Ubuntu para simular la persistencia).



⚙️ Ejercicio 1: Implementación - Lógica Base (La Tragedia de la Amnesia)
# Contexto: Vamos a demostrar CÓMO se pierden los datos si no usamos volúmenes.
#
# Requisitos Ejecutables:
# 1. Crea un contenedor de ubuntu y entra a su terminal interactiva:
#    docker run -it --name contenedor_olvidadizo ubuntu bash
# 2. Estando dentro de Ubuntu, crea un archivo de texto con un secreto:
#    echo "La contraseña de AWS es XYZ" > secreto.txt
# 3. Sal del contenedor escribiendo: exit  (Esto apagará el contenedor).
# 4. Bórralo definitivamente: docker rm contenedor_olvidadizo
# 5. Crea uno idéntico de nuevo: docker run -it --name contenedor_nuevo ubuntu bash
# 6. Intenta leer el secreto usando: cat secreto.txt
#
# Pega aquí el mensaje de error que te dio Linux en el paso 6. Acabas de perder los datos de tu empresa.

# --- TU OUTPUT DE CONSOLA AQUÍ ---
1- docker run -it --name storague_container ubuntu bash
2- touch secreto.txt
3- echo "La contraseña de AWS es XYZ" > secreto.txt
4- exit
5- docker rm storague_container
6- docker ps -a: no hay contenedor con el nombre de storague_container
7- docker run -it --name storague_container ubuntu bash
8- cat secreto.txt: cat: secreto.txt: No such file or directory



🚀 Ejercicio 2: Implementación - Escenario Real (Creando el Disco Duro Inmortal)
# Contexto: Ya no quieres perder datos. Vas a crear un volumen y conectarlo.
#
# Requisitos Ejecutables:
# 1. Sal del contenedor anterior (`exit`) y asegúrate de estar en tu terminal de Windows/Linux.
# 2. Crea un volumen llamado `datos_financieros`: docker volume create datos_financieros
# 3. Crea un contenedor inyectándole este volumen en la carpeta `/info`:
#    docker run -it --name server_seguro -v datos_financieros:/info ubuntu bash
# 4. Dentro del contenedor, muévete a la carpeta compartida (`cd /info`) y crea el archivo:
#    echo "Datos de facturación 2026" > facturas.txt
# 5. Sal del contenedor (`exit`) y bórralo sin miedo: docker rm server_seguro
# Escribe aquí los comandos exactos que usaste en los pasos 2 y 3.

# --- TUS COMANDOS AQUÍ ---
1- exit
2- docker volume create datos_financieros
3- docker run it --name server_seguro -v datos_financieros:/info ubuntu bash
4- o tambien docker exec -it <nombre_o_ID> bash
5- cd info
6- echo "Datos de factura 2026" > facturas.txt
7- cat facturas.txt = Datos de factura 2026
8- exit
9- docker rm server_seguro
10: Error response from daemon: cannot remove container "server_seguro": container is running: stop the container before removing or force remove
11- docker stop server_seguro
12- docker rm server_seguro


🚀 Ejercicio 3: Implementación - Escenario Real (La Resurrección)
# Contexto: El 'server_seguro' fue destruido, pero el volumen 'datos_financieros' sobrevivió.
# Vamos a crear un servidor completamente nuevo y conectarle el disco duro que salvamos.
#
# Requisitos Ejecutables:
# 1. Levanta un nuevo contenedor con otro nombre, pero conectando el MISMO volumen a la MISMA ruta:
#    docker run -it --name server_resucitado -v datos_financieros:/info ubuntu bash
# 2. Entra a la carpeta: cd /info
# 3. Lee el archivo: cat facturas.txt
# Pega aquí el output de tu consola. ¡Deberías ver tus datos intactos a pesar de que es un contenedor nuevo!

# --- TU OUTPUT DE CONSOLA AQUÍ ---
1- docker ps -a: el contenedor server_seguro no esta, pero el volumen datos_financieros si esta.
2- docker run -t --name server_resucitado -v datos_financieros:/info ubuntu bash
3- o tambien docker exec -t server_resucitado bash
4- cd info
5- cat facturas.txt
6- datos de facturas 2026

Nota es bueno y hasta buena practica que cuando se cree un contenedor crearle un volumen y atacharlo asi tenemos persistencia de datos.


🐛 Ejercicio 4: Lectura de Código y Debugging (El Error de la Base de Datos)
# Contexto: Un Junior en la agencia debe desplegar una base de datos PostgreSQL usando Docker.
# Él lee la documentación oficial de Postgres, que dice que los datos internamente se 
# guardan en la ruta `/var/lib/postgresql/data`.
#
# El Junior ejecuta este comando:
# docker run -d --name mi_postgres postgres
#
# Al día siguiente, su computadora se reinicia. El Junior ejecuta `docker start mi_postgres` 
# y la base de datos arranca, PERO todas las tablas que el cliente había creado están vacías.
#
# Pregunta Debugging: Explícale al Junior por qué perdió todos los datos. Usando tus conocimientos 
# de Volúmenes, ¿cómo debió haber escrito el comando `docker run` usando un volumen llamado 
# `pg_data` apuntando a la ruta interna que mencionaba la documentación?

# --- TU EXPLICACIÓN Y COMANDO CORREGIDO AQUÍ ---
El comando correcto que debio de usar es el docker run -d --name mi_postgres -v pg_data:/var/lib/postgresql/data postgres
tu comando lo que hizo fue arrancar el contenedor sin el volumen al que pertenece la tabla y el contenedor al no detener el volumen con datos la tabla aparecera en blanco.



🧠 FASE 3: CONSOLIDACIÓN TEÓRICA

❓ Pregunta Teórica 1:
¿Cuál es la principal diferencia de uso entre un Named Volume (Volumen administrado por Docker) y un Bind Mount (Vincular una carpeta específica de tu escritorio al contenedor)? (Pista: ¿Cuál usarías para desarrollar tu código en VS Code viendo cambios en vivo, y cuál usarías para guardar los datos de producción de una base de datos?).
La principal diferencia es bind mount no es persisten, si se borra el contenedor el volumen tambien sera borrado y no se recomienda para bases de datos en produccion. Por el contrario named volume  es persistente, usualmente se crea antes del contenedor y por esta caracteristica yo la usaria en produccion y para bases de datos ya que si le pasa algo al contenedor, simplemente lo elimino y creo otra imagen y contenedor y atacho el named volume y seguimos con los datos del anterior contenedor... Por ultimo para implementaciones de prueba usaria named volume.


❓ Pregunta Teórica 2:
Si ejecutas docker system prune -a --volumes, Docker limpiará todo tu sistema borrando imágenes sin uso, contenedores apagados y volúmenes desconectados. ¿Por qué este comando es una herramienta de limpieza excelente, pero debe ejecutarse con extrema precaución en un servidor de AWS de la Agencia Flow?
Yo personalmente no lo usaria, prefiero verificar manualmente que imagen o contenedor y proceder con su eliminacion asi tengo mas control de lo que se borra, este comando es peligroso y mucho mas si se esta en produccion, ya que se puede venir abajo la implementacion y el malestar de millones de usuarios.


🗣️ Prueba de Feynman (Explicación):
Escenario: Un cliente te pregunta: "Si el contenedor es como una computadora virtual que se borra cuando falla, ¿dónde quedan mis bases de datos?".
Explícale el concepto de Docker Volumes usando la analogía de un trabajador (Contenedor), una mochila (el sistema de archivos efímero) y una caja fuerte empotrada en la pared de la oficina (Volumen).
Los 2 volumenes named volume y bind mount son esenciales para docker, pero funcionan de manera distinta a la hora de eliminarse y en su versatilidad. El named volume es mas versatil, es como usa mochila cuando, se usa para guardar datos del cliente y cuando se despide al empleado se desecha junto con su mochila, en cambio binf mount volume es como una caja fuerte, si al empleado lo despiden(eliminar contenedor) la caja fuerte va a persistir aun qque el empleado ya no este.