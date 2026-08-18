🐙 DÍA 35: MÓDULO 0 - Ramificación (Branches) y Conflictos (Merge)
📦 Dependencias del Módulo:

Entorno: VS Code + Terminal Linux.
Herramientas: Repositorio de Git del día anterior.

📖 FASE 1: TEORÍA
La regla de oro del desarrollo profesional es: Nunca se programa directamente en la rama main. La rama main es el código de producción, lo que el cliente está usando en este momento. Si necesitas hacer un cambio, creas una Rama (Branch), que es un clon exacto de tu código en ese momento. Trabajas en ese universo paralelo y, cuando terminas y pruebas que no rompe nada, lo fusionas (Merge) con main.


DOCUMENTACIÓN OFICIAL
🔗 Doc Oficial: Git Branching - Basic Branching and Merging


🎯 El Propósito
¿Qué problema resolvemos hoy? Trabajar en múltiples cosas a la vez sin romper producción. Puedes tener una rama para "agregar_login", otra para "cambiar_colores", y trabajar en ambas de forma aislada.
Además, resolveremos Conflictos: ¿Qué pasa si tú cambiaste la línea 10 en tu rama, pero un compañero cambió la misma línea 10 en main? Git entrará en pánico y te pedirá ayuda humana para resolverlo.


🔑 Puntos Clave: Ramas y Fusiones
Branch (Rama): Un puntero paralelo. (Comando: git branch).

Checkout / Switch (Cambiar): El acto de "viajar" a otra rama. Tus archivos en VS Code cambiarán mágicamente frente a tus ojos dependiendo de la rama en la que estés. (Comando moderno: git switch).

Merge (Fusión): Traer los cambios de una rama hacia la rama en la que estás parado actualmente.

Conflictos de Fusión: Ocurren cuando Git no sabe qué versión de una línea conservar. Git inyectará "Marcadores" en tu código (<<<<<<< HEAD, =======, >>>>>>>). Tú debes borrar los marcadores y dejar el código final.


⚠️ Buenas y Malas Prácticas
✅ Buena Práctica: Nombres de ramas descriptivos. Ejemplos: feature/boton-login, bugfix/error-factura.

❌ Mala Práctica: Hacer un git merge sin antes asegurarte de estar posicionado en la rama destino (usualmente main). Terminarás fusionando main hacia tu rama de pruebas por error.


💻 Implementación Oficial (Comandos Core)
# 1. Crear una rama nueva y viajar hacia ella inmediatamente
git switch -c feature/nuevo-mensaje  o git checkout -b nombre-rama

# 2. Ver en qué rama estás actualmente (la que tiene un asterisco *)
git branch

# 3 crear una nueva rama
git branch new_branch

# 4 subir la nueva rama al repositorio
git push -u origin nombre-de-la-rama

# 5. Viajar de regreso a la rama principal (main)
git switch main o nombre de la rama

# 6. Fusionar tu rama nueva hacia main (¡Debes estar parado en main primero!)
git merge feature/nuevo-mensaje

# 7. Borrar la rama paralela porque ya terminaste y la fusionaste
git branch -d feature/nuevo-mensaje

#### Pasos ####
1- git switch -c Api/Create o git branch Api/Create luego git switch Api/Create
2- git branch # ver las ramas que hay
3- trabajar en la rama
4- git push -u origin Api/Create # subir la rama al repo
5- git git switch origin main
6- git merge Api/Create # despues de posicionarse en la rama original hacerlo
7- git push -u origin main
### opcional ####
git branch -d Api/Create # eliminar la rama copia


💻 FASE 2: PRÁCTICA DIARIA
(Instrucción: Abre tu carpeta agencia_flow_pruebas en VS Code para hacer esto. Necesitas ver cómo cambian los archivos físicamente).


