# 🚀 DÍA 16 - Módulo 0: Binary Search - Búsqueda Eficiente

# 📚 Teoría Concisa 

# Binary Search (Búsqueda Binaria): Algoritmo eficiente para buscar en datos ORDENADOS, 
# divide el espacio de búsqueda a la mitad en cada iteración.

# Concepto fundamental:
# Si el arreglo está ordenado, puedes descartar la mitad de los datos
# en cada paso comparando con el elemento del medio.

# Algoritmo básico:
# 1. Encuentra elemento del medio
# 2. Si medio == objetivo: encontrado
# 3. Si objetivo < medio: busca en mitad izquierda
# 4. Si objetivo > medio: busca en mitad derecha
# 5. Repite hasta encontrar o agotar espacio

# Complejidad:
# Tiempo: O(log n) - divide espacio a la mitad cada vez
# Espacio: O(1) iterativo, O(log n) recursivo (stack)

# Comparación con búsqueda lineal:
# Lineal: O(n) - revisa cada elemento
# Binaria: O(log n) - en 1,000,000 elementos → ~20 comparaciones

# Prerequisito crítico:
# Los datos DEBEN estar ordenados. Si no lo están, ordena primero
# (costo O(n log n)) o usa búsqueda lineal (O(n)).

# Variantes de Binary Search:
# 1. Búsqueda exacta: encontrar valor específico
# 2. Lower bound: primer elemento >= objetivo
# 3. Upper bound: primer elemento > objetivo
# 4. First occurrence: primera aparición en duplicados
# 5. Last occurrence: última aparición en duplicados
# 6. Closest element: elemento más cercano al objetivo
# 7. Peak finding: encontrar máximo local
# 8. Search in rotated array: en arreglo rotado ordenado

# Template genérico de Binary Search:
# def binary_search_template(arr, condicion):
#     izq, der = 0, len(arr) - 1
#     resultado = -1
#     
#     while izq <= der:
#         mid = izq + (der - izq) // 2  # Evita overflow
#         
#         if condicion(arr[mid]):
#             resultado = mid
#             # Ajustar búsqueda según necesidad
#             izq = mid + 1
#         else:
#             # Mover al otro lado
#             der = mid - 1
#     
#     return resultado

# Casos edge importantes:
# - Arreglo vacío
# - Un solo elemento
# - Elemento no existe
# - Todos elementos iguales
# - Duplicados

# Aplicaciones prácticas:
# - Búsqueda en bases de datos indexadas
# - Autocompletado
# - Búsqueda en rangos de fechas
# - Encontrar versión con bug (git bisect)
# - Optimización (encontrar valor óptimo)
# - Scheduling problems

# Problemas que usan Binary Search:
# - Búsqueda en matriz 2D ordenada
# - Encontrar raíz cuadrada
# - Capacity to ship packages
# - Koko eating bananas
# - Median of two sorted arrays

# Buenas prácticas:
# Usa mid = izq + (der - izq) // 2 (no (izq + der) // 2)
# Clarifica límites: ¿inclusivo o exclusivo?
# Maneja casos edge primero
# Considera duplicados si existen
# Verifica que datos estén ordenados

# Errores comunes:
# Olvidar que datos deben estar ordenados
# Infinite loop por mal ajuste de izq/der
# Off-by-one errors en límites
# Overflow con (izq + der) // 2 en otros lenguajes
# No considerar duplicados

# Ejemplo práctico - Binary Search básico:

def binary_search(arr, objetivo):
    if len(arr) == 0:
        return "The array is empty."
    if len(arr) == 1:
        return arr[0]
    if objetivo not in arr:
        # esto evita hacer todo el proceso de búsqueda si el objetivo no está presente,
        # y asi no tiene que recorrer todo el proceso de búsqueda, para saber si esta o no para retornar -1.
        return "The target is not in the array."
    # Ordenado y sin duplicados
    Data = sorted(set(arr))
    izq, der = 0, len(Data) - 1
    while izq <= der:
        mid = izq + (der - izq) // 2 # Evita overflow 
        if arr[mid] == objetivo:
            return mid
        elif arr[mid] < objetivo:
            izq = mid + 1
        else:
            der = mid - 1
    return "The target is not in the array."

# Ejemplo - Binary Search recursivo:

