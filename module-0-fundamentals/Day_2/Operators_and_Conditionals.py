# 🚀 DÍA 2 - Módulo 0: Operadores y Control de Flujo

# 📚 Teoría Concisa 

# Operadores en Python
# Los operadores permiten realizar operaciones entre valores y variables.

# Operadores Aritméticos:
# + (suma), - (resta), * (multiplicación), / (división), // (división entera), % (módulo/resto), ** (potencia)

# Operadores de Comparación:
# == (igual), != (diferente), > (mayor), < (menor)
# >= (mayor o igual), <= (menor o igual)

# Operadores Lógicos:
# and (y), or (o), not (no)

# Operadores de Asignación Compuesta:
# +=, -=, *=, /=, //=, %=, **=

# Control de Flujo - Condicionales:
# if: ejecuta código si la condición es True
# elif: alternativa si la condición anterior fue False
# else: se ejecuta si ninguna condición anterior fue True

# Buenas prácticas:
# Usa paréntesis para claridad en condiciones complejas
# Evita comparaciones redundantes (if variable == True → if variable) solo en el caso de la variable tenga un valor booleano
# Prefiere guard clauses (validaciones tempranas) sobre anidamiento profundo, osea la anidacion mas grande de primero
# Usa operador ternario para asignaciones simples: valor = x if condicion else y
# operador ternario:
x = 10
resultado = "par" if x % 2 == 0 else "impar"
print(resultado)  # par

# Errores comunes:
# Confundir = con == en condiciones
# Olvidar los dos puntos : después de if/elif/else
# Indentación incorrecta (Python usa espacios, no llaves)
# Comparar tipos incompatibles (ej: "5" > 3 puede dar resultados inesperados)

# Ejemplo práctico - Guard Clauses:

# ❌ Mal - anidamiento profundo
def process_order(order):
    if order is not None:
        if order.get("items"):
            if order.get("total") > 0:
                return "Procesando orden"
    return "Orden inválida"

# ✅ Bien - guard clauses (validación temprana)
def process_order_clean(order):
    if order is None:
        return "Orden inválida"
    if not order.get("items"):
        return "Orden sin items"
    if order.get("total") <= 0:
        return "Total inválido"
    return "Procesando orden"

# Documentación oficial: https://docs.python.org/3/tutorial/controlflow.html


# 💻 Ejercicios Acumulativos
# Ejercicio 1: Calculadora de Descuentos con Reglas de Negocio
# Contexto: Sistema de e-commerce con diferentes niveles de descuento según monto y membresía.
# Requisitos:
# Variables: precio_producto, cantidad, es_miembro_premium (bool)
# Calcula el subtotal (precio * cantidad)
# Aplica descuentos según estas reglas:
#   - Si es miembro premium: 15% de descuento
#   - Si el subtotal > $500 y NO es premium: 10% de descuento
#   - Si el subtotal > $1000 y NO es premium: 12% de descuento
#   - Si no aplica ninguna: 0% de descuento
# Calcula el total final y muestra: subtotal, descuento aplicado (%), monto ahorrado, total final

# Ejemplo de output esperado:
# Subtotal: $600.00
# Descuento aplicado: 15% (miembro premium)
# Ahorro: $90.00
# Total final: $510.00
def discount_Calculator(Product_price, Amount, premium):
    subtotal = Product_price * Amount
    if subtotal > 1000 and not premium:
        discount = subtotal * 0.12
        return f"Subtotal: {subtotal}, discount: 12%, Save: {discount}, Total: {subtotal - discount}"
    elif subtotal > 500 and not premium:
        discount = subtotal * 0.10
        return f"Subtotal: {subtotal}, discount: 10%, Save: {discount}, Total: {subtotal - discount}"
    elif premium:
        discount = subtotal * 0.15
        return f"Subtotal: {subtotal}, discount: 15%, Save: {discount}, Total: {subtotal - discount}"
    else:
        return f"Subtotal: {subtotal}"
         
print(discount_Calculator(500, 3, True ))


# Ejercicio 2: Validador de Credenciales de Usuario
# Contexto: Sistema de registro que valida credenciales antes de crear cuenta.
# Requisitos:
# Variables: username, password, age, email
# Valida TODAS estas condiciones (usa guard clauses):
#   - username debe tener entre 4 y 20 caracteres
#   - password debe tener al menos 8 caracteres
#   - age debe ser >= 18
#   - email debe contener "@" y "."
# Si TODAS las validaciones pasan: imprime "✅ Usuario registrado exitosamente"
# Si alguna falla: imprime el mensaje de error específico y detén la validación
# Usa operadores lógicos (and, or, not) apropiadamente
# Casos de prueba:
# username = "user", password = "pass123", age = 17, email = "test@mail.com"
# username = "john_doe", password = "secure123", age = 25, email = "john@example.com"
def validator(Username, password, age, email):
    validator1 = len(Username) + 1
    validator2 = len(password) + 1
    if validator1 > 4 and validator1 < 20 and validator2 > 8 and age >= 18 and "@" and "." in email and "." in email:
        return f"Username: {Username}, Password: {password}, Age: {age}, email: {email}"
    return "Error"