⚙️ Ejercicio 1: Implementación - Lógica Base (El Universo Paralelo)
# Contexto: El cliente quiere que agregues una variable de "Versión" al script, pero 
# no quiere que toques el código oficial (main) hasta que lo pruebes bien.
#
# Requisitos Ejecutables:
# 1. Ejecuta el comando para crear y moverte a una nueva rama llamada 'feature/version'.
# 2. Ejecuta 'git branch' para confirmar que estás en ella (el * debe estar en verde junto a tu rama).
# 3. En 'script.py', agrega una nueva línea que diga `version = "1.0"` y haz un commit en esta rama.
# Escribe aquí los comandos exactos que usaste.

# --- TUS COMANDOS AQUÍ ---
1- git switch -c feature/version
2- git branch  ## si lo esta
3+ git add .
4- git commit -m "Nueva rama feature/version"
5- git push -u origin feature/version
6- print("Version = 1.0") # agregue el codigo
7- git status # para verificar
8- git add .
9- git commit -m "Version = 1.0"
10- git push = Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:eric22gh/agencia_flow_repo.git
   83d1ade..d14f2bf  feature/version -> feature/version


🚀 Ejercicio 2: Implementación - Escenario Real (El Viaje en el Tiempo y la Fusión)
# Contexto: Tu variable de versión funcionó perfecto. Ahora necesitas integrarla al 
# código principal de la empresa (fusionar).
#
# Requisitos Ejecutables:
# 1. Cámbiate a la rama 'main'. (Nota en VS Code cómo mágicamente desaparece la línea 'version = 1.0').
# 2. Ejecuta el comando para fusionar 'feature/version' HASTA tu rama actual 'main'.
# 3. (Notarás en VS Code que la línea volvió a aparecer, ahora en main).
# 4. Elimina la rama 'feature/version' para mantener el repositorio limpio.
# Escribe aquí los comandos que usaste.

# --- TUS COMANDOS AQUÍ ---
1- git switch main
2- git merge feature/version : Fast-forward
 script.py | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)
3- git branch -d feature/version
4- git push origin main


🚀 Ejercicio 3: Implementación - Escenario Real (Provocando un Conflicto de Fusión)
# Contexto: Vamos a simular un desastre controlado. Vas a editar la MISMA línea en dos ramas distintas.
#
# Requisitos Ejecutables:
# 1. Estando en 'main', edita 'script.py' para que diga `version = "1.1"` y haz un commit.
# 2. Crea una rama nueva llamada 'hotfix/version-urgente' y muévete a ella.
# 3. Borra el "1.1" y pon `version = "2.0"`. Haz un commit en esta nueva rama.
# 4. Regresa a 'main' e intenta fusionar la rama 'hotfix/version-urgente'. 
# 5. ¡Git entrará en conflicto! Pega aquí las últimas 2 líneas que te arrojó la terminal 
#    indicando el "Merge conflict".

# --- TU OUTPUT DE CONSOLA (EL ERROR) AQUÍ ---
1- print("Hola cliente premium!. adios")
print("Version = 1.1")
2- git add .
3- git commit -m "Version 1.1"
4- git push
4- git switch -c hotfix/version-urgente
7- git push -u  origin hotfix/version-urgente
5- print("Hola cliente premium!. adios")
print("Version = 2.0")
6- git add .
7- git commit -m "Version 2.0"
9- git push
8- git switch main
9- git merge hotfix/version-urgente
10- Fast-forward
 script.py | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
 Nota hice los pasos, pero al parecer no me genero ningun conflicto o no se si lo hice mal.

Nota: haciendo la implementacion del ejercio 3 al hacer el commit de la version 1.0 no hice el git push, despues cambie ala rama hotfix/version-urgente realice el commit de la version 2.0 pero no hice el git push, luego regrese con git switch main y realice el git merge hotfix/version-urgente y no ocurrio ningun comflicto, me di cuenta que tengo que hacer el git push para hacer el conflicto.

### implementacion correcta ###
1- git checkout -b ramaA
2- echo 'print("Hola desde A")' > script.py
3- git commit -am "Cambio en rama A"
4- git checkout main
5- git checkout -b ramaB
6- echo 'print("Hola desde B")' > script.py
7- git commit -am "Cambio en rama B"
8- git checkout main
9- git merge ramaA
10- git merge ramaB
<<<<<<< HEAD
print("Hola desde A")
=======
print("Hola desde B")
>>>>>>> ramaB


