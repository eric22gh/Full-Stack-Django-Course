# 🚀 DÍA 5 - Módulo 0: Manejo de Errores y Excepciones

# 📚 Teoría Concisa 

# Excepciones en Python
# Las excepciones son errores que ocurren durante la ejecución del programa.
# Python permite capturar y manejar estos errores de forma controlada.

# Estructura básica try/except:
# try:
#     # código que puede fallar
# except TipoDeError:
#     # qué hacer si falla
# else:
#     # se ejecuta si NO hubo error, osea se ejecuta despues del try
# finally:
#     # SIEMPRE se ejecuta (con o sin error)

# Excepciones comunes:
# ValueError: conversión de tipos inválida(de un tipo a otro tipo)
# TypeError: operación con tipo incorrecto (Cuando multiplico o resto de dato, que no se puede)
# KeyError: clave no existe en diccionario
# IndexError: índice fuera de rango en lista
# ZeroDivisionError: división por cero
# FileNotFoundError: archivo no existe
# AttributeError: atributo/método no existe

# Lanzar excepciones:
# raise ValueError("Mensaje de error")
# raise TypeError("Tipo incorrecto")
# raise KeyError("llave incorrecta o no existe")
# raise AttributeError("Attributo incorrecto")

# Excepciones personalizadas:
# class MiError(Exception):
#     pass
# Unaa excepción personalizada es una clase creada por el programador que extiende (hereda) de una clase de excepción existente, 
# como Exception en Python o Throwable/Exception en Java. Su propósito es representar errores específicos de tu aplicación que no están cubiertos 
# por las excepciones estándar del lenguaje.


# Buenas prácticas:
# Captura excepciones ESPECÍFICAS, no genéricas (except Exception:)
# Usa else para código que solo debe ejecutarse si no hay error
# Usa finally para limpieza (cerrar archivos o conexiones)
# No uses try/except para control de flujo normal
# Lanza excepciones con mensajes descriptivos
# Valida datos ANTES de procesarlos cuando sea posible
# Logging de errores para debugging en producción

# Errores comunes:
# Capturar Exception genérico (oculta bugs)
# try/except vacío sin manejo
# No propagar errores críticos
# Usar excepciones para control de flujo
# No limpiar recursos en caso de error

# Ejemplo práctico - Validación robusta:

# ❌ Mal - captura genérica sin información
def dividir_malo(a, b):
    try:
        return a / b
    except:
        return None  # ¿Qué falló? No sabemos