print(validator("Ana hernandez", "hbckdvkdnvknd", 44, "feralieh@gmail.com"))


# Ejercicio 3: Sistema de Clasificación de Productos por Stock
# Contexto: Dashboard de inventario que alerta sobre niveles de stock.
# Requisitos:
# Variables: nombre_producto, stock_actual, stock_minimo, stock_maximo
# Clasifica el estado del stock:
#   - Si stock_actual == 0: "❌ AGOTADO - Reordenar urgente"
#   - Si stock_actual < stock_minimo: "⚠️ BAJO - Reordenar pronto"
#   - Si stock_minimo <= stock_actual <= stock_maximo: "✅ ÓPTIMO"
#   - Si stock_actual > stock_maximo: "📦 EXCESO - Reducir pedidos"
# Calcula el porcentaje de stock actual respecto al máximo
# Sugiere acción (cantidad a pedir o reducir)

def Inventory_Alert(Product_Name, Actual_stock, Minimun_Stock, Maximun_Stock):
    porcent_actual_stock_vs_maximun = (Actual_stock / Maximun_Stock) * 100
    Optimal_range = (Maximun_Stock - Minimun_Stock)
    if Minimun_Stock <= Actual_stock <= Maximun_Stock:
        return "Optimal Stock "
    elif porcent_actual_stock_vs_maximun >= Optimal_range:
        return "We need to reduce the product"
    elif porcent_actual_stock_vs_maximun <= Optimal_range:
        return "We need to order"
    elif Actual_stock == 0:
        return "Out of stock, order now"
    elif Actual_stock < Minimun_Stock:
        return "Actual stock low, order now"
    elif Actual_stock > Maximun_Stock:
        return "We need to reduce stock"
    
print(Inventory_Alert("Laptop Hp", 10, 2, 10))



# Ejercicio 4: Calculadora de Precio con IVA y Propinas (Integrador)
# Contexto: Sistema de punto de venta para restaurante.
# Requisitos:
# Variables: precio_base, pais, incluye_propina (bool), calidad_servicio (str: "excelente", "bueno", "regular")
# Usa el diccionario de IVA del Día 1: España 21%, México 16%, USA 8%, default 10%
# Si incluye_propina es True:
#   - "excelente": 20% de propina
#   - "bueno": 15% de propina
#   - "regular": 10% de propina
# Calcula en orden: subtotal → IVA → propina (sobre subtotal, no sobre total con IVA)
# Retorna diccionario con: base, iva_amount, propina_amount, total
# Valida que pais exista y calidad_servicio sea válida

def Restaurant_Calculator(Price, country, include_taxes, service):
    Iva = {"name" : "spain", "taxes" : 0.21}, {"name" : "mexico", "taxes" : 0.16}, {"name" : "USA", "taxes" : 0.08}
    for Ivas in Iva:
        if include_taxes and country in Ivas["name"] and service == "excelent":
            subtotal = Price
            Iva_tax =  Ivas["taxes"]
            tip_gift = subtotal * 0.20
            Total = subtotal + Iva_tax + tip_gift
            return {"base" : subtotal , "Iva amount" : Iva_tax, "Tip amount" : tip_gift, "Total" : Total}
        
        if include_taxes and country in Ivas["name"] and service == "good":
            subtotal = Price
            Iva_tax =  Ivas["taxes"]
            tip_gift = subtotal * 0.15
            Total = subtotal + Iva_tax + tip_gift
            return {"base" : subtotal , "Iva amount" : Iva_tax, "Tip amount" : tip_gift, "Total" : Total}
        
        if include_taxes and country in Ivas["name"] and service == "regulary":
            subtotal = Price
            Iva_tax =  Ivas["taxes"]
            tip_gift = subtotal * 0.10
            Total = subtotal + Iva_tax + tip_gift
            return {"base" : subtotal , "Iva amount" : Iva_tax, "Tip amount" : tip_gift, "Total" : Total}
            
        
print(Restaurant_Calculator(15000, "spain", True, "good"))



# Ejercicio 5: Sistema de Aprobación de Créditos (Lógica Compleja)
# Contexto: Banco evalúa solicitudes de crédito con múltiples criterios.
# Requisitos:
# Variables: edad, ingreso_mensual, historial_crediticio (str: "excelente", "bueno", "malo"), deuda_actual, monto_solicitado
# Criterios de aprobación (TODOS deben cumplirse):
#   - Edad entre 21 y 65 años
#   - Ingreso mensual >= $1500
#   - Historial crediticio NO sea "malo"
#   - deuda_actual <= 40% del ingreso mensual
#   - monto_solicitado <= 5 veces el ingreso mensual
# Calcula la tasa de interés según historial:
#   - "excelente": 8% anual
#   - "bueno": 12% anual
#   - Si no califica: N/A
# Output: "APROBADO" o "RECHAZADO" + razón específica + tasa de interés si aplica

