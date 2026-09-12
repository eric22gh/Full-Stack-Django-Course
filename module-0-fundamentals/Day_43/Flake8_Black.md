🐍 DÍA 43: MÓDULO 0 - Productividad y Código Limpio (Flake8 y Black)
📦 Dependencias del Módulo:

Entorno: VS Code + Terminal.
Herramientas: Python 3 instalado en tu máquina local.

📖 FASE 1: TEORÍA
Python tiene un manual de estilo oficial llamado PEP 8. Te dice cuántos espacios dejar, cómo nombrar variables y cómo organizar tu código para que cualquier programador del mundo lo entienda al instante.

Pero revisar todo eso a mano es perder el tiempo. Los desarrolladores Senior usan dos herramientas automáticas:

Linter (El Policía de Sintaxis): Herramientas como flake8. Leen tu código y te gritan si rompiste alguna regla de estilo o si declaraste una variable que nunca usaste.

Formatter (El Peluquero Automático): Herramientas como black. No te gritan; simplemente agarran tu código feo y lo reescriben mágicamente en milisegundos dejándolo hermoso y 100% compatible con PEP 8.


DOCUMENTACIÓN OFICIAL
🔗 Doc Oficial: Flake8 Rules / Black Formatter


🎯 El Propósito
Estandarización extrema y ahorro de tiempo en las revisiones de código (Code Reviews). El equipo nunca debe discutir sobre "dónde poner el salto de línea", la herramienta black toma esas decisiones por nosotros.


🔑 Puntos Clave:
Aislamiento (El VENV): Estas herramientas de limpieza son librerías de Python. Por lo tanto, SIEMPRE se instalan dentro de un Entorno Virtual (venv), jamás en tu sistema global.

Black es Inflexible: El lema de Black es "The Uncompromising Code Formatter". No te deja configurarlo a tu gusto personal. Lo hace a su manera (que es el estándar de la industria), punto. Eso elimina debates en el equipo.

Integración Continua (CI/CD): Más adelante (Módulo 3.6), configuraremos GitHub para que, si un compañero sube código que no pasa la revisión de flake8, GitHub rechace el código automáticamente.


⚠️ Buenas y Malas Prácticas
✅ Buena Práctica: Configurar VS Code para que ejecute black cada vez que presionas Ctrl + S (Guardar). Tu código se limpiará solo mientras trabajas.

❌ Mala Práctica: Ignorar los errores de flake8. Si te marca que "importaste la librería X pero no la estás usando", bórrala. Un import sin uso consume RAM y ralentiza el inicio de la app.


💻 Implementación Oficial (Comandos Core)
# 1. Crear entorno virtual y activarlo
python -m venv venv
# (Windows) venv\Scripts\activate
# (Linux/Mac) source venv/bin/activate

# 2. Instalar el policía y el peluquero
pip install flake8 black

# 3. Correr el policía para que audite tu código (Te arrojará una lista de errores)
flake8 mi_script.py

# 4. Correr el peluquero para que arregle el código mágicamente
black mi_script.py


💻 FASE 2: PRÁCTICA DIARIA
(Regla E2E: Crea una carpeta llamada codigo_limpio, ábrela en VS Code y realiza estos flujos completos en tu terminal local).



⚙️ Ejercicio 1: Implementación E2E - Lógica Base (Setup Profesional)
# Contexto: Vamos a preparar el entorno de trabajo como se hace en la vida real
# antes de tirar la primera línea de código.
#
# Requisitos Ejecutables (Flujo Completo):
# 1. Abre la terminal en la carpeta 'codigo_limpio' y crea un entorno virtual llamado `venv`.
# 2. Activa el entorno virtual (asegúrate de que aparezca '(venv)' en tu terminal).
# 3. Instala las dos librerías: `pip install flake8 black`.
# 4. "Congela" tus dependencias guardándolas en un archivo: `pip freeze > requirements.txt`
# 5. Crea un archivo `.gitignore` y añade `venv/` adentro.
#
# Pega aquí el contenido de tu archivo `requirements.txt` (deberías ver black, flake8 y
# algunas librerías extras que ellas instalan por detrás).