# ✅ Bien - excepciones específicas con mensajes
def dividir_bueno(a: float, b: float) -> float:
    """
    Divide dos números de forma segura.
    
    Args:
        a: Dividendo
        b: Divisor
        
    Returns:
        Resultado de la división
        
    Raises:
        TypeError: Si a o b no son números
        ValueError: Si b es cero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Los argumentos deben ser números, recibido: {type(a)}, {type(b)}")
    
    if b == 0:
        raise ValueError("El divisor no puede ser cero")
    
    return a / b

# Ejemplo - Validación con múltiples excepciones:
def procesar_edad(edad_str: str) -> int:
    """Convierte y valida edad de string a int."""
    try:
        edad = int(edad_str)
    except ValueError:
        raise ValueError(f"Edad debe ser un número, recibido: '{edad_str}'")
    
    if edad < 0:
        raise ValueError(f"Edad no puede ser negativa: {edad}")
    
    if edad >= 100:
        raise ValueError(f"Edad no realista: {edad}")
    
    return edad

# Ejemplo - finally para limpieza:
def leer_archivo_seguro(ruta: str) -> str:
    """Lee archivo y garantiza cierre."""
    archivo = None
    try:
        archivo = open(ruta, 'r')
        contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        raise FileNotFoundError(f"Archivo no encontrado: {ruta}")
    finally:
        if archivo:
            archivo.close()  # SIEMPRE cierra

# Documentación oficial: https://docs.python.org/3/tutorial/errors.html


# 💻 Ejercicios Acumulativos

# Ejercicio 1: Conversor de Tipos Robusto
# Contexto: Sistema que recibe datos del frontend como strings y debe convertirlos de forma segura.
# Requisitos:
# Crea estas funciones con manejo de errores:
#   1. convertir_a_entero(valor: str) -> int
#      - Convierte string a int
#      - Maneja ValueError con mensaje claro
#      - Valida que el resultado esté en rango -1000000 a 1000000
#      
#   2. convertir_a_decimal(valor: str) -> float
#      - Convierte string a float
#      - Maneja ValueError
#      - Valida que no sea infinito o NaN
#      
#   3. convertir_a_booleano(valor: str) -> bool
#      - Acepta: "true", "false", "1", "0", "yes", "no" (case-insensitive)
#      - Lanza ValueError si no es valor válido
#      
#   4. convertir_datos_formulario(datos: dict) -> dict
#      - Recibe: {"edad": str, "precio": str, "activo": str}
#      - Usa las funciones anteriores
#      - Retorna dict con valores convertidos
#      - Si CUALQUIER conversión falla, retorna: {"error": str, "campo": str}

# Casos de prueba:
# convertir_a_entero("25") → 25
# convertir_a_entero("abc") → ValueError
# convertir_a_entero("9999999") → ValueError (fuera de rango)
# convertir_datos_formulario({"edad": "30", "precio": "99.99", "activo": "true"})
# convertir_datos_formulario({"edad": "abc", "precio": "99.99", "activo": "true"})
def convertir_a_entero(valor: str) -> int:
    """Convierte un string a entero.
    
    Args:
        valor: String a convertir.
        
    Returns:
        int: Valor convertido.
        
    Raises:
        ValueError: Si la conversión falla o el valor está fuera de rango.
    """
    try:
        nuevo_valor = int(valor)
    except ValueError:
        raise ValueError(f"No se puede convertir '{valor}' a entero.")
    
    if nuevo_valor < -1000000 or nuevo_valor > 1000000:
        raise ValueError(f"El valor debe estar en el rango de -1000000 a 1000000, recibido: {nuevo_valor}")
    
    return nuevo_valor

def convertir_a_decimal(valor: str) -> float:
    """Convierte un string a float.
    
    Args:
        valor: String a convertir.
        
    Returns:
        float: Valor convertido.
        
    Raises:
        ValueError: Si la conversión falla, o si el valor es NaN o infinito.
    """
    try:
        nuevo_valor = float(valor)
    except ValueError:
        raise ValueError(f"No se puede convertir '{valor}' a decimal.")
    
    if nuevo_valor != nuevo_valor or nuevo_valor == float('inf'):
        raise ValueError(f"El valor no puede ser NaN o infinito.")
    
    return nuevo_valor

def convertir_a_booleano(valor: str) -> bool:
    """Convierte un string a booleano.
    
    Args:
        valor: String a convertir.
        
    Returns:
        bool: Valor convertido.
        
    Raises:
        ValueError: Si el valor no es válido.
    """
    valor = valor.strip().lower()
    if valor in ("true", "1", "yes"):
        return True
    elif valor in ("false", "0", "no"):
        return False
    else:
        raise ValueError(f"Valor inválido para booleano: '{valor}'")

def convertir_datos_formulario(datos: dict) -> dict:
    """Convierte datos del formulario.
    
    Args:
        datos: Diccionario con las claves "edad", "precio", "activo".
        
    Returns:
        dict: Diccionario con valores convertidos o error.
    """
    nuevo_datos = {}
    for clave, valor in datos.items():
        try:
            if clave == "edad":
                nuevo_datos[clave] = convertir_a_entero(valor)
            elif clave == "precio":
                nuevo_datos[clave] = convertir_a_decimal(valor)
            elif clave == "activo":
                nuevo_datos[clave] = convertir_a_booleano(valor)
        except ValueError as error:
            return {"error": str(error), "campo": clave}
    
    return nuevo_datos

# Casos de prueba
print(convertir_datos_formulario({"edad": "30", "precio": "99.99", "activo": "true"}))
print(convertir_datos_formulario({"edad": "abc", "precio": "99.99", "activo": "true"}))



# Ejercicio 2: Validador de Productos con Excepciones Personalizadas
# Contexto: Sistema de inventario que valida productos antes de agregarlos.
# Requisitos:
# Define estas excepciones personalizadas:
#   class ProductoInvalidoError(Exception):
#       pass
#   
#   class StockNegativoError(Exception):
#       pass
#   
#   class PrecioInvalidoError(Exception):
#       pass

# Crea función validar_producto(producto: dict) -> bool:
#   - Valida que tenga claves: "nombre", "precio", "stock"
#   - nombre: no vacío, string
#   - precio: float positivo
#   - stock: int no negativo
#   - Lanza la excepción apropiada con mensaje descriptivo
#   - Retorna True si todo es válido

# Crea función agregar_producto_seguro(productos: list, nuevo_producto: dict) -> dict:
#   - Usa validar_producto()
#   - Si es válido: agrega a lista y retorna {"exito": True, "mensaje": str}
#   - Si falla validación: captura excepción y retorna {"exito": False, "error": str}
#   - NO permite que el programa se detenga por error

# Casos de prueba:
# agregar_producto_seguro([], {"nombre": "Laptop", "precio": 1200.0, "stock": 10})
# agregar_producto_seguro([], {"nombre": "", "precio": 1200.0, "stock": 10})
# agregar_producto_seguro([], {"nombre": "Mouse", "precio": -25.0, "stock": 5})
# agregar_producto_seguro([], {"nombre": "Teclado", "precio": 75.0, "stock": -3})
class InvalidProductError(Exception):
    pass
class NegativeStockError(Exception):
    pass
class InvalidPriceError(Exception):
    pass
def validate_product(product : dict) -> bool:
    if "nombre" not in product or "precio" not in product or "stock" not in product:
        raise InvalidProductError("The product dont have the correct keys")
    if not isinstance(product["nombre"], str) or product["nombre"].strip() == "":
        raise InvalidProductError("The name is invalid")
    if not isinstance(product["precio"], (int, float)) or product["precio"] <= 0:
        raise InvalidPriceError("The price is invalid")
    if not isinstance(product["stock"], int) or product["stock"] < 0:
        raise NegativeStockError("The stock is invalid")
    return True
def add_safe_product(products : list, new_product : dict) -> dict:
    try:
        if validate_product(new_product):
            products.append(new_product)
            return {"exito": True, "mensaje": "Product added successfully"}
    except (InvalidProductError, InvalidPriceError, NegativeStockError) as Error:
        return {"exito": False, "error": str(Error)}
    
print(add_safe_product([], {"nombre": "Laptop", "precio": 1200.0, "stock": 10}))
print(add_safe_product([], {"nombre": "", "precio": 1200.0, "stock": 10}))
print(add_safe_product([], {"nombre": "Mouse", "precio": -25.0, "stock": 5}))
print(add_safe_product([], {"nombre": "Teclado", "precio": 75.0, "stock": -3}))


# Ejercicio 3: Sistema de División Segura con Logging
# Contexto: Calculadora que debe manejar operaciones problemáticas sin crashear.
# Requisitos:
# Crea función calcular_operacion(a: float, b: float, operacion: str) -> dict:
#   - Operaciones: "suma", "resta", "multiplicacion", "division"
#   - Para división: maneja ZeroDivisionError
#   - Para operación inválida: maneja ValueError
#   - Para tipos incorrectos: maneja TypeError
#   - Retorna:
#     Éxito: {"resultado": float, "error": None}
#     Fallo: {"resultado": None, "error": str, "tipo_error": str}
#   - Implementa un sistema de "logging" simple:
#     Guarda cada operación en una lista global: operaciones_log
#     Formato: {"operacion": str, "a": float, "b": float, "resultado": float | None, "error": str | None}

# Crea función obtener_estadisticas_operaciones() -> dict:
#   - Analiza operaciones_log
#   - Retorna: {
#       "total_operaciones": int,
#       "exitosas": int,
#       "fallidas": int,
#       "errores_por_tipo": dict  # {"ZeroDivisionError": 3, "ValueError": 2}
#     }
def calculate_operation(a: float, b: float, operacion: str) -> dict:
    opers = ["suma", "resta", "multiplicacion", "division"]
    operaciones_log = []
    try:
        try:
            if operacion == opers[0]:
                result = a + b
        except TypeError as error:
            raise TypeError(f"I dont acept this value")
        operaciones_log["operacion" : operacion, "a" : a, "b" : b, "resultado" : result, "error" : error]
        
        try:
            if operacion == opers[1]:
                result = a - b
        except TypeError as error:
            raise TypeError(f"I dont acept this value")
        operaciones_log["operacion" : operacion, "a" : a, "b" : b, "resultado" : result, "error" : error]
        
        try:
            if operacion == opers[2]:
                result = a * b
        except TypeError as error:
            raise TypeError(f"I dont acept this value")
        operaciones_log["operacion" : operacion, "a" : a, "b" : b, "resultado" : result, "error" : error]
        
        try:
            if operacion == opers[3]:
                result = a / b
        except ZeroDivisionError as error:
            raise ZeroDivisionError("You cant divide 0")
        operaciones_log["operacion" : operacion, "a" : a, "b" : b, "resultado" : result, "error" : error]
    except TypeError:
        raise TypeError({"resultado": None, "error": error, "tipo_error": TypeError})
    
    return {
        "operations" : operacion,
        "succesfuly" : result,
        "fails" : error,
        "type" : error
    }
print(calculate_operation(52, 6, "suma"))
print(calculate_operation(52, 6, "resta"))
print(calculate_operation(52, 6, "multiplicacion"))
print(calculate_operation(52, 6, "division"))
# Casos de prueba:
# calcular_operacion(10, 5, "suma") → {"resultado": 15.0, "error": None}
# calcular_operacion(10, 0, "division") → {"resultado": None, "error": "...", "tipo_error": "ZeroDivisionError"}
# calcular_operacion(10, 5, "potencia") → error de operación inválida
# calcular_operacion("10", 5, "suma") → TypeError



# Ejercicio 4: Procesador de Archivo CSV Robusto
# Contexto: Sistema que lee y procesa datos de ventas desde texto CSV simulado.
# Requisitos:
# Simula contenido CSV como string:
# csv_data = """producto,cantidad,precio
# Laptop,2,1200.50
# Mouse,5,25.00
# Teclado,abc,75.00
# Monitor,3,invalid
# """

