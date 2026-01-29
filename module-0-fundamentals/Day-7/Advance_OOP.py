# 🚀 DÍA 7 - Módulo 0: Herencia, Polimorfismo y Composición

# 📚 Teoría Concisa (20 min)

# Herencia en Python
# La herencia permite crear clases nuevas basadas en clases existentes,
# reutilizando y extendiendo funcionalidad.

# Conceptos fundamentales:
# Clase padre/base/superclase: La clase original
# Clase hija/derivada/subclase: La clase que hereda
# super(): Función para llamar métodos de la clase padre
# Sobrescritura (Override): Redefinir método del padre en la hija
# Polimorfismo: Diferentes clases responden al mismo método de forma distinta

# Sintaxis de herencia:
# class ClaseHija(ClasePadre): # la clase hija hereda metodos de la clase padre
#     def __init__(self, params): # iniciar los atributos de la clase hijo
#         super().__init__(params_padre) # init para usar metodos de la clase padre
#         self.atributo_nuevo = valor

# Composición:
# Una clase contiene instancias de otras clases como atributos
# "Tiene-un" vs "Es-un": Composición vs Herencia
# Ejemplo: Auto "tiene-un" Motor (composición)
#          Deportivo "es-un" Auto (herencia)

# Polimorfismo:
# Capacidad de diferentes clases de responder al mismo método
# Duck typing: "Si camina como pato y habla como pato, es un pato"
# si camina como perro y habla como perro, es un perro

# Buenas prácticas:
# Usa herencia para relaciones "es-un" claras
# Usa composición para relaciones "tiene-un"
# No abuses de la herencia (máximo 2-3 niveles)
# Llama a super().__init__() en el constructor de la hija
# Sobrescribe métodos solo cuando necesites cambiar comportamiento
# Prefiere composición sobre herencia en casos dudosos
# Usa isinstance() para verificar tipos

# Errores comunes:
# No llamar super().__init__() en clases hijas
# Herencia profunda (muchos niveles)
# Usar herencia cuando debería ser composición
# Sobrescribir métodos sin entender el original
# Olvidar que los métodos heredados están disponibles

# Ejemplo práctico - Herencia:

# Clase base
class Empleado:
    """Clase base para todos los empleados."""
    
    def __init__(self, nombre: str, salario: float):
        self.nombre = nombre
        self.salario = salario
    
    def calcular_pago_mensual(self) -> float:
        """Calcula pago mensual base."""
        return self.salario
    
    def __str__(self) -> str:
        return f"{self.nombre} - ${self.salario}"

# Clases derivadas
class EmpleadoTiempoCompleto(Empleado):
    """Empleado de tiempo completo con beneficios."""
    
    def __init__(self, nombre: str, salario: float, bono_anual: float): # atributos de la nueva clase
        super().__init__(nombre, salario) # atributos de la clase padre
        self.bono_anual = bono_anual
    
    def calcular_pago_mensual(self) -> float:
        """Incluye porción mensual del bono."""
        pago_base = super().calcular_pago_mensual() # metodo de la clase padre
        bono_mensual = self.bono_anual / 12
        return pago_base + bono_mensual

class EmpleadoPorHoras(Empleado):
    """Empleado que cobra por horas trabajadas."""
    
    def __init__(self, nombre: str, tarifa_hora: float): # atributo de la clase nueva
        super().__init__(nombre, 0)  # Salario base 0, atributos de la clase padre
        self.tarifa_hora = tarifa_hora
        self.horas_trabajadas = 0
    
    def registrar_horas(self, horas: int) -> None:
        """Registra horas trabajadas."""
        self.horas_trabajadas += horas
    
    def calcular_pago_mensual(self) -> float:
        """Calcula según horas trabajadas."""
        return self.tarifa_hora * self.horas_trabajadas

# Polimorfismo en acción: capacidad de distintas clases de responder al mismo metodo
empleados = [
    EmpleadoTiempoCompleto("Ana", 3000, 6000),
    EmpleadoPorHoras("Carlos", 25)
]

