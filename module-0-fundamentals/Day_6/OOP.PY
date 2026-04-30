# 🚀 DÍA 6 - Módulo 0: Programación Orientada a Objetos (POO) Básica

# 📚 Teoría Concisa (20 min)

# Programación Orientada a Objetos (POO)
# La POO es un paradigma que organiza el código en "objetos" que tienen atributos (datos) y métodos (comportamientos).

# Conceptos fundamentales:
# Clase: Plantilla o molde para crear objetos
# Objeto: Instancia de una clase
# Atributo: Variable que pertenece a un objeto
# Método: Función que pertenece a una clase/objeto
# self: Referencia al objeto actual

# Definición básica de clase:
# class NombreClase: 
#     def __init__(self, parametros):
#         self.atributo = valor
#     
#     def metodo(self):
#         return self.atributo

# Métodos especiales:
# __init__: Constructor (se ejecuta al crear objeto)
# __str__: Representación en string del objeto
# __repr__: Representación técnica del objeto

# Tipos de atributos:
# Atributos de instancia: Únicos para cada objeto (self.nombre)
# Atributos de clase: Compartidos por todas las instancias

# Encapsulación básica:
# Público: nombre
# "Privado" por convención: _nombre (un guión bajo)
# "Muy privado": __nombre (dos guiones bajos - name mangling)

# Buenas prácticas:
# Una clase debe tener una responsabilidad clara
# Usa nombres en PascalCase para clases: class ProductoInventario
# Métodos deben ser verbos: calcular_total(), validar_stock()
# Atributos deben ser sustantivos: precio, cantidad, nombre
# Inicializa todos los atributos en __init__
# Usa type hints en los métodos de clase
# Implementa __str__ para debug amigable

# Errores comunes:
# Olvidar self en métodos
# Olvidar self al acceder atributos
# No llamar __init__ del padre en herencia
# Modificar atributos de clase pensando que son de instancia
# Crear clases que hacen demasiadas cosas

# Ejemplo práctico - Clase básica:

# ❌ Mal - sin POO, datos dispersos
producto_nombre = "Laptop"
producto_precio = 1200.00
producto_stock = 5

def calcular_valor_producto():
    return producto_precio * producto_stock

# ✅ Bien - con POO, datos organizados
class Producto:
    """Representa un producto del inventario."""
    
    def __init__(self, nombre: str, precio: float, stock: int): # type hints/ attributos de clase
        """
        Inicializa un producto.
        
        Args:
            nombre: Nombre del producto
            precio: Precio unitario
            stock: Cantidad en inventario
        """
        self.nombre = nombre # atributo de instancia
        self.precio = precio
        self.stock = stock
    
    def calcular_valor_total(self) -> float: # METODOS 
        """Calcula el valor total del stock."""
        return self.precio * self.stock
    
    def __str__(self) -> str: # representacion legible
        """Representación legible del producto."""
        return f"{self.nombre} - ${self.precio} ({self.stock} unidades)"

# Uso:
laptop = Producto("Laptop Dell", 1200.00, 5) # crear objeto
print(laptop)  # Laptop Dell - $1200.0 (5 unidades)
print(f"Valor total: ${laptop.calcular_valor_total()}")  # $6000.0

# Ejemplo - Atributos de clase:
class Configuracion:
    """Configuración global de la aplicación."""
    
    # Atributo de clase (compartido)
    IVA_RATE = 0.21
    
    def __init__(self, nombre_app: str):
        # Atributo de instancia (único por objeto)
        self.nombre_app = nombre_app
    
    @classmethod
    def obtener_iva(cls) -> float:
        """Método de clase para acceder al IVA."""
        return cls.IVA_RATE

# Documentación oficial: https://docs.python.org/3/tutorial/classes.html


# 💻 Ejercicios Acumulativos

# Ejercicio 1: Clase Básica - CuentaBancaria
# Contexto: Sistema bancario simple que maneja cuentas.
# Requisitos:
# Crea clase CuentaBancaria con:
#   Atributos:
#     - titular: str (nombre del titular)
#     - saldo: float (saldo actual, inicia en 0.0)
#     - numero_cuenta: str
#   
#   Métodos:
#     1. __init__(self, titular: str, numero_cuenta: str)
#        - Inicializa con saldo en 0.0
#     
#     2. depositar(self, monto: float) -> bool
#        - Suma monto al saldo si monto > 0
#        - Retorna True si éxito, False si monto inválido
#     
#     3. retirar(self, monto: float) -> bool
#        - Resta monto del saldo si hay fondos suficientes
#        - Retorna True si éxito, False si fondos insuficientes
#     
#     4. consultar_saldo(self) -> float
#        - Retorna el saldo actual
#     
#     5. __str__(self) -> str
#        - Retorna: "Cuenta {numero_cuenta} - Titular: {titular} - Saldo: ${saldo}"

