# 🚀 DÍA 9 - Módulo 0: Decoradores Básicos y Uso Práctico

# 📚 Teoría Concisa

# Decoradores en Python
# Los decoradores son funciones que modifican el comportamiento de otras funciones.
# Son una forma elegante de extender funcionalidad sin modificar el código original.
# Es como ponerle “chocolate” a una función para que haga algo extra, pero sin cambiar la función original.

# Concepto clave: Las funciones son objetos de primera clase
# - Se pueden asignar a variables
# - Se pueden pasar como argumentos
# - Se pueden retornar desde otras funciones

# Sintaxis básica:
# @decorador
# def funcion():
#     pass

# Es equivalente a:
# funcion = decorador(funcion)

# Estructura de un decorador:
# def mi_decorador(funcion):
#     def wrapper(*args, **kwargs):
#         # código antes
#         resultado = funcion(*args, **kwargs)
#         # código después
#         return resultado
#     return wrapper

# Decoradores comunes útiles:
# @property: convierte método en atributo
# @staticmethod: método sin acceso a self
# @classmethod: método con acceso a la clase (cls)
# @functools.wraps: preserva metadata de función decorada
# @logger: ejemplo personalizado para logging


# Usos prácticos de decoradores:
# - Logging automático
# - Medición de tiempo de ejecución
# - Validación de parámetros
# - Control de acceso/permisos
# - Caché de resultados
# - Retry logic (reintentos)

# Buenas prácticas:
# Usa functools.wraps para preservar metadata
# Nombra wrappers descriptivamente cuando sean específicos
# Decoradores simples para una responsabilidad
# Documenta qué hace el decorador
# *args, **kwargs para flexibilidad

# Errores comunes:
# Olvidar return en el wrapper
# No usar *args, **kwargs (limita uso)
# No preservar metadata con @wraps
# Decoradores demasiado complejos
# Modificar argumentos sin documentarlo

# Ejemplo práctico - Decorador básico:

# Sin decorador - código repetitivo
def sumar(a, b):
    print("Ejecutando función...")
    resultado = a + b
    print("Función completada")
    return resultado

def restar(a, b):
    print("Ejecutando función...")
    resultado = a - b
    print("Función completada")
    return resultado

# ✅ Con decorador - DRY (Don't Repeat Yourself)
def logger(funcion):
    """Decorador que registra ejecución de función."""
    def wrapper(*args, **kwargs): # Aquí usamos *args y **kwargs para que el decorador funcione con cualquier cantidad de parámetros.
        # *args Permite recibir múltiples argumentos posicionales. Se guardan como una tupla.
        # **kwargs Permite recibir argumentos con nombre (clave = valor). Se guardan como un diccionario.
        print(f"Ejecutando: {funcion.__name__}")
        resultado = funcion(*args, **kwargs)
        print(f"Completado: {funcion.__name__}")
        return resultado
    return wrapper

@logger 
def sumar(a, b):
    return a + b

@logger
def restar(a, b):
    return a - b

# Uso:
print(sumar(5, 3))  # Logs automáticos

# Ejemplo - Decorador con parámetros:
import time

def medir_tiempo(funcion):
    """Mide tiempo de ejecución."""
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"{funcion.__name__} tomó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def procesar_datos(n):
    return sum(range(n))

# Ejemplo - Preservar metadata con wraps:
from functools import wraps

def mi_decorador(funcion):
    @wraps(funcion)  # Preserva __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        return funcion(*args, **kwargs)
    return wrapper

# Documentación oficial: https://docs.python.org/3/glossary.html#term-decorator


# 💻 Ejercicios Acumulativos

# Ejercicio 1: Decoradores de Logging Básicos
# Contexto: Sistema que necesita registrar todas las llamadas a funciones.
# Requisitos:
# Crea estos decoradores:

# 1. log_llamada(funcion)
#    - Imprime: "Llamando a: {nombre_funcion}"
#    - Ejecuta la función
#    - Imprime: "Completado: {nombre_funcion}"
#    - Retorna el resultado
def Call_log(funtion):
    def wrapper(*args, **kwargs):
        print(f"llamando a: {funtion.__name__}")
        result = funtion(*args, **kwargs)
        print(f"Completado: {funtion.__name__}")
        return result
    return wrapper

# 2. log_argumentos(funcion)
#    - Imprime: "Función: {nombre} llamada con args={args}, kwargs={kwargs}"
#    - Ejecuta la función
#    - Retorna el resultado
def argument_log(Funtion):
    def wrapper(*args, **kwargs):
        print(f"Funcion: {Funtion.__name__} llamada con args={args}, kwards={kwargs}")
        result = Funtion(*args, **kwargs)
        return result
    return wrapper