for emp in empleados:
    print(f"{emp.nombre}: ${emp.calcular_pago_mensual()}")  # Mismo método para las 2 clases, pero diferente comportamiento

# Ejemplo - Composición:

class Motor:
    """Representa el motor de un vehículo."""
    
    def __init__(self, caballos_fuerza: int):
        self.caballos_fuerza = caballos_fuerza
        self.encendido = False
    
    def encender(self) -> str:
        self.encendido = True
        return "Motor encendido"
    
    def apagar(self) -> str:
        self.encendido = False
        return "Motor apagado"

class Auto:
    """Auto que tiene un motor (composición)."""
    
    def __init__(self, marca: str, modelo: str, caballos_fuerza: int):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(caballos_fuerza)  # Composición, volver una variable una clase, var = clase(objeto)
    
    def arrancar(self) -> str:
        return self.motor.encender()

# Documentación oficial: https://docs.python.org/3/tutorial/classes.html#inheritance


# 💻 Ejercicios Acumulativos

# Ejercicio 1: Jerarquía de Cuentas Bancarias
# Contexto: Sistema bancario con diferentes tipos de cuentas.
# Requisitos:
# Crea clase base CuentaBancaria con:
#   Atributos:
#     - titular: str
#     - saldo: float
#     - numero_cuenta: str
#   
#   Métodos:
#     1. __init__(self, titular: str, numero_cuenta: str, saldo_inicial: float = 0)
#     2. depositar(self, monto: float) -> bool
#     3. retirar(self, monto: float) -> bool (básico, solo verifica fondos)
#     4. consultar_saldo(self) -> float
#     5. __str__(self) -> str

# Crea clase derivada CuentaAhorro(CuentaBancaria):
#   Atributos adicionales:
#     - tasa_interes: float (ej: 0.02 para 2%)
#   
#   Métodos:
#     1. __init__(self, titular: str, numero_cuenta: str, tasa_interes: float)
#        - Llama a super().__init__()
#     2. aplicar_interes(self) -> float
#        - Calcula interés: saldo * tasa_interes
#        - Lo suma al saldo
#        - Retorna monto de interés generado
#     3. __str__(self) -> str
#        - Extiende el __str__ del padre agregando info de tasa de interés

# Crea clase derivada CuentaCorriente(CuentaBancaria):
#   Atributos adicionales:
#     - sobregiro_permitido: float (monto que puede quedar negativo)
#   
#   Métodos:
#     1. __init__(self, titular: str, numero_cuenta: str, sobregiro: float)
#     2. retirar(self, monto: float) -> bool
#        - Sobrescribe el método del padre
#        - Permite retirar si: saldo - monto >= -sobregiro_permitido
#     3. obtener_sobregiro_disponible(self) -> float
#        - Retorna cuánto sobregiro aún puede usar

class BankAccount:
    def __init__(self, name : str, balance : float, account : str):
        self.name = name
        self.balance = balance
        self.account = account
        
    def Deposit(self, amount : float):
        if amount > 0.0:
            self.balance += amount
        else:
            return "There is no money to add in your bank account"
        
    def Withdrawn(self, amount : float):
        if amount <= self.balance:
            return self.balance - amount
        else:
            return "You dont have enough money to continue the withdraw"
        
    def Your_Balance(self):
        if not self.balance:
            return "There is any money in your bank account"
        else:
            return self.balance
        
    def __str__(self):
        return f"Hi Mr/Mrs {self.name}, this is your account number {self.account} with a balance of {self.balance} dolars."
    
    
class SavingsAccount(BankAccount):
    def __init__(self, name : str, balance : float, account : str, taxes : float):
        super().__init__(name, balance, account)
        self.taxes = taxes
        self.new_balance = None
        
    def Apply_taxes(self):
        tax_amount = self.balance * (self.taxes / 100)
        self.new_balance = self.balance + tax_amount
        return f"the new amount is {self.new_balance}"
    
    def __str__(self):
        return super().__str__() + f"In addition this account have a new balance with taxes: {self.new_balance}"
    