class AccountBank:
    
    def __init__(self, name : str, account : str, balance : float):
        self.__name = name
        self.__account = account
        self.__balance = balance
        
    def Deposit(self, money : float) -> bool:
        if money > 0.0:
            self.__balance += money
            return True
        else:
            return False
        
    def Withdrawn(self, money : float) -> bool:
        if money <= self.__balance:
            self.__balance -= money
            return True
        else:
            return False
        
    def Balance(self) -> float:
        return self.__balance
    
    def __str__(self) -> str:
        return f"HI Mister: {self.__name}, this is your account: {self.__account} yhere is a balance: {self.__balance}"
    
data = AccountBank("Eric Edwards", "895-78965-122", 25660.0)
data.Deposit(10000)
data.Withdrawn(20000)
print(data)

# Ejercicio 2: Clase con Validación - Estudiante
# Contexto: Sistema escolar que registra estudiantes y calificaciones.
# Requisitos:
# Crea clase Estudiante con:
#   Atributos:
#     - nombre: str
#     - edad: int
#     - calificaciones: list[float] (inicia vacía)
#   
#   Métodos:
#     1. __init__(self, nombre: str, edad: int)
#        - Valida que edad esté entre 12 y 30
#        - Si no es válida, asigna edad = 18 por defecto
#     
#     2. agregar_calificacion(self, calificacion: float) -> bool
#        - Agrega calificación si está entre 0 y 100
#        - Retorna True si se agregó, False si es inválida
#     
#     3. calcular_promedio(self) -> float
#        - Retorna promedio de calificaciones
#        - Si no hay calificaciones, retorna 0.0
#     
#     4. obtener_estado(self) -> str
#        - Si promedio >= 70: "Aprobado"
#        - Si promedio < 70: "Reprobado"
#        - Si no hay calificaciones: "Sin calificaciones"
#     
#     5. __str__(self) -> str
#        - Retorna: "{nombre} ({edad} años) - Promedio: {promedio} - {estado}"

class Student:
    def __init__(self, name : str, age : int, notes : float):
        self._age = age if 12 <= age <= 30 else 18
        self._name = name
        self._notes = notes
        self._student_grades = []
        
    def Add_Students_Grades(self,name : str, cualifications : float, age : int) -> bool:
        if self._age > 12 and self._age < 30:
            if cualifications > 0 and cualifications < 100:
                self._student_grades.append((name, cualifications, age))
                return True
            return False      
        return False   
        
    def Average(self) -> float:
        if len(self._student_grades) == 0:
            return 0.0
        count = 0
        for name, cualifications, age in self._student_grades:
            count += cualifications
        return count / len(self._student_grades)
        
    def Status(self) -> None:
        for name, cualification, age in self._student_grades:
            if cualification > 70.0:
                print(f"The student: {name} approve with a grade of {cualification}")
            elif cualification < 70.0:
                print(f"The student: {name} with a grade of {cualification} dont approve")
            else:
                print("With out cualifications")
                
     
    def __str__(self) -> str:
        return f"The studen: {self._name} age: {self._age} years, with a average: {self._notes}, Staus: {'Approve' if self._notes > 70 else ('Dont Apprve' if self._notes < 70 else 'with out cualifications')}"
        
data = Student("helen", 25, 65.0)
data.Add_Students_Grades("helen",75.5, 22)
data.Add_Students_Grades("carlos",85.5, 21)
data.Add_Students_Grades("eric",55.5, 25)
data.Add_Students_Grades("berto",68, 22)
print(data.Average())
data.Status() 
print(data)