🐛 Ejercicio 4: Lectura de Código y Debugging (Resolviendo el Desastre)
# Contexto: En el Ejercicio 3, Git te detuvo. Si abres 'script.py' en VS Code en este 
# momento, verás algo horrible parecido a esto:
#
# <<<<<<< HEAD
# version = "1.1"
# =======
# version = "2.0"
# >>>>>>> hotfix/version-urgente
#
# El desarrollador Junior ve esto y te dice: "¡Git me llenó el código de flechas y basura, 
# se arruinó el archivo!".
#
# Pregunta Debugging: Explícale al Junior qué significan los bloques `HEAD` y `hotfix...`. 
# Luego, explica cuáles son los 3 pasos exactos (usando VS Code y la terminal) para 
# deshacerse de ese error y terminar de fusionar el código correctamente.

# --- TU EXPLICACIÓN Y PASOS DE RESOLUCIÓN AQUÍ ---

El error en vs code  `HEAD` y `hotfix...`. ocurre cuando editamos 2 ramas en la misma linea de codigo y a la hora de hacer la fusion de ramas con git merge, git entra en conflicto porque no sabe cual rama escoger, para resolver este conflicto sigue estos pequeños pasos:
se veran las lineas de codigo que estan en cnflicto de esta manera: <<<<<<< HEAD
print("Hola desde A")
=======
print("Hola desde B")
>>>>>>> ramaB
decide que linea de codigo vas a utilizar ya sea print("Hola desde A") o print("Hola desde B"), borra la linea de codigo que no vas a usar y los signos de == y >>> y luego presiona el boton de resulto. finalmente haz un git add . y luego commit y por ultimo git push.


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA
❓ Pregunta Teórica 1:
¿Por qué en los equipos de desarrollo profesionales existe la regla estricta de que "Nadie hace commits directamente en la rama main"? ¿Qué riesgo mitigamos al obligar a todos a crear ramas para sus tareas?
Primeramente hacer commits a la rama main es una mala practica y un gravisimo error ya que podriamos traer abajo o dejar a personas sin el servicio de la app o plataforma por mucho tiempo, lo correcto es crear una rama de prueba antes de lanzar la implementacion o app a produccion(rama main), en esa rama test se pueden hacer todas las correciones sin ningun riesgo y finalmente aprovado y superado el test, se pueden fusionar las ramas con un git merge y luego con un git push lanzarlo a producion.


❓ Pregunta Teórica 2:
Cuando tienes un conflicto de fusión (Merge Conflict), ¿es porque la herramienta de Git falló, o es un mecanismo de seguridad intencional? Justifica tu respuesta.
En resumen es un mecanismo de seguridad intencional, ocurre cuando se edita una linea de codigo en las 2 ramas y a la hora de hacer el git merge, git no sabe cual linea de codigo elegir o quedarse con el, entonces lo que corresponde como desarrollador es primeramente trartar de evitar esto errores y luego escoger manualmente por git con cual linea de codigo se va a quedar.



🗣️ Prueba de Feynman (Explicación):
Escenario: Un cliente no entiende cómo puedes trabajar en la nueva página de "Pagos" durante dos semanas y, al mismo tiempo, arreglar un error urgente en la página "Inicio" el mismo día, sin mezclar ambos trabajos.
Explícale el concepto de Ramificación (Branches) usando la analogía de jugar un videojuego, guardar la partida en el "Slot 1" antes de un jefe difícil, y luego abrir el "Slot 2" para ir a explorar otro mapa.
El sistema de git hace la vida de un dev mas facil al poder trabajar con 2 o mas implementaciones al mismo tiempo mediante ramas, de esta manera se crea una o las ramas que se necesite para la implementacion, luego se cambia hacia ellas y se trabaja en ellas y no en la rama del proyecto(main) es como estar jungando una partida del bloodborne y estamos en el jefe final, entonces guardamos la partido en una slot para nor perder el avance y asu vez podemos jugar otra partida o otro juego y guardar el avaance en la otra slot y asi nada se pierde....en palabras sencillas las rammas son como slots de memoria.