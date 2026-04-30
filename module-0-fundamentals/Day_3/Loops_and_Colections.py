# 🚀 DÍA 3 - Módulo 0: Bucles y Manejo de Colecciones

# 📚 Teoría Concisa 

# Bucles en Python
# Los bucles permiten ejecutar código repetidamente.

# Bucle FOR:
# Se usa cuando sabes cuántas iteraciones necesitas o iteras sobre una colección
# Sintaxis: for elemento in coleccion:

# Bucle WHILE:
# Se usa cuando no sabes cuántas iteraciones necesitas (depende de una condición)
# Sintaxis: while condicion:

# Control de Bucles:
# break: Sale del bucle inmediatamente
# continue: Salta a la siguiente iteración
# else en bucles: Se ejecuta si el bucle termina normalmente (sin break)

# Funciones útiles con colecciones:
# range(start, stop, step): genera secuencia de números
# enumerate(lista): devuelve índice y valor
# zip(lista1, lista2): combina dos listas
# len(coleccion): longitud de la colección
# sum(lista): suma elementos numéricos
# max(lista), min(lista): valor máximo/mínimo de la lista

# Métodos de listas:
# append(item): agrega al final
# extend(lista): agrega múltiples elementos
# remove(item): elimina primera ocurrencia
# pop(index): elimina y retorna elemento
# insert(index, item): inserta en posición específica
# sort(): ordena la lista en su lugar
# reverse(): invierte la lista

# Métodos de diccionarios:
# keys(): retorna las claves
# values(): retorna los valores
# items(): retorna pares (clave, valor)
# get(key, default): obtiene valor con default si no existe
# update(dict): actualiza con otro diccionario/Une 2 diccionarios

# Buenas prácticas:
# Usa nombres descriptivos en variables de iteración: for product in products (no for p in products)
# Prefiere enumerate() cuando necesitas el índice
# Evita modificar una lista mientras la iteras (crea una copia)
# Usa comprensiones de lista para transformaciones simples
# break/continue con moderación (pueden dificultar legibilidad)

# Errores comunes:
# Modificar lista durante iteración causa comportamiento inesperado
# Olvidar inicializar acumuladores antes del bucle
# while sin condición de salida (bucle infinito)
# Índices fuera de rango en listas

# Ejemplo práctico - Iteración eficiente:

# ❌ Mal - usando índices innecesariamente, Nota Depende de el contexto.
products = ["Laptop", "Mouse", "Keyboard"]
for i in range(len(products)):
    print(products[i])

# ✅ Bien - iteración directa
for product in products:
    print(product)

# ✅ Mejor - cuando necesitas índice
for index, product in enumerate(products):
    print(f"{index + 1}. {product}")
# enumerate comienza desde 0 por defecto.
# Puedes personalizar el índice de inicio usando el argumento start

# Ejemplo - Acumuladores:
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Total: {total}")  # 150

# Documentación oficial: https://docs.python.org/3/tutorial/controlflow.html#for-statements


# 💻 Ejercicios Acumulativos

# Ejercicio 1: Procesador de Lista de Compras con Totales
# Contexto: Sistema de carrito de compras que calcula totales y estadísticas.
# Requisitos:
# Lista de productos (cada producto es un diccionario con: nombre, precio, cantidad)
# Usando un bucle for:
#   - Calcula el subtotal de cada producto (precio * cantidad)
#   - Suma el total general del carrito
#   - Cuenta cuántos productos hay
#   - Encuentra el producto más caro (por precio unitario)
#   - Encuentra el producto con mayor valor total (precio * cantidad)
# Imprime un resumen detallado del carrito

# Datos de prueba:
productos_carrito = [
    {"nombre": "Laptop", "precio": 1200.00, "cantidad": 1},
    {"nombre": "Mouse", "precio": 25.50, "cantidad": 2},
    {"nombre": "Teclado", "precio": 750.00, "cantidad": 1},
    {"nombre": "Monitor", "precio": 800.00, "cantidad": 2},
]
def Sales_Sumary(products):
    total = 0
    Most_expensive = 0
    Total_value = 0
    for product in products:
        subtotal = product["precio"] * product["cantidad"] 
        total += product["cantidad"]
        if product["precio"] * 1 > Most_expensive:
            Most_expensive = product["precio"] 
            Most_expensive_product = product["nombre"]
        if product["precio"] * product["cantidad"] > Total_value:
            Total_value = product["precio"] * product["cantidad"]
            Total_value_product = product["nombre"]
        print(f"El subtotal de cada producto es: {subtotal}")
    print(f"La suma total de el carrito es: {total}, hay un total de {len(productos_carrito)} productos, el producto mas caro por unidad es: {Most_expensive_product}, el producto mas caro por cantidad es: {Total_value_product}")
            
Sales_Sumary(productos_carrito)


# Ejercicio 2: Filtrador de Usuarios por Criterios Múltiples
# Contexto: Panel de administración que filtra usuarios según criterios.
# Requisitos:
# Lista de usuarios (cada usuario es un diccionario con: name, edad, active, balance)
# Usando bucles, crea 3 listas filtradas:
#   - usuarios_activos: solo usuarios con active=True
#   - usuarios_mayores: edad >= 30 y active=True
#   - usuarios_con_balance: balance > 100 y active=True
# Cuenta cuántos usuarios hay en cada categoría
# Imprime el name de cada usuario en cada categoría

# Datos de prueba:
usuarios = [
    {"name": "Ana", "age": 28, "active": True, "balance": 150.00},
    {"name": "Carlos", "age": 35, "active": True, "balance": 50.00},
    {"name": "María", "age": 42, "active": False, "balance": 200.00},
    {"name": "Luis", "age": 31, "active": True, "balance": 300.00},
    {"name": "Sofia", "age": 25, "active": True, "balance": 80.00},
]
# Importante: NO modifiques la lista original, crea nuevas listas
def Users_Systems(Data):
    Active_User = []
    Older_User = []
    Balance_User = []
    for User in Data:
        if User["active"]:
            Active_User.append(User["name"])
        if User["active"] and User["age"] >= 30:
            Older_User.append(User["name"])
        if User["active"] and User["balance"] > 100:
            Balance_User.append(User["name"])   
    Active_User.append(Older_User) 
    Active_User.append(Balance_User)
    for names in Active_User:
        print(names)
    return f"Amount of User in active user: {len(Active_User)}, amount of User in Older user: {len(Older_User)}, Amount of User in Balancer user: {len(Balance_User)},"

print(Users_Systems(usuarios))

# Ejercicio 3: Generador de Reporte de Inventario con Alertas
# Contexto: Sistema de inventario que genera reportes y alertas automáticas.
# Requisitos:
# Lista de productos con: id, nombre, stock, stock_minimo, precio
# Recorre todos los productos y genera 3 listas:
#   - productos_criticos: stock < stock_minimo
#   - productos_sin_stock: stock == 0
#   - productos_optimos: stock >= stock_minimo
# Calcula el valor total del inventario (stock * precio de todos los productos)
# Para productos críticos, calcula cuántas unidades faltan para alcanzar el mínimo
# Imprime un reporte organizado por categoría

# Datos de prueba:
inventario = [
    {"id": 1, "nombre": "Laptop Dell", "stock": 5, "stock_minimo": 10, "precio": 1200.00},
    {"id": 2, "nombre": "Mouse Logitech", "stock": 0, "stock_minimo": 20, "precio": 25.00},
    {"id": 3, "nombre": "Teclado Mecánico", "stock": 15, "stock_minimo": 10, "precio": 80.00},
    {"id": 4, "nombre": "Monitor LG", "stock": 3, "stock_minimo": 8, "precio": 250.00},
    {"id": 5, "nombre": "Webcam HD", "stock": 25, "stock_minimo": 15, "precio": 60.00},
]
def Reports(Datas):
    productos_criticos = []
    productos_sin_stock = []
    productos_optimos = []
    warning = []
    calculate = 0
    TotaL_Value_Inventory = 0
    for product in Datas:
        if product["stock"] < product["stock_minimo"]:
            productos_criticos.append(product["nombre"])
            print(f"Productos Criticos: {product["nombre"]}")
        if product["stock"] == 0:
            productos_sin_stock.append(product["nombre"])
            print(f"Productos Sin Stock: {product["nombre"]}")
        if product["stock"] >= product["stock_minimo"]:
            productos_optimos.append(product["nombre"])
            print(f"Productos Optimos: {product["nombre"]}")
        TotaL_Value_Inventory += product["stock"] * product["precio"]
        if product["stock"] < product["stock_minimo"]:
            if product["stock"] == 0:
                warning.append((product["nombre"], "Sin stock"))
            else:
                calculate = product["stock_minimo"] - product["stock"]
                warning.append((product["nombre"], calculate))
    for nombre, cantidad in warning:
        print(f"Nombre del producto: {nombre}, cantidad previa para llegar al minimo: {cantidad}")
    print(f"El valor total del inventario es: {TotaL_Value_Inventory}")