# Crea función parsear_linea_csv(linea: str, numero_linea: int) -> dict | None:
#   - Separa por comas
#   - Convierte cantidad a int, precio a float
#   - Si hay error de conversión:
#     * Imprime advertencia: "⚠️ Línea {numero_linea}: error de conversión - {detalle}"
#     * Retorna None (no detiene el proceso)
#   - Si es válida: retorna {"producto": str, "cantidad": int, "precio": float}

# Crea función procesar_csv(csv_contenido: str) -> dict:
#   - Divide en líneas
#   - Ignora primera línea (headers)
#   - Procesa cada línea con parsear_linea_csv()
#   - Retorna: {
#       "productos_validos": list[dict],
#       "lineas_procesadas": int,
#       "lineas_validas": int,
#       "lineas_con_error": int,
#       "total_vendido": float  # suma de (cantidad * precio) de productos válidos
#     }

# El programa debe procesar TODAS las líneas, incluso si algunas fallan
def Csv_linear(line: str, num_line: int,) ->dict:
    parts = line.split(",")
    product = parts[0]
    amount_str = parts[1]
    price_str = parts[2]
    try:
        amount = int(amount_str)
        price = float(price_str)
    except (TypeError, ValueError) as error:
        raise ValueError(f"Error de conversion en la linea: {error}")
    return {
        "Product": product,
        "Amount": amount,
        "Price": price
    }
    