class CurrentAccount(BankAccount):
    def __init__(self, name : str, balance : float, account : str, overdraft : float):
        super().__init__(name, balance, account)
        self.overdraft = overdraft
        
    def Withdrawn(self, amount : float):
        if amount <= self.balance + self.overdraft:
            self.balance -= amount
            return f"Your new balance is {self.balance}"
        else:
            return "You dont have enough money to continue the withdraw"
        
    def Available_overdraft(self):
        return f"You have available an overdraft of {self.overdraft}"

bank = BankAccount("John Doe", 1000, "123-456-789")
savings = SavingsAccount("Jane Doe", 2000, "987-654-321", 2)
current = CurrentAccount("Jim Beam", 500, "456-789-123", 300)
print(bank)
print(savings.Apply_taxes())
print(current.Withdrawn(700))


# Ejercicio 2: Sistema de Vehículos con Herencia
# Contexto: Concesionaria que maneja diferentes tipos de vehículos.
# Requisitos:
# Crea clase base Vehiculo con:
#   Atributos:
#     - marca: str
#     - modelo: str
#     - año: int
#     - precio: float
#   
#   Métodos:
#     1. __init__(self, marca: str, modelo: str, año: int, precio: float)
#     2. calcular_impuesto(self) -> float
#        - Retorna precio * 0.10 (10% base)
#     3. obtener_info(self) -> str
#        - Retorna descripción básica
#     4. __str__(self) -> str

# Crea clase Auto(Vehiculo):
#   Atributos adicionales:
#     - num_puertas: int
#   
#   Métodos:
#     1. __init__(self, marca: str, modelo: str, año: int, precio: float, num_puertas: int)
#     2. calcular_impuesto(self) -> float
#        - Si num_puertas > 4: precio * 0.12
#        - Sino: usa impuesto del padre (super().calcular_impuesto())

# Crea clase Moto(Vehiculo):
#   Atributos adicionales:
#     - cilindrada: int (cc)
#   
#   Métodos:
#     1. __init__(self, marca: str, modelo: str, año: int, precio: float, cilindrada: int)
#     2. calcular_impuesto(self) -> float
#        - Si cilindrada > 500: precio * 0.08
#        - Sino: precio * 0.05

# Crea clase Camion(Vehiculo):
#   Atributos adicionales:
#     - capacidad_carga: float (toneladas)
#   
#   Métodos:
#     1. __init__(self, marca: str, modelo: str, año: int, precio: float, capacidad: float)
#     2. calcular_impuesto(self) -> float
#        - precio * 0.15 (siempre 15% para camiones)

# Crea función calcular_impuestos_flota(vehiculos: list[Vehiculo]) -> float:
#   - Recibe lista de vehículos (polimorfismo)
#   - Calcula suma total de impuestos de todos
#   - Demuestra que funciona con cualquier tipo de vehículo


class Vehicule:
    def __init__(self, brand : str, model : str, year : int, price : float):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        
    def calculate_taxes(self) -> float:
        return self.price * 0.10
    
    def car_info(self) ->str:
        return f"Car brand: {self.brand} model: {self.model}"
    
    def __str__(self):
        return f"Information: With a price of : {self.price} with have a {self.brand} {self.model} from {self.year} year"
    
class Auto(Vehicule):
    def __init__(self, brand : str, model : str, year : int, price : float, doors : int):
        super().__init__(brand, model, year, price)
        self.doors = doors
        
    def calculate_taxes_son(self):
        if self.doors > 4:
            return self.price * 0.12
        else:
            new_taxes = super().calculate_taxes()
            return new_taxes
        