# 3. log_resultado(funcion)
#    - Ejecuta la función
#    - Imprime: "{nombre_funcion} retornó: {resultado}"
#    - Retorna el resultado
def result_log(funtion):
    def wrapper(*args, **kwargs):
        result = funtion(*args, **kwargs)
        print(f"{funtion.__name__} retorno: {result}")
        return result
    return wrapper

# Aplica los decoradores a estas funciones:
@Call_log
def suma(a, b):
    return a + b

@argument_log
def create_user(name, last_name, age, premium=True):
    return {"Name" : name, "Lastname" : last_name, "Age" : age, "Is premium" : premium}

@result_log
def Calculate_average(*args):
    return sum(args) / len(args)

print(Calculate_average(5.2, 56.2, 1.0, 55.6, 10.3))
print(create_user("eric", "edwards", 21, False))
print(suma(45, 10))

# Ejercicio 2: Decorador de Medición de Tiempo
# Contexto: Necesitas medir performance de funciones críticas.
# Requisitos:
# Crea decorador cronometro(funcion):
#   - Usa time.time() o time.perf_counter()
#   - Registra tiempo antes de ejecutar
#   - Ejecuta la función
#   - Calcula tiempo transcurrido
#   - Imprime: "{nombre_funcion} ejecutado en {tiempo:.4f} segundos"
#   - Retorna el resultado original
# Usa functools.wraps para preservar metadata
from functools import wraps
import time
def Chronometer(funtion):
    @wraps(funtion)
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = funtion(*args, **kwargs)
        time_end = time.time()
        total =  time_end - time_start
        print(F"{funtion.__name__} running in {total:.4f} seconds")
        return result
    return wrapper

# Aplica a estas funciones:
# @cronometro
# def buscar_en_lista(lista, objetivo):
#     return objetivo in lista
@Chronometer
def search_in_list(data, obj):
    return obj in data

# @cronometro
# def ordenar_lista(lista):
#     return sorted(lista)
@Chronometer
def order_list(data):
    return sorted(data)

@Chronometer
def factorial(num):
    if num <= 1:
        return num
    for n in range(1, num):
        num *= n
    return num
print(order_list([56, 100, 1, 2, 10, 3]))
print(factorial(50))
print(search_in_list([56, 100, 1, 2, 10, 3], 3))

# Ejercicio 3: Decorador de Validación de Parámetros
# Contexto: Sistema que valida inputs antes de procesarlos.
# Requisitos:
# Crea estos decoradores de validación:

# 1. validar_positivo(funcion)
#    - Valida que todos los argumentos numéricos sean > 0
#    - Si alguno es <= 0: lanza ValueError con mensaje descriptivo
#    - Sino: ejecuta función normalmente
def Validate_p(funtion):
    @wraps(funtion)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"Argument {arg} must be positive")
        return funtion(*args, **kwargs)
    return wrapper


# 2. validar_tipo(tipo_esperado)
#    - Decorador parametrizado: un decorador parametrizado es un decorador que acepta argumentos. En este caso, el tipo esperado para el primer argumento de la función decorada.
#    - Valida que el primer argumento sea del tipo esperado
#    - Si no: lanza TypeError
#    - Uso: @validar_tipo(str), @validar_tipo(int)
def Validate_type(type_expected):
    def decorator(funtion):
        @wraps(funtion)
        def wrapper(*args, **kwargs):
            if isinstance(args[0], type_expected):
                return funtion(*args, **kwargs)
            else:
                raise TypeError(f"The first argument must be {type_expected.__name__}")
        return wrapper
    return decorator

# 3. validar_rango(minimo, maximo)
#    - Decorador parametrizado
#    - Valida que el primer argumento esté entre minimo y maximo
#    - Si no: lanza ValueError
def Validate_range(min, max):
    def decorator(funtion):
        @wraps(funtion)
        def wrapper(*args, **kwargs):
            if min <= args[0] and args[0] <= max:
                return funtion(*args, **kwargs)
            else:
                raise ValueError(f"The first argument must be between {min} and {max}")
        return wrapper
    return decorator

# Aplica a estas funciones:
# @validar_positivo
# def calcular_descuento(precio, porcentaje):
#     return precio * (porcentaje / 100)
@Validate_p
def calculate_discount(price, percentage):
    return price * (percentage / 100)

# @validar_tipo(str)
# def procesar_nombre(nombre):
#     return nombre.upper()
@Validate_type(str)
def process_name(name):
    return name.upper()

