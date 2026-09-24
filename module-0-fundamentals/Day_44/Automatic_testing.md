🐍 DÍA 44: MÓDULO 0 - Testing Automático (La Red de Seguridad con Pytest)
📦 Dependencias del Módulo:

Entorno: VS Code + Terminal.
Herramientas: Python 3 + Entorno Virtual (venv).


📖 FASE 1: TEORÍA
Imagina que eres un mecánico de aviones. Arreglas una turbina, ¿y luego qué? ¿Subes pasajeros y rezas para que vuele? No. Haces pruebas en tierra, simulas estrés y mides resultados.

En software, eso se llama Testing Automatizado. En lugar de ejecutar tu script y hacer print() para ver si funciona, escribes otro código cuyo único trabajo es poner a prueba tu código principal y verificar (Assert) que el resultado sea el esperado.
El estándar absoluto de la industria en Python es una librería llamada pytest.


DOCUMENTACIÓN OFICIAL
🔗 Doc Oficial: Pytest Documentation


🎯 El Propósito
Paz mental (Sleep-at-night factor). Evitar regresiones (que un código nuevo rompa un código viejo que ya funcionaba). Te permite refactorizar código sin miedo.


🔑 Puntos Clave: Reglas de Pytest
El Nombre Mágico: Para que Pytest encuentre tus pruebas automáticamente, tus archivos deben empezar con test_ (ej. test_calculadora.py) o terminar con _test.py.

Las Funciones Mágicas: Dentro del archivo, las funciones que hacen las pruebas también deben llamarse test_algo() (ej. def test_suma():).

La Palabra assert: Es la clave de todo. Significa "Yo afirmo que esto es verdad". (ej. assert 2 + 2 == 4). Si la afirmación es falsa, la prueba estalla en rojo (Fails). Si es verdadera, pasa en verde (Passes).

TDD (Test-Driven Development): Una metodología avanzada donde primero escribes la prueba (que obviamente fallará porque el código no existe), y luego escribes el código para que la prueba pase a verde.


⚠️ Buenas y Malas Prácticas
✅ Buena Práctica: Una aserción (assert) por cada cosa específica que quieras probar. Nombra tus tests de forma muy descriptiva (ej. def test_usuario_menor_de_edad_no_puede_comprar():).

❌ Mala Práctica: Usar bases de datos de producción reales para correr tests. Las pruebas siempre generan datos basura, por lo que deben usar bases de datos de prueba (mocks/fixtures).


💻 Implementación Oficial (Comandos Core)
# 1. Instalar pytest en tu entorno virtual
pip install pytest

# 2. Correr todos los tests de la carpeta actual
pytest

# 3. Correr tests con más detalle (Verbose - muestra qué test pasó o falló específicamente)
pytest -v



💻 FASE 2: PRÁCTICA DIARIA
(Regla E2E: Crea una carpeta testing_flow, ábrela en VS Code y realiza estos flujos completos en tu terminal).

⚙️ Ejercicio 1: Implementación E2E - Lógica Base (Tu Primer Semáforo en Verde)
# Contexto: Vamos a crear un módulo de facturación básico y asegurarnos de que
# matemáticamente funcione.
#
# Requisitos Ejecutables (Flujo Completo):
# 1. En tu carpeta, crea un `venv`, actívalo e instala `pytest`.
# 2. Crea un archivo llamado `facturas.py` con este código:
#    def calcular_total(subtotal, impuesto):
#        return subtotal + (subtotal * impuesto)
# 3. Crea OTRA archivo llamado `test_facturas.py` con este código:
#    from facturas import calcular_total
#
#    def test_calcular_total_con_impuesto():
#        resultado = calcular_total(100, 0.13)
#        assert resultado == 113.0
# 4. Ejecuta el comando en tu terminal: `pytest -v`
# 5. La terminal te arrojará un mensaje en VERDE indicando que el test pasó ("PASSED").
# Pega aquí el output final que te dio `pytest -v`.

# --- TU OUTPUT AQUÍ ---
1- mkdir testing_flow
2- cd testing_flow
3- python -m venv te-venv
4- source te-venv/Scripts/activate
5- pip install pytest
6- touch facturas.py test_facturas.py: ya pegue los 2 codigos que me pediste
7- pytest -v
============================================= test session starts =============================================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0 -- C:\Users\EAedw\OneDrive\Desktop\testing_flow\te-venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\EAedw\OneDrive\Desktop\testing_flow
collected 1 item