class Moto(Vehicule):
    def __init__(self, brand : str, model : str, year : int, price : float, displacement : int):
        super().__init__(brand, model, year, price)
        self.displacement = displacement
        
    def calculate_taxes_son_2(self):
        if self.displacement > 500:
            return self.price * 0.08
        else:
            return self.price * 0.05
        
class Truck(Vehicule):
    def __init__(self, brand : str, model : str, year : int, price : float, load_capacity : float):
        super().__init__(brand, model, year, price)
        self.load_capacity = load_capacity
        
    def calculate_taxes_son_3(self):
        return self.price * 0.15
    
def calculate_taxes_fleet(vehicules : list):
    total_taxes = 0.0
    for vehicule in vehicules:
        if isinstance(vehicule, Auto): # verificar si el objeto es igual a las clases de nombre Auto, Moto o Truck
            total_taxes += vehicule.calculate_taxes_son()
        elif isinstance(vehicule, Moto):
            total_taxes += vehicule.calculate_taxes_son_2()
        elif isinstance(vehicule, Truck):
            total_taxes += vehicule.calculate_taxes_son_3()
    return total_taxes

vehicles = [
    Auto("Toyota", "Corolla", 2020, 20000, 4),
    Moto("Yamaha", "YZF-R3", 2019, 5000, 321),
    Truck("Ford", "F-150", 2018, 30000, 2.5)
]
print(f"The total taxes of the fleet is: {calculate_taxes_fleet(vehicles)}")


# Ejercicio 3: Composición - Sistema de Computadoras
# Contexto: Tienda de computadoras que ensambla equipos con componentes.
# Requisitos:
# Crea clases para componentes:

# Clase Procesador:
#   Atributos: marca: str, modelo: str, nucleos: int, precio: float
#   Métodos: __init__(), __str__()
class Processor:
    def __init__(self, brand : str, model : str, core : int, price : float):
        self.brand = brand
        self.model = model 
        self.core = core
        self.price = price
        
    def __str__(self):
        return f"The computer brand: {self.brand}, model: {self.model}, {self.core} cores, with a price around: {self.price}."

# Clase MemoriaRAM:
#   Atributos: capacidad_gb: int, velocidad_mhz: int, precio: float
#   Métodos: __init__(), __str__()

class Ram:
    def __init__(self, capacity : int, mhz : int, price : float):
        self.capacity = capacity
        self.mhz = mhz
        self.price = price
        
    def __str__(self):
        return f"General Info: Capacity: {self.capacity} and, with clock speed arroud: {self.mhz}. Market price: {self.price}"

# Clase DiscoDuro:
#   Atributos: capacidad_gb: int, tipo: str ("SSD" o "HDD"), precio: float
#   Métodos: __init__(), __str__()

class HardDrive:
    def __init__(self, capacity : int, type_drive : str, price : float):
        self.capacity = capacity
        self.type_drive = type_drive
        self.price = price
        
    def __str__(self):
        return f"Hard Drive Info: Capacity: {self.capacity}, Type: {self.type_drive}, Price: {self.price}"

# Crea clase Computadora usando composición:
#   Atributos:
#     - procesador: Procesador
#     - ram: MemoriaRAM
#     - disco: DiscoDuro
#     - nombre: str
#   
#   Métodos:
#     1. __init__(self, nombre: str, procesador: Procesador, ram: MemoriaRAM, disco: DiscoDuro)
#     2. calcular_precio_total(self) -> float
#        - Suma precio de todos los componentes
#     3. obtener_especificaciones(self) -> str
#        - Retorna string con todas las especificaciones
#     4. es_gaming(self) -> bool
#        - Retorna True si: procesador.nucleos >= 6 AND ram.capacidad_gb >= 16 AND disco.tipo == "SSD"
#     5. __str__(self) -> str 

