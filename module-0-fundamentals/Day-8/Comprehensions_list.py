# 🚀 DÍA 8 - Módulo 0: List Comprehensions, Generadores y Funciones Lambda

# 📚 Teoría Concisa (20 min)

# List Comprehensions
# Forma compacta y pythonic de crear listas a partir de iterables.
# Sintaxis: [expresion for item in iterable if condicion]

# Ventajas:
# - Más legible que bucles tradicionales
# - Más rápido en ejecución
# - Código más conciso

# Funciones Lambda
# Funciones anónimas pequeñas de una sola expresión.
# Sintaxis: lambda parametros: expresion

# Generadores
# Funciones que usan yield en vez de return para generar valores bajo demanda.
# Ventajas:
# - Eficientes en memoria (no guardan toda la lista) 
# - Lazy evaluation (generan valores cuando se necesitan)

# Generator Expressions
# Similar a list comprehensions pero con paréntesis ()
# Sintaxis: (expresion for item in iterable if condicion)

# Funciones útiles con iterables:
# map(funcion, iterable): aplica función a cada elemento
# filter(funcion, iterable): filtra elementos según condición
# reduce(funcion, iterable): aplica una funcion acomulativa a cada iterable de la lista (de functools)
# zip(): combina iterables
# enumerate(): índice + valor
# sorted(): ordena con key personalizada

# Buenas prácticas:
# Usa list comprehensions para transformaciones simples
# No abuses: si tiene más de 2 líneas, usa bucle tradicional
# Lambda solo para funciones triviales (sorting, filtering)
# Generadores para procesamiento de grandes volúmenes de datos
# Nombres descriptivos incluso en lambdas si es posible

# Errores comunes:
# List comprehension demasiado complejo (difícil de leer)
# Usar lambda para funciones complejas (mejor def) ya que el es para funciones simples
# No aprovechar generadores cuando hay mucha data, son para muchos datos(yield)
# Confundir [] (lista) con () (generador)


# Ejemplo práctico - List Comprehensions:
# ❌ Mal - bucle tradicional para caso simple
numeros = [1, 2, 3, 4, 5]
cuadrados = []
for num in numeros:
    cuadrados.append(num ** 2)

# ✅ Bien - list comprehension
cuadrados = [num ** 2 for num in numeros] 
""" lista de numeros elevados a la 2 """
square = [numbers * 3 for numbers in numeros]

# Con condición
pares = [num for num in numeros if num % 2 == 0]

# Anidado (transformar múltiples listas)
matriz = [[1, 2], [3, 4], [5, 6]]
plana = [num for fila in matriz for num in fila]  # [1, 2, 3, 4, 5, 6]

# Ejemplo - Funciones Lambda:

# ❌ Mal - lambda complejo
calcular = lambda x, y: x + y if x > 0 else x - y if y > 0 else 0

# ✅ Bien - lambda simple
suma = lambda x, y: x + y

# Uso común: sorting con key
productos = [{"nombre": "Laptop", "precio": 1200}, {"nombre": "Mouse", "precio": 25}]
ordenados = sorted(productos, key=lambda p: p["precio"])

# Ejemplo - Generadores:

# Función generadora
def generar_cuadrados(n):
    """Genera cuadrados de números del 0 al n."""
    for i in range(n):
        yield i ** 2

# Uso
for cuadrado in generar_cuadrados(5):
    print(cuadrado)  # 0, 1, 4, 9, 16

# Generator expression
cuadrados_gen = (x ** 2 for x in range(1000000))  # No consume memoria hasta usar

# Ejemplo - map() y filter():

numeros = [1, 2, 3, 4, 5]

# map: transforma cada elemento
cuadrados = list(map(lambda x: x ** 2, numeros))

# filter: filtra elementos
pares = list(filter(lambda x: x % 2 == 0, numeros))

# Documentación oficial: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions


# 💻 Ejercicios Acumulativos

# Ejercicio 1: List Comprehensions Básicas
# Contexto: Procesamiento de datos de productos.
# Requisitos:
# Dada esta lista de productos:
productos = [
    {"nombre": "Laptop", "precio": 1200, "stock": 5, "categoria": "Electrónica"},
    {"nombre": "Mouse", "precio": 25, "stock": 50, "categoria": "Electrónica"},
    {"nombre": "Teclado", "precio": 75, "stock": 30, "categoria": "Electrónica"},
    {"nombre": "Silla", "precio": 150, "stock": 10, "categoria": "Muebles"},
    {"nombre": "Escritorio", "precio": 300, "stock": 8, "categoria": "Muebles"},
    {"nombre": "Lámpara", "precio": 45, "stock": 0, "categoria": "Muebles"},
]