def binary_search_recursivo(arr, objetivo, izq=0, der=None):
    """Versión recursiva de binary search."""
    if der is None:
        der = len(arr) - 1
    
    if izq > der:
        return -1
    
    mid = izq + (der - izq) // 2
    
    if arr[mid] == objetivo:
        return mid
    elif arr[mid] < objetivo:
        return binary_search_recursivo(arr, objetivo, mid + 1, der)
    else:
        return binary_search_recursivo(arr, objetivo, izq, mid - 1)

# Ejemplo - First occurrence (con duplicados):

def first_occurrence(arr, objetivo):
    """Encuentra primera aparición del objetivo."""
    izq, der = 0, len(arr) - 1
    resultado = -1
    
    while izq <= der:
        mid = izq + (der - izq) // 2
        
        if arr[mid] == objetivo:
            resultado = mid
            der = mid - 1  # Sigue buscando a la izquierda
        elif arr[mid] < objetivo:
            izq = mid + 1
        else:
            der = mid - 1
    
    return resultado

# Ejemplo - Lower bound (primer elemento >= objetivo):

def lower_bound(arr, objetivo):
    """
    Encuentra índice del primer elemento >= objetivo.
    Retorna len(arr) si todos son menores.
    """
    izq, der = 0, len(arr)
    
    while izq < der:
        mid = izq + (der - izq) // 2
        
        if arr[mid] < objetivo:
            izq = mid + 1
        else:
            der = mid
    
    return izq

# Ejemplo - Búsqueda en rango de respuestas:

def sqrt_binary_search(n, precision=0.0001):
    """Encuentra raíz cuadrada usando binary search."""
    if n < 0:
        return None
    if n == 0:
        return 0
    
    izq, der = 0, n
    
    while der - izq > precision:
        mid = (izq + der) / 2
        
        if mid * mid > n:
            der = mid
        else:
            izq = mid
    
    return (izq + der) / 2

# Documentación: https://docs.python.org/3/library/bisect.html


# 💻 Ejercicios Acumulativos

# Ejercicio 1: Implementaciones Básicas de Binary Search
import random
arrays = [random.randint(0, 100) for x in range(15)]
def BinarySearch(Array : list, obj : int) -> int | str:
    if len(Array) == 0:
        return 0
    elif len(Array) == 1:
        return Array[0]
    elif obj not in Array:
        return "The target is not in the array"
    Array = sorted(set(Array))
    left, right = 0, len(Array) - 1
    while left <= right:
        medium = left + (right - left) // 2
        if Array[medium] == obj:
            return medium
        elif Array[medium] < obj:
            left = medium + 1
        else:
            right = medium - 1

print(BinarySearch([2, 10, 56, 7, 7], 70))

def BinarySearch2(Array : list, objective : str) -> str | int:
    if len(Array) == 0:
        return "The array is empty"
    elif len(Array) == 1:
        return Array[0]
    elif objective not in Array:
        return - 1
    Array = sorted(set(Array))
    left, right = 0, len(Array) - 1
    while left <= right:
        medium = left + (right - left) // 2
        if Array[medium].replace("", " ") == objective:
            return Array[medium]
        elif Array[medium] < objective:
            left = medium + 1
        else:
            right = medium - 1
            
print(BinarySearch2(["Eric", "Helen", "Alvaro", "Betty", "Zoraida", "Carlos"], "Eric"))

def BinarySearchRecursive(Array : list, obj : int, left = 0, right = None):
    if right is None:
        right = len(Array) - 1
    if left > right:
        return  -1
    medium = left + (right - left) // 2
    if Array[medium] == obj:
        return Array[medium]
    elif Array[medium] < obj:
        return BinarySearchRecursive(Array, obj, medium + 1, right)
    else:
        return BinarySearchRecursive(Array, obj, left, medium - 1)
    
print(BinarySearchRecursive(arrays, 4))
    

# Ejercicio 2: Binary Search recursivo
def RecursiveBinary(arr : list,  obj : int, left = 0, right = None):
    if right is None:
        right = len(arr) - 1
    if len(arr) == 1:
        return arr[0]
    if left > right:
        return -1
    medium = left + (right - left) // 2
    if arr[medium] == obj:
        return medium
    elif arr[medium] < obj:
        return RecursiveBinary(arr, obj, medium + 1, right)
    else:
        return RecursiveBinary(arr, obj, left, medium - 1)
    