# --- TU OUTPUT AQUÍ ---
1- python3 -m venv venv
2- source venv/Scripts/activate
3- pip install black flake8
4- pip freeze > requirements.txt
5- echo "venv/" > .gitignore
6-  pip list
Package         Version
--------------- -------
asgiref         3.12.1
black           26.5.1
click           8.5.0
colorama        0.4.6
Django          6.1.1
flake8          7.3.0
iniconfig       2.3.0
mccabe          0.7.0
mypy_extensions 1.1.0
packaging       26.3
pathspec        1.1.1
pip             26.2.1
platformdirs    4.11.8
pluggy          1.6.0
pycodestyle     2.14.0
pyflakes        3.4.0
Pygments        2.21.0
pytest          9.1.1
pytokens        0.4.1
sqlparse        0.6.0
tzdata          2026.3
las anteriores son las dependencias que se instalaron automáticamente al instalar black y flake8.



🚀 Ejercicio 2: Implementación E2E - Escenario Real (El Grito del Policía)
# Contexto: Un Junior escribió un código que funciona, pero que rompe todas las
# reglas visuales de PEP 8. Vamos a usar el Linter para auditarlo.
#
# Requisitos Ejecutables (Flujo Completo):
# 1. Con tu `venv` activado, crea un archivo llamado `feo.py`.
# 2. Copia y pega exactamente este código HORRIBLE (con todo y sus espacios locos):

import os, sys
def sumar_numeros ( a,b ):
    return a+b
print(   sumar_numeros(2, 5)   )

# 3. Guarda el archivo. Ejecuta el policía: `flake8 feo.py`
# 4. La terminal te arrojará varios errores con códigos como E401, E211, E201, etc.
# Pega aquí exactamente los errores que te arrojó la terminal.

# --- TU OUTPUT DE FLAKE8 AQUÍ ---
1- python3 -m venv venv
2- touch feo.py
4- copie y pegue el código HORRIBLE
nota el archivo feo.py no lo cree porque ya tenioa uno creado previamente llamado practice.py
5- errores:
practice.py:1:1: F401 'os' imported but unused
practice.py:1:1: F401 'sys' imported but unused
practice.py:1:10: E401 multiple imports on one line
practice.py:2:1: E302 expected 2 blank lines, found 0
practice.py:2:18: E211 whitespace before '('
practice.py:2:20: E201 whitespace after '('
practice.py:2:22: E231 missing whitespace after ','
practice.py:2:24: E202 whitespace before ')'
practice.py:4:1: E305 expected 2 blank lines after class or function definition, found 0
practice.py:4:7: E201 whitespace after '('
practice.py:4:31: E202 whitespace before ')'
practice.py:4:33: W292 no newline at end of file


🚀 Ejercicio 3: Implementación E2E - Escenario Real (El Arreglo Automático)
# Contexto: En lugar de arreglar a mano todos los errores de espacios que `flake8`
# nos marcó en el Ejercicio 2, usaremos la magia de `black`.
#
# Requisitos Ejecutables (Flujo Completo):
# 1. En la misma terminal (con el venv activo), ejecuta: `black feo.py`
# 2. La terminal te dirá "reformatted feo.py".
# 3. Abre `feo.py` en VS Code y sorpréndete viendo cómo el código se acomodó solo.
# 4. Vuelve a ejecutar a la policía: `flake8 feo.py`
#
# Pega aquí cómo quedó el código dentro de `feo.py` después de que Black lo arregló.
# (Nota: Flake8 igual se quejará con un error "F401 'os' imported but unused", porque
# Black arregla el formato, ¡pero no borra tu lógica ni tus importaciones inútiles!).

# --- TU CÓDIGO REFORMATEADO AQUÍ ---
1- source venv/Scripts/activate
2- black practice.py
3-  black practice.py
reformatted practice.py
All done! ✨ 🍰 ✨
1 file reformatted.
4- flake8 practice.py
5- asi quedo el código:
import os, sys
def sumar_numeros(a, b):
    return a + b
print(sumar_numeros(2, 5))