# Ejercicio 3: Clase con Lista Interna - CarritoCompras
# Contexto: E-commerce que maneja carritos de compra.
# Requisitos:
# Crea clase CarritoCompras con:
#   Atributos:
#     - items: list[dict] (cada item: {"nombre": str, "precio": float, "cantidad": int})
#     - cliente: str
#   
#   Métodos:
#     1. __init__(self, cliente: str)
#        - Inicializa items como lista vacía
#     
#     2. agregar_item(self, nombre: str, precio: float, cantidad: int) -> bool
#        - Crea dict y lo agrega a items si precio > 0 y cantidad > 0
#        - Retorna True si se agregó
#     
#     3. calcular_subtotal(self) -> float
#        - Suma (precio * cantidad) de todos los items
#     
#     4. contar_items(self) -> int
#        - Retorna cantidad total de items (suma de todas las cantidades)
#     
#     5. obtener_item_mas_caro(self) -> dict | None
#        - Retorna el item con mayor precio unitario
#        - None si carrito vacío
#     
#     6. __str__(self) -> str
#        - Retorna: "Carrito de {cliente} - {count} items - Total: ${subtotal}"

class ShoppingCart:
    def __init__(self, client : str):
        self._client = client
        self._items = []
        
    def Add_Item(self, name : str, price : float, quantity : int) -> bool:
        if price > 0 and quantity > 0:
            item = {"name" : name, "price" : price, "quantity" : quantity}
            self._items.append(item)
            return True
        return False
    
    def Subtotal(self) -> float:
        total = 0.0
        for item in self._items:
            total += item["price"] * item["quantity"]
        return total
    
    def Count_Items(self) -> int:
        count = 0
        for item in self._items:
            count += item["quantity"]
        return count
    
    def Most_Expensive_Item(self) -> dict | None:
        if not self._items:
            return None
        most_expensive = self._items[0]
        for item in self._items:
            if item["price"] > most_expensive["price"]:
                most_expensive = item
        return most_expensive
    
    def __str__(self) -> str:
        return f"Shopping Cart of {self._client} - {self.Count_Items()} items - Total: ${self.Subtotal()}"
cart = ShoppingCart("Alice")
cart.Add_Item("Laptop", 1200.0, 1)
cart.Add_Item("Mouse", 25.0, 2)
cart.Add_Item("Keyboard", 75.0, 1)
print(cart)
print(cart.Most_Expensive_Item())


# Ejercicio 4: Clase con Atributos de Clase - Empleado
# Contexto: Sistema de RRHH que maneja empleados y contador global.
# Requisitos:
# Crea clase Empleado con:
#   Atributos de clase:
#     - total_empleados: int = 0 (contador compartido)
#     - salario_minimo: float = 1000.0 (compartido)
#   
#   Atributos de instancia:
#     - nombre: str
#     - salario: float
#     - departamento: str
#     - id_empleado: int (autogenerado desde total_empleados)
#   
#   Métodos:
#     1. __init__(self, nombre: str, salario: float, departamento: str)
#        - Valida que salario >= salario_minimo
#        - Si es menor, asigna salario_minimo
#        - Incrementa total_empleados
#        - Asigna id_empleado = total_empleados
#     
#     2. aumentar_salario(self, porcentaje: float) -> None
#        - Aumenta salario en el porcentaje dado (ej: 10 para 10%)
#     
#     3. puede_ser_gerente(self) -> bool
#        - Retorna True si salario >= 3000.0
#     
#     4. __str__(self) -> str
#        - Retorna: "Empleado #{id} - {nombre} ({departamento}) - ${salario}"
#     
#     5. @classmethod obtener_total_empleados(cls) -> int
#        - Retorna total_empleados
# NOTA: - @classmethod sirve para métodos que trabajan con la clase en sí y no con un objeto específico
class Employees:
    # atributos de una clase
    total_employees : int = 0
    Minimun_wage : float = 1000.0
    
    # atributos de una instancia
    def __init__(self, name : str, salary : float, department : str):
        self._name = name
        self._department = department
        self._salary = salary
        if self._salary >= Employees.Minimun_wage:
            self._salary = salary
            Employees.total_employees += 1
        else:
            self._salary = Employees.Minimun_wage
            Employees.total_employees += 1
        self._name = name
        self._department = department
        
    def Salary_increase(self, porcent : float):
        Increase = self._salary * (porcent / 100)
        return self._salary + Increase
    
    def if_Manager(self):
        if self._salary >= 3000:
            return True
        else:
            return False
        
    def __str__(self):
        return f"The employee {self._name} from the deparment: {self._department} earn a {self._salary} dolars per month"

    @classmethod
    def Amount_of_employees(cls):
        return cls.total_employees
    
data = Employees("Eric Calvin", 2000, "sales")
print(data.Salary_increase(20))
print(data.if_Manager())
print(data)
print(data.Amount_of_employees())