# @validar_rango(0, 100)
# def calcular_calificacion(puntos):
#     return "Aprobado" if puntos >= 60 else "Reprobado"
@Validate_range(0, 100)
def calculate_score(points):
    return "Approved" if points >= 60 else "Failed"

print(calculate_discount(100, 20))
print(process_name("eric"))
print(calculate_score(85))


# Ejercicio 4: Decorador de Caché Simple (Memoization)
# Contexto: Optimizar funciones con cálculos repetidos.
# Requisitos:
# Crea decorador cache(funcion):
#   - Usa un diccionario para almacenar resultados previos
#   - Clave: tupla de argumentos
#   - Antes de ejecutar función:
#     * Verifica si argumentos ya están en caché
#     * Si sí: retorna resultado guardado sin ejecutar función
#     * Si no: ejecuta, guarda en caché, retorna resultado
#   - Imprime "Cache hit" o "Cache miss" para debug
# PISTA: Usa diccionario dentro del wrapper o como atributo de la función
def Cache(funtion):
    cache_dict = {}
    """ Guarda resultados previos para evitar cálculos repetidos, especialmente útil en funtiones recursivas como Fibonacci.
    si encuentra el numero fibonnaci(key) en el diccionareio, el no vuelve a calcularlo, si n o que toma el resultado(value) y lo retorna,
    si no lo encuentra, el calcula el resultado, lo guarda en el diccionario y luego lo retorna.
    asi se ahorra recursos.
    """
    @wraps(funtion)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items())) # los items son los numeros fibonnaci.
        if key in cache_dict:
            print("Cache hit")
            return cache_dict[key]
        else:
            print("Cache miss")
            result = funtion(*args, **kwargs)
            cache_dict[key] = result
            return result
    return wrapper

# Aplica a estas funciones:
# @cache
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
@Cache
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
    
# @cache
# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)
@Cache
def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(fibonacci(30))  
print(factorial(20))  
print(fibonacci(30))  # Cache hit
print(factorial(20))  # Cache hit


# Ejercicio 5: Sistema de Decoradores para API (Integrador)
# Contexto: Sistema de endpoints que necesita autorización, logging y manejo de errores.
# Requisitos:
# Crea estos decoradores que se pueden combinar:

# 1. requiere_autenticacion(funcion)
#    - Simula verificación de autenticación
#    - La función recibe un parámetro usuario: dict
#    - Si usuario es None o usuario.get("autenticado") != True:
#      * Lanza PermissionError("Usuario no autenticado")
#    - Sino: ejecuta función normalmente
def Authentication_required(funtion):
    def wrapper(User, *args, **kwargs):
        if User is None or User.get("authenticated") != True:
            raise PermissionError("User not authenticated")
        return funtion(User, *args, **kwargs)

# 2. requiere_rol(rol_requerido: str)
#    - Decorador parametrizado
#    - Verifica que usuario["rol"] == rol_requerido
#    - Si no: lanza PermissionError(f"Requiere rol: {rol_requerido}")
def Role_required(role_required):
    def decorator(funtion):
        def wrapper(User, *args, **kwargs):
            if User.get("rol") != role_required:
                raise PermissionError(f"Requires role: {role_required}")
            return funtion(User, *args, **kwargs)
        return wrapper
    return decorator

# 3. manejo_errores(funcion)
#    - Envuelve ejecución en try/except
#    - Captura cualquier excepción
#    - Retorna dict: {"error": str, "mensaje": str}
#    - Si no hay error: retorna dict: {"exito": True, "data": resultado}
def Error_handler(funtion):
    def wrapper(*args, **kwargs):
        try:
            result = funtion(*args, **kwargs)
            return {"success": True, "data": result}
        except Exception as e:
            return {"error": type(e).__name__, "message": str(e)}
    return wrapper

# 4. log_api(funcion)
#    - Registra: "API {nombre_funcion} - Usuario: {usuario['nombre']}"
#    - Ejecuta función
#    - Registra: "API {nombre_funcion} - Completado"
def API_log(funtion):
    def wrapper(User, *args, **kwargs):
        print(f"API {funtion.__name__} - User: {User['name']}")
        result = funtion(User, *args, **kwargs)
        print(f"API {funtion.__name__} - Completed")
        return result
    return wrapper

# Crea estas funciones simulando endpoints:

# @manejo_errores
# @log_api
# @requiere_autenticacion
# def obtener_perfil(usuario):
#     return {"id": usuario["id"], "nombre": usuario["nombre"]}
@Error_handler
@API_log
@Authentication_required
def get_profile(User):
    return {"id": User["id"], "name": User["name"]}

