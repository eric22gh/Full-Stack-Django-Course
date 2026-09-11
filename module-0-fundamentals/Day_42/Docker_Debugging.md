🐳 DÍA 42: MÓDULO 0 - Docker Debugging (La Autopsia de Contenedores)
📦 Dependencias del Módulo:

Entorno: VS Code + Terminal.
Herramientas: Docker Desktop activo.


📖 FASE 1: TEORÍA
En la vida real, los contenedores fallan. Una librería falta, una contraseña es incorrecta o un puerto está bloqueado. Como los contenedores son cajas cerradas, no puedes simplemente abrir una pantalla para ver qué pasa. Tienes que usar el "estetoscopio" de Docker para escuchar el corazón del contenedor (Logs) o abrir la caja quirúrgicamente (Shell interactivo).


DOCUMENTACIÓN OFICIAL
🔗 Doc Oficial: Docker Logs / Docker Exec


🎯 El Propósito
Reducir el tiempo de resolución de problemas (Time to Resolution - TTR). Si un despliegue falla en AWS, debes saber exactamente qué comandos tirar para extraer el error y solucionarlo, en lugar de reiniciar el servidor a ciegas esperando un milagro.

🔑 Puntos Clave: Las 3 Armas del Debugging
Lectura de Logs (docker logs): Es el equivalente a ver el historial clínico. Todo lo que el programa de Python imprime (print()) o los errores que arroja (Tracebacks), van a parar a los logs del contenedor.

Invasión Quirúrgica (docker exec -it): Te permite abrir una terminal dentro de un contenedor que ya está corriendo. (Útil para revisar si los archivos existen en las rutas correctas o probar ping).

Inspección del Molde (docker inspect): Te escupe un archivo JSON gigante con el ADN del contenedor (Rutas de volúmenes físicos, dirección IP interna, variables de entorno que está usando).



⚠️ Buenas y Malas Prácticas
✅ Buena Práctica: Usar docker logs -f <contenedor> (El parámetro -f significa "follow"). Mantendrá la terminal abierta mostrando los logs nuevos en tiempo real mientras el cliente usa la aplicación.

❌ Mala Práctica: Entrar a un contenedor de producción con docker exec -it, abrir nano y editar el código de Python ahí mismo para arreglar un error urgente. (Recuerda: si el contenedor se reinicia, el arreglo se perderá). osea no es bueno trabajr el contenedor en caliente osea en produccion.


💻 Implementación Oficial (Comandos Core)
# 1. Ver los logs (historial) de un contenedor
docker logs mi_app_django

# 2. Ver los logs en vivo (como si estuvieras viendo la Matrix)
docker logs -f mi_app_django

# 3. Ver SOLO las últimas 10 líneas de logs (útil si hay miles de líneas)
docker logs --tail 10 mi_app_django

# 4. Inyectar una terminal Bash/Sh en un contenedor corriendo
docker exec -it mi_app_django bash   # (Usa 'sh' si 'bash' no existe, ej. en imágenes Alpine)

# 5. Inspeccionar el ADN del contenedor
docker inspect mi_app_django


💻 FASE 2: PRÁCTICA DIARIA
(Regla E2E: Crea una carpeta docker_debug, ábrela en VS Code).


⚙️ Ejercicio 1: Implementación E2E - Lógica Base (El Estetoscopio de Logs)
# Contexto: Tienes un bot que cada segundo genera un reporte de ventas. 
# Necesitas ver la historia pasada y monitorear el futuro en vivo.
#
# Requisitos Ejecutables (Flujo Completo):
# 1. Ejecuta este comando que crea un contenedor que imprime números sin parar:
#    docker run -d --name bot_ruidoso ubuntu bash -c "while true; do echo 'Reporte de venta generado'; sleep 1; done"
# 2. Usa el comando normal para ver los logs y pega aquí un par de líneas de lo que arroja.
# 3. Usa el comando con `-f` para "seguir" los logs. Verás cómo aparece una nueva línea 
#    cada segundo. (Usa Ctrl+C para salir).
# 4. Usa el comando para ver SOLO las últimas 3 líneas del log (`--tail`). Pega tu comando aquí.
# 5. Destruye el contenedor: `docker rm -f bot_ruidoso`