def process(content: str) -> dict:
    # Dividir por saltos de línea y ignorar la primera linea
    lines = content.splitlines()
    data = lines[1:]
    
    valid_products = []
    lines_process = 0
    Valid_lines = 0
    lines_with_errors = 0
    total = 0.0
    for index, line in enumerate(data, start=2):
        lines_process += 1
        try:
            result = Csv_linear(line, index)
            valid_products.append(result)
            Valid_lines += 1
            total += result["Amount"] * result["Price"]
        except ValueError:
            lines_with_errors += 1
    return {
        "Valid Products" : valid_products,
        "Lines process" : lines_process,
        "valid lines" : Valid_lines,
        "Error lines" : lines_with_errors,
        "Total" : total
    }

csv_data = """Product,Amount,Price
Laptop,2,1200.50
Mouse,5,25.00
Teclado,abc,75.00
Monitor,3,invalid
"""
print(process(csv_data))

# Ejercicio 5: Sistema de Autenticación con Manejo Completo de Errores (Integrador)
# Contexto: Sistema de login que debe ser robusto y seguro.
# Requisitos:
# Define excepciones personalizadas:
#   class CredencialesInvalidasError(Exception):
#       pass
#   
#   class UsuarioBloqueadoError(Exception):
#       pass
#   
#   class UsuarioNoEncontradoError(Exception):
#       pass

