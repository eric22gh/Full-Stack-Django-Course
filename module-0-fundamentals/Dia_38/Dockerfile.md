## DÍA 38: MÓDULO 0 - Dockerfile Profundo (Capas, Caché y Optimización)
# 📦 Dependencias del Módulo:

# Entorno: VS Code + Terminal Linux / PowerShell.
# Herramientas: Docker Desktop activo.


# 📖 FASE 1: TEORÍA
# Ayer usamos la imagen oficial de Nginx. Hoy crearemos la imagen de tu propio programa en Python. 
# Para decirle a Docker cómo construir esa imagen, usamos un archivo mágico llamado Dockerfile.
# El secreto mejor guardado de los Arquitectos Cloud es entender que Docker construye las imágenes en CAPAS (Layers). 
# Cada línea de tu Dockerfile crea una capa nueva. Docker es inteligente: si modificas una línea al final del archivo, 
# Docker usará la "Caché" (memoria) para las líneas anteriores y solo reconstruirá el final. Si lo haces mal, 
# harás que Docker reconstruya todo desde cero cada vez, haciendo que tus despliegues sean lentísimos.


# DOCUMENTACIÓN OFICIAL
#🔗 Doc Oficial: Dockerfile reference / Best practices for writing Dockerfiles


#🎯 El Propósito
#Convertir nuestro código local en una Imagen Inmutable que podamos enviar a cualquier servidor del mundo. 
#Además, optimizar la velocidad de construcción (Build) y el peso de la imagen final.


# 🔑 Puntos Clave: Comandos del Dockerfile

# FROM: Siempre es la primera línea. Define tu sistema operativo / lenguaje base (ej. FROM python:3.10-slim).
# WORKDIR: Crea una carpeta dentro del contenedor y se "mueve" hacia ella (como hacer un mkdir + cd). (ej. WORKDIR /app).
# COPY: Copia archivos de tu laptop hacia el contenedor. (ej. COPY app.py /app/).
# RUN: Ejecuta comandos de terminal durante la construcción de la imagen (ej. RUN pip install -r requirements.txt). Se usa para preparar la imagen.
# CMD: Es el comando final que se ejecutará cuando el contenedor arranque. Solo puede haber un CMD por Dockerfile.
# .dockerignore: Funciona igual que el .gitignore. Le dice a Docker qué archivos de tu laptop NO debe meter en la imagen (como tu entorno virtual venv o carpetas ocultas de git).



#⚠️ Buenas y Malas Prácticas

#✅ Buena Práctica: Separar el COPY requirements.txt del COPY . . (todo el código) para aprovechar la caché. Si solo cambias una línea de Python, Docker no debería reinstalar todas las librerías.

# ❌ Mala Práctica: Usar la imagen ubuntu gigante y luego instalarle Python a mano con comandos RUN. Mejor usa directamente python:3.10-slim (una versión minimalista ya preparada).


#💻 Implementación Oficial (Comandos CLI)
# 1. Construir la imagen a partir del Dockerfile en la carpeta actual (.)
#docker build -t mi-app-python .

# 2. Construir forzando a no usar la caché (si sospechas de un error)
#docker build --no-cache -t mi-app-python .

# 3. Ver cuánto pesa tu imagen recién creada
#docker images

Nota: pasos para crear una imagen
1- crear la carpeta donde va la imagen
2- craer el entorno virtual
2- crear un dockerignore
4- craer un archivo requierements donde van las dependencias
5- craer un dockerfile(sin extencion)
6- añadir el entorno virtual al dockerignore
7- craer el archivo en el lenguaje que quieras, ya que va ser el output de tu imagen
8- codigo en el dockerfile:  FROM python:3.10-slim
#    WORKDIR /app
#    COPY requirements.txt .
#    RUN pip install -r requirements.txt
#    COPY bot.py .
#    CMD ["python", "bot.py"]
9- despues de todo usamos el comando docker build -t (nombre de la imagen)
10 docker run (nombre de la imagen)



#💻 FASE 2: PRÁCTICA DIARIA
#(Instrucción: Crea una carpeta llamada docker_build en tu PC, ábrela en VS Code y crea los archivos que se piden a continuación).