# Usa list comprehensions para crear:
# 1. nombres_productos: lista solo con nombres
Products_name = [name["nombre"] for name in productos]
print(Products_name)
# 2. precios_mayores_100: lista de productos donde precio > 100
prices = [name["nombre"] for name in productos if name["precio"] > 100]
print(prices)
# 3. productos_sin_stock: lista de nombres de productos con stock == 0
out_stock = [name["nombre"] for name in productos if name["stock"] == 0]
print(out_stock)
# 4. valores_inventario: lista de (precio * stock) de cada producto
inventory = list(map(lambda producto: (producto["precio"] * producto["stock"]), productos))
"""Map aplica una operacio a cada iterable de la lista y lambda es una pequeña funcion que va a multiplicar los valores"""
print(inventory)
# 5. productos_descuento: lista de dicts con 20% descuento en precio
#    Formato: {"nombre": str, "precio_original": int, "precio_descuento": float}
Disccount_product = [
    {"Name": product["nombre"], "Original Price": product["precio"], "Discount price": product["precio"] * 0.20}
    for product in productos
]
print(Disccount_product)

# Ejercicio 2: Funciones Lambda con sorted() y filter()

# Contexto: Análisis y ordenamiento de datos de estudiantes.
# Requisitos:
# Dada esta lista:
estudiantes = [
    {"nombre": "Ana", "edad": 20, "promedio": 85.5, "carrera": "Ingeniería"},
    {"nombre": "Carlos", "edad": 22, "promedio": 92.0, "carrera": "Medicina"},
    {"nombre": "María", "edad": 19, "promedio": 78.5, "carrera": "Ingeniería"},
    {"nombre": "Luis", "edad": 21, "promedio": 88.0, "carrera": "Derecho"},
    {"nombre": "Sofia", "edad": 20, "promedio": 95.5, "carrera": "Medicina"},
]

# Usa lambda y funciones built-in para:
# 1. ordenar_por_promedio: sorted() por promedio descendente
averague = sorted(estudiantes, key=lambda name: name["promedio"])
print(averague)
# 2. ordenar_por_nombre: sorted() alfabéticamente por nombre
Students_name = sorted(estudiantes, key=lambda name: name["nombre"])
print(Students_name)
# 3. filtrar_aprobados: filter() estudiantes con promedio >= 80
approve_students = list(filter(lambda student : student["promedio"] > 80.0, estudiantes))
print(approve_students)
# 4. filtrar_ingenieria: filter() estudiantes de carrera "Ingeniería"
engineer_student = list(filter(lambda name : name["carrera"] == "Ingeniería", estudiantes))
print(engineer_student)
# 5. estudiante_mayor_promedio: max() el estudiante con mayor promedio
best_student = max(estudiantes, key=lambda name: name["promedio"])
print(best_student)
# 6. edad_promedio: usar map() para extraer edades y calcular promedio
averague_student = sum(map(lambda student : student["edad"], estudiantes ))
amount_student = len(estudiantes)
age_averague = averague_student / amount_student
print(f"The age avergaue of the students is: {age_averague}")

# Ejercicio 3: Generadores para Procesar Grandes Volúmenes
# Contexto: Sistema que procesa logs sin cargar todo en memoria.
# Requisitos:
# Crea estas funciones generadoras:

# 1. generar_numeros_pares(inicio: int, fin: int)
#    - Genera números pares entre inicio y fin
#    - Usa yield
def Even_numbers(start: int, end: int):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number

for even in Even_numbers(1, 20):
    print(even)

# 2. generar_fibonacci(n: int)
#    - Genera los primeros n números de Fibonacci, Ques es una secuencia donde cada número es la suma de los dos anteriores
#    - Usa yield
def fibonacci(n: int):
    a, b = 0, 1
    fib = []
    for _ in range(0, n):
        fib.append(a)
        a, b = b, a + b
    yield fib
for fibo in fibonacci(10):
    print(fibo)

# 3. procesar_transacciones(transacciones: list[dict])
#    - Recibe lista de transacciones: {"id": int, "monto": float, "tipo": str}
#    - Genera solo transacciones donde monto > 100
#    - Usa yield
def transaction(transactions : list[dict]):
    yield [data for data in transactions if data["monto"] > 100]
