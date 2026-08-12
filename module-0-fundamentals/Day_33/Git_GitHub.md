🐙 DÍA 33: MÓDULO 0 - Git Local (La Máquina del Tiempo del Código)
📦 Dependencias del Módulo:
Entorno: VS Code + Terminal Linux.
Herramientas: git (Si no lo tienes en Ubuntu: sudo apt install git).


📖 FASE 1: TEORÍA
Git es un Sistema de Control de Versiones (VCS). Antes de Git, los programadores guardaban sus archivos como proyecto_final.py, proyecto_final_v2.py, proyecto_final_ahora_si.py. Git elimina esa basura. Mantiene un solo archivo, pero guarda un "historial fotográfico" de cada cambio que haces, permitiéndote viajar al pasado si rompes algo.


DOCUMENTACIÓN OFICIAL
🔗 Doc Oficial: Git Basics / Git Cheat Sheet


🎯 El Propósito
¿Qué problema exacto resuelve Git? El miedo a romper el código que ya funciona. Git te da una red de seguridad. Si el sistema de facturación del cliente funciona el viernes, y el lunes agregas una función nueva que destruye todo, Git te permite restaurar el código exacto del viernes en un segundo.


🔑 Puntos Clave: Los 3 Estados de Git
Para entender Git, debes entender dónde están tus archivos:

Working Directory (Directorio de Trabajo): Es tu carpeta normal en tu laptop. Aquí modificas el código.

Staging Area (Área de Preparación): Es la sala de espera. Aquí mandas los archivos que planeas guardar en la próxima foto. (Comando: git add).

Repository / Commit (Repositorio): Es el álbum de fotos oficial. Cuando tomas la foto, los archivos del Staging Area se guardan permanentemente con un mensaje. (Comando: git commit).


⚠️ Buenas y Malas Prácticas
✅ Buena Práctica: Hacer "Commits Atómicos". Un commit por cada función lógica. (Ej. Un commit para "Agrega botón de login", otro commit separado para "Arregla color del header").

❌ El Error Típico: Escribir mensajes de commit inútiles.

❌ Mala Práctica: Escribir git commit -m "actualización" o git commit -m "cosas". En 6 meses, no sabrás qué "cosas" cambiaste. Usa verbos imperativos: "Agrega validación de correo en login".


💻 Implementación Oficial (Comandos Core)

(Regla del módulo: Abre tu terminal en VS Code y ejecuta esto de verdad. Crea una carpeta llamada agencia_flow_pruebas para hacer los ejercicios).

# 1. Configuración inicial (Solo se hace una vez en la vida en tu laptop)
git config --global user.name "Tu Nombre"
git config --global user.email "tu@correo.com"

# 2. Inicializar un repositorio en una carpeta vacía
git init

# 3. Ver el estado actual de los archivos (El comando más usado)
git status

# 4. Mover archivos al Staging Area (El '.' añade todos los archivos modificados)
git add .

# 5. Tomar la foto (Guardar en el historial permanentemente)
git commit -m "Inicia proyecto con estructura básica"

# 6. Ver el historial de fotos (commits)
git log --oneline nota: para salir del git log se usa el q en el teclado

# compara tu Working Directory con el último commit. Te muestra qué líneas borraste y cuáles agregaste.
git diff 


💻 FASE 2: PRÁCTICA DIARIA

⚙️ Ejercicio 1: Implementación - Lógica Base (Setup Inicial)
# Contexto: Es tu primer día usando Git en esta máquina. Tienes que presentarte 
# ante el sistema y crear tu primer repositorio de pruebas.
#
# Requisitos Ejecutables:
# 1. Crea una carpeta y entra en ella. Inicializa Git (debes ver un mensaje que 
#    dice "Initialized empty Git repository...").
# 2. Configura tu nombre y correo globalmente (si no lo has hecho).
# 3. Escribe en tu respuesta los 3 comandos exactos que ejecutaste en tu terminal.

# --- TUS COMANDOS AQUÍ ---
1- Creao en el escritorio una carpetar proyecto integrador
2- La habro con vs code y luego habro la terminnal
3- git init: entrega de resultado "Initialized empty Git repository" 
4- git config --global user.name "Nmae"
5- git config --global user.email "nhgjh99@gmail.com"



🚀 Ejercicio 2: Implementación - Escenario Real (Primer Release)
# Contexto: Un cliente te pidió un script muy simple que diga "Hola Agencia Flow".
# Creas el archivo, pero tu jefe te exige que todo entregable debe estar en el historial de Git.
#
# Requisitos Ejecutables:
# 1. Dentro de tu carpeta con Git, crea un archivo llamado 'script.py' y ponle adentro un `print("Hola Agencia")`.
# 2. Revisa el estado de Git. Notarás que el archivo está en rojo (Untracked).
# 3. Pásalo al área de preparación (Staging Area).
# 4. Haz un commit con un mensaje descriptivo y profesional.
# 5. Pega aquí el resultado (la salida de la consola) que te dio el comando 'git commit'.

# --- TU OUTPUT DE CONSOLA AQUÍ ---
1- touch script.py
2- print("hola agencia")
3- git status: Untracked files
4- git add .
5- git commit -m "Primer mensaje de entrada del script de agencia flow"
6- git status: working tree clean