#⚙️ Ejercicio 1: Implementación - Lógica Base (El Código y el Ignorador)
# Contexto: Vamos a preparar los archivos locales antes de empacarlos.
#
# Requisitos Ejecutables:
# 1. Crea un archivo `bot.py` que contenga: `print("¡Bot de Agencia Flow ejecutándose desde Docker!")`
# 2. Crea un archivo `requirements.txt` y ponle adentro la palabra `requests` (simulando una librería).
# 3. Crea una carpeta local llamada `venv` (simulando tu entorno virtual). ¡NO queremos que esto entre a Docker!
# 4. Crea un archivo llamado `.dockerignore` y escribe adentro `venv/`.
#
# (No hay output de consola para este ejercicio, solo confírmame que creaste los 4 elementos en tu VS Code).

# --- TU CONFIRMACIÓN AQUÍ ---
1- touch bot.py
2- touch requierements.txt
3- python3 -m venv docker_venv
4- touch .dockerignore
5- docker_venv/



#🚀 Ejercicio 2: Implementación - Escenario Real (Tu primer Dockerfile optimizado)
# Contexto: Es hora de escribir la receta. Vamos a aplicar la técnica ninja de la "Caché de Docker".
#
# Requisitos Ejecutables:
# 1. Crea un archivo llamado exactamente `Dockerfile` (sin extensión).
# 2. Pega esta estructura adentro y lee con cuidado el orden:
#    FROM python:3.10-slim
#    WORKDIR /app
#    COPY requirements.txt .
#    RUN pip install -r requirements.txt
#    COPY bot.py .
#    CMD ["python", "bot.py"]
# 3. Abre tu terminal y construye la imagen ejecutando: docker build -t bot-agencia .(el punto es para decirle a docker donde esta mi imagen)
# 4. Ejecuta el contenedor: docker run bot-agencia
# Pega aquí el output final de tu consola cuando corriste el contenedor.

# --- TU OUTPUT DE CONSOLA AQUÍ ---
1- touch dockerfile
2- docker build -t bot-agencia .
3- docker images: IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
bot-agencia:latest   5defac94b05d        202MB         49.7MB
4- docker run bot-agencia
5- $ docker run bot-agencia
!Bot de agencia flow ejecutandose desde docker!



#🚀 Ejercicio 3: Implementación - Escenario Real (Probando la Magia de la Caché)
# Contexto: El cliente quiere que el mensaje del bot diga algo distinto. 
# Vamos a modificar el código y reconstruir la imagen para ver qué tan rápido es Docker.
#
# Requisitos Ejecutables:
# 1. Modifica tu archivo `bot.py` para que ahora imprima: "¡Bot actualizado a la versión 2.0!"
# 2. Vuelve a ejecutar el comando de construcción: docker build -t bot-agencia .
# 3. Observa atentamente los logs que escupe la terminal mientras construye. 
#    Notarás que en los pasos del 1 al 4 (incluyendo la instalación de librerías) dice la palabra "CACHED". 
#    Docker fue inteligente y no reinstaló 'requests' porque el requirements.txt NO cambió.
# Pega aquí una línea de tu terminal donde se vea claramente la palabra "CACHED" durante esta segunda construcción.

# --- TU OUTPUT DE CONSOLA (LÍNEA CON CACHED) AQUÍ ---

1- print("!Bot de agencia actualizado a la version 2.0!")
2- docker build -t bot-agencia
3- => CACHED [2/5] WORKDIR /app                                                                                                                                           0.0s
 => CACHED [3/5] COPY requirements.txt .                                                                                                                                0.0s
 => CACHED [4/5] RUN pip install -r requirements.txt                                                                                                                    0.0s
 => [5/5] COPY bot.py . 
 4- docker run bot-agencia
 5- docker run bot-agencia
!Bot de agencia actualizado a la version 2.0!