test_facturas.py::test_calculadora_total_impuesto PASSED                                                 [100%]

============================================== 1 passed in 0.04s ==============================================
Nota: basicamente hay que crear un archivo extra para el test, y importar como modulo el codigo en el que se esta trabajando, despues nombrar el nuevo archivo con nombres de test y un descriptivo al igual que la funcion dentro de ese codigo y finalment llamar a la funcion imporatada, guardar el resultado en una variable y luego con el assert comparar ese resultado con el resultado esperado, si es igual el test pasa, si no es igual el test falla. Lo comprobamos con el pytest -v y nos dira si paso o no.


🚀 Ejercicio 2: Implementación E2E - Escenario Real (Cazando el Bug - Red to Green)
# Contexto: El cliente pidió que la factura aplique un descuento ANTES de cobrar
# el impuesto. Hiciste el cambio, pero quieres probarlo automáticamente.
#
# Requisitos Ejecutables (Flujo Completo):
# 1. En `facturas.py`, agrega esta nueva función INCOMPLETA/MALA a propósito:
#    def aplicar_descuento(precio, descuento):
#        return precio - 5  # <-- Esto está mal, resta 5 fijos en lugar de aplicar el porcentaje
# 2. En `test_facturas.py`, agrega el test que verifica la realidad:
#    def test_aplicar_descuento_porcentaje():
#        resultado = aplicar_descuento(100, 0.20)
#        assert resultado == 80.0  # El 20% de 100 es 20. 100 - 20 = 80.
# 3. Ejecuta `pytest -v`. ¡Verás una explosión ROJA (FAILED)! Pytest te dirá que
#    esperaba 80.0 pero recibió 95.0.
# 4. Ahora, ve a `facturas.py`, arregla la fórmula matemática para que aplique
#    el porcentaje real.
# 5. Vuelve a correr `pytest -v`. ¡Ahora todo debe estar VERDE!
# Pega aquí el código de tu función `aplicar_descuento` arreglada y el output final en verde.

# --- TU CÓDIGO CORREGIDO Y OUTPUT AQUÍ ---
1- error: =========================================== short test summary info ===========================================
FAILED test_facturas.py::test_aplicar_descuento - assert 95 == 80.0
2- correcto:
test_facturas.py::test_aplicar_descuento PASSED                                                         [ 66%]
codigo corregido:
def aplicar_descuento(precio, descuento):
    return precio - (precio * descuento)  # <-- Ahora aplica el porcentaje correctamente


🚀 Ejercicio 3: Implementación E2E - Escenario Real (Manejando Errores Esperados)
# Contexto: ¿Qué pasa si el cliente envía un número negativo como precio? El sistema
# debería estallar y arrojar un `ValueError`. ¡También podemos hacer tests para
# verificar que los errores se disparen correctamente!
#
# Requisitos Ejecutables (Flujo Completo):
# 1. En `facturas.py`, agrega esto al inicio de la función `calcular_total` del Ejercicio 1:
#    if subtotal < 0:
#        raise ValueError("El subtotal no puede ser negativo")
# 2. En `test_facturas.py`, agrega este test usando la herramienta `raises` de pytest:
#    import pytest
#    # ... resto de tu código ...
#    def test_calcular_total_negativo_lanza_error():
#        with pytest.raises(ValueError):
#            calcular_total(-50, 0.13)
# 3. Ejecuta `pytest -v`.
# Pega aquí el output de consola. (El test pasará en VERDE, porque Pytest esperaba que el
# sistema estallara con ValueError, ¡y lo hizo!).

# --- TU OUTPUT AQUÍ ---
1- resultado test_facturas.py::test_calcular_negativo_total PASSED                                                    [ 75%]



🐛 Ejercicio 4: Lectura de Código y Debugging (El Test Fantasma)
# Contexto: Un Junior en la agencia escribe pruebas para su código de usuarios.
# Crea un archivo llamado `pruebas_usuarios.py`. Adentro escribe:
#
# def revisar_login():
#     usuario = login("admin", "1234")
#     assert usuario == True
#
# El Junior ejecuta el comando `pytest`. La terminal le responde con un mensaje
# amarillo diciendo "collected 0 items". Pytest ignoró sus pruebas por completo.
#
# Pregunta Debugging: Basado en las reglas clave de la teoría, ¿cuáles son los DOS
# errores de nomenclatura (nombres) que cometió el Junior, que hicieron que Pytest
# fuera incapaz de encontrar su prueba? ¿Cómo deberían llamarse su archivo y su función?