print(RecursiveBinary(arrays, 1))


# Ejercicio 3: Binary Search en Problemas de Optimización
# Contexto: Búsqueda de raiz cuadrada de un nuemro
import math, random
def BinarySearchSqrt(Data : list, number : int):
    sqrt_number = math.sqrt(number)
    sqrt_number = int(sqrt_number)
    print(sqrt_number)
    if len(Data) == 0:
        return "There is not data in the list"
    left, right = 0, len(Data) - 1
    Data = sorted(set(Data))
    print(Data)
    while left <= right:
        medium = left + (right - left) // 2
        if Data[medium] == sqrt_number:
            return medium
        elif Data[medium] < sqrt_number:
            left = medium + 1
        else:
            right = medium - 1
    return "I did not found it"
   
data = [random.randint(1, 10) for x in range(10)] 
print(BinarySearchSqrt(data, 8))



# Ejercicio 4: Sistema de Búsqueda en Logs y Eventos (Integrador)
# Contexto: Sistema que busca eficientemente en logs ordenados por timestamp.

class LogEntry:
    def __init__(self, timestamp, message):
        self.timestamp = timestamp
        self.message = message
def search_logs(logs, target_timestamp):
    """Busca el log más cercano al timestamp objetivo."""
    izq, der = 0, len(logs) - 1
    resultado = None
    
    while izq <= der:
        mid = izq + (der - izq) // 2
        
        if logs[mid].timestamp == target_timestamp:
            return logs[mid]
        elif logs[mid].timestamp < target_timestamp:
            resultado = logs[mid]  # Posible candidato
            izq = mid + 1
        else:
            der = mid - 1
    
    return resultado  # Retorna el log más cercano menor o igual al objetivo


data = [LogEntry(i, f"Log {i}") for i in range(0, 100, 10)]
print(search_logs(data, 25).message)  # Debería retornar "Log 20"
print(search_logs(data, 30).message) 



# 📖 Ejercicios de Lectura de Código

# Ejercicio 6: Análisis de Implementaciones

# Código 1: Binary search con overflow potencial
def binary_search_malo_1(arr, objetivo):
    """¿Qué problema tiene en otros lenguajes?"""
    izq, der = 0, len(arr) - 1
    
    while izq <= der:
        mid = (izq + der) // 2  # Puede causar overflow en Java/C++
        
        if arr[mid] == objetivo:
            return mid
        elif arr[mid] < objetivo:
            izq = mid + 1
        else:
            der = mid - 1
    
    return -1
# ¿Cómo arreglarlo?
# la solución es usar mid = izq + (der - izq) // 2, que evita el riesgo de overflow al calcular el punto medio.

# Código 2: Loop infinito
def binary_search_malo_2(arr, objetivo):
    """¿Por qué puede hacer loop infinito?"""
    izq, der = 0, len(arr)  # Nota: der = len(arr)
    
    while izq < der:
        mid = (izq + der) // 2
        
        if arr[mid] == objetivo:
            return mid
        elif arr[mid] < objetivo:
            izq = mid  # ¿Problema aquí?
        else:
            der = mid
    
    return -1
# ¿Cuándo entra en loop infinito?
# va  entrar en unloop porque el valor no va a cambiar y siempre va a ser el mismo(menor que derecha) por lo tanto se va a generar un loop infinito.

# Código 3: Off-by-one error
def first_occurrence_malo(arr, objetivo):
    """Tiene off-by-one error."""
    izq, der = 0, len(arr) - 1
    resultado = -1
    
    while izq < der:  # ¿Debería ser <=?
        mid = izq + (der - izq) // 2
        
        if arr[mid] == objetivo:
            resultado = mid
            der = mid - 1
        elif arr[mid] < objetivo:
            izq = mid + 1
        else:
            der = mid - 1
    
    return resultado
# ¿Qué casos falla?
# Falla en casos donde el objetivo es el primer elemento del arreglo o cuando todos los elementos son iguales al objetivo.


# Preguntas:
# ¿Por qué mid = izq + (der - izq) // 2 es mejor?
#  Porque evita el riesgo de overflow que puede ocurrir con mid = (izq + der) // 2 en lenguajes con enteros limitados.