# --- TUS LOGS Y COMANDO 'TAIL' AQUÍ ---

1- docker run -d --name bot_ruidoso ubuntu bash -c "while true; do echo 'Reporte de venta generado'; sleep 1; done"
2- docker logs bot_ruidoso 0 docker logs --tail 5 bot_ruidoso
3- resultado: Reporte de venta generado
Reporte de venta generado
Reporte de venta generado
4- docker logs -f bot_ruidoso
5- docker logs --tail 3 bot_ruidoso
6- docker rm -f bot_ruidoso


🚀 Ejercicio 2: Implementación E2E - Escenario Real (La Invasión Quirúrgica)
# Contexto: Desplegaste un servidor web de Nginx. El cliente dice que la página no 
# carga correctamente. Sospechas que el archivo "index.html" no está donde debería estar 
# adentro del servidor. Tienes que entrar a mirar.
#
# Requisitos Ejecutables (Flujo Completo):
# 1. Levanta un servidor web simple en segundo plano:
#    docker run -d --name mi_web nginx
# 2. Ejecuta el comando para "abrir una terminal bash adentro del contenedor en ejecución".
#    (El comando empieza con `docker exec -it...`).
# 3. ¡Estás dentro del contenedor! Navega a la carpeta pública de Nginx:
#    cd /usr/share/nginx/html
# 4. Usa el comando `ls` y pega aquí lo que te respondió Linux. (Ahí confirmas que los 
#    archivos HTML sí existen).
# 5. Sal del contenedor (`exit`) y destruye el servidor (`docker rm -f mi_web`).

# --- TU OUTPUT DEL COMANDO 'ls' AQUÍ ---

1- docker run -d --name my_web nginx
2- docker exec -it my_web bash
3- cd /usr/share/nginx/html/
4- ls: 50x.html  index.html
5- exit
6- docker rm -f my_web


🚀 Ejercicio 3: Implementación E2E - Escenario Real (La Autopsia Post-Mortem)
# Contexto: Un contenedor tuyo (basado en Alpine Linux) falló y quieres saber exactamente 
# qué variables de entorno usó al momento de crearse, porque sospechas que tu 
# 'docker-compose.yml' inyectó una contraseña errónea.
#
# Requisitos Ejecutables (Flujo Completo):
# 1. Crea un contenedor inyectándole una variable de entorno de prueba (No correrá nada, solo morirá):
#    docker run -d --name server_falla -e SECRETO_API="ClaveFalsa123" alpine
# 2. Ejecuta `docker ps`. Verás que el contenedor NO está corriendo (porque Alpine no tiene 
#    nada que hacer y se apaga de inmediato).
# 3. A pesar de estar apagado, ejecuta `docker inspect server_falla`. 
#    La terminal escupirá un JSON gigante.
# 4. Busca en ese texto gigante la sección "Env" (puedes hacer scroll hacia arriba).
#    Pega aquí esa sección donde se ve claramente la variable `SECRETO_API`.
# 5. Destruye el cadáver del contenedor: `docker rm server_falla`

# --- TU OUTPUT DE 'Env' EN EL JSON AQUÍ ---
1- docker run -d --name server_falla -e SECRETO_API="ClaveFalsa123" alpine (La -e significa una variable de entorno)
2- docker ps -a: 
CONTAINER ID   IMAGE                     COMMAND                  CREATED          STATUS                
      PORTS                    NAMES