# Base de datos simulada:
# usuarios_db = [
#     {"username": "admin", "password": "Admin123!", "fail_intents": 0, "bloqueado": False},
#     {"username": "user1", "password": "User123!", "fail_intents": 2, "bloqueado": False},
#     {"username": "blocked_user", "password": "Pass123!", "fail_intents": 3, "bloqueado": True},
# ]

# Crea estas funciones:
#   1. buscar_usuario(username: str) -> dict:
#      - Busca en usuarios_db
#      - Lanza UsuarioNoEncontradoError si no existe
#      
#   2. verificar_password(usuario: dict, password: str) -> bool:
#      - Verifica si password coincide
#      - Lanza CredencialesInvalidasError si no coincide
#      
#   3. verificar_estado_cuenta(usuario: dict) -> bool:
#      - Verifica si fail_intents < 3 y no está bloqueado
#      - Lanza UsuarioBloqueadoError si está bloqueado
#      
#   4. autenticar_usuario(username: str, password: str) -> dict:
#      - Usa las 3 funciones anteriores en orden
#      - Si autenticación exitosa:
#        * Resetea fail_intents a 0
#        * Retorna: {"autenticado": True, "usuario": username, "mensaje": "Login exitoso"}
#      - Si falla:
#        * Incrementa fail_intents
#        * Si fail_intents >= 3: bloquea cuenta (bloqueado = True)
#        * Retorna: {"autenticado": False, "error": str, "intentos_restantes": int}
#      - Maneja TODAS las excepciones personalizadas
#      - NUNCA debe crashear el programa

# Crea función intentar_login_multiple(intentos: list[dict]) -> dict:
#   - Recibe lista de intentos: [{"username": str, "password": str}, ...]
#   - Intenta autenticar cada uno
#   - Retorna estadísticas: {
#       "total_intentos": int,
#       "exitosos": int,
#       "fallidos": int,
#       "usuarios_bloqueados": list[str]
#     }

def find_user(username: str) -> dict:
    users_db = [
        {"username": "admin", "password": "Admin123!", "fail_intents": 0, "blocked": False},
        {"username": "user1", "password": "User123!", "fail_intents": 2, "blocked": False},
        {"username": "blocked_user", "password": "Pass123!", "fail_intents": 3, "blocked": True},
    ]
    for user in users_db:
        if user["username"] == username:
            return user
    raise ErrorUserNotFound(f"User '{username}' not found")

def verify_password(user: dict, password: str) -> bool:
    if user["password"] != password:
        raise ErrorWithCredencials("Wrong password")
    return True
def verify_account_status(user: dict) -> bool:
    if user["blocked"] or user["fail_intents"] >= 3:
        raise ErrorUserBlocked(f"User '{user['username']}' is blocked")
    return True
def authenticate_user(username: str, password: str) -> dict:
    try:
        user = find_user(username)
        verify_account_status(user)
        verify_password(user, password)
        user["fail_intents"] = 0
        return {"autenticate": True, "user": username, "message": "Successful login"}
    except ErrorUserNotFound as e:
        return {"autenticate": False, "error": str(e), "remaining attempts": 0}
    except ErrorUserBlocked as e:
        return {"autenticate": False, "error": str(e), "remaining attempts": 0}
    except ErrorWithCredencials as e:
        user["fail_intents"] += 1
        if user["fail_intents"] >= 3:
            user["blocked"] = True
        intentos_restantes = max(0, 3 - user["fail_intents"])
        return {"autenticate": False, "error": str(e), "remaining attempts": intentos_restantes}
def try_multiple_logins(attempts: list[dict]) -> dict:
    total_intentos = len(attempts)
    exitosos = 0
    fallidos = 0
    usuarios_bloqueados = []
    
    for intento in attempts:
        resultado = authenticate_user(intento["username"], intento["password"])
        if resultado["autenticate"]:
            exitosos += 1
        else:
            fallidos += 1
            if "blocked" in resultado["error"].lower():
                usuarios_bloqueados.append(intento["username"])
    
    return {
        "total Intents": total_intentos,
        "Sucessfuly": exitosos,
        "fails": fallidos,
        "Blocked users": usuarios_bloqueados
    }