# --- TU EXPLICACIÓN Y NOMBRES CORREGIDOS AQUÍ ---
Primeramente al hacer una funcion es una buena practica hacerla lo mas descritiva posible, ese nombre de funcio(revisar_login) es muy simple, aque me refiero carece de informarcion como cual login esta verificando de donde es un posible nombre de login, login_usiarios_web_store, ahora bien esto es solo para el archivo de la implementacion, ahora seguimos con el archivo del test, dicho archivo si o si tiene que llevar en su nombre ya sea al inicio o al final el nombre de test, por ejemplo test_login_web.py y asi mismo la funcion, un posible nombre para ella seria test_login_web():... NOTA IMPORTANTE solo en esta funcion y archivo de test se usa la palabra assert para validar si el rultado del test es el esperado... finalmente pytest ignoro los test por la simple razon de que no encontro su palabra clave test en el archivo y la funcion.



🧠 FASE 3: CONSOLIDACIÓN TEÓRICA
❓ Pregunta Teórica 1:
Tu código de producción en Python (facturas.py) se sube a los servidores de AWS para que el cliente lo use. Sin embargo, en una arquitectura limpia, la carpeta con los tests (test_facturas.py) NO necesita instalarse en producción. ¿En qué momento exacto del ciclo de vida del software (recuerda GitHub Actions / CI/CD) deberían ejecutarse los tests automatizados?
Con la grandiosa app de git hub actions podemos automatizaar pruebas de teste a nuestro codigo antes de subirlo al produccion, es una herramienta con la podemos crear o añadir el flujo CI/CD para nuestra app y su cicllo de software.


❓ Pregunta Teórica 2:
Imagina que modificas la lógica central de la base de datos de tu SaaS y ejecutas pytest. Un test que tú no tocaste, llamado test_pago_tarjeta(), falla repentinamente. ¿Por qué este fallo (Regresión) demuestra el mayor valor de tener tests automatizados, en lugar de no tenerlos y depender del equipo de QA (humanos probando la página manualmente)?
El ser humano es propenso a varios errores en esta area, ya sea por desconsentracion o cansacio, cundo se hace un test se debe de terner cuidado con el nombre de archivos y con los comenados que se usan. En este caso el test pudo fallar por cualquiera de esta razones. Hoy en dia por esta razon se a dado un gran auje y apoyo al testing automatizado ya que son varios puntos de mejora con respecto al testing manual... Por ejemplo el ahorre del tiempo a la hora de configurar, la versatilidad, cansacion y disposicion no es lo mismo decirle a un QA un viernes que haga un testing a decirle a un bot o plataforma como git ub actions con sus configuraciones que lo haga y asi sucesivament el testing automatizado tiene muchos beneficios con respecto al testing manual.


🗣️ Prueba de Feynman (Explicación):
Escenario: Un cliente te pregunta por qué te vas a demorar 2 días extra programando "tests automáticos" si la aplicación ya parece funcionar bien en tu computadora.
Explícale el concepto usando la analogía de una fábrica de autos, los maniquíes de pruebas de choque (Crash Test Dummies) y las llamadas a revisión masivas (Recall).
El testing automatizado es como tener maniquíes de pruebas de choque en una fábrica de autos. Aunque un auto parezca funcionar bien en la línea de ensamblaje, no podemos estar seguros de que sea seguro hasta que lo sometamos a pruebas rigurosas. Los maniquíes simulan accidentes y nos muestran cómo se comporta el auto bajo condiciones extremas. De manera similar, los tests automáticos ponen a prueba nuestro código en diferentes escenarios para asegurarnos de que funcione correctamente y no tenga errores ocultos. Si no hacemos estas pruebas, podríamos enfrentar problemas graves más adelante, como llamadas a revisión masivas (recalls) en la industria automotriz, donde los autos tienen que ser retirados del mercado debido a fallas que podrían haberse detectado con pruebas adecuadas. Por eso, invertir tiempo en escribir tests automáticos ahora nos ahorra mucho más tiempo y problemas en el futuro. 