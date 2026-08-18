🐙 DÍA 36: MÓDULO 0 - Flujos Profesionales, .gitignore y Desastres (revert / reset)
📦 Dependencias del Módulo:

Entorno: VS Code + Terminal Linux.
Herramientas: Tu repositorio local agencia_flow_pruebas.

📖 FASE 1: TEORÍA
Hoy cerramos Git con dos salvavidas absolutos.
Primero, El Arte de Ignorar: Cuando programas, tu computadora genera archivos basura (__pycache__), o peor aún, archivos con contraseñas reales (.env). Si subes un archivo .env a GitHub, un bot lo leerá en 2 segundos y te hackeará AWS. Git tiene una "Lista Negra" para evitar esto.
Segundo, El Arte de Arrepentirse: Si hiciste un commit y lo arruinaste todo, hay dos formas de volver atrás: crear un "antídoto" (revert) o borrar la historia como si nunca hubiera pasado (reset).


DOCUMENTACIÓN OFICIAL
🔗 Doc Oficial: Gitignore / Undoing Things (Revert vs Reset)


🎯 El Propósito
¿Qué problema resolvemos hoy? La fuga de datos y la corrección de errores en producción. Evitarás que secretos corporativos lleguen a internet y sabrás cómo actuar si descubres que tu último commit rompió la pasarela de pagos.

🔑 Puntos Clave: .gitignore, Revert y Reset
El archivo .gitignore: Es un archivo de texto plano oculto. Todo nombre de archivo o carpeta que escribas ahí dentro será invisible para Git. ¡Ni siquiera te dejará hacerle add!

git revert <ID_DEL_COMMIT> (El Método Seguro): No borra el pasado. En su lugar, crea un commit nuevo que aplica exactamente los cambios inversos. Si agregaste la palabra "Hola", el revert creará un commit que borra la palabra "Hola". Es seguro para usar en main porque no altera la historia de tus compañeros.

git reset --hard <ID_DEL_COMMIT> (La Bomba Nuclear): Corta el historial con un hacha. Borra todos los commits posteriores y destruye los cambios en tu disco duro para dejarlo exactamente como estaba en esa foto. JAMÁS se usa en main si ya hiciste Push, porque causarás un caos en el GitHub de tus compañeros.

⚠️ Buenas y Malas Prácticas
✅ Buena Práctica: Crear el archivo .gitignore en el primer minuto de vida de tu proyecto, antes de hacer tu primer commit.

❌ Mala Práctica: Hacer un git reset --hard en la rama main y luego forzar el push (git push -f) a GitHub. Acabas de borrar el trabajo de la empresa.



💻 Implementación Oficial (Comandos Core)
# 1. Crear un archivo .gitignore y agregarle cosas
echo ".env" > .gitignore
echo "__pycache__/" >> .gitignore

# 2. Ver el ID de tus commits (necesitas los primeros 7 caracteres, ej. a1b2c3d)
git log --oneline

# 3. Deshacer un commit creando un "anti-commit" (Seguro)
git revert a1b2c3d

# 4. Viajar en el tiempo y DESTRUIR el futuro (Peligroso)
git reset --hard a1b2c3d

# 5. Sacar un archivo del Staging Area si le hiciste 'git add' por error
git restore --staged archivo.py

# 6. rm elimina los archivos del indice --cached → significa que lo quita del repo, pero lo deja en tu disco local (no lo borra físicamente) .env → el archivo que quieres dejar de rastrear.
git rm --cached .env

# 7- te mueve hacia el commit que necesites
git checkout <commit>



💻 FASE 2: PRÁCTICA DIARIA
(Instrucción: Usa tu misma carpeta de pruebas en VS Code).


⚙️ Ejercicio 1: Implementación - Lógica Base (El Escudo .gitignore)
# Contexto: Vas a crear el archivo que guarda las contraseñas reales de AWS para la agencia, 
# pero necesitas asegurarte de que NUNCA se suba a GitHub.
#
# Requisitos Ejecutables:
# 1. Crea un archivo llamado '.env' y ponle adentro `AWS_SECRET="super_secreto_123"`.
# 2. Ejecuta `git status`. Verás que Git te sugiere agregarlo. (¡NO LO HAGAS!).
# 3. Crea un archivo llamado `.gitignore` (con el punto al inicio) y escribe adentro `.env`.
# 4. Ejecuta `git status` otra vez.
# 5. Notarás que el archivo '.env' desapareció de la vista de Git, pero '.gitignore' sí aparece.
# 6. Haz 'add' y 'commit' del archivo .gitignore.
# Pega aquí el output final de tu último `git status` que comprueba que el '.env' ya no es detectado.