class ErrorWithCredencials(Exception):
    pass
class ErrorUserBlocked(Exception):
    pass
class ErrorUserNotFound(Exception):
    pass

data = [
    {"username": "admin2", "password": "Admin123!"},
    {"username": "admin", "password": "wrongpass"},
    {"username": "user1", "password": "wrongpass"},
    {"username": "blocked_user", "password": "Pass123!"},
    {"username": "noexiste", "password": "pass"},
]
print(try_multiple_logins(data))
# Casos de prueba:
# autenticar_usuario("admin", "Admin123!") → éxito
# autenticar_usuario("admin", "wrongpass") → fallo, incrementa intentos
# autenticar_usuario("user1", "wrongpass") → fallo, BLOQUEA (ya tenía 2 intentos)
# autenticar_usuario("blocked_user", "Pass123!") → UsuarioBloqueadoError
# autenticar_usuario("noexiste", "pass") → UsuarioNoEncontradoError



# 📖 Ejercicios de Lectura de Código

# Ejercicio 6: Identificación de Malas Prácticas en Manejo de Errores
# Analiza este código e identifica todos los problemas:

# Problema 1: Captura genérica
def procesar_datos(datos):
    try:
        resultado = int(datos) * 2
        return resultado
    except:  # ¿Qué problemas tiene esto? es una captura generica no especifica que tipo de error tendria.
        pass

# Problema 2: No propaga errores críticos
def guardar_archivo(contenido, ruta):
    try:
        archivo = open(ruta, 'w')
        archivo.write(contenido)
        archivo.close()
    except Exception as e:
        print(f"Error: {e}")
        return True  # ¿Debería retornar True si falló? en vez de usar return se usa raise para propagar el error, y no deberia retornar true si no que el error.

# Problema 3: Try/except para control de flujo
def verificar_existencia(items, item_buscar):
    try:
        index = items.index(item_buscar)
        return True
    except ValueError:
        return False  # ¿Hay mejor forma? si, usar "if item_buscar in items: return True else: return False".

# Problema 4: No usa finally para limpieza
def leer_y_procesar(archivo):
    f = open(archivo, 'r')
    try:
        datos = f.read()
        return datos.upper()
    except FileNotFoundError:
        return None
    # ¿Qué pasa con f si hay error? la lectura del archivo puede fallar y quedaria abierta, deberia cerrarse en un finally.

# Problema 5: Mensaje de error poco útil
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Error")  # No se esta usando una buena practica que es el mensaje descriptivo para el error.

# Preguntas:
# ¿Por qué nunca debes usar except: sin especificar excepción? porque atrapa demasiado y oculta los erroes, si se ocupa algo mas generico se usa except Exception, aunque no es recomendable.

# ¿Cuándo es apropiado capturar Exception genérico? cuando se quiere capturar cualquier error, aunque no es recomendable... tambien se usa a la hora de crear manejo de errores personalizados.

# ¿Qué pasa si no cierras recursos en caso de error? Puede generer un gasto de recursos innecesarios y posibles fugas de memoria.

# ¿Cómo escribirías mensajes de error útiles? Describiendo claramente qué salió mal y, si es posible la solucion.



# Ejercicio 7: Refactorización de Código sin Manejo de Errores
# Refactoriza agregando manejo robusto de errores:
# Refactoriza cada función:
# - Identifica qué puede fallar
# - Agrega try/except apropiados
# - Valida inputs
# - Lanza excepciones con mensajes claros
# - Usa type hints
# - Agrega docstrings con sección Raises

def calcular_promedio_edad(usuarios):
    """Calcula promedio de edad de usuarios."""
    total = 0
    for usuario in usuarios:
        edad = int(usuario["edad"])  # ¿Qué puede fallar? aqui puede fallar si la edad no es un numero o no esta presente en el diccionario.
        total += edad
    
    promedio = total / len(usuarios)  # ¿Y aquí? aqui puede fallar si la lista de usuarios esta vacia.
    return promedio