transacciones = [
    {"id": 1, "monto": 50, "tipo": "compra"},
    {"id": 2, "monto": 150, "tipo": "compra"},
    {"id": 3, "monto": 200, "tipo": "venta"},
]
for datas in transaction(transacciones):
    print(datas)
    
# 4. leer_lineas_grandes(texto: str)
#    - Simula lectura de archivo grande
#    - Recibe texto multi-línea
#    - Genera una línea a la vez
#    - Usa yield
def read_large_lines(text : str):
    for line in text.splitlines():
        yield line
large_text = "Línea 1: Esta es una línea de ejemplo." + "\nLínea 2: Otra línea de ejemplo." + "\nLínea 3: Última línea de ejemplo."
for line in read_large_lines(large_text):
    print(line)

# Crea función consumir_generador(generador) -> list:
#   - Consume un generador y retorna lista
#   - Imprime cada valor antes de agregarlo a la lista
def consume_generator(generator) -> list:
    result = []
    for value in generator:
        print(value)
        result.append(value)
    return result

for even in Even_numbers(1, 10):
    print(consume_generator(Even_numbers(1, 10)))


# Ejercicio 4: Combinando map(), filter() y reduce()
# Contexto: Pipeline de procesamiento de datos de ventas.
from functools import reduce # Que hace reduce: en Python es una función que aplica de manera acumulativa otra función a los elementos de un iterable (como una lista)
ventas = [
    {"producto": "Laptop", "cantidad": 2, "precio_unitario": 1200},
    {"producto": "Mouse", "cantidad": 5, "precio_unitario": 25},
    {"producto": "Teclado", "cantidad": 1, "precio_unitario": 75},
    {"producto": "Monitor", "cantidad": 2, "precio_unitario": 300},
]
# Usa map(), filter() y reduce() con lambda:
# 1. calcular_totales: map() para crear lista de (cantidad * precio_unitario)
Totals = list(map(lambda name : name["cantidad"] * name["precio_unitario"], ventas))
# 2. ventas_grandes: filter() ventas donde (cantidad * precio_unitario) > 200
Best_sold = list(filter(lambda name : name["cantidad"] * name["precio_unitario"] > 200, ventas))
# 3. suma_total: reduce() para sumar todos los totales
Totals_sum = reduce(lambda x, y : x + y, Totals)
# 4. producto_mas_caro: reduce() para encontrar producto con mayor precio_unitario
most_expensive = reduce(lambda x, y : x if x["precio_unitario"] > y["precio_unitario"] else y, ventas)
# 5. cantidad_total_items: reduce() para sumar todas las cantidades
data = list(map(lambda x : x["cantidad"], ventas))
total_items = reduce(lambda x, y : x + y, data)
# Crea función pipeline_ventas(ventas: list[dict]) -> dict:
#   - Usa las operaciones anteriores
#   - Retorna: {
#       "total_ventas": float,
#       "cantidad_items": int,
#       "producto_mas_caro": str,
#       "ventas_mayores_200": int  (cuenta cuántas)
#     }
def Sold_pipelines(ventas : list[dict]) -> dict:
    return {
        "Amount of solds" : Totals,
        "Amount of items" : total_items,
        "Most expensive product" : most_expensive,
        "Solds Bigger than 200 dolars" : Best_sold
    }
print(Sold_pipelines(ventas))


# Ejercicio 5: Sistema de Procesamiento de Datos Completo (Integrador)
# Contexto: ETL (Extract, Transform, Load) de datos de empleados.
empleados_raw = [
    "Juan Pérez,28,IT,3500,5",
    "Ana García,35,Ventas,4200,8",
    "Carlos López,42,IT,5500,12",
    "María Rodríguez,31,Marketing,3800,6",
    "Luis Martínez,29,IT,3600,4",
    "Sofia Torres,38,Ventas,4500,10",
]
# Formato: "nombre,edad,departamento,salario,años_experiencia"
# Crea estas funciones usando técnicas aprendidas:
# 1. parsear_empleado(linea: str) -> dict
#    - Convierte string a dict
#    - Usa split() y conversión de tipos
#    - Retorna: {"nombre": str, "edad": int, "departamento": str, "salario": float, "años_experiencia": int}
def parse_employee(line : str) -> dict:
    name, age, department, salary, experience = line.split(",")
    return {
        "Name": name,
        "Age": int(age),
        "Department": department,
        "Salary": float(salary),
        "Experience": int(experience)
    }

# 2. procesar_empleados(datos_raw: list[str]) -> list[dict]
#    - Usa map() con parsear_empleado
#    - Retorna lista de dicts
def process_employees(data : list[str]) -> list[dict]:
    return list(map(parse_employee, data))