def Credit_Apply(Age, Month_earn, History, Owe, Request):
    if Age >= 21 and Age <= 65 and Month_earn >= 1500 and History != "malo" and Owe <= Month_earn * 0.4 and Request <= (Owe * 5):
        if History == "excelente":
            return "APROBADO con una tasa de interes del 8% anual"
        elif History == "bueno":
            return "APROBADO con una tasa de interes del 12% anual"
        else:
            return "RECHAZADO"   
    else:
        return "RECHAZADO"
print(Credit_Apply(55, 350000, "excelente", 100000, 1000))

# 📖 Ejercicios de Lectura de Código
# Ejercicio 6: Refactorización de Condicionales Anidados
# Analiza este código y refactorízalo usando guard clauses:

def verificar_pedido(pedido, usuario):
    if pedido is not None:
        if usuario is not None:
            if usuario.get("activo"):
                if pedido.get("total") > 0:
                    if pedido.get("items"):
                        return "Pedido válido"
                    else:
                        return "Sin items"
                else:
                    return "Total inválido"
            else:
                return "Usuario inactivo"
        else:
            return "Usuario no encontrado"
    else:
        return "Pedido no encontrado"
    
# repuesta del ejercicio 6
def verificar_pedido(pedido, usuario):
    if pedido is not None:
        return "Pedido no encontrado"
    if usuario is not None:
        return "Usuario no encontrado"
    if usuario.get("activo"):
        return "Usuario inactivo"
    if pedido.get("total") > 0:
        return "Total inválido"
    if pedido.get("items"):
        return "Sin items"
    else:
        return "Pedido válido"
print(verificar_pedido("sink", "eric"))
                      

# Preguntas:
# ¿Cuántos niveles de anidamiento tiene?
# tiene 5 niveles de anidamiento

# ¿Cómo mejorarías la legibilidad?
# Usando if, elif, else, usando Snake_case y variables descriptivas



# Ejercicio 7: Debugging de Operadores y Condiciones
# Este código tiene errores lógicos. Encuéntralos sin ejecutar:

precio = 100
descuento = 0.15
precio_final = precio - descuento  # ¿Está bien este cálculo? 
# NO, porque para calcular un descuento se usa el operardor de multiplicacion (*)

# edad = "25"
# puede_votar = edad >= 18  # ¿Funcionará correctamente?
# No funciona porque no se puede comparar un string con un integer

# stock = 5
# reorden = stock < 10 and stock > 0 or stock == 0  # ¿Qué evalúa realmente?
# Evalua si el stock es menor que 10 y si mayor que 0 o igual a 0.

# es_premium = True
# descuento_aplicado = es_premium == True  # ¿Es redundante?
# si lo es porque es_premium ya tiene un valor bool.

# total = 100
# if total = 150:  # ¿Qué error tiene esta línea?
    # print("Total actualizado")
# Se le a dado un valor a total cuando ya lo tiene, cuando lo que se quiere es comparar.


# 🧪 Evaluación Teórica

# Pregunta 1
# Explica la diferencia entre los operadores == y = en Python. ¿Qué pasa si usas = dentro de un if?
# La diferencia es que == es un operador de comparacion y = es uno de asigacion, si lo usamos dentro de if se le va a dar un nuevo valor 
# a la variable.

# Pregunta 2
# ¿Qué son las "guard clauses" y por qué mejoran la legibilidad del código?
# Los guard clauses en palabras sencillas son validaciones tempranas, se ponen las validaciones mas grandes al principio y asi evitar
# anidamiento excesivo.

# Pregunta 3
# Explica el orden de evaluación de los operadores lógicos (and, or, not).
# ¿Qué es el "short-circuit evaluation"? Da un ejemplo práctico donde esto sea importante.
# el operador not esta en la parte mas alta de jerarquia se validad a el primero, el or en la parte media y el and es el ultimo de la jerarquia.
# Short-circuit: evita evaluar condiciones innecesarias en pocas palabras condiciones en una sola linea.


# Reflexión personal:
# ¿Qué fue lo más difícil?
# el analisis de los ajercicios

# ¿Entendiste las guard clauses?
# si es muy importante hacer validaciones tempranas y asi evitar anidamientos excivos

# ¿Cuánto tiempo real te tomó?
# Me tomo unas 4 horas el dia 2

# ¿Qué concepto necesitas repasar?
# El concepto de short-circuit evaluation


# 🎯 Objetivo de mañana (Día 3): Bucles (for, while) y manejo de colecciones (listas, diccionarios)