## corrected version
def calcular_promedio_edad(usuarios: list[dict]) -> float:
    """Calcula promedio de edad de usuarios.
    
    Args:
        usuarios: Lista de diccionarios con clave "edad"
        
    Returns:
        Promedio de edades como float
        
    Raises:
        ValueError: Si edad no es convertible a int
        ZeroDivisionError: Si la lista de usuarios está vacía
        KeyError: Si falta la clave "edad" en algún usuario
    """
    if not usuarios:
        raise ZeroDivisionError("La lista de usuarios está vacía")
    
    total = 0
    for usuario in usuarios:
        try:
            edad = int(usuario["edad"])
        except KeyError:
            raise KeyError("Falta la clave 'edad' en algún usuario")
        except ValueError:
            raise ValueError(f"Edad inválida para el usuario: {usuario}")
        total += edad
    
    promedio = total / len(usuarios)
    return promedio


def actualizar_precio(productos, producto_id, nuevo_precio):
    """Actualiza precio de producto."""
    for producto in productos:
        if producto["id"] == producto_id:
            producto["precio"] = float(nuevo_precio)  # ¿Y esto? aqui puede fallar si el nuevo_precio no es un numero.
            return True
    return False

## corrected version
def actualizar_precio(productos: list[dict], producto_id: int, nuevo_precio: float) -> bool:
    """Actualiza precio de producto.
    
    Args:
        productos: Lista de diccionarios con claves "id" y "precio"
        producto_id: ID del producto a actualizar
        nuevo_precio: Nuevo precio a asignar
        
    Returns:
        True si se actualizó, False si no se encontró el producto
        
    Raises:
        ValueError: Si nuevo_precio no es convertible a float
    """
    try:
        nuevo_precio_float = float(nuevo_precio)
    except ValueError:
        raise ValueError(f"Precio inválido: {nuevo_precio}")
    
    for producto in productos:
        if producto["id"] == producto_id:
            producto["precio"] = nuevo_precio_float
            return True
    return False


# 🧪 Evaluación Teórica

# Pregunta 1
# Explica la diferencia entre try/except/else/finally. Da un ejemplo de cuándo usarías cada parte.
# ¿Por qué es importante finally para manejo de recursos (archivos, conexiones DB)?
# try: se usa para envolver el código que puede generar una excepción.
# except: se usa para manejar la excepción si ocurre.
# else: se usa para código que solo debe ejecutarse si no hubo error en el try.
# finally: se usa para código que siempre debe ejecutarse, independientemente de si hubo error(sirve para limpiar recursos y si evitar un uso innecesario).
# ejemplo:
# try:
#     archivo = open("data.txt", "r")
#     datos = archivo.read()
# except FileNotFoundError:
#     print("Archivo no encontrado")
# else:
#     print("Archivo leído exitosamente")
# finally:
#     archivo.close()  # Siempre cierra el archivo

# Pregunta 2
# ¿Cuál es la diferencia entre capturar excepciones específicas (ValueError) vs genéricas (Exception)?
# ¿Cuándo es aceptable usar except Exception? Da ejemplos de cada caso.
# Capturar excepciones específicas permite manejar errores de manera más precisa y entender qué salió mal. 
# Capturar genéricas puede ocultar errores inesperados y dificultar la depuración.
# Es aceptable usar except Exception en casos donde se desea capturar cualquier error para evitar que el programa crashee,
# como en un servidor web que debe seguir funcionando a pesar de errores en solicitudes individuales.


# Pregunta 3
# Explica qué son las excepciones personalizadas y cuándo deberías crearlas.
# ¿Cómo ayudan a hacer el código más legible y mantenible? Da un ejemplo del mundo real.
# Las excepciones personalizadas son clases que heredan de la clase base Exception y representan errores específicos de una aplicación.
# Deberías crearlas cuando los errores estándar no describen adecuadamente el problema en tu contexto.
# ejemplo Error: UserNotFoundError para indicar que un usuario no existe en un sistema de autenticación.
# Ayudan a hacer el código más legible y mantenible al proporcionar mensajes de error claros.



# Reflexión personal:
# ¿Qué fue lo más difícil?
# El manejo de else y finaly

# ¿Entendiste cuándo usar cada tipo de excepción?
# si lo entrendi muy bien 

# ¿Cuánto tiempo real te tomó?
# mas de 4 horas 

# ¿Qué concepto necesitas repasar?
# cuando usar else



# 🎯 Objetivo de mañana (Día 6): Programación Orientada a Objetos (POO) - Clases, objetos, herencia