# 3. filtrar_por_departamento(empleados: list[dict], dept: str) -> list[dict]
#    - Usa list comprehension
def filter_by_department(employees : list[dict], dept : str) -> list[dict]:
    return [employee for employee in employees if employee["Department"] == dept]

# 4. calcular_bono(empleado: dict) -> float
#    - Bono = salario * 0.10 * años_experiencia
#    - Usa lambda en map()
def calculate_bonus(employee : dict) -> float:
    bonus = employee["Salary"] * 0.10 * employee["Experience"]
    return bonus

# 5. generar_reporte_departamento(empleados: list[dict], dept: str)
#    - Genera información del departamento bajo demanda
#    - Función generadora que yield:
#      * Nombre de cada empleado
#      * Su salario
#      * Su bono calculado
#    - Formato: "Juan Pérez - Salario: $3500 - Bono: $1750"
def generate_department_report(employees : list[dict], dept : str):
    for employee in employees:
        if employee["Department"] == dept:
            bonus = calculate_bonus(employee)
            yield f"{employee['Name']} - Salario: ${employee['Salary']} - Bono: ${bonus}"
            
for report in process_employees(empleados_raw):
    for data in generate_department_report([report], "IT"):
        print(data)

# 6. analizar_datos_completo(datos_raw: list[str]) -> dict
#    - Pipeline completo usando todas las funciones
#    - Retorna: {
#        "total_empleados": int,
#        "departamentos": list[str],  (únicos, ordenados)
#        "salario_promedio": float,
#        "empleados_it": list[dict],
#        "top_3_salarios": list[dict],  (usa sorted con lambda)
#        "bono_total": float  (suma de todos los bonos, usa reduce)
#      }
def analyze_complete_data(data : list[str]) -> dict:
    employees = process_employees(data)
    total_employees = len(employees)
    departments = sorted(set(employee["Department"] for employee in employees))
    average_salary = sum(employee["Salary"] for employee in employees) / total_employees
    it_employees = filter_by_department(employees, "IT")
    top_3_salaries = sorted(employees, key=lambda e: e["Salary"], reverse=True)[:3]
    total_bonus = reduce(lambda acc, e: acc + calculate_bonus(e), employees, 0)

    return {
        "total_empleados": total_employees,
        "departamentos": departments,
        "salario_promedio": average_salary,
        "empleados_it": it_employees,
        "top_3_salarios": top_3_salaries,
        "bono_total": total_bonus
    }
print(analyze_complete_data(empleados_raw))


# 📖 Ejercicios de Lectura de Código

# Ejercicio 6: Análisis de List Comprehensions Complejas
# Analiza y explica qué hace cada comprehension:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. ¿Qué genera esto? 
resultado1 = [x ** 2 for x in numeros if x % 2 == 0]
# genera los numeros pares de una lista de numeros elevados al cuadrado.

# 2. ¿Y esto?
resultado2 = [x if x > 5 else x * 2 for x in numeros]
#genera una lista de numeros en donde si x es mayor a 5 se deja igual y si no se multiplica por 2.

# 3. ¿Comprehension anidado?
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado3 = [num for fila in matriz for num in fila if num % 2 != 0]
# genera los numeros impares de una lista de listas(matriz) y los devuelve en una sola lista.

# 4. ¿Dict comprehension?
resultado4 = {x: x ** 2 for x in numeros if x <= 5}
# genera un diccionario con los numeros menores o iguales a 5, en donde su clave es el numero y su valor es el numero elevado al cuadrado.

# 5. ¿Set comprehension?
palabras = ["hola", "mundo", "hola", "python", "mundo"]
resultado5 = {palabra.upper() for palabra in palabras}
# genera un set de mayuzculas y sin duplicados de una lista de palabras.  

# 6. ¿Esto es eficiente?
resultado6 = [x for x in range(1000000) if x % 2 == 0]  # ¿Lista o generador?
# No es eficiente ya que es mejor usar un generadorya que un generador no consume memoria hasta que se necesite,
# mientras que una lista consume memoria desde el inicio.

# Preguntas:
# ¿Cuál es la diferencia entre [] y () en comprehensions?
# [] se usa para list comprehensions y () se usa para generator expressions. mientras que list comprehensions usa memoria desde el inicio, 
# generator expressions consume memoria bajo demanda y es mejor para grandes datos.