#🐛 Ejercicio 4: Lectura de Código y Debugging (El Junior y los Tiempos de Carga)
# Contexto: Un Junior en la agencia escribe su primer Dockerfile. Es este:
#
# FROM python:3.10
# WORKDIR /app
# COPY . .
# RUN pip install -r requirements.txt
# CMD ["python", "main.py"]
#
# El Junior se queja: "Cada vez que modifico una sola línea de mi código Python y hago 'docker build', 
# Docker se queda 5 minutos reinstalando todas las librerías desde internet. ¡Docker es lentísimo!".
#
# Pregunta Debugging: Analizando la técnica del Ejercicio 2, ¿por qué el orden que 
# usó el Junior (`COPY . .` ANTES del `RUN pip install`) está destruyendo la caché de Docker? 
# ¿Cómo se lo reescribirías para solucionarlo?

# --- TU EXPLICACIÓN Y DOCKERFILE CORREGIDO AQUÍ ---
A mi parecer y si no me equivoco el principal problema es lo que esta escribiendo en copy, ya que el lo que hace es copiar todos los archivos de la laptop en esa carpeta y usar el . que lo que significa es all, a la hora de modificar una linea de codigo, docker va a tomar en cuenta todo la linea de codigo, sin importar que solo se allan modificado 2 o uno haciendo el proceso lento. Tambien le añadiria que esta instalando una version de python grande entonces esto le añade mas trabajo al contenedor. yo solo escribiria de la siguiente amnera: 
 FROM python:3.10-slim
#    WORKDIR /app
#    COPY requirements.txt .
#    RUN pip install -r requirements.txt
#    COPY bot.py .
#    CMD ["python", "bot.py"]



#🧠 FASE 3: CONSOLIDACIÓN TEÓRICA
#❓ Pregunta Teórica 1:
#¿Cuál es la diferencia técnica entre el comando RUN y el comando CMD dentro de un Dockerfile? (Pista: Uno se usa en la fase de "cocina", el otro en la fase de "comer").
RUN: Se ejecuta en tiempo de CONSTRUCCIÓN (Build Time). Es el horno. (Sirve para instalar cosas que se quedarán grabadas en la Imagen).
CMD: Se ejecuta en tiempo de EJECUCIÓN (Run Time). Es cuando te comes el pastel. (Es el comando que arranca cuando haces docker run).



#❓ Pregunta Teórica 2:
#En el FROM usamos python:3.10-slim. Si hubiéramos usado solo python:3.10 (que pesa alrededor de 1 GB), ¿por qué subir imágenes tan pesadas afectaría negativamente los costos de ancho de banda y almacenamiento de un servidor EC2 en la nube?
En from colocamos el sitema operativo que va a correr el contenedor, se podria decir que es su capa de personalizacion, al tener una capa ligera como la python:3.10-slim el contenedor usa menos recursos para iniciar y por ende la implementacion en local o en la nube tendra una mejor respuesta por el contario si se usa un sistema operativo pesado como python:3.10 afectaria el rendimiento de toda la implementacion haciendola mas lenta y asu vez consumir mas recursos y con tiempos de respuesta prolongados. En el mundo de TI el tiempo de respuesta de una implementacion es valiosa.



# 🗣️ Prueba de Feynman (Explicación):
#Escenario: Tienes que explicarle a un compañero de universidad por qué el orden de las líneas en el Dockerfile importa tanto (el concepto de Caché).
#Explícaselo usando la analogía de hacer un pastel de 3 pisos, donde el piso de abajo es el pan, el del medio es el relleno y el de arriba es el betún (glaseado). ¿Qué pasa si te equivocas con el sabor del betún (última línea) vs qué pasa si te equivocas horneando el pan (primera línea)?
El orden en el dockerfile importa y mucho ya que ya que si ponemos por ejemplo si se pone copy antes que requierements.txt lo que va a pasar es que cada vez que se cambie una linea de codigo docker va a tener que instalar las dependencias otra vez, una buena practica es poner lo que casi nunca cambia de primero como la base, sistema operativo, dependencias y despues lo que cambia constantemente osea el codigo fuente. Una forma de que quede mas claro es si estas haciendo un pastel y tu cliente no se decide si el fondo de chocolate, en medio fresa y el primer piso vainilla  o fondo de chocolate, en medio vainilla y el primer piso fresa... Una solucion para ir adelantando es escoger el primero y si el cliente al final se decide por la segunda forma, se puede reutilizar el piso del fondo. 