🐛 Ejercicio 4: Lectura de Código y Debugging (El CI/CD Estricto)
# Contexto: En el módulo de GitHub Actions (CI/CD) que veremos en el futuro,
# escribiremos un script para que cada vez que alguien haga un `git push`, un
# servidor de GitHub ejecute `flake8 .` en tu código. Si `flake8` encuentra UN SOLO error,
# el código es RECHAZADO y no puede fusionarse con `main`.
#
# Un desarrollador Junior te dice: "¡Eso es muy extremo! Mi código funciona perfecto
# y calcula bien las facturas, ¿por qué el sistema me rechaza mi código solo porque
# dejé unos espacios extra o una variable que no usé? Deberíamos quitar esa regla".
#
# Pregunta Debugging: Como Arquitecto del proyecto, explícale al Junior por qué
# mantenemos esa regla estricta de Flake8/Black en el pipeline automático y cuál es
# el "costo oculto" para el equipo si permitimos código desordenado (aunque funcione).

# --- TU EXPLICACIÓN AQUÍ ---
Primeramente una de las reghlas en las que se basa nuestra empresa es el codigo limpio y claro por eso tomamos medidas estrictas las cuales dse llaman flake8 que automaticamente encuentra posibles errores o malas practicas como saltos de linea o espacios no necesarios en el codigo, nosotros al implementar esto en git hub actions es una de las razones por las que tu codigo no pasa el test, pero pueesde usar la solucion llamada black que formatea codigo y elimina espacios haciendo tu codigo mas limpio y ligero.



🧠 FASE 3: CONSOLIDACIÓN TEÓRICA
❓ Pregunta Teórica 1:
Ambas herramientas analizan tu código, pero tienen propósitos distintos. ¿Por qué en un flujo de trabajo profesional ejecutarías PRIMERO black (Formatter) y SEGUNDO flake8 (Linter), y no al revés?
El proposito de ambos es ayudar atener un codigo mas limpio y legible, a la hora de realizar un proyecto personal son de gran ayuda ya que ayudan ala buena presentacion del proyecto, pero ambos se enfocan en distintas cosas, el proposito de flack8 es encontrar y enseñarte los errores y malas practicas en tu codigo un ejemplo fue que vimos en los ejercicios anteriores saltos de linea y espacios innecesarios. POr otra parte esta Black, supongamos que con flake8 encontramos 200 espacios inecesarios, te imaginas ir 1 x 1 corigiendolos? eso no es escalable, es ahi donde entra black con un comando y pocos clicks elimina y corrige estos errores encontrados por flake8.

Nota en el mundo dev se usa primero black y luego flake8 por black va a eliminar el 90% de la basura de una vez y ya luego se usa flake8 para los errores de logica.


❓ Pregunta Teórica 2:
Si vas a desplegar un contenedor Docker para poner tu aplicación web en producción en AWS, ¿deberías agregar flake8 y black en tu archivo requirements.txt de producción? Justifica tu respuesta entendiendo la diferencia entre "Dependencias de Desarrollo" y "Dependencias de Producción".
Considero que flake8 y black son dependencias de desarrollo o de test, solo se usan en local y antes de que la app salga a produccion tiene que pasa  el test y tener un codigo limpio y legible antes de ir a produccion y no despues. Por eso tenerlos en produccion no tendria sentido.


🗣️ Prueba de Feynman (Explicación):
Escenario: Tienes que explicarle a un compañero qué hacen exactamente Flake8 y Black en tu código Python.
Explícaselo usando la analogía de Escribir un libro y pasarlo por dos personas distintas: Un Corrector Ortográfico/Tipográfico (Black) y un Editor de Contenido (Flake8).
Flake8 es como un editor de contenido que revisa tu libro y te dice: "Oye, aquí tienes una frase confusa, esta palabra está mal escrita, y este párrafo no tiene sentido". Te da una lista de errores y sugerencias para mejorar la claridad y coherencia de tu texto.
Black, por otro lado, es como un corrector ortográfico y tipográfico que toma tu libro y automáticamente corrige errores de ortografía, gramática y formato. No te da sugerencias; simplemente hace que tu texto sea más legible y estéticamente agradable.