# ¿Cuándo una list comprehension se vuelve demasiado compleja?
# Una list comprehension se vuelve demasiado compleja cuando tiene más de 2 líneas o cuando la lógica dentro de la expresión es difícil de entender.
# cuando sucede esto es mejor usar un bucle tradicional.

# ¿Cómo reescribirías la #3 con bucles tradicionales?
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def traditional(data : list[list]) -> list:
    new_data = []
    for fila in data:
        for num in fila:
            if num % 2 != 0:
                new_data.append(num)
    return new_data
                
# Ejercicio 7: Refactorización de Código con Técnicas Modernas
# Refactoriza este código usando list comprehensions, lambda y generadores:
# Código 1: Usar list comprehension
productos = [
    {"nombre": "Laptop", "precio": 1200},
    {"nombre": "Mouse", "precio": 25},
    {"nombre": "Teclado", "precio": 75},
]

precios_con_iva = []
for producto in productos:
    precio_con_iva = producto["precio"] * 1.21
    precios_con_iva.append(precio_con_iva)

""" codigo refactorizado """
price = [product["precio"] * 1.21 for product in productos]
print(price)

# Código 2: Usar filter con lambda
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
""" codigo refactorizado """
pares = list(filter(lambda num : num % 2 == 0, numeros))
print(pares)
        
# Código 3: Usar sorted con lambda
usuarios = [
    {"nombre": "Carlos", "edad": 35},
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Luis", "edad": 42},
]
usuarios_ordenados = []
for usuario in usuarios:
    usuarios_ordenados.append(usuario)
usuarios_ordenados.sort(key=lambda u: u["edad"])
""" codigo refactorizado """
order = sorted(usuarios, key=lambda item : item["edad"]) # [::-1]
print(order)

# Código 4: Convertir a generador
def obtener_cuadrados(n):
    resultado = []
    for i in range(n):
        resultado.append(i ** 2)
    return resultado
""" codigo refactorizado """
gene = list(n ** 2 for n in range(10))
print(gene)

# Código 5: Usar map con lambda
precios = [100, 200, 300, 400]
precios_con_descuento = []
for precio in precios:
    nuevo_precio = precio * 0.9
    precios_con_descuento.append(nuevo_precio)
""" codigo refactorizado """
prices = list(map(lambda num : num * 0.9, precios))
print(prices)


# 🧪 Evaluación Teórica

# Pregunta 1
# Explica la diferencia entre una list comprehension [x for x in lista] y un generator expression (x for x in lista).
# ¿Cuándo usarías cada uno? Da un ejemplo de cuándo un generador es claramente mejor.
# la principal diferencia es que generator usa menos memoria que lis comprehension ya que solo usa memoria bajo demanda y el otro usa memoria desde el inicio.
# usaria list comprehension para pocos datos y generator para grandes datos.
# por ejemplo si quiero generar los numeros pares del 1 al 1000000 o datos bajo demanda de una web es mejor generator
# list comprehension es mejor para generar una lista de los numeros pares del 1 al 10 o una lista de los nombres de una clase que son pocos.

# Pregunta 2
# ¿Cuándo deberías usar una función lambda vs una función definida con def?
# ¿Qué limitaciones tienen las funciones lambda?
# las funciones lambda son solo para funciones basicas o de una sola linea, si la funcion es mas compleja es mejor def.

# Pregunta 3
# Explica qué es "lazy evaluation" en el contexto de generadores.
# ¿Por qué los generadores son más eficientes en memoria para procesar grandes datasets?
# "lazy evaluation" significa que los generadores no calculan su valor hasta que se necesitan(bajo demanda), 
# lo que los hace mas eficintes es que solo procesan datos bajo demanda y no guardan toda la lista en memoria.


# Reflexión personal:
# ¿Qué fue lo más difícil?
# entender la diferencia entre map y filter, tambien como usar y posicionar lambda, map y filter juntos.

# ¿Entendiste cuándo usar comprehensions vs bucles?
# si, para bucles mas complejos de mas de una linea o dificiles de leer es mejor los bucles tradicionales, de no ser asi se puede usar comprehensions.

# ¿Cuánto tiempo real te tomó?
# Me tomo unas 5 hotras

# ¿Qué concepto necesitas repasar?
# me gustaria repasar mas a fondo el uso de lambda, map y filter juntos.

# 🎯 Objetivo de mañana (Día 9): Decoradores básicos y uso práctico

# Conexión con proyectos finales:
# 💰 Cost Optimizer: Filtrado eficiente de recursos AWS, generadores para procesar logs grandes
# 🔐 SecureVault: Pipeline de procesamiento de secrets, filtrado por permisos con comprehensions