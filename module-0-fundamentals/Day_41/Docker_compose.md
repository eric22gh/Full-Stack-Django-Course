🐳 DÍA 41: MÓDULO 0 - Docker Compose (Orquestación Multi-Contenedor en Espiral)
📦 Dependencias del Módulo:

Entorno: VS Code + Terminal.
Herramientas: Docker Desktop activo.

📖 FASE 1: TEORÍA
Hasta ayer, tu flujo de trabajo para levantar un proyecto era Imperativo:
docker network create mi_red
docker volume create mi_volumen
docker run -d --network mi_red -v mi_volumen:/data db
docker build -t mi_app .
docker run -d --network mi_red -p 80:80 mi_app

Imagina hacer esto todos los días, para 5 proyectos distintos. Es inviable.
La solución es Docker Compose. Es una herramienta Declarativa. Tú creas un archivo llamado docker-compose.yml, donde escribes en texto plano cómo quieres que sea tu infraestructura. Luego, escribes un solo comando (docker compose up) y Docker automáticamente crea las redes, los volúmenes, construye las imágenes y levanta todos los contenedores en el orden correcto.

DOCUMENTACIÓN OFICIAL
🔗 Doc Oficial: Docker Compose Overview / Compose File Reference


🎯 El Propósito
Infraestructura como Código (IaC). Poder subir la "receta" de tu infraestructura a GitHub (el .yml), de modo que si un compañero nuevo entra a la Agencia Flow, solo tenga que escribir docker compose up para tener Base de Datos, Backend y Frontend corriendo en 10 segundos.


🔑 Puntos Clave: Sintaxis YAML
El archivo docker-compose.yml se basa en indentación (espacios). Tiene 3 secciones principales:

services: Aquí defines los contenedores (ej. la app web, la base de datos).

volumes: Aquí declaras los Named Volumes que los servicios usarán.

networks: (Opcional) Docker Compose crea una red automática para todos los servicios de ese archivo, pero puedes definir redes extra si lo deseas.


⚠️ Buenas y Malas Prácticas
✅ Buena Práctica: Usar un archivo .env para inyectar las contraseñas en el docker-compose.yml.

❌ Mala Práctica: Escribir contraseñas directamente (POSTGRES_PASSWORD=12345) dentro del archivo docker-compose.yml y luego subirlo a GitHub.



💻 Implementación Oficial (Comandos Core)
# 1. Levantar toda la infraestructura en segundo plano (-d)
docker compose up -d

# 2. Reconstruir las imágenes antes de levantar (si cambiaste tu código Python/Dockerfile)
docker compose up -d --build

# 3. Ver qué contenedores de esta infraestructura están corriendo
docker compose ps

# 4. Ver los logs de todos los servicios al mismo tiempo (para debuggear)
docker compose logs -f

# 5. Apagar todo y DESTRUIR contenedores y redes (Los volúmenes SOBREVIVEN por defecto)
docker compose down

# 6. Apagar todo y DESTRUIR LOS VOLÚMENES TAMBIÉN (Bomba nuclear de datos)
docker compose down -v



💻 FASE 2: PRÁCTICA DIARIA
(Regla E2E: Crea una carpeta llamada proyecto_compose, ábrela en VS Code y realiza estos flujos completos).

⚙️ Ejercicio 1: Implementación E2E - Lógica Base (El Servidor Aislado con Volumen)
# Contexto: Vamos a traducir el flujo imperativo de comandos a código declarativo.
# Requisitos Ejecutables (Flujo Completo):
# 1. En VS Code, crea el archivo `docker-compose.yml`. Escribe esta estructura exacta:
#
# services:
#   mi_base_de_datos:
#     image: redis:alpine
#     ports:
#       - "6379:6379"
#     volumes:
#       - datos_redis:/data
#
# volumes:
#   datos_redis:
#
# 2. En tu terminal, ejecuta: `docker compose up -d`
# 3. Ejecuta `docker compose ps o docker compose ls` para confirmar que está corriendo.
# 4. Destruye la infraestructura preservando los datos: `docker compose down`
# 
# Pega aquí el output que te dio el comando `docker compose up -d`. 
# (Notarás que Docker creó la red y el volumen automáticamente).

# --- TU OUTPUT DE CONSOLA AQUÍ ---
1- touch docker-compose.yml
2- services:
#   mi_base_de_datos:
#     image: redis:alpine
#     ports:
#       - "6379:6379"
#     volumes:
#       - datos_redis:/data
#
# volumes:
#   datos_redis:
3- docker compose up -d: [+] up 13/13
 ✔ Image redis:alpine                            Pulled                      7.8s
 ✔ Network proyecto_compose_default              Created                     0.1s
 ✔ Volume proyecto_compose_datos_redis           Created                     0.0s
 ✔ Container proyecto_compose-mi_base_de_datos-1 Started  
 4- docker compose ps: 
 NAME                                  IMAGE          COMMAND                  SERVICE            CREATED              STATUS              PORTS