class Computer:
    def __init__(self, processor : str, ram : int, disk : int, name : str):
        self.new_data1 = Processor(processor,  model="Generic", core=8, price=300.0)
        self.new_data2 = Ram(ram, mhz=3200, price=150.0)
        self.new_data3 = HardDrive(disk, type_drive="SSD", price=200.0)
        self.name = name
        
    def Total_taxes(self):
        total_price = self.new_data1.price + self.new_data2.price + self.new_data3.price
        return total_price
    
    def Information(self):
        return f"Computer Name: {self.name}\nProcessor: {self.new_data1.model}\nRAM: {self.new_data2.capacity}\nHard Drive: {self.new_data3.capacity}"
    
    def Is_gaming(self):
        if self.new_data1.core >= 6 and self.new_data2.capacity >= 16 and self.new_data3.type_drive == "SSD":
            return True
        else:
            return False
        
    def __str__(self):
        return f"Computer {self.name} with total price of: {self.Total_taxes()}"
    
menu = Computer("i7-9700K", 8, 512, "Lenovo")
print(menu.Total_taxes())
print(menu.Information())
print(menu.Is_gaming())
print(menu)
        

# Ejercicio 4: Herencia Múltiple Niveles - Sistema de Empleados
# Contexto: Empresa con jerarquía de empleados y roles específicos.
# Requisitos:
# Crea jerarquía de 3 niveles:

# Nivel 1 - Clase base Persona:
#   Atributos: nombre: str, edad: int, identificacion: str
#   Métodos: __init__(), obtener_info() -> str, __str__()
class Person:
    def __init__(self, name : str, age : int, iden : str):
        self.name = name
        self.age = age
        self.iden = iden
        
    def Info(self) -> str:
        return f"Person Name: {self.name}, Age: {self.age}, ID: {self.iden}"
    
    def __str__(self):
        return f"{self.name} - {self.iden}"

# Nivel 2 - Clase Empleado(Persona):
#   Atributos adicionales: salario: float, departamento: str, años_experiencia: int
#   Métodos:
#     1. __init__() - llama a super().__init__()
#     2. calcular_bono_experiencia(self) -> float
#        - años_experiencia * 100
#     3. obtener_info() -> str
#        - Extiende el del padre con info de empleado
class Employee(Person):
    def __init__(self, name : str, age : int, iden : str, salary : float, department : str, years_experience : int):
        super().__init__(name, age, iden)
        self.salary = salary
        self.department = department
        self.years_experience = years_experience
        
    def Calculate_bonus_experience(self) -> float:
        return self.years_experience * 100
    
    def Info(self) -> str:
        parent_info = super().Info()
        return f"{parent_info}, Salary: {self.salary}, Department: {self.department}, Years of Experience: {self.years_experience}"
    

# Nivel 3a - Clase Gerente(Empleado):
#   Atributos adicionales: equipo: list[str] (nombres de empleados a cargo)
#   Métodos:
#     1. __init__() - llama a super().__init__(), equipo inicia vacío
#     2. agregar_subordinado(self, nombre: str) -> None
#     3. calcular_bono_gerencia(self) -> float
#        - 500 por cada persona en el equipo
#     4. calcular_salario_total(self) -> float
#        - salario + bono_experiencia + bono_gerencia
class Manager(Employee):
    def __init__(self, name : str, age : int, iden : str, salary : float, department : str, years_experience : int):
        super().__init__(name, age, iden, salary, department, years_experience)
        self.team = []
        
    def Add_subordinate(self, name : str) -> None:
        self.team.append(name)
        
    def Calculate_bonus_management(self) -> float:
        return len(self.team) * 500
    
    def Calculate_total_salary(self) -> float:
        bonus_experience = self.Calculate_bonus_experience() # capturando el valor del metodo de la clase padre
        bonus_management = self.Calculate_bonus_management()
        return self.salary + bonus_experience + bonus_management

