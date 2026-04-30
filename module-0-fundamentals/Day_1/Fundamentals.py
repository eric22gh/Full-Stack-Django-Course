# 🚀 DÍA 1 - Módulo 0: Fundamentos de Lógica de Programación
# 📚 Teoría Concisa 
# Variables y Tipos de Datos en Python: Las variables son contenedores que almacenan información en memoria. 
# Python es un lenguaje de tipado dinámico (no necesitas declarar el tipo explícitamente).

# Tipos de datos fundamentales:
# int: números enteros → age = 25
# float: números decimales → price = 19.99
# str: cadenas de texto → name = "Juan"
# bool: booleanos → is_active = True
# list: listas mutables → numbers = [1, 2, 3]
# tuple: tuplas inmutables → coords = (10, 20)
# dict: diccionarios → key : value = {"name": "Ana", "age": 30}
# set: conjuntos → unique_numbers = {1, 2, 3}

# Buenas prácticas:
# Usa nombres descriptivos: user_count en vez de us
# Snake_case para variables: total_price
# UPPER_CASE para constantes: MAX_RETRIES = 3
# Evita palabras reservadas: class, for, if, def, self, etc. 

# Errores comunes:
# Confundir = (asignación) con == (comparación)
# No inicializar variables antes de usarlas
# Olvidar que strings son inmutables


# Ejemplo práctico:
texto = "Hola"
# texto[0] = "h"   # ❌ Error: los strings no permiten asignación por índice
texto = "Hola"
# nuevo_texto = "h" + texto[1:]   # Resultado: "hola"  # ✅ Correcto: crea un nuevo string

# ❌ Mal - nombres poco descriptivos
x = 100
# y = x * # aux: el aux no esta definido.

# ✅ Bien - código autodocumentado
product_price = 100
tax_rate = 0.21
total_with_tax = product_price * (1 + tax_rate)

print(f"Precio final: ${total_with_tax:.2f}") 

# Documentación de los ejercicios del día 1: https://docs.python.org/3/library/stdtypes.html

# 💻 Ejercicios Acumulativos

# Ejercicio 1: Sistema de Variables para un Perfil de Usuario
# Contexto: Estás construyendo un sistema de registro. Necesitas almacenar y validar información básica.
# Requisitos:
# Crea variables para: nombre completo, edad, email, saldo de cuenta
# Calcula si el usuario es mayor de edad (>=18)
# Formatea un mensaje de bienvenida con todos los datos
# Calcula un descuento del 10% si es mayor de 65 años
name = "eric"+" "+"hernandez"
age = 70
email = "fera@gmail.com"
Account_balance = 250000
if age >= 18 and age < 65:
    print(f"welcome to our bank: {name}, age: {age}, email : {email}, with a balance account: {Account_balance}")
elif age > 65:
    disscount = Account_balance * 0.010
    print(f"welcome to our bank: {name}, age: {age}, email : {email}, with a balance account: {disscount}")
    


# Ejercicio 2: Conversor de Tipos y Validación
# Contexto: Recibes datos del frontend como strings. Necesitas convertirlos y validar.
# Requisitos: Convierte estas variables string a sus tipos correctos:
# y Calcula el total: price * quantity, Verifica si el producto está disponible Y el total es menor a $600
# Imprime un mensaje según el resultado

# price_str = "99.99" → float
# quantity_str = "5" → int
# is_available_str = "True" → bool
price = 99.99
quantity = 5
is_available = True
Total_price = price * quantity
if is_available == True and Total_price < 600:
    print("The product is available and its price lower than $600")
else:
    print(Total_price)

# Ejercicio 3: Estructura de Datos para Productos
# Contexto: Necesitas modelar productos de un inventario.
# Requisitos: Crea un diccionario para un producto con: id, nombre, precio, stock, categoría
# Crea una lista con 3 productos diferentes
# Calcula el valor total del inventario (precio × stock de cada producto)
# Encuentra el producto más caro usando un loop

Inventory = [{"Product_id": 1, "name": "Laptop", "price": 2500, "stock": 5, "category" : "technology"},
             {"Product_id": 2, "name": "Smart_Tv", "price": 25000, "stock": 6, "category" : "technology"},
             {"Product_id": 3, "name": "Wood", "price": 30, "stock": 100, "category" : "Home"}
             ]
expensive = 0
for products in Inventory:
    Total_Value = products["price"] * products["stock"]
    print(f"The total value of this product: {products["name"]}  is {Total_Value}")
    if products["price"] > expensive:
        expensive = products["price"]
        product = products["name"]
print(f"The most expensive product is: {product}")
    