proyecto_compose-mi_base_de_datos-1   redis:alpine   "docker-entrypoint.s…"   mi_base_de_datos   About a minute ago   Up About a minute   0.0.0.0:6379->6379/tcp, [::]:6379->6379/tcp
5- docker compose down:
[+] down 2/2
 ✔ Container proyecto_compose-mi_base_de_datos-1 Removed                     0.6s
 ✔ Network proyecto_compose_default              Removed   



🚀 Ejercicio 2: Implementación E2E - Escenario Real (La Arquitectura Completa - App + DB)
# Contexto: Llegó la hora de la verdad. Vas a orquestar TU propio código Python (Dockerfile) 
# para que hable con una base de datos (Postgres) usando Compose.
#
# Requisitos Ejecutables (Flujo Completo Espiral):
# 1. Crea `app.py`:
#    import os
#    db_host = os.environ.get('DB_HOST', 'Desconocido')
#    print(f"¡Backend arrancado! Conectando a la base de datos en: {db_host}")
# 2. Crea `Dockerfile`:
#    FROM python:3.10-slim
#    WORKDIR /app
#    COPY app.py .
#    CMD ["python", "app.py"]
# 3. Edita tu `docker-compose.yml` para tener DOS servicios (borra el redis del ej1):
#
# services:
#   backend_flow:
#     build: .                 # Le dice a Compose que use el Dockerfile de esta carpeta
#     environment:
#       - DB_HOST=db_postgres  # Variable de entorno que lee app.py
#     depends_on:
#       - db_postgres          # Espera a que la base de datos arranque primero
#
#   db_postgres:
#     image: postgres:15-alpine
#     environment:
#       - POSTGRES_PASSWORD=temporal123
#     volumes:
#       - pg_datos:/var/lib/postgresql/data
#
# volumes:
#   pg_datos:
#
# 4. Ejecuta: `docker compose up -d`
# 5. Lee los logs de tu aplicación para ver si leyó la variable correctamente: 
#    `docker compose logs backend_flow`
# 6. Apaga todo: `docker compose down`
# Pega aquí el output que te dio el comando `docker compose logs backend_flow`.

# --- TU OUTPUT DE LOGS AQUÍ ---

1- touch app.py
2- en la app escribi lo siguiente: import os
db_host = os.environ.get("DB_HOST", "Desconocido")
print(f"Backend iniciando, Conectando a la base de datos en: {db_host}")
3- touch dockerfile
4- en el dockerfile puse: FROM python:3.9-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
5- en el archivo docker-compose.yml puse: 
services:
  backend_flow:
    build: .
    environment:
      - DB_HOST=db_postgres
    depends_on:
      - db_postgres
  db_postgres:
    image: postgres:15-alpine
    environment:
      - POSTGRES_PASSWORD=Temporal123
    volumes:
      - pg_datos:/var/lib/postgresql/data
volumes:
  pg_datos:
6- docker compose up -d: 
7- docker compose ps: 
NAME                             IMAGE                COMMAND                  SERVICE       CREATED          STATUS          PORTS
proyecto_compose-db_postgres-1   postgres:15-alpine   "docker-entrypoint.s…"   db_postgres   56 seconds ago   Up 55 seconds   5432/tcp
8- docker compose logs backend_flow:
backend_flow-1  | Backend iniciando, Conectando a la base de datos en: db_postgres
9- docker compose down: 
[+] down 3/3
 ✔ Container proyecto_compose-backend_flow-1 Removed                                                    0.0s
 ✔ Container proyecto_compose-db_postgres-1  Removed                                                    0.2s
 ✔ Network proyecto_compose_default          Removed                                                    0.2s


🚀 Ejercicio 3: Implementación E2E - Escenario Real (Inyección Segura de Secretos)
# Contexto: En el Ejercicio 2, escribiste "POSTGRES_PASSWORD=temporal123" en texto plano. 
# Si subes eso a GitHub (Día 34), te hackearán. Vamos a integrar el Día 36 (.gitignore y .env).
#
# Requisitos Ejecutables (Flujo Completo Espiral):
# 1. Crea un archivo `.env` en tu carpeta y escribe adentro: 
#    MI_SECRETO_DB=SuperPassword2026!
# 2. Crea tu archivo `.gitignore` y escribe adentro: `.env`
# 3. Modifica el servicio de postgres en tu `docker-compose.yml` para que lea el archivo `.env`:
#
#   db_postgres:
#     image: postgres:15-alpine
#     environment:
#       - POSTGRES_PASSWORD=${MI_SECRETO_DB}  # Compose inyecta la variable automáticamente
#     # ... resto del código intacto ...
#
# 4. Levanta todo de nuevo: `docker compose up -d`
# 5. Verifica que la infraestructura levantó sin errores.
# 6. Destruye ABSOLUTAMENTE TODO, incluyendo los volúmenes para reiniciar el sistema 
#    desde cero: `docker compose down -v`
# 
# Pega aquí el comando de validación `git status` comprobando que el archivo `.env` está oculto.