# --- TU OUTPUT DE CONSOLA AQUÍ ---
1- mkdir .env
2- cd .env
3- touch secrets.py
4- echo 'AWS_SECRET="super_secreto_123"' > secrets.py 
5- git status
6- touch .gitignore
7- echo ".env" > .gitignore
8- git status
9- como resultado solo me sale el gitignore:  (use "git add <file>..." to include in what will be committed)
        .gitignore
10- git add .
11- git commit -m "creacion del gitignore"
12- git push: Writing objects: 100% (3/3), 282 bytes | 141.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:eric22gh/agencia_flow_repo.git
   f6ceac2..d857b27  main -> main


🚀 Ejercicio 2: Implementación - Escenario Real (El Antídoto - Revert)
# Contexto: Modificaste 'script.py' con una nueva función que suma 2+2, pero te equivocaste 
# y pusiste que sume 2+3. Le hiciste commit y ya lo subiste. ¡Producción está fallando!
#
# Requisitos Ejecutables:
# 1. En 'script.py', agrega `print(2+3)` al final. Haz un commit con el mensaje "Agrega calculadora rota".
# 2. Ejecuta `git log --oneline` y copia el ID de ese último commit malo.
# 3. Ejecuta `git revert <ID_DEL_COMMIT>` (Se abrirá un editor en la terminal para confirmar 
#    el mensaje, en Nano guarda con Ctrl+O y sal con Ctrl+X. En Vim, teclea :wq).
# 4. Revisa 'script.py' en VS Code. ¡El error desapareció!
# Escribe aquí el comando exacto de revert que usaste y el nuevo ID del commit que se 
# generó (lo puedes ver con git log --oneline de nuevo).

# --- TUS COMANDOS Y RESULTADOS AQUÍ ---
1- print(2+3)
2- git add .
3- git commit -m "Agrega calculadora rota"
4- git push 
5- git log --oneline: 615b98c
6- git revert 615b98c
7-  git revert 615b98c
[main 41405e6] Revert "calculadora rota"
 1 file changed, 1 insertion(+), 2 deletions(-)
 8- Nota tienes razon volvio al ultimo commit antes del print(2+3) y no aparece nada con el git status, recordar que el git revert nunca se hace en la rama main(produccion), para eso esta la rama de testing.
 nota al hacer el git revert el si queda en el historial: git log --oneline



🚀 Ejercicio 3: Implementación - Escenario Real (La Bomba Nuclear - Reset Hard)
# Contexto: Estás haciendo pruebas en tu laptop. Creas un archivo 'basura.txt' y le haces commit. 
# Creas otro archivo 'test.py' y le haces commit. 
# Te das cuenta de que todo este trabajo no sirve y quieres borrarlo de la historia por completo, 
# dejándolo como estaba ayer.
#
# Requisitos Ejecutables:
# 1. Haz un par de commits rápidos con cambios basura.
# 2. Haz `git log --oneline` y busca el ID del commit "bueno" al que quieres regresar 
#    (probablemente el commit del revert del ejercicio 2).
# 3. Ejecuta `git reset --hard <ID_DEL_COMMIT_BUENO>`.
# 4. Observa tu explorador de archivos en VS Code. ¡Los archivos basura fueron vaporizados!
# Escribe aquí el comando exacto que usaste.

# --- TU COMANDO AQUÍ ---
1- touch basura.txt
2- touch test.py
3- git add .
4- git commit -m "Archivos de prueba"
5- git log --oneline : 41405e6
6- git reset --hard 41405e6
HEAD is now at 41405e6 Revert "calculadora rota"
8- git push
9- Nota final: En efecto se borraron los 2 archivos basura de vs code y al hacer git log --oneline no se muestra el commit o ID de "Archivos de prueba"


