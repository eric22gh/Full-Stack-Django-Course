# 🚀 DÍA 4 - Módulo 0: Funciones, Scope y Modularización

# 📚 Teoría Concisa 

# Funciones en Python: on bloques de código reutilizables que realizan una tarea específica.

# Definición de funciones:
# def nombre_funcion(parametros):
#     """Docstring: describe qué hace la función"""
#     # código
#     return valor

# Tipos de argumentos:
# Posicionales: def suma(a, b)
# Por defecto: def saludo(nombre, mensaje="Hola")
# Keyword arguments: funcion(param=valor)
# *args: permite pasar un número variable de argumentos posicionales a una función. → Se reciben como una tupla.
# Nota: para cuando no sabes cuántos valores simples te van a pasa

# **kwargs: permite pasar un número variable de argumentos con nombre (keyword arguments). → Se reciben como un diccionario.
# para cuando no sabes cuántos pares clave=valor te van a pasar.

def ejemplo_args(*args):
    print("args como tupla:", args)
ejemplo_args(1, 2, 3)
# salida: args como tupla: (1, 2, 3), ejemplo recive varios datos y los devuelve como una tupla.


def ejemplo_kwargs(**kwargs):
    print("kwargs como diccionario:", kwargs)

ejemplo_kwargs(nombre="Eric", edad=25, ciudad="San José")
# salida: kwargs como diccionario: {'nombre': 'Eric', 'edad': 25, 'ciudad': 'San José'}, recive datos con clave : valor y los devuelve como diccionario.