# Ejercicio 5: Clase Calculadora Simple (Integrador)
# Contexto: Calculadora que mantiene historial de operaciones.
# Requisitos:
# Crea clase Calculadora con:
#   Atributos:
#     - historial: list[dict] (cada operación: {"operacion": str, "resultado": float})
#   
#   Métodos:
#     1. __init__(self)
#        - Inicializa historial vacío
#     
#     2. sumar(self, a: float, b: float) -> float
#        - Calcula suma
#        - Guarda en historial: {"operacion": "5.0 + 3.0", "resultado": 8.0}
#        - Retorna resultado
#     
#     3. restar(self, a: float, b: float) -> float
#        - Calcula resta y guarda en historial
#     
#     4. multiplicar(self, a: float, b: float) -> float
#        - Calcula multiplicación y guarda en historial
#     
#     5. dividir(self, a: float, b: float) -> float | None
#        - Si b == 0: retorna None y guarda error en historial
#        - Sino: calcula y guarda en historial
#     
#     6. obtener_historial(self) -> list[dict]
#        - Retorna copia del historial
#     
#     7. limpiar_historial(self) -> None
#        - Vacía el historial
#     
#     8. contar_operaciones(self) -> int
#        - Retorna cantidad de operaciones en historial

class Calculate:
    def __init__(self):
        self.history = []
        
    def Sum_numbers(self, a : float, b : float):
        result = a + b
        item = {"operator" : "suma", "result" : result}
        self.history.append(item)
        return result
    
    def Subtract_numbers(self, a : float, b : float):
        result = a - b
        item = {"operator" : "subtract", "result" : result}
        self.history.append(item)
        return result
    
    def Multiply_numbers(self, a : float, b : float):
        result = a * b
        item = {"operator" : "multiply", "result" : result}
        self.history.append(item)
        return result
    
    def Divide_numbers(self, a : float, b : float):
        if b == 0:
            item = {"operator" : "divide", "result" : None}
            self.history.append(item)
            return None
        else:
            result = a / b
            item = {"operator" : "divide", "result" : result}
            self.history.append(item)
            return result
        
    def See_History(self):
        count = 0
        for datas in self.history:
                count += 1
                print(f"{count}- Operation: {datas["operator"]} and the result was: {datas["result"]}")
                
    def Clean_history(self):
        self.history.clear()
        return "The history is succesfuly cleaned"
    
    def Count_operations(self):
        count = len(self.history)
        return f"The amount of operations is {count}"

data = Calculate()
print(data.Sum_numbers(4, 8))
print(data.Divide_numbers(4, 8))
print(data.Subtract_numbers(4, 8))
print(data.Multiply_numbers(4, 8))
data.See_History()           
            


# 📖 Ejercicios de Lectura de Código

# Ejercicio 6: Identificación de Errores en Clases
# Analiza este código e identifica los problemas:

# Problema 1: Olvidar self
# class Usuario:
#     def __init__(nombre, edad):  # ¿Qué falta? falta el self
#         self.nombre = nombre
#         self.edad = edad
    
#     def saludar():  # ¿Qué falta? falta declarar el self
#         print(f"Hola, soy {nombre}")  # ¿Y aquí? no se declaro el attributo de metodo por lo tanto nombre no esta definido

# Problema 2: Atributo de clase usado como de instancia
class Contador:
    total = 0
    
    def __init__(self):
        self.total = 0  # ¿Es correcto? no es correcto por total es un attributo de clase y no de instancia
    
    def incrementar(self):
        self.total += 1  # ¿Qué incrementa realmente? incrementa el attributo de instancia y no el de clase, para aumentar el de clase se usa classmethod
        


# Problema 3: No inicializar atributos
class Producto:
    def __init__(self, nombre):
        self.nombre = nombre
        # Falta inicializar self.precio ya que se usa en el metodo posterior
    
    def calcular_con_iva(self):
        return self.precio * 1.21  # ¿Qué pasa aquí? sucedeera un error ya que el attributo de instancia (precio) no esta definido
    

# Problema 4: Modificar parámetro mutable
class ListaCompras:
    def __init__(self, items=[]):  # ¡PELIGRO! esto no es una buena practica, darle un valor por defecto(lista vacia) a la hora de inicializar con init, es recoemendable nombrar el attributo y despues poner el attributo de instancia(lista)
        self.items = items