🚀 Ejercicio 3: Implementación - Escenario Real (El Auditor de Cambios)
# Contexto: El cliente pide un cambio urgente. Quiere que el script ahora diga 
# "Hola Cliente Premium". Modificas el archivo en VS Code y lo guardas.
# Antes de hacer el commit, quieres asegurarte de qué líneas exactas borraste y cuáles agregaste.
#
# Requisitos Ejecutables:
# 1. Modifica 'script.py' cambiando el texto del print.
# 2. Ejecuta el comando 'git diff' ANTES de hacer 'git add'. Este comando compara tu 
#    Working Directory con el último Commit.
# 3. Pega aquí las 2 o 3 líneas del resultado de 'git diff' donde se ve un signo '-' (rojo) 
#    y un signo '+' (verde) mostrando tu cambio de código. Luego haz add y commit.

# --- TU RESULTADO DE GIT DIFF AQUÍ ---
1- print("Hola cliente premium")
2- git diff
3- resultado: --- a/script.py
+++ b/script.py
@@ -1 +1 @@
-print("Hola Agencia!")
\ No newline at end of file
+print("Hola cliente premium!")
\ No newline at end of file
4- git add .
5- git commit -m "Segundo mensaje de entrada del script de agencia flow"



🐛 Ejercicio 4: Lectura de Código y Debugging (El Commit Fantasma)
# Contexto: Un compañero Junior está frustrado. Modificó el archivo 'database.py' 
# para arreglar un error crítico de conexión. 
# En su terminal, él ejecuta directamente:
# git commit -m "Arregla conexión a base de datos"
#
# Pero la terminal le responde: 
# "nothing to commit, working tree clean" (o "no changes added to commit").
# Sin embargo, si él abre el archivo en VS Code, el nuevo código SÍ está ahí, ya guardado.
#
# Pregunta Debugging: Según la teoría de los "3 Estados de Git", ¿en qué área olvidó meter
# el archivo el Junior y qué comando debió ejecutar ANTES del 'git commit'?

# --- TU EXPLICACIÓN AQUÍ ---   
Como punto numero uno, debido a mi experiencia uno de los problemas es que el archivo database.py despues de haberlo guardado no le dieron el comando necesario, con el git add database. el archivo pasa del working directory al staging area en espera de un commit. al no hacer la terminal tendra el siguiente mensaje working tree clean. al realizar estos dos pasos cambiara el estado del archivo en este caso el script.py, despues de que se alla usado el comando git commit -m "Arregla la base de datos"
git add database.py


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA
❓ Pregunta Teórica 1 (Escenario Staging):
Imagina que trabajaste todo el día y modificaste 5 archivos distintos. 3 archivos son para una nueva función de "Login", y 2 archivos son de pruebas experimentales que aún están rotas. ¿Cómo te ayuda específicamente el "Staging Area" (Área de Preparación) a no guardar los archivos rotos en el historial oficial del proyecto?
El Starring area es una de pre*entreno antes del entranamiento(Git commit -m) o sala de espera, en el podemos ver a todos los pacientes que estan esperando para entrar al quirofano. Nosottros como dueños del repositorio podemos elejir que archivos o perosnas queremos o mejor convenga en ese momentoto a pasar a la sala de espera o al git commit -m "Nueva funcion de witgets".


❓ Pregunta Teórica 2 (Escenario Google Drive):
Un cliente te sugiere: "¿Para qué complicarnos con Git y la terminal? Mejor programemos directo en una carpeta de Google Drive compartida, ahí también se guarda el historial de versiones de los archivos".
¿Por qué Google Drive (o Dropbox) es una pesadilla para un equipo de 3 programadores trabajando en el mismo archivo .py al mismo tiempo, a diferencia de Git?
Uno de los puntos fuertes de git es la cooperacion a la hora de trabajar con codigo, no necesitamos tener 3 o 4 codigos para cada uno. Git tiene un sistema de verificacion y compartir en usuarios por este mismo problema que problema: el de descargar multiples codigos para cada trabajador y despues hacer un solo proyecto, con esta excelente solucion de git se procede asi: se descarga el repositorio de git hub(cada trabajador lo hace) y despues ponen sus datos( name y correo con git config), luego se procede a empezar el proyecto cada uno cumpliendo con su parte y despues de que cada uno termina su parte se hace un git push para subir los cambios al repositorio y asi todos los trabajadores tienen el mismo codigo y no hay problemas de compatibilidad.


🗣️ Prueba de Feynman (Explicación):
Escenario: Tienes que explicarle a un escritor de novelas por qué usas Git para escribir código.
Explícale los tres pasos (Working Directory -> Staging Area -> Commit) usando la analogía de 1) Escribir un borrador en sucio, 2) Elegir qué páginas llevar al fotógrafo, y 3) Revelar el álbum de fotos final.
El sistema de git llego a simplificar la laborar de los programadotres y te lo voy a explicar de una forma simple, imagina que eres un escritor de novelas y estas escribiendo tu libro, primero escribes un borrador en sucio (Working Directory) y luego decides que paginas quieres llevar al fotografo (Staging Area) y finalmente revelas el album de fotos final (Commit). A si es como funciona git, primero escribes tu codigo y luego decides que partes quieres guardar y finalmente lo guardas en el historial de git.