# @manejo_errores
# @log_api
# @requiere_autenticacion
# @requiere_rol("admin")
# def eliminar_usuario(usuario, usuario_id_eliminar):
#     return f"Usuario {usuario_id_eliminar} eliminado por {usuario['nombre']}"
@Error_handler
@API_log
@Authentication_required
def delete_user(User, user_id_to_delete):
    return f"User {user_id_to_delete} deleted by {User['name']}"

# Prueba con diferentes usuarios:
usuario_admin = {"id": 1, "name": "Admin User", "authenticated": True, "rol": "admin"}
usuario_regular = {"id": 2, "name": "Regular User", "authenticated": True, "rol": "user"}
usuario_invitado = {"id": 3, "name": "Guest User", "authenticated": False, "rol": "guest"}
print(get_profile(usuario_admin))  # Éxito
print(get_profile(usuario_invitado))  # Error de autenticación
print(delete_user(usuario_admin, 5))  # Éxito
print(delete_user(usuario_regular, 5))  # Error de rol


# 📖 Ejercicios de Lectura de Código

# Ejercicio 6: Análisis de Decoradores Problemáticos
# Identifica los problemas en estos decoradores:

# Problema 1: No retorna resultado
def decorador_malo1(funcion):
    def wrapper(*args, **kwargs):
        print("Ejecutando...")
        funcion(*args, **kwargs)  # ¿Qué falta? capturar el valor de la función y retornarlo
    return wrapper

# Problema 2: No usa *args, **kwargs
def decorador_malo2(funcion):
    def wrapper():  # ¿Qué pasa si función tiene parámetros? No podrá recibirlos, lo que limita su uso a funciones sin parámetros.
        return funcion()
    return wrapper

@decorador_malo2
def sumar(a, b):  # ¿Funcionará? No, porque el wrapper no acepta parámetros, lo que causará un error al intentar pasar argumentos a sumar.
    return a + b

# Problema 3: No preserva metadata
def decorador_malo3(funcion):
    def wrapper(*args, **kwargs):
        return funcion(*args, **kwargs) # ¿Qué pasa con mi_funcion.__name__ y mi_funcion.__doc__? Se perderán, 
                                        # ya que el wrapper no tiene @wraps(funcion) para preservar la metadata de la función original.
    return wrapper

@decorador_malo3
def mi_funcion():
    """Esta es mi función."""
    pass

print(mi_funcion.__name__)  # ¿Qué imprime? Imprime "wrapper" en lugar de "mi_funcion", lo que puede causar confusión al depurar o documentar el código.

# Problema 4: Modifica argumentos sin documentar
def decorador_malo4(funcion):
    def wrapper(*args, **kwargs):
        result = tuple(x * 2 for x in args)  # Modifica args silenciosamente
        return result 
    return wrapper

# Problema 5: Decorador parametrizado mal implementado
# def decorador_malo5(parametro):
#     def wrapper(*args, **kwargs):  # ¿Dónde está el problema? Falta una variable que guarde la funcion.
#         return funcion(*args, **kwargs)
#     return wrapper

# Preguntas:
# ¿Por qué es crítico retornar el resultado de la función?
# porque si no se retorna el resultado, la función decorada no devolverá nada (None), lo que puede romper el programa ya que espera un valor 

# ¿Qué pasa si no usas *args, **kwargs?
# El decorador solo funcionará con funciones que no tengan parámetros, lo que limita su utilidad.

# ¿Cómo se soluciona la pérdida de metadata?
# la perdida de metada se soluciona usando @functools.wraps(funcion) en el wrapper, lo que preserva el nombre, la documentación y otros atributos de la función.

# ¿Cuál es la estructura correcta de un decorador parametrizado?
# def decorador_parametrizado(parametro):
#     def decorator(funcion):
#         @wraps(funcion)
#         def wrapper(*args, **kwargs):
#             # priny("Parámetro:", parametro)
#             resultado = funcion(*args, **kwargs)
#             return resultado
#         return wrapper
#     return decorator


# Ejercicio 7: Refactorización Usando Decoradores
# Refactoriza este código repetitivo usando decoradores:
import time
def procesar_pedido(pedido_id):
    print(f"Iniciando procesamiento de pedido {pedido_id}")
    inicio = time.time()
    try:
        # Lógica de negocio
        if pedido_id < 0:
            raise ValueError("ID inválido")
        resultado = f"Pedido {pedido_id} procesado"
        fin = time.time()
        print(f"Tiempo: {fin - inicio:.4f}s")
        return resultado
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def pay_order(order_id):
    def wrapper(*args, **kwargs):
        print(f"Paying order {order_id}")
        start = time.time()
        try:
            if order_id < 0:
                raise ValueError("Invalid order ID, must be a number greater than 0")
            result = f"Order {order_id} paid"
            end = time.time()
            print(f"Time: {end - start:.4f}s")
            return result
        except Exception as e:
            print(f"Error: {e}")
            return None