# Ejercicio 4: Mutabilidad - Lista vs Tupla
# Contexto: Entender cuándo usar listas (mutables) vs tuplas (inmutables).
# Requisitos:
# Crea una tupla con coordenadas GPS que NO deben cambiar
# Crea una lista con tareas pendientes que SÍ pueden cambiar
# Intenta modificar la tupla y captura el error
# Agrega 2 tareas nuevas a la lista
# Elimina la primera tarea completada
coords = (22.0, 3.0, 10.2)
Task_List = ["Mow the lawn", "Wash the dishes", "paint the wall"]
try:
    coords[0] = 33.0
except TypeError as e:
    print("No se puede cambiar una tupla")
Task_List.append("wash the car")
Task_List.append("Go to the grocery store")
Task_List.pop(0)
print(Task_List)

# Ejercicio 5: Sistema de Cálculo de Impuestos (Integrador)
# Contexto: Construyes una función para calcular precios finales con impuestos variables.
# Variables: precio base, país (string)

# Diccionario de tasas de impuestos por país:
# España: 21%, México: 16%, USA: 8%

# Calcula el precio final según el país
# Si el país no existe, usa una tasa por defecto del 10%
# Retorna un diccionario con: base, tax_rate, tax_amount, total

def calculate_price(price, country):
    taxes = {"name" : "spain", "taxes" : 0.21}, {"name" : "mexico", "taxes" : 0.16}, {"name" : "USA", "taxes" : 0.08}
    for object in taxes:
        if object["name"] != country:
            return f"Base taxes: 10%, price: {price}, country: {country} with a total: {price * 0.010}"
        else:
            total = price * object["taxes"]
            return f"Base taxes: {object["taxes"]}, price: {price}, country: {country} with a total: {price + total}"

print(calculate_price(35000, "spain"))

# 📖 Ejercicios de Lectura de Código 
# Ejercicio 6: Refactorización de Código Malo: Analiza este código y lista 5 problemas:
pythonx = "John Doe"
a = 25
b = a >= 18
c = 1000.50
d = c * 1.21
print(x, a, b, d)
data = [x, a, c]
data[0] = "Jane Doe"  # ¿Qué problema tiene esto?

# 1- Tiene variables poco descriptivos
# 2- NO poseen el formato snakecase
# 3- Problemas de inmutabilidad, los strings son inmutables
# 4- NO usan UPPER CASE para variables constantes
# 5- NO esta evitando palabras reservadas

#Preguntas del codigo anterior:
# ¿Qué nombres de variables mejorarías?
# respuesta: la de pythonx, las letras que son poco descritivas.

# ¿Hay algún cálculo que debería ser una constante?
#respuesta: SI en efecto el caculo de la variable d.

# ¿Es correcto modificar data[0]? ¿Por qué?
# respuesta: NO es correcto ya que los strings son inmutables, hay que tenerlo muy presente.


# Ejercicio 7: Debugging de Tipos
# Este código tiene errores. Encuéntralos sin ejecutar:
pythonuser_age = "30"
discount_rate = 0.1
# can_drive = # user_age > 18  # ¿Funciona?
# respuesta: No funciona ya que la variable user_age no esta declarada y es un error muy comun.

#total = "100" + 20  # ¿Qué pasa aquí?
# respuesta: error ya que no se puede sumar un string con integer

config = ("localhost", 5432)
#config[0] = "127.0.0.1"  # ¿Es posible?
# respuesta: NO ya que la tupla(config en este caso) es inmutable


# 🧪 Evaluación Teórica 
# Pregunta 1 ¿Cuál es la diferencia entre una lista [] y una tupla ()? Da un ejemplo de cuándo usarías cada una en una aplicación web Django.
# respuesta: la principal diferencia es que las tuplas son inmutables y las listas mutables... Yo usaria tuplas para almacenar ceriticados o contraseñas
# en la app web y listas para almacenar comentarias.

# Pregunta 2 Explica qué significa "Python es un lenguaje de tipado dinámico". ¿Qué ventajas y desventajas tiene esto en proyectos grandes?
# respuesta: La ventaje de python es que no es declarativo, no requiere que todo lo que se escriba o declara tenga su tipo de dato.... 
# python tiene una gran flexibilidad y rapidez en el desarrollo ya que es de tipado dinamico,
# pero en proyectos grandes puede traer riesgos de errores difíciles de detectar 
# y problemas de escalabilidad si no se aplican buenas prácticas.

# Pregunta 3 ¿Por qué es importante usar nombres de variables descriptivos? Da un ejemplo de código "autodocumentado" vs código con malos nombres.
# respuesta: En mi opinion es mas facil a la hora de encontrar errores, tambien hace ver al codigo mas limpio ya que es una buena practica.

# 📊 Autoevaluación y Feedback 
# ¿Qué fue lo más difícil?
# respuesta: trarte de analizar y entender algunos ejercicios.
# ¿Qué concepto necesitas repasar?
# respuesta: funciones y estructuras de datos
# ¿Cuánto tiempo real te tomó?
# respuesta: me tomo unas 2 horas aproximadamente