74635b18203e   alpine                    "/bin/sh"                24 seconds ago   Exited (0) 24 seconds ago                            server_falla
81c693d5ec9d   28a898719c18              "/usr/bin/buildkitd-…"   2 days ago       Exited (1) 2 days ago                                buildx_buildkit_default
3- docker inspect server_falla(correcto me refleja un JSON grande)
4- "Env": [
                "SECRETO_API=ClaveFalsa123",
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
5- docker rm server_falla


🐛 Ejercicio 4: Lectura de Código y Debugging (El Error de la Consola Equivocada)
# Contexto: El junior de la agencia levantó un servidor de Base de Datos Alpine muy rápido:
# docker run -d --name super_db alpine sleep infinity
#
# Luego, quiso entrar al servidor para revisar unos archivos y ejecutó:
# docker exec -it super_db bash
#
# La terminal arrojó un error:
# OCI runtime exec failed: exec failed: container_linux.go:380: starting container process caused: exec: "bash": executable file not found in $PATH: unknown
#
# Pregunta Debugging: Explícale al Junior, basado en la teoría de optimización de imágenes 
# del Día 38, por qué el comando `bash` no existe en ese contenedor y qué otra terminal 
# (más pequeña/ligera) debe llamar en su lugar para poder entrar.

# --- TU EXPLICACIÓN Y COMANDO CORREGIDO AQUÍ ---
el comando `bash` no existe en el contenedor Alpine porque Alpine es una distribución de Linux muy ligera y minimalista que no incluye Bash por defecto para mantener su tamaño pequeño. En su lugar, Alpine utiliza `sh` (shell) como su intérprete de comandos predeterminado. Por lo tanto, para entrar al contenedor, el junior debería usar el siguiente comando corregido:
docker exec -it super_db sh


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA
❓ Pregunta Teórica 1:
Tu aplicación Django está fallando y devolviendo "Error 500" a los clientes. Tienes dos opciones para ver el error de Python:
A) Entrar al contenedor con docker exec -it app bash y buscar un archivo de texto con errores.
B) Usar docker logs mi_app_django.
¿Por qué la arquitectura de Docker (y los programas modernos de consola) favorece la opción B y asume que todo programa debe "escupir" (stdout/stderr) sus errores a la terminal en lugar de guardarlos en archivos ocultos?
Es una buenas practica usar docker logs en vez de docker exec -it para entrar al contenedor y buscar archivos de logs. Al usar docker logs, se puede acceder a los errores y mensajes de salida directamente desde la terminal sin necesidad de modificar el contenedor en ejecución. Esto facilita el monitoreo en tiempo real y evita cambios no persistentes en el contenedor que podrían perderse si este se reinicia.
Nota: los contenedores envían todo a las salidas estándar de Linux (stdout y stderr). Esto permite que herramientas externas (como Datadog o AWS CloudWatch) capturen esos textos automáticamente sin tener que meterse a rebuscar archivos en cada contenedor.


❓ Pregunta Teórica 2:
Explicamos que usar docker exec -it para editar código de Python en producción con "Nano/Vim" es una pésima práctica. Si encuentras un error en tu código Python en producción usando los logs, describe cuáles son los 3 pasos reales (desde tu computadora local hasta el servidor) para arreglar ese error de manera profesional y persistente, respetando la filosofía inmutable de Docker.
Usar docker logs es una buena practica y los 3 pasos para arreglar un error de manera profesional y persistente son:
1. Localmente, en tu computadora, abre el proyecto de Python y corrige el error
2. Construye una nueva imagen de Docker con el código corregido usando `docker build`
3. Despliega la nueva imagen en el servidor, reemplazando el contenedor anterior


🗣️ Prueba de Feynman (Explicación):
Escenario: Un desarrollador Junior te ve usando docker logs y docker inspect y te pregunta: "¿Por qué hacemos tanto esfuerzo analizando desde afuera? ¿Por qué no mejor instalamos 'Escritorio Remoto' (RDP/VNC) adentro de los contenedores para entrar y usar el mouse como en Windows?".
Explícale por qué no hacemos eso, usando la analogía de la diferencia entre Un Piloto volando un Avión desde la cabina con botones físicos (VM tradicional) vs Un Controlador Aéreo guiando a un Drone desde tierra mirando pantallas de radar (Docker).

Primeramente, en una VM tradicional o docker inmspect, el piloto tiene acceso directo a todos los controles físicos del avión(la parte interna del contenedor), lo que le permite interactuar con el sistema de manera completa y directa(propensa a fallos si no se sabe lo que se esta haciendo). 
En cambio, Docker logs funciona más como un controlador aéreo que guía un dron desde tierra. El controlador no necesita estar dentro del dron para operarlo; en su lugar, utiliza herramientas externas para monitorear y controlar el dron de manera eficiente. Esto permite mantener los contenedores ligeros, seguros y fáciles de gestionar en pocas palabras es una buena buena practica usar docker logs por su simplesa y asertividad.