Reports(inventario)
    

# Ejercicio 4: Sistema de Búsqueda y Actualización de Productos
# Contexto: Sistema que busca productos y actualiza información usando bucles while.
# Requisitos:
# Usa la lista de inventario del ejercicio anterior
# Implementa búsqueda por nombre (case-insensitive, búsqueda parcial)
# Si encuentra el producto:
#   - Muestra toda su información
#   - Pregunta si desea actualizar el stock (simula con variable)
#   - Actualiza el stock sumando la cantidad ingresada
# Si no encuentra el producto, muestra mensaje apropiado(no se encontro el producto)
# Usa un bucle while para permitir múltiples búsquedas (termina con búsqueda vacía)

# Simula el input del usuario con una lista:
busquedas_simuladas = ["laptop", "mouse", "camara", "grabadora"]  # lo termina la cantidad de productos a buscar

def Update_products(data, busquedas_simuladas, question, update_amount):
    print("Informacion de los productos")
    # por cada busque ver los elementos en la lista de diccionarios
    for busqueda in busquedas_simuladas:
        found = False
        query = busqueda.lower()
        for product in data:
            nombre = product.get("nombre", "").lower()
            # por cada busqueda en la lista de diccionarios quedate con el valor de nombre
            if query in nombre:
                found = True
                # si el dato del usuario esta en la lsita de diccionarios que solo tiene el nombre
                print("Producto encontrado:", product)
                if question == "update":
                    product["stock"] = product.get("stock", 0) + update_amount
                    #actualiza el valor de stock en el diccionario y le da un nuevo valor.
                    print(f"El stock ha sido actualizado a: {product['stock']}")
        if not found:
            print(f"El producto '{busqueda}' no se encontro")
        
inventario = [
    {"id": 1, "nombre": "Laptop Dell", "stock": 5, "stock_minimo": 10, "precio": 1200.00},
    {"id": 2, "nombre": "Mouse Logitech", "stock": 0, "stock_minimo": 20, "precio": 25.00},
    {"id": 3, "nombre": "Teclado Mecánico", "stock": 15, "stock_minimo": 10, "precio": 80.00},
    {"id": 4, "nombre": "Monitor LG", "stock": 3, "stock_minimo": 8, "precio": 250.00},
    {"id": 5, "nombre": "Webcam HD", "stock": 25, "stock_minimo": 15, "precio": 60.00},
]
    
new_Inventory = [product for product in inventario]
Update_products(new_Inventory, busquedas_simuladas, "update", 5 )


# Ejercicio 5: Análisis de Ventas Mensuales (Integrador Complejo)
# Contexto: Dashboard que analiza ventas de múltiples meses y productos.
# Requisitos:
# Diccionario con ventas por mes (cada mes tiene lista de ventas)
# Cada venta: {"producto": str, "cantidad": int, "precio_unitario": float}
# Calcula para cada mes:
#   - Total de ventas (cantidad * precio_unitario de todas las ventas)
#   - Producto más vendido (por cantidad)
#   - Número total de transacciones
# Calcula estadísticas globales:
#   - Mes con mayores ventas
#   - Mes con menor ventas
#   - Promedio de ventas mensuales
#   - Total del año
# Identifica el producto estrella del año (mayor cantidad vendida total)