lista1 = ListaCompras()
lista1.items.append("Pan")
lista2 = ListaCompras()  # ¿Qué contiene lista2.items? una lista vacia

# Preguntas:
# ¿Por qué self es obligatorio en métodos?
# El self es muy importante ya que se usa para referenciar al objeto actual, sin el no funcionaria el metodo

# ¿Cuándo usar atributos de clase vs instancia?
# El atributo de clase  se usa cuando una o dos variables lo va a usar toda la clase por ejemplo clase tienda y atributo comprador... 
# ya el atributo de instancia seria todo lo que va a comprar el comprador, precio, iva, descuento y subtotal.

# ¿Qué pasa si no inicializas un atributo en __init__?
# Probablemente no funcionen los atributos de instancia ya que es vital para que ellos funcionen

# ¿Por qué no debes usar listas vacías como default?
# No se deben usar listas, diccionarios ni set como valores por defecto en las funciones o metodos ya que son mutables y compartirian valores
# eso quiere decir que cada vez que se use la funcion se encontrar el item que se agrego primero en la lista, es mejor ponerle de valor por defecto NONE.


# Ejercicio 7: Refactorización de Código Procedural a POO
# Refactoriza este código usando una clase:

# Código procedural (sin POO):
libro_titulo = "1984"
libro_autor = "George Orwell"
libro_paginas = 328
libro_prestado = False

def prestar_libro():
    global libro_prestado
    if not libro_prestado:
        libro_prestado = True
        return True
    return False

def devolver_libro():
    global libro_prestado
    libro_prestado = False

def obtener_info_libro():
    estado = "Prestado" if libro_prestado else "Disponible"
    return f"{libro_titulo} por {libro_autor} - {libro_paginas} páginas - {estado}"

# Refactoriza creando una clase Libro con:
# - Atributos: titulo, autor, paginas, prestado
# - Métodos: prestar(), devolver(), obtener_info(), __str__()
# - Constructor que inicialice todos los atributos (prestado en False por defecto)

class Book:
    def __init__(self, title : str, author : str, pages : int):
        self._title = title
        self._author = author
        self._pages = pages
        self._borrowed = False
        
    def Borrow_Book(self) -> bool:
        if not self._borrowed:
            self._borrowed = True
            return True
        return False
    
    def Return_Book(self):
        self._borrowed = False
        
    def Get_Book_Info(self) -> str:
        status = "Borrowed" if self._borrowed else "Available"
        return f"{self._title} by {self._author} - {self._pages} pages - {status}"
    
    def __str__(self) -> str:
        return f"The book: {self._title} written by {self._author} with {self._pages} pages is {'Borrowed' if self._borrowed else 'Available'}"
    
data = Book("1984", "George Orwell", 328)
print(data.Borrow_Book())
print(data.Get_Book_Info())
print(data)

# 🧪 Evaluación Teórica

# Pregunta 1
# Explica qué es una clase y qué es un objeto. ¿Cuál es la diferencia?
# Da un ejemplo del mundo real (no de programación) que ilustre esta relación.
# Una Clase es un molde o plantilla para crear objectos y los objetos son datos o instancia de una clase... 
# un ejemplo puede ser que la clase sea una fabrica y los objetos sean los productos de la fabrica

# Pregunta 2
# ¿Qué es self en Python y por qué es necesario en los métodos de clase?
# ¿Qué pasa si olvidas usar self al acceder a un atributo?
# en pocas palabras el self es una referencia al objeto actual, es necesario para que los attributos en los metodos y de instancia funcionen..
# ya que si no se usan aparece un error en pantalla de atributo no declarado.

# Pregunta 3
# Explica la diferencia entre atributos de clase y atributos de instancia.
# Da un ejemplo de cuándo usarías cada uno en una aplicación real.
# los atributos de clase son atributos globales que se usaran en todo la clase, un ejemplo seria el costos del iva que es global para todos los productos.
# los atributos de instancia son datos locales que son diferentes en cada metodo como por ejemplo el precio o subtotal de un producto.


# Reflexión personal:
# ¿Qué fue lo más difícil?
# entender para que sirve @classmethod

# ¿Entendiste la diferencia entre clase y objeto?
# si los objetos son datos para las clases y las clases moldean esos objetos

# ¿Cuánto tiempo real te tomó?
# unas 5 horas

# ¿Qué concepto necesitas repasar?
# Conceptos de clases method y para que se usa

# 🎯 Objetivo de mañana (Día 7): Herencia, polimorfismo y composición en POO