# --- TU OUTPUT DE GIT STATUS AQUÍ ---
1- touch .env
2- escribi: MI_SECRETO_DB=SuperPassword2026! en el env
3- touch .gitignore
6- escribi en el .gitignore env
7- EN EL DOCKER COMPOSE: 
db_postgres:
    image: postgres:15-alpine
    environment:
      - POSTGRES_PASSWORD=${MI_SECRETO_DB}
8- docker compose up -d
9- sin errores
10- docker compose down -v
11- git status: 
 .gitignore
        Docker-compose.yml
        Dockerfile
        app.py

nothing added to commit but untracked files present (use "git add" to track)


🐛 Ejercicio 4: Lectura de Código y Debugging (El YAML Traicionero)
# Contexto: Un Junior intenta copiar tu archivo del Ejercicio 1. Él escribe esto:
#
# services:
# mi_base_de_datos:
# image: redis:alpine
# ports:
# - "6379:6379"
#
# Cuando el Junior ejecuta `docker compose up -d`, la terminal le arroja un error espantoso 
# diciendo: "yaml: line 2: mapping values are not allowed in this context".
#
# Pregunta Debugging: ¿Qué regla estricta de formato tiene el lenguaje YAML que el 
# Junior ignoró por completo al copiar tu código? 

# --- TU EXPLICACIÓN AQUÍ ---
El problema claramente esta en la linea 2, ya que el Junior no respetó la indentación. En YAML, la indentación es crucial para definir jerarquías y relaciones entre elementos. Cada nivel de indentación debe estar representado por espacios (no tabulaciones), y los elementos hijos deben estar correctamente alineados bajo sus elementos padres. En este caso, "mi_base_de_datos" debería estar indentado con dos espacios bajo "services:", y "image" y "ports" deberían estar indentados con dos espacios adicionales bajo "mi_base_de_datos:". La falta de esta estructura correcta provoca el error de mapeo que se menciona.


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA
❓ Pregunta Teórica 1:
En el Ejercicio 2 agregamos la instrucción depends_on. ¿Por qué en una arquitectura moderna es importante decirle a Docker Compose que el backend_flow depende de la db_postgres antes de arrancar? ¿Qué error lógico ocurriría si el backend arranca primero?
Hoy en dia con la automatizacion del despliegue de insfractura con sistemas es una gran ventaja en terminos de agilidad y rapidez, pero dicho sistema no le importa que va despues o antes el solo va a segiuir desplegando y en ciertos casos como el de la pregunta puede dar error. El backend necesita de una base de datos para una correcta funcion, si el arracan y se crea antes que la base de datos se podrian generar erroreres de datos, autentificacion, migracion y otros mas. Por eso es la importancia en el despliegue automatizado de docker compose el escribir y declarar el depens on.


❓ Pregunta Teórica 2:
En el docker-compose.yml del Ejercicio 2, NO declaramos ninguna sección networks:. Sin embargo, backend_flow y db_postgres pueden comunicarse entre ellos mágicamente usando sus nombres. Según la teoría, ¿qué hace Docker Compose por debajo de la mesa para que esto sea posible sin que nosotros escribamos comandos docker network create?
A la hora desplegar una infraestructura con docker compose, gracias a declaraciones en el archivo docker-compose.yml se desplegan infraestruturas como la red, en caso de que no se especifique la red, docker compose creara una red por defecto para que toda su infraestructura declarada dentro del docker-compose.yml se converse entre si.



🗣️ Prueba de Feynman (Explicación):
Escenario: Tienes que explicarle a un gerente de proyecto la diferencia entre usar comandos sueltos de Docker (Imperativo) vs usar Docker Compose (Declarativo).
Explícale el concepto usando la analogía de un Director de Orquesta Sinfónica (Docker Compose) vs ir atril por atril diciéndole a cada músico cuándo empezar a tocar.
En todo campo de la vida hacer las cosas uno a uno puede zonar simple y efectivo, pero a grandes cantidades no es escalable, ahi es donde entra docker compose en vez de docker run o docker create network ya que con ellos se crean contenedores y redes uno a uno, como no es eficiente para casos de gran escala entra docker compose para varias o infraestructura reutilizable. Compose es como tener a un ditrector de orquesta con 1000 artistas para un evento y por medio de las pautas guiar o por otro lado tenes a docker run o create que seria como ir de uno en uno con los artistas y explicarles las guias y cuando tocar fuerto o suave.