# ¿Cuándo usar izq <= der vs izq < der?
# Usar izq <= der cuando quieres incluir ambos extremos en la búsqueda, y izq < der cuando quieres excluir el extremo derecho (o izquierdo) para evitar off-by-one errors.

# ¿Cómo evitar loops infinitos en binary search?
# Asegurándote de que los índices se actualicen correctamente en cada iteración.



# Ejercicio 7: Refactorización y Optimización
# Refactoriza estos códigos:

# Código 1: Búsqueda lineal que debería ser binaria
def encontrar_en_ordenado(arr, objetivo):
    """Usa búsqueda lineal en arreglo ordenado."""
    for i, val in enumerate(arr):
        if val == objetivo:
            return i
    return -1
# Refactoriza usando binary search - O(n) → O(log n)
def encontrar_en_ordenado(arr, objetivo):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0 if arr[0] == objetivo else -1
    left, right = 0, len(arr) - 1
    while left <= right:
        medium = left + (right - left) // 2
        if arr[medium] == objetivo:
            return medium
        elif arr[medium] < objetivo:
            left = medium + 1
        else:
            right = medium - 1
    return -1

# Código 3: Encontrar rango sin binary search
def encontrar_rango_v1(arr, objetivo):
    """Busca linealmente."""
    primero = -1
    ultimo = -1
    
    for i in range(len(arr)):
        if arr[i] == objetivo:
            if primero == -1:
                primero = i
            ultimo = i
    
    return (primero, ultimo)
# Refactoriza usando binary search - O(n) → O(log n)
def encontrar_rango_v2(arr, objetivo):
    """Usa binary search para lower_bound y upper_bound."""
    def lower_bound(arr, objetivo):
        izq, der = 0, len(arr)
        while izq < der:
            mid = izq + (der - izq) // 2
            if arr[mid] < objetivo:
                izq = mid + 1
            else:
                der = mid
        return izq
    
    def upper_bound(arr, objetivo):
        izq, der = 0, len(arr)
        while izq < der:
            mid = izq + (der - izq) // 2
            if arr[mid] <= objetivo:
                izq = mid + 1
            else:
                der = mid
        return izq
    
    primero = lower_bound(arr, objetivo)
    ultimo = upper_bound(arr, objetivo) - 1
    
    if primero <= ultimo and ultimo < len(arr) and arr[primero] == objetivo and arr[ultimo] == objetivo:
        return (primero, ultimo)
    return (-1, -1)



# 🧪 Evaluación Teórica

# Pregunta 1
# Explica por qué binary search es O(log n). ¿Qué significa "log n" en términos prácticos?
# "Log n" significa que el número de comparaciones crece de manera logarítmica con el tamaño del arreglo.
# En términos prácticos, esto significa que incluso para arreglos muy grandes, 
# el número de comparaciones necesarias para encontrar un elemento es relativamente pequeño. Por ejemplo, para un arreglo de 1,000,000 elementos, binary search haría como máximo alrededor de 20 comparaciones (porque 2^20 ≈ 1,000,000). Esto es mucho más eficiente que una búsqueda lineal que podría requerir hasta 1,000,000 comparaciones en el peor caso.

# Si tienes 1,000,000 elementos, ¿cuántas comparaciones máximo hace binary search?
# Binary search haría como máximo alrededor de 20 comparaciones para un arreglo de 1,000,000 elementos, porque 2^20 ≈ 1,000,000.

# Pregunta 2
# ¿Por qué binary search requiere que los datos estén ordenados? ¿Qué pasa si no lo están?
# Binary search requiere que los datos estén ordenados porque el algoritmo se basa en la capacidad de descartar la mitad del espacio de búsqueda en cada paso.
# Si los datos no están ordenados, no puedes determinar si el objetivo está a la izquierda o a la derecha del punto medio, lo que hace que el algoritmo no funcione correctamente. En un arreglo no ordenado.



# 🎯 Próximos pasos: Continuar con Linux CLI Essentials (Día 17)

# Conexión con proyectos finales:
# 💰 Cost Optimizer: Búsqueda binaria en recursos ordenados por costo, encontrar top N más caros eficientemente
# 🔐 SecureVault: Búsqueda en logs de auditoría por timestamp, encontrar secrets en rangos de 