# Nota: muchas veces se usan juntos en funciones para máxima flexibilidad
def combinado(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

combinado(10, 20, nombre="Eric", hobby="Python")
# args: (10, 20)
# kwargs: {'nombre': 'Eric', 'hobby': 'Python'}

# Scope (Alcance de variables):
# Local: variables dentro de una función
# Global: variables fuera de funciones
# Nonlocal: en funciones anidadas
# Built-in: funciones predefinidas de Python

# Return vs Print:
# return: devuelve un valor que puede ser usado
# print: solo muestra en consola, no devuelve nada útil

# Buenas prácticas:
# Una función debe hacer UNA cosa y hacerla bien (Single Responsibility)
# Nombres descriptivos en verbos: calculate_total(), validate_email()
# Usa docstrings para documentar (Google Style o NumPy Style)
# Evita funciones largas (máximo 20-30 líneas)
# Evita efectos secundarios (modificar variables globales)
# Prefiere return sobre modificar parámetros mutables
# Usa type hints para claridad: def suma(a: int, b: int) -> int: ponerle el tipo a las variable en la funcion

# Errores comunes:
# Confundir print con return
# Modificar listas/diccionarios pasados como argumentos (mutabilidad)
# Usar valores mutables como defaults: def func(lista=[])  # ❌ PELIGROSO
# No retornar nada cuando se espera un valor
# Shadowing (usar mismo nombre para variable local y global)

# Ejemplo práctico - Función bien estructurada:

# ❌ Mal - función hace demasiadas cosas
def procesar_usuario(nombre, edad, email):
    print(f"Usuario: {nombre}")
    if edad < 18:
        print("Menor de edad")
        return False
    if "@" not in email:
        print("Email inválido")
        return False
    print("Usuario válido")
    return True

# ✅ Bien - funciones específicas con responsabilidad única
def es_mayor_edad(edad: int) -> bool:
    """Verifica si la edad es mayor o igual a 18."""
    return edad >= 18

def es_email_valido(email: str) -> bool:
    """Valida formato básico de email."""
    return "@" in email and "." in email

def validar_usuario(nombre: str, edad: int, email: str) -> dict:
    """
    Valida datos de usuario y retorna resultado.
    
    Nums:
        nombre: Nombre completo del usuario
        edad: Edad en años
        email: Correo electrónico
        
    Returns:
        dict: {"valido": bool, "errores": list}
    """
    errores = []
    
    if not es_mayor_edad(edad):
        errores.append("Debe ser mayor de edad")
    
    if not es_email_valido(email):
        errores.append("Email inválido")
    
    return {
        "valido": len(errores) == 0,
        "errores": errores
    }

# Ejemplo - Scope:
contador = 0  # Global

def incrementar():
    global contador  # Necesario para modificar global
    contador += 1
    return contador

# Documentación oficial: https://docs.python.org/3/tutorial/controlflow.html#defining-functions

# 💻 Ejercicios Acumulativos

# Ejercicio 1: Sistema de Cálculo de Descuentos Modular
# Contexto: Refactorizar lógica de descuentos en funciones reutilizables.
# Requisitos:
# Crea estas funciones:
#   1. calcular_descuento_membresia(subtotal: float, es_premium: bool) -> float
#      - Premium: 15% descuento
#      - No premium: 0%
#   
#   2. calcular_descuento_volumen(subtotal: float) -> float
#      - subtotal > $1000: 12%
#      - subtotal > $500: 10%
#      - Menor: 0%
#   
#   3. aplicar_mejor_descuento(subtotal: float, es_premium: bool) -> dict
#      - Calcula ambos descuentos
#      - Aplica el MAYOR descuento (no acumulables)
#      - Retorna: {"subtotal": float, "descuento_aplicado": str, "monto_descuento": float, "total": float}
#
# Usa type hints en todas las funciones
# Incluye docstrings estilo Google
# Casos de prueba:
# aplicar_mejor_descuento(600, True) → descuento premium 15%, aplicar_mejor_descuento(600, False) → descuento volumen 10%, aplicar_mejor_descuento(1200, False) → descuento volumen 12%
def Calculate_Membership_Discount(subtotal: float, is_premium: bool) -> float: # el valor que debe retornar es float
    if is_premium:
        """Valida si premium es true, asi ahce una serie de calculos"""
        apply = "15%"
        discount = subtotal * 0.15
        total = subtotal - discount
        return f"Subtotal: {subtotal}, Descuento premium: {apply}%, Monto de descuento: {discount}, para un total de : {total}"
    
def Calculate_Volume_Discount(subtotal: float) -> float:
    if subtotal > 1000.0:
        """Valida si subtotal es mayor a 10000, si es asi hace una serie de calculos"""
        apply = "12%"
        discount = subtotal * 0.12
        total = subtotal - discount
        return f"Subtotal: {subtotal}, Descuento volumen: {apply}%, Monto de descuento: {discount}, para un total de : {total}"
    elif subtotal > 500.0:
        """Valida si subtotal es mayor a 500, si es asi hace una serie de calculos"""
        apply = "10%"
        discount = subtotal * 0.10
        total = subtotal - discount
        return f"Subtotal: {subtotal}, Descuento volumen: {apply}%, Monto de descuento: {discount}, para un total de : {total}"
    else:
        return "Descuento volumen: 0%"
    
def Apply_Best_Discount(subtotal: float, is_premium: bool, apply: str, discount: float) -> dict:
    if discount > 0.15:
        total = subtotal * discount
        total_final =  subtotal - total
        return f"Subtotal: {subtotal}, applicion del mejor descuento: {apply}%, Monto de descuento: {discount}, para un total de : {total_final}"
        
print(Calculate_Membership_Discount(10000.0, True))
print(Calculate_Volume_Discount(500.0))
print(Apply_Best_Discount(5000.0, False, "35", 0.35))

# Ejercicio 2: Validadores de Datos Reutilizables
# Contexto: Sistema de validación para formularios de registro.
# Requisitos:
# Crea funciones de validación independientes:
#   1. validar_username(username: str) -> tuple[bool, str]
#      - Largo entre 4-20 caracteres
#      - Solo letras, números y guión bajo
#      - Retorna: (es_valido, mensaje_error)
#   
#   2. validar_password(password: str) -> tuple[bool, str]
#      - Mínimo 8 caracteres
#      - Al menos una mayúscula
#      - Al menos un número
#      - Retorna: (es_valido, mensaje_error)
#   
#   3. validar_email(email: str) -> tuple[bool, str]
#      - Contiene @ y .
#      - @ no está al inicio ni al final
#      - Retorna: (es_valido, mensaje_error)
#   
#   4. validar_edad(edad: int) -> tuple[bool, str]
#      - Entre 18 y 50
#      - Retorna: (es_valido, mensaje_error)
#   
#   5. validar_registro_completo(username: str, password: str, email: str, edad: int) -> dict
#      - Usa todas las funciones anteriores
#      - Retorna: {"valido": bool, "errores": list}

# Casos de prueba:
# validar_username("ab") → (False, "Username debe tener entre 4-20 caracteres")
# validar_password("pass") → (False, "Password debe tener al menos 8 caracteres")
# validar_registro_completo("john_doe", "SecurePass123", "john@email.com", 25) → {"valido": True, "errores": []}
def Username_validation(username: str) -> tuple[bool, str]:
    is_valid = False
    if len(username) > 4 and len(username) < 20:
        for name in username:
            if not (name.isalnum() or name == "_"):
                is_valid=True
                return(is_valid, "the username is valid")
    return(is_valid, "Username error")
    
def Password_Validation(userpassword:str) -> tuple[bool, str]:
    import string
    Data = list(string.ascii_uppercase)
    is_valid = False
    if len(userpassword) >= 8:
        for letters in userpassword:
            if (letters.isalnum() or letters in Data):
                is_valid=True
                return(is_valid, "the password is valid")
    return(is_valid, "Password error")
    
def Validate_email(email: str)  -> tuple[bool, str]:
    is_valid = False
    if "@" in email and "." in email: 
        if not email.startswith("@") and not email.endswith("@"):
            is_valid=True
            return(is_valid, "the email is valid ")
    return(is_valid, "Email error")
    
def Validate_Age(age:int) -> tuple[bool, str]:
    is_valid = False
    if age > 18 and age < 50:
        is_valid=True
        return(is_valid, "The age is valid ")
    return(is_valid, "Age error")

def Complete_Validate(username: str, userpassword: str, email: str, age: int):
    erorrs = []
    if not Username_validation(username)[0]:
        erorrs.append("Username error")
    if not Password_Validation(userpassword)[0]:
        erorrs.append("Password error")
    if not Validate_email(email)[0]:
        erorrs.append("Email error")
    if not Validate_Age(age)[0]:
        erorrs.append("Age error")
    
    # is_valid = False
    if len(erorrs) == 0:
        is_valid = True
        return {
            "Is Valid" : is_valid,
            "Erorrs" : []
        }
    else:
        is_valid = False
        return {
            "Is Valid" : is_valid,
            "Erorrs" : erorrs
        }
print(Username_validation("ab"))
print(Password_Validation("pass"))
print(Validate_email("john@email.com"))
print(Validate_Age(42))
print(Complete_Validate("john damer doe", "SecurePass123", "johnemail.com", 5))

                   
# Ejercicio 3: Calculadora de Estadísticas con Funciones
# Contexto: Librería de funciones estadísticas para análisis de datos.
# Requisitos:
# Crea funciones estadísticas:
#   1. calcular_promedio(numeros: list[float]) -> float
#      - Retorna el promedio de la lista
#      - Maneja lista vacía retornando 0.0
#   
#   2. encontrar_maximo(numeros: list[float]) -> float
#      - Retorna el valor máximo
#      - Maneja lista vacía retornando None
#   
#   3. encontrar_minimo(numeros: list[float]) -> float
#      - Retorna el valor mínimo
#      - Maneja lista vacía retornando None
#   
#   4. calcular_rango(numeros: list[float]) -> float
#      - Retorna diferencia entre max y min
#   
#   5. analizar_lista(numeros: list[float]) -> dict
#      - Usa todas las funciones anteriores
#      - Retorna: {"promedio": float, "maximo": float, "minimo": float, "rango": float}
# NO uses las funciones built-in sum(), max(), min() - impleméntalas tú mismo con bucles
def Averague(args):
    count = 0
    amount = len(args)
    if not isinstance(args, tuple):
        return "I only accept a tuple"
    # elif not all(isinstance(num, int) for num in args):
    #     return "All the numbers in the list must be int"
    else:
        if amount == 0:
            return 0.0
        for num in args:
            count += num
        Averague_result = count / amount
        return f"The averague of the tuple is: {Averague_result:.2f}"

def Find_Bigger(args: tuple[int]):
    Bigger = 0
    amount = len(args)
    if not isinstance(args, tuple):
        return "I only accept a float"
    # elif not all(isinstance(num, int) for num in args):
    #     return "All the numbers in the tuple must be int"
    else:
        if amount == 0:
            return None
        for num in args:
            if num > Bigger:
                Bigger = num
        return Bigger
    
def Find_Smaller(args: tuple[int])  -> float:
    Smaller = args[0]
    amount = len(args)
    if not isinstance(args, tuple):
        return "I only accept a tuple"
    # elif not all(isinstance(num, int) for num in args):
    #     return "All the numbers in the tuple must be int"
    else:
        if amount == 0.0:
            return None
        for num in args:
            if num < Smaller:
                Smaller = num
        return Smaller
    
def Calculate_Range(args: tuple[int]):
    min_max = []
    Bigger = Find_Bigger(args)
    if Bigger:
        min_max.append(Bigger)
    
    Smaller = Find_Smaller(args)
    if Smaller:
        min_max.append(Smaller)
    
    if len(min_max) == 2:
        result = Bigger - Smaller
        return f"The range between the bigger and small number is: {result}"
    return 0.0

def Analist(args: tuple[int]):
    resume = {}
    if Averague(args):
        resume["Average"] = Averague(args)
    if Find_Bigger(args):
        resume["Bigger"] = Find_Bigger(args)
    if Find_Smaller(args):
        resume["Smaller"] = Find_Smaller(args)
    if Calculate_Range(args):
        resume["Amount"] = Calculate_Range(args)
    return resume

print(Averague((10, 2, 100, 52, 1)))
print(Find_Bigger((10, 2, 100, 52, 1)))
print(Find_Smaller((10, 2, 100, 52, 1)))
print(Calculate_Range((10, 2, 100, 52, 1)))
print(Analist((10, 2, 100, 52, )))

# Ejercicio 4: Sistema de Procesamiento de Inventario Modular
# Contexto: Funciones para procesar y analizar inventario de productos.
# Requisitos:
# Crea funciones para trabajar con lista de productos (dict):
#   1. filtrar_por_stock_bajo(productos: list[dict], stock_minimo: int = 10) -> list[dict]
#      - Retorna productos con stock < stock_minimo
#   
#   2. calcular_valor_inventario(productos: list[dict]) -> float
#      - Suma (precio * stock) de todos los productos
#   
#   3. buscar_producto_por_id(productos: list[dict], producto_id: int) -> dict | None
#      - Retorna producto si existe, None si no
#   
#   4. actualizar_stock(productos: list[dict], producto_id: int, cantidad: int) -> bool
#      - Actualiza stock del producto (suma cantidad al stock actual)
#      - Retorna True si actualizó, False si no encontró producto
#      - IMPORTANTE: Modifica la lista original
#   
#   5. generar_reporte_inventario(productos: list[dict]) -> dict
#      - Retorna: {
#          "total_productos": int,
#          "valor_total": float,
#          "productos_criticos": list,
#          "producto_mas_caro": dict
#        }

# Datos de prueba:
inventario = [
    {"id": 1, "nombre": "Laptop", "precio": 1200.00, "stock": 5},
    {"id": 2, "nombre": "Mouse", "precio": 25.00, "stock": 0},
    {"id": 3, "nombre": "Teclado", "precio": 7500.00, "stock": 15},
    {"id": 4, "nombre": "Monitor", "precio": 300.00, "stock": 3},
]

def Filter_Low_Stock(products: list[dict], min_stock: int = 10) -> list[dict]: # le estamos dando el valor a min_stock
    low_stock_products = []
    for product in products:
        if product["stock"] < min_stock:
            low_stock_products.append(product)
    return low_stock_products

def Calculate_Inventory_Value(products: list[dict]) -> float:
    total_value = 0.0
    for product in products:
        total_value += product["precio"] * product["stock"]
    return total_value

def Find_Product_By_ID(products: list[dict], product_id: int) -> dict:
    for product in products:
        if product["id"] == product_id:
            return product
    return "The product was not found in the inventory"

def Update_Stock(products: list[dict], product_id: int, quantity: int) -> bool:
    for product in products:
        if product["id"] == product_id:
            product["stock"] += quantity
            return True
    return False

def Generate_Inventory_Report(products: list[dict]) -> dict:
    total_products = len(products)
    total_value = Calculate_Inventory_Value(products)
    critical_products = Filter_Low_Stock(products)
    for product in products:
        expensive_product = products[0]
        if product["precio"] > expensive_product["precio"]:
            expensive_product = product
    most_expensive_product = expensive_product
    
    return {
        "total_productos": total_products,
        "valor_total": total_value,
        "productos_criticos": critical_products,
        "producto_mas_caro": most_expensive_product
    }
print(Filter_Low_Stock(inventario))
print(Calculate_Inventory_Value(inventario))    
print(Find_Product_By_ID(inventario, 3))
print(Update_Stock(inventario, 2, 10))
print(Generate_Inventory_Report(inventario))


# Ejercicio 5: Sistema de Cálculo de Impuestos Multi-región (Integrador)
# Contexto: Sistema complejo de cálculo de impuestos con múltiples reglas.
# Requisitos:
# Crea un sistema modular con estas funciones:
#   1. obtener_tasa_iva(pais: str) -> float
#      - Retorna tasa de IVA según país
#      - USA: 0.08, México: 0.16, España: 0.21, Default: 0.10
#   
#   2. calcular_iva(subtotal: float, pais: str) -> float
#      - Usa obtener_tasa_iva()
#      - Retorna monto de IVA
#   
#   3. obtener_tasa_propina(calidad_servicio: str) -> float
#      - "excelente": 0.20, "bueno": 0.15, "regular": 0.10, Default: 0.00
#   
#   4. calcular_propina(subtotal: float, calidad: str) -> float
#      - Usa obtener_tasa_propina()
#      - Retorna monto de propina sobre subtotal
#   
#   5. aplicar_descuento_corporativo(subtotal: float, es_corporativo: bool, cantidad_empleados: int = 0) -> float
#      - Si es_corporativo y cantidad_empleados > 50: 10% descuento
#      - Si es_corporativo y cantidad_empleados > 20: 5% descuento
#      - Retorna monto de descuento
#   
#   6. calcular_ticket_completo(
#        subtotal: float,
#        pais: str = "USA",
#        incluye_propina: bool = False,
#        calidad_servicio: str = "bueno",
#        es_corporativo: bool = False,
#        cantidad_empleados: int = 0
#      ) -> dict
#      - Usa TODAS las funciones anteriores
#      - Orden de cálculo:
#        1. Aplicar descuento corporativo al subtotal
#        2. Calcular IVA sobre subtotal después de descuento
#        3. Calcular propina sobre subtotal después de descuento (si aplica)
#      - Retorna: {
#          "subtotal_original": float,
#          "descuento_corporativo": float,
#          "subtotal_con_descuento": float,
#          "iva": float,
#          "propina": float,
#          "total": float,
#          "desglose": {
#              "pais": str,
#              "tasa_iva": float,
#              "tasa_propina": float,
#              "es_corporativo": bool
#          }
#        }

def Get_VAT_Rate(country: str) -> float:
    vat_rates = {
        "USA": 0.08,
        "Mexico": 0.16,
        "Spain": 0.21
    }
    return vat_rates.get(country, 0.10) 

def Calculate_VAT(subtotal: float, country: str) -> float:
    vat_rate = Get_VAT_Rate(country) # obtenemos la tasa de iva del pais
    return subtotal * vat_rate

def Get_Tip_Rate(service_quality: str) -> float:
    tip_rates = {
        "excellent": 0.20,
        "good": 0.15,
        "regular": 0.10
    }
    return tip_rates.get(service_quality, 0.00)

def Calculate_Tip(subtotal: float, quality: str) -> float:
    tip_rate = Get_Tip_Rate(quality)
    return subtotal * tip_rate

def Apply_Corporate_Discount(subtotal: float, is_corporate: bool, employee_count: int = 0) -> float:
    if is_corporate:
        if employee_count > 50:
            return subtotal * 0.10
        elif employee_count > 20:
            return subtotal * 0.05
    return 0.0

def Calculate_Complete_Ticket(
    subtotal: float,
    country: str = "USA",
    includes_tip: bool = False,
    service_quality: str = "good",
    is_corporate: bool = False,
    employee_count: int = 20
    ) -> dict:
    discount = Apply_Corporate_Discount(subtotal, is_corporate, employee_count)
    subtotal_after_discount = subtotal - discount
    vat = Calculate_VAT(subtotal_after_discount, country)
    tip = Calculate_Tip(subtotal_after_discount, service_quality) if includes_tip else 0.0
    total = subtotal_after_discount + vat + tip
    return {
        "subtotal_original": subtotal,
        "descuento_corporativo": discount,
        "subtotal_con_descuento": subtotal_after_discount,
        "iva": vat,
        "propina": tip,
        "total": total,
        "desglose": {
            "pais": country,
            "tasa_iva": Get_VAT_Rate(country),
            "tasa_propina": Get_Tip_Rate(service_quality),
            "es_corporativo": is_corporate
        }
    }
print(Calculate_Complete_Ticket(1000.0, "Mexico", True, "excellent", True, 60))


# 📖 Ejercicios de Lectura de Código

# Ejercicio 6: Análisis de Problemas con Scope y Mutabilidad
# Identifica los problemas en este código:

# Problema 1: Variable global modificada sin declaración
total_ventas = 0

def registrar_venta(monto):
    total_ventas += monto  # ¿Qué error da esto?
    return total_ventas
# la variable monto no tiene ningun valor asi que la suma va a dar 0

# Problema 2: Default mutable (MUY PELIGROSO)
def agregar_item(item, lista=[]):
    lista.append(item)
    return lista
# es peligro darle un valor por default a una lista multable, ya que cada vez que se llama a esa funcion se va a ir acomulando cada dato.

resultado1 = agregar_item("A")  # ["A"]
resultado2 = agregar_item("B")  # ¿Qué retorna? ¿["B"] o ["A", "B"]? va a retornar ["A", "B"]

# Problema 3: Modificación inesperada de argumento
def duplicar_precios(productos):
    for producto in productos:
        producto["precio"] *= 2
    return productos

inventario_original = [{"nombre": "Laptop", "precio": 1000}]
inventario_duplicado = duplicar_precios(inventario_original)
# ¿Qué pasó con inventario_original?
# el inventario original se va a actualizar, ya que esta usandose un operador de asignacion.

# Problema 4: Función sin return
def calcular_descuento(precio, porcentaje):
    descuento = precio * porcentaje
    precio_final = precio - descuento
    print(precio_final)  # Solo imprime, no retorna

total = calcular_descuento(100, 0.15)  # ¿Qué valor tiene total?
# total no tinen ningun valor ya que print no devuelve ningun valor solo muestra en pantalla

# Preguntas:
# ¿Cómo se soluciona el problema del global?
# una de las soluciones en usando la funcion global, adentro de la funcio: global (variable)

# ¿Por qué nunca debes usar listas/dicts como defaults?
# Porque son mutables y no es una buena practica

# ¿Cómo evitar modificar el argumento original?
# Lo que podemos hacer es hacer una copia y trabajar con la copia

# ¿Cuál es la diferencia entre print y return?
# Return retornar un valor util y print solo muestra en pantalla



# Ejercicio 7: Refactorización de Función Monolítica
# Refactoriza esta función en funciones más pequeñas y específicas:

def procesar_pedido_completo(productos, cliente, direccion, metodo_pago):
    # Validar productos
    if not productos:
        return {"error": "Sin productos"}
    
def Subtotal(productos):
    subtotal = 0
    for producto in productos:
        if producto["stock"] <= 0:
            return {"error": f"Sin stock: {producto['nombre']}"}
        subtotal += producto["precio"] * producto["cantidad"]
    return subtotal

def Validar(cliente):
    # Validar cliente
    if not cliente.get("email") or "@" not in cliente["email"]:
        return {"error": "Email inválido"}
    if cliente.get("edad", 0) < 18:
        return {"error": "Menor de edad"}

def Direecion(pais):
    # Calcular envío
    direccion = {
        "USA": 0.08,
        "Mexico": 0.16,
        "Spain": 0.21
    }
    subtotal = 200
    costo_envio = 0
    if direccion.get(pais) == "USA":
        costo_envio = 10 if subtotal < 100 else 0
        return subtotal + costo_envio
    elif direccion.get(pais) == "México":
        costo_envio = 15 if subtotal < 100 else 5
        return subtotal + costo_envio
    else:
        costo_envio = 20
    
def Descuento(cliente="es_premium"):
    # Aplicar descuento
    descuento = 0
    subtotal = 200
    costo_envio = 20
    if cliente.get("es_premium"):
        descuento = subtotal * 0.15
        return descuento
    elif subtotal > 500:
        descuento = subtotal * 0.10
        return descuento

def Calcular(subtotal, descuento, costo_envio, metodo_pago):
    # Calcular total
    total = subtotal - descuento + costo_envio
    
    # Validar pago
    if metodo_pago not in ["tarjeta", "paypal", "transferencia"]:
        return {"error": "Método de pago inválido"}
    
    return {
        "subtotal": subtotal,
        "descuento": descuento,
        "envio": costo_envio,
        "total": total,
        "metodo_pago": metodo_pago
    }

print(Calcular(450, 0.12, 20, "paypal"))


# 🧪 Evaluación Teórica

# Pregunta 1
# Explica la diferencia entre parámetros posicionales, por defecto, *Nums y **kwargs.
# Da un ejemplo de cuándo usarías cada uno en una aplicación real.
# *Nums son argumentos posicionales de una funcion, se usa para cuando no sabes cuantos tipos de variables vas a recibir, el los toma y los convierte en tupla.
# **kwargs son argumentos posicionales de una funcion, recive los datos de clave-valor y los retorna como un diccionario.

# Pregunta 2
# ¿Qué es el "scope" de una variable? Explica la diferencia entre local, global y nonlocal.
# ¿Cuándo es aceptable usar variables globales y cuándo debes evitarlas?
# basicamente es cuando no se declara una variable correctamente, la variable local se puede usar en el bucle for de una funcion y que no tenga que ver con variables globales, 
# ya que estas usualmente van afuera de la funcion y esta no las detecta, pero una variable global si puede detectar una local.
# nonlocal es una variable intermedia, se puede modificar afuera y adentro de la funcion.

# Pregunta 3
# ¿Por qué usar listas o diccionarios como valores por defecto en funciones es peligroso?
# Muestra un ejemplo del problema y cómo solucionarlo correctamente.
# No es una buena practica ya que son variable mutables, una solucion segura es ponerle el valor de NONE a la lista o dict y asi ninguna llamada va acumulando elementos en la misma lista compartida.



# Reflexión personal:
# ¿Qué fue lo más difícil?
# *args y kwargs no lo entendi al 100

# ¿Entendiste scope y mutabilidad?
# si completamente

# ¿Cuánto tiempo real te tomó?
# Unas 4 horas segmentadas 

# ¿Qué concepto necesitas repasar?
# *args y kwargs


# 🎯 Objetivo de mañana (Día 5): Manejo de errores y excepciones, try/except, validación robusta