# Datos de prueba:
def Month_Sales(Data):
    total_anual = 0
    mes_mayor_ventas = ""
    mes_menor_ventas = ""
    mayor_ventas = 0
    menor_ventas = float('inf')  # Inicia con infinito para encontrar el menor
    producto_estrella = {}
    
    for mes, ventas in Data.items():
        total_ventas_mes = 0
        total_transacciones = len(ventas)
        producto_mas_vendido = ""
        cantidad_producto_mas_vendido = 0

        for venta in ventas:
            total_ventas_mes += venta["cantidad"] * venta["precio_unitario"]
            
            # Determinar el producto más vendido
            if venta["cantidad"] > cantidad_producto_mas_vendido:
                cantidad_producto_mas_vendido = venta["cantidad"]
                producto_mas_vendido = venta["producto"]
        
        # Actualizar el total anual
        total_anual += total_ventas_mes
        
        # Determinar mes con mayores y menores ventas
        if total_ventas_mes > mayor_ventas:
            mayor_ventas = total_ventas_mes
            mes_mayor_ventas = mes
        if total_ventas_mes < menor_ventas:
            menor_ventas = total_ventas_mes
            mes_menor_ventas = mes
        
        # Guardar el producto estrella
        if producto_mas_vendido in producto_estrella:
            producto_estrella[producto_mas_vendido] += cantidad_producto_mas_vendido
        else:
            producto_estrella[producto_mas_vendido] = cantidad_producto_mas_vendido

        # Imprimir resultados mensuales
        print(f"Total de ventas en {mes}: ${total_ventas_mes:.2f}")
        print(f"Producto más vendido en {mes}: {producto_mas_vendido} ({cantidad_producto_mas_vendido} unidades)")

    # Calcular el producto estrella del año
    producto_mas_vendido_anual = max(producto_estrella, key=producto_estrella.get)
    cantidad_producto_mas_vendido_anual = producto_estrella[producto_mas_vendido_anual]

    # Imprimir estadísticas globales
    print(f"\nEstadísticas Anuales:")
    print(f"Total del año: ${total_anual:.2f}")
    print(f"Mes con mayores ventas: {mes_mayor_ventas} (${mayor_ventas:.2f})")
    print(f"Mes con menores ventas: {mes_menor_ventas} (${menor_ventas:.2f})")
    print(f"Producto estrella del año: {producto_mas_vendido_anual} ({cantidad_producto_mas_vendido_anual} unidades)")
        
ventas_anuales = {
    "Enero": [
        {"producto": "Laptop", "cantidad": 5, "precio_unitario": 1200.00},
        {"producto": "Mouse", "cantidad": 20, "precio_unitario": 25.00},
        {"producto": "Teclado", "cantidad": 15, "precio_unitario": 75.00},
    ],
    "Febrero": [
        {"producto": "Laptop", "cantidad": 3, "precio_unitario": 1200.00},
        {"producto": "Monitor", "cantidad": 10, "precio_unitario": 300.00},
        {"producto": "Mouse", "cantidad": 25, "precio_unitario": 25.00},
    ],
    "Marzo": [
        {"producto": "Laptop", "cantidad": 8, "precio_unitario": 1200.00},
        {"producto": "Teclado", "cantidad": 12, "precio_unitario": 75.00},
        {"producto": "Mouse", "cantidad": 30, "precio_unitario": 25.00},
    ],
}
# incompleto
Month_Sales(ventas_anuales)

# Usa diccionarios para acumular ventas por producto globalmente


# 📖 Ejercicios de Lectura de Código

# Ejercicio 6: Análisis de Bucle con Errores Comunes
# Este código tiene varios problemas. Identifícalos:

productos = ["Laptop", "Mouse", "Teclado", "Monitor"]

# Problema 1: Modificar lista durante iteración
# for producto in productos:
#     if producto == "Mouse":
#         productos.remove(producto)  # ¿Qué puede salir mal?
# No es una buena practica modificar una lista cuenta se itera, es mejor hacer una copia de la lista, porque causa comportamiento inesperado.