################################################
def enviar_email(destinatario):
    print(f"Iniciando envío de email a {destinatario}")
    inicio = time.time()
    try:
        # Lógica de negocio
        if "@" not in destinatario:
            raise ValueError("Email inválido")
        resultado = f"Email enviado a {destinatario}"
        fin = time.time()
        print(f"Tiempo: {fin - inicio:.4f}s")
        return resultado
    except Exception as e:
        print(f"Error: {e}")
        return None

def Send_email(destinatary):
    def wrapper(*args, **kwargs):
        print(f"Sending email to {destinatary}")
        start = time.time()
        try:
            if "@" not in destinatary:
                raise ValueError("Invalid email address")
            result = f"Email sent to {destinatary}"
            end = time.time()
            print(f"Time: {end - start:.4f}s")
            return result
        except Exception as e:
            print(f"Error: {e}")
            return None
#################################################
def generar_reporte(tipo):
    print(f"Iniciando generación de reporte {tipo}")
    inicio = time.time()
    try:
        # Lógica de negocio
        if not tipo:
            raise ValueError("Tipo de reporte requerido")
        resultado = f"Reporte {tipo} generado"
        fin = time.time()
        print(f"Tiempo: {fin - inicio:.4f}s")
        return resultado
    except Exception as e:
        print(f"Error: {e}")
        return None

def report_generate(type):
    def wrapper(*args, **kwargs):
        print(F"Generating report: {type}")
        start_time = time.time()
        try:
            if not type:
                raise ValueError("I need a type of report")
            result = f"Report generated {type}"
            end_time = time.time()
            print(f"Time process: {end_time - start_time:.5f} seconds")
            return result
        except Exception as e:
            print(f"An error is detected: {e}")
            return None


# 🧪 Evaluación Teórica

# Pregunta 1
# Explica qué es un decorador en Python y cómo funciona internamente.
# ¿Qué significa que @decorador es "syntax sugar"?
# Un decorador es una forma de extender elegantemente la funcionalidad de una funcion si tocar el codigo base, envuelve la funcion original con uan nueva funcion(wrapper),
# que ejecuta codigo antes y despues de la funcion original.
# El @decorador es "syntax sugar" porque es una forma más concisa y legible de aplicar un decorador a una función.


# Pregunta 2
# ¿Por qué es importante usar *args y **kwargs en la función wrapper de un decorador?
# ¿Qué limitaciones tendría un decorador sin ellos?
# Es imporatnte usar *args y **kwargs para que asi el docardor acepte cualquier cantidad de argumentos, lo que hace al decorador mas flexible,
# si no se usaran, el decorador solo funcionará con funciones que no tengan parámetros, lo que limita su utilidad.

# Pregunta 3
# Explica qué hace @functools.wraps y por qué es importante usarlo.
# ¿Qué metadata se pierde si no lo usas? Da ejemplos concretos.
# functools.wraps es un decorador que se usa dentro de la función wrapper de un decorador para preservar la metadata de la función original,
# se preserva su nombre (__name__), su documentación (__doc__) y otros atributos.
# si no se usaran, se perdería el nombre de la función original, lo que puede causar confusión al depurar o documentar el código. 
# Por ejemplo, si decoramos una función llamada "mi_funcion" sin usar @wraps, el atributo __name__ de la función decorada sería "wrapper" en lugar de "mi_funcion".

# Reflexión personal:
# ¿Qué fue lo más difícil?
# entender decoradores, diferenciar wrapper y wraps

# ¿Entendiste cómo funcionan los decoradores internamente?
# si correcto envuelven la funcion original y asu vez extienden su funcion sin tocar el codigo original

# ¿Cuánto tiempo real te tomó?
# unas 7 horas

# ¿Qué concepto necesitas repasar?
# diferenciar wrapper y wraps


# 🎯 Objetivo de mañana (Día 10): Big O Notation aplicado a Django ORM queries

# Conexión con proyectos finales:
# 💰 Cost Optimizer: Decoradores para logging de llamadas AWS API, caché de resultados, medición de tiempo
# 🔐 SecureVault: Decoradores para autenticación, autorización, audit logging, validación de permisos