# Nivel 3b - Clase Desarrollador(Empleado):
#   Atributos adicionales: lenguajes: list[str], proyectos_completados: int
#   Métodos:
#     1. __init__() - llama a super().__init__()
#     2. agregar_lenguaje(self, lenguaje: str) -> None
#     3. calcular_bono_proyectos(self) -> float
#        - proyectos_completados * 200
#     4. calcular_salario_total(self) -> float
#        - salario + bono_experiencia + bono_proyectos

class Developer(Employee):
    def __init__(self, name : str, age : int, iden : str, salary : float, department : str, years_experience : int, projects_completed : int):
        super().__init__(name, age, iden, salary, department, years_experience)
        self.languages = []
        self.projects_completed = projects_completed
    def Add_language(self, language : str) -> None:
        self.languages.append(language)
    def Calculate_bonus_projects(self) -> float:
        return self.projects_completed * 200
    def Calculate_total_salary(self) -> float:
        bonus_experience = self.Calculate_bonus_experience()
        bonus_projects = self.Calculate_bonus_projects()
        return self.salary + bonus_experience + bonus_projects
    
manager = Manager("Alice", 40, "MGR123", 8000, "Ventas", 10)
manager.Add_subordinate("Bob")
manager.Add_subordinate("Charlie")
print(manager.Info())
print(f"Total Salary: ${manager.Calculate_total_salary()}")

# Ejercicio 5: Sistema de Productos con Polimorfismo (Integrador)
# Contexto: E-commerce con diferentes tipos de productos y cálculo de envío.
# Requisitos:
# Crea clase base Producto:
#   Atributos: nombre: str, precio: float, peso_kg: float
#   Métodos:
#     1. __init__()
#     2. calcular_costo_envio(self) -> float
#        - Básico: peso_kg * 2.0
#     3. calcular_precio_final(self) -> float
#        - precio + costo_envio
#     4. __str__()

class Product:
    def __init__(self, name : str, price : float, weight : float):
        self.name = name
        self.price = price 
        self.weight = weight
        
    def delivery_cost(self) -> float:
        basic = self.weight * 2.0
        return basic
    
    def total_price(self) -> float:
        delivery = self.delivery_cost()
        self.price += delivery
        return self.price
    
    def __str__(self):
        return f"The product: {self.name} including delivery the total price is: {self.price}"
        

# Crea ProductoElectronico(Producto):
#   Atributos adicionales: garantia_meses: int
#   Métodos:
#     1. __init__()
#     2. calcular_costo_envio(self) -> float
#        - Sobrescribe: peso_kg * 3.0 (envío especial para electrónicos)
#     3. tiene_garantia_extendida(self) -> bool
#        - Retorna True si garantia_meses >= 24

class ElectronicProduct(Product):
    def __init__(self, name : str, price : float, weight : float, warranty_months : int):
        super().__init__(name, price, weight)
        self.warranty_months = warranty_months
        
    def delivery_cost(self) -> float:
        special_delivery = self.weight * 3.0
        return special_delivery
    
    def extended_warranty(self) -> bool:
        if self.warranty_months >= 24:
            return True
        else:
            return False


# Crea ProductoFragil(Producto):
#   Atributos adicionales: es_muy_fragil: bool
#   Métodos:
#     1. __init__()
#     2. calcular_costo_envio(self) -> float
#        - Si es_muy_fragil: peso_kg * 5.0
#        - Sino: peso_kg * 3.5
class Fragile(Product):
    def __init__(self, name : str, price : float, weight : float, is_fragile : bool):
        super().__init__(name, price, weight)
        self.is_fragile = is_fragile
        
    def fragile_delivery_cost(self) -> float:
        if self.is_fragile == True:
            Fragile_delivery = self.weight * 5.0
            return Fragile_delivery
        else:
            Fragile_delivery = self.weight * 3.5
            return Fragile_delivery
            
# Crea ProductoLibro(Producto):
#   Atributos adicionales: num_paginas: int, autor: str
#   Métodos:
#     1. __init__()
#     2. calcular_costo_envio(self) -> float
#        - peso_kg * 1.5 (envío económico para libros)
class BookProduct(Product):
    def __init__(self, name : str, price : float, weight : float, pages : int, autor : str):
        super().__init__(name, price, weight)
        self.pages = pages
        self.autor = autor
        
    def book_delivery(self) -> float:
        total = self.weight + 1.5
        return total