🐛 Ejercicio 4: Lectura de Código y Debugging (El Error Más Común del .gitignore)
# Contexto: Un compañero de trabajo de la Agencia Flow creó un archivo `.env` ayer y, por 
# accidente, ejecutó `git add .` y `git commit`. 
# Hoy se dio cuenta de su error y rápidamente creó el archivo `.gitignore` y metió la 
# palabra `.env` adentro.
# 
# Sin embargo, me llama asustado: "¡Eric, puse el archivo en el .gitignore, pero cuando
# edito el `.env`, Git lo sigue viendo y lo marca como 'modified'!".
#
# Pregunta Debugging: Explícale al compañero por qué el `.gitignore` NO funciona 
# mágicamente en archivos que ya fueron comiteados en el pasado. 
# Busca en Google o en la doc oficial cuál es el comando exacto (empieza con `git rm...`) 
# que debe ejecutar para "destrackear" (sacar del sistema de Git) ese archivo sin borrarlo 
# físicamente de su computadora.

# --- TU EXPLICACIÓN Y EL COMANDO SALVAVIDAS AQUÍ ---
El comando que se utiliza en esta situacion es el git rm --cached .env: el rm borra archivos del indice local,  el --cached lo quita del repo, seguido del archivo que quieres eliminar, todo esto se realiza ya que el archivo env ya se subio al repo antes del gitignore asi que no va a funcionar, por eso es que el gitignore es una de las primeras cosas que se hace cuando se inicia un repositorio.



🧠 FASE 3: CONSOLIDACIÓN TEÓRICA
❓ Pregunta Teórica 1:
Estás trabajando en la rama oficial main. El cliente te pide deshacer la función que subiste ayer. Tienes dos opciones: git revert o git reset --hard.
Sabiendo que 5 programadores más de tu equipo ya hicieron git pull de esa rama esta mañana, ¿por qué hacer un git reset --hard arruinará el día de tus 5 compañeros, y por qué git revert es la solución pacífica?
Siguiendo las buenas practicas de git, antes de iniciar con cualquier cosa, crearia otra rama y despues con git log conseguiria el id que necesito para volver al codigo antes de hacer la funcion y finalmente usaria git revert porque asi queda un registro de lo que se hizo, si yo realizo un git reset --hard "ID" los programadores verian algo extraño y trendrian un conflicto a la hora de hacer merge, porque estan trabajando sobre una funcion que ya no esta y no sabrian el porque. de mi parte les ordenaria que dejen de trabajar en los cambios que bajaron con git pull y cuando yo termine de hacer el merge de la funcion anterior a la rama main y finalmente realizar el git push, se les comunicaria que ya pueden hacer el git pull para traer los cambios nuevos a su repo.


❓ Pregunta Teórica 2:
En tu próximo módulo usaremos Python, y Python crea una carpeta llamada __pycache__ automáticamente cada vez que corres un código. ¿Cuál es el riesgo o inconveniente de NO incluir __pycache__/ en tu archivo .gitignore desde el día 1?
La carpeta __pycache__/ que se genera en python a la hora de hacer run en python no tiene contraseñas o datos sencibles, se usa para que los modulos en python funcionen mas rapido, se le puede considerar un archivo basura y ya que estamos hablando de basura lo correcto es agregarlo al .gitignore ya que no queremos basura en nuestro repositorio.


🗣️ Prueba de Feynman (Explicación):
Escenario: Tienes que explicarle al nuevo Junior por qué no debe subir el archivo .env (que contiene llaves de AWS o base de datos) a GitHub. Explícaselo usando la analogía.
Subir el la carpeta .env a git con un git push es una mala practica en el mundo dev, esta carppeta contiene contraseñas y otras cosas sencibles, por eso es que una de las primeras cosas que se hacen al crear un repositorio es crear el archivo gitignore para evitar estos inconvenientes y no resivir ningun hackeo a nuestra app o implemnetancion. Una forma facil de entender este tema es tu como ser u
humano las llavez de tu habitacion es algo de suma importancia son las llavez de tu enterno y los mas seguro es que se queden contigo(en local) ya que si las dejas en la puerta(la nube de git) un hacker podria entrar a tu casa y robarte.