# # Problema 2: Índice fuera de rango
# for i in range(5):
#     print(productos[i])  # ¿Qué pasa en i=4?
# Da error fuera del rango, la lista tiene 4 elementos pero i cuenta el indice 0, entonces el i=4 no existe == fuera de rango

# # Problema 3: Bucle infinito potencial
# contador = 0
# while contador < 10:
#     print(contador)
#     if contador == 5:
#         continue
#     contador += 1  # ¿Dónde debería estar esto? deberia de estar despues de while ya que asi no va a generar un bucle infinito

# # Problema 4: Acumulador no inicializado
# # total = 0  # Falta esta línea
# numeros = [10, 20, 30]
# for num in numeros:
#     total += num  # ¿Qué error da? Da error de variable no asignada, ya que la variable total no existe.

# Preguntas:
# ¿Por qué no debes modificar una lista mientras la iteras?
# Porque podria dar errores inesperados

# ¿Cómo evitar el índice fuera de rango?
# Se le puede agregar un + 1 al indice, cuando lo creamos con enumerate

# ¿Dónde debe ir el incremento en el while con continue?
# debe de ir duespues de el while

# ¿Qué pasa si usas una variable sin inicializar?
# Da error de variable no asignada previamente



# Ejercicio 7: Refactorización con Enumerate y Zip
# Refactoriza estos códigos usando funciones de Python:

# Código 1: Usa enumerate en vez de range(len())
productos = ["Laptop", "Mouse", "Teclado"]
precios = [1200, 25, 75]

for index, productos in enumerate(productos):
    print(f"{index + 1}. {productos}: ${precios[index]}")

# Código 2: Usa zip para iterar dos listas simultáneamente
nombres = ["Ana", "Carlos", "María"]
edades = [28, 35, 42]

for data1, data2 in zip(nombres, edades):
    print(f"{data1} tiene {data2} años")

# Código 3: Simplifica este bucle con sum()
numeros = [10, 20, 30, 40, 50]
total = 0
for num in numeros:
    total += num
print(total)
# se puede simplificar con un Total = sum(numeros) 



# 🧪 Evaluación Teórica

# Pregunta 1
# Explica la diferencia entre for y while. Da un ejemplo de cuándo es más apropiado usar cada uno.
# ¿Qué riesgos tiene usar while incorrectamente?
# La diferencia principal es que con for se tiene que saber las veces que se va a contar y con while es cuando no se sabe ese dato,
# ejemplo de uso de while cuando se ocupa que el bucle se detenga en determinada variable. hay que tener cuidado con esto ya que se corre el 
# riesgo de que si la variable no esta el bucle se torna infinito.

# Pregunta 2
# ¿Qué hace enumerate() y por qué es preferible a usar range(len())?
# Escribe un ejemplo práctico donde enumerate() haga el código más legible.
# Usar len() a la hora de ocupar indices es una mala practica, es mas legible usar enumerate para indices, por ejemplo cuando quieres acceder 
# a un valor de una lista.

# Pregunta 3
# Explica qué significa "modificar una lista durante iteración" y por qué es problemático.
# ¿Cómo puedes iterar sobre una lista y eliminar elementos de forma segura?
# NO es recomendable cambiar una lista mienstras se itera, es mejor hacer una copia y cambiarla despues, ya que se pueden dar errore inesperados,
# SE pueden eliminar elementos de forma segura de una lista con el metodo remove()


# Reflexión personal:
# ¿Qué fue lo más difícil?
# lista de diccionarios sobre diccionarios, se me complico mucho el Ejercicio 5, Análisis de Ventas Mensuales

# ¿Entendiste la diferencia entre for y while?
# Si lo entendi muy bien

# ¿Cuánto tiempo real te tomó?
# Honestamente unas 4 horas ya que el ejercicio 5 se me complico mucho

# ¿Qué concepto necesitas repasar?
# Diria que diccionarios

# Nota: Solucionar el ejercicio 5 y ponerle pseudocodigo para un futuro mejor entendimiento.


# 🎯 Objetivo de mañana (Día 4): Funciones, scope y modularización de código