# Crea clase Carrito usando composición:
#   Atributos: productos: list[Producto]
#   Métodos:
#     1. __init__()
#     2. agregar_producto(self, producto: Producto) -> None
#     3. calcular_subtotal(self) -> float
#        - Suma de todos los producto.precio (sin envío)
#     4. calcular_total_envio(self) -> float
#        - Suma de todos los calcular_costo_envio() (polimorfismo)
#     5. calcular_total_final(self) -> float
#        - subtotal + total_envio
#     6. obtener_resumen(self) -> str
#        - Retorna resumen detallado con:
#          * Lista de productos
#          * Subtotal
#          * Costo de envío
#          * Total final

class ShoppingCart:
    def __init__(self):
        self.products = []
        
    def Add_product(self, product : Product) -> None:
        self.products.append(product)
        
    def Subtotal(self) -> float:
        subtotal = 0.0
        for product in self.products:
            subtotal += product.price
        return subtotal
    
    def Total_delivery(self) -> float:
        total_delivery = 0.0
        for product in self.products:
            total_delivery += product.delivery_cost()
        return total_delivery
    
    def Final_total(self) -> float:
        subtotal = self.Subtotal()
        delivery = self.Total_delivery()
        return subtotal + delivery
    
    def Summary(self) -> str:
        product_list = "\n".join([str(product) for product in self.products])
        subtotal = self.Subtotal()
        delivery = self.Total_delivery()
        final_total = self.Final_total()
        return f"Products:\n{product_list}\nSubtotal: {subtotal}\nDelivery Cost: {delivery}\nFinal Total: {final_total}"
cart = ShoppingCart()
electronic = ElectronicProduct("Laptop", 1000.0, 2.5, 24)
fragile = Fragile("Vase", 150.0, 1.0, True)
book = BookProduct("Python Programming", 50.0, 0.5, 300, "John Doe")
cart.Add_product(electronic)
cart.Add_product(fragile)
cart.Add_product(book)
print(cart.Summary())

# 📖 Ejercicios de Lectura de Código

# Ejercicio 6: Análisis de Herencia Problemática
# Analiza este código e identifica los problemas:

# Problema 1: 
class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, nombre: str, raza: str):
        self.raza = raza  # ¿Qué falta? al no llamar al supper(). no se esta declarando los atributos de la clase padre
    
    def ladrar(self):
        print(f"{self.nombre} dice guau")  # ¿Funcionará?, No, porque el attributo nombre no esta definido o no existe en la clase perro

# Problema 2: Herencia cuando debería ser composición
class Motor:
    def __init__(self, hp: int):
        self.hp = hp

class Auto(Motor):  # ¿Es correcto? Auto "es-un" Motor? creo que no NO, Auto "tiene-un" Motor asi debria ser
    # ejemplo correcto:
    # class Auto:
    #     def __init__(self, marca: str, motor: Motor):
    #         self.marca = marca
    #         self.motor = motor
    def __init__(self, marca: str, hp: int):
        super().__init__(hp)
        self.marca = marca

# Problema 3: Sobrescritura incorrecta
class Calculadora:
    def sumar(self, a: float, b: float) -> float:
        return a + b

class CalculadoraCientifica(Calculadora):
    def sumar(self, a: float, b: float, c: float) -> float:  # ¿Problema? cambiar la firma del método sobrescrito puede causar confusión y errores al llamar al método desde una instancia de la clase base.
        return a + b + c

# Problema 4: Herencia profunda innecesaria
class A:
    pass

class B(A):
    pass

class C(B):
    pass

class D(C):
    pass

class E(D):  # Demasiados niveles de herencia, puede complicar el mantenimiento y la lectura del código. No es una buena práctica.
    pass

# Preguntas:
# ¿Por qué es crítico llamar a super().__init__()?
# ES de extrema importancia ya que es una parte vital en Herencia ya que asi se trabaja con los atributos de la clase padre.

# ¿Cuándo usar herencia vs composición?  # herencia se usa cuando la relacion es tiene un con la clase hija, pero cuando es un, es mejor hacerla compuesta y asi ayuda a la legibilitad del codigo.

# ¿Qué problemas causa cambiar la firma de un método sobrescrito? NO es una buena practica ya que sobre escribir el metodo de la clase padre puede llegar a dar errores, solo hazlo cuando se necesite y con cuidado ya que no es una buena practica.

# ¿Cuántos niveles de herencia son aceptables? es una buena practica tener 2  o 3 maximo niveles de herencia.



# Ejercicio 7: Refactorización - Composición vs Herencia
# Este código usa herencia incorrectamente. Refactorízalo usando composición:

class Direccion:
    def __init__(self, calle: str, ciudad: str):
        self.calle = calle
        self.ciudad = ciudad

class Persona(Direccion):  # ¿Persona "es-una" Dirección? no lo es, entonces seria compuesto
    def __init__(self, nombre: str, calle: str, ciudad: str):
        super().__init__(calle, ciudad)
        self.nombre = nombre
    
    def obtener_ubicacion(self) -> str:
        return f"{self.calle}, {self.ciudad}"
    
# correjido:

class Address:
    def __init__(self, street : str, city : str):
        self.street = street
        self.city = city
        
class Person:
    def __init__(self, name : str, address : Address):
        self.name = name
        self.address = address
        
    def Get_location(self) -> str:
        return f"{self.address.street}, {self.address.city}"


# 🧪 Evaluación Teórica

# Pregunta 1
# Explica la diferencia entre herencia y composición. Da un ejemplo del mundo real de cada uno.
# ¿Cuándo deberías usar herencia y cuándo composición?
# en herencia se usa la relacion tiene un, que es decir la clasae hija le pertenece ala clase padre, ejemplo un carro tiene un modelo, nombre, año entonces la clase seria carro y sus atributos modelo, nombre, año....
# Composicion, se usa cuando la relacion es un, ejemplo un motor no es un carro, pero un carro tiene un motor, entonces la clase carro tendria como atributo una clase motor.

# Pregunta 2
# ¿Qué es polimorfismo? Explica cómo permite que diferentes clases respondan al mismo método.
# Da un ejemplo práctico de polimorfismo en una aplicación web.
# ES un concepto importante en POO se da cuando varias clases reacionan de diferentes maneras con un mismo metodo, un ejemplo de esto en la programacio web
# tenes una api que maneja datos en la web de varios clientes(clases) que hacen una peticion y se llama a un solo metodo que es get_dashboard, todos tienen el mismo metodo pero
# se va aser un dashboard diferente por cada cliente(clases).

# Pregunta 3
# ¿Qué hace super() y por qué es importante usarlo en clases derivadas?
# ¿Qué pasa si no llamas a super().__init__() en una clase hija?
# A la hora de usar herencia es importante heredar los atributos del padre a la clase hija y esto se hace con super() con ella los atributos de el padre van a estar declarados en la clase hija.
# si no se llama a super().__init__()  en la clase hija se puede llevar a errores de calculo y inesperados.



# Reflexión personal:
# ¿Qué fue lo más difícil?
# Sobreescribir un metodo, no lo entendi al 100, aunq me parece que no es una buena practica, me puedes corregir si estoy mal.

# ¿Entendiste cuándo usar herencia vs composición?
# si correcto

# ¿Cuánto tiempo real te tomó?
# 7 horas

# ¿Qué concepto necesitas repasar?
# el concepto de sobreescribir metodos


# 🎯 Objetivo de mañana (Día 8): List comprehensions, generadores y funciones lambda
