# 🚀 DÍA 15 - Módulo 0: Algoritmos de Sorting - Ordenamiento Eficiente

# 📚 Teoría 

# Algoritmos de Ordenamiento (Sorting) El ordenamiento es fundamental en ciencias de la computación.
# Diferentes algoritmos tienen diferentes trade-offs de tiempo, espacio y casos de uso.

# Algoritmos Simples - O(n²):
# 
# 1. Bubble Sort:
#    - Compara elementos adyacentes e intercambia si están desordenados
#    - Repite hasta que no haya intercambios
#    - Tiempo: O(n²) peor caso, O(n) mejor caso (ya ordenado)
#    - Espacio: O(1)
#    - Estable: Sí
#
# 2. Selection Sort:
#    - Encuentra el mínimo y lo coloca al inicio
#    - Repite para el resto del arreglo
#    - Tiempo: O(n²) siempre
#    - Espacio: O(1)
#    - Estable: No (implementación estándar)
#
# 3. Insertion Sort:
#    - Inserta cada elemento en su posición correcta en la parte ordenada
#    - Tiempo: O(n²) peor caso, O(n) mejor caso
#    - Espacio: O(1)
#    - Estable: Sí
#    - Eficiente para arreglos pequeños o casi ordenados

# Algoritmos Eficientes - O(n log n):
#
# 4. Merge Sort:
#    - Divide el arreglo en mitades recursivamente
#    - Ordena cada mitad
#    - Fusiona las mitades ordenadas
#    - Tiempo: O(n log n) siempre (consistente)
#    - Espacio: O(n) - necesita arreglo temporal
#    - Estable: Sí
#    - Divide & Conquer
#
# 5. Quick Sort:
#    - Elige un pivote
#    - Particiona: menores a la izquierda, mayores a la derecha
#    - Ordena recursivamente cada partición
#    - Tiempo: O(n log n) promedio, O(n²) peor caso
#    - Espacio: O(log n) stack recursivo
#    - Estable: No (implementación estándar)
#    - In-place
#    - Generalmente más rápido en práctica

# Comparación de Complejidades:
# Algoritmo      | Mejor    | Promedio  | Peor     | Espacio | Estable
# ---------------|----------|-----------|----------|---------|--------
# Bubble Sort    | O(n)     | O(n²)     | O(n²)    | O(1)    | Sí
# Selection Sort | O(n²)    | O(n²)     | O(n²)    | O(1)    | No
# Insertion Sort | O(n)     | O(n²)     | O(n²)    | O(1)    | Sí
# Merge Sort     | O(n lgn) | O(n lgn)  | O(n lgn) | O(n)    | Sí
# Quick Sort     | O(n lgn) | O(n lgn)  | O(n²)    | O(lgn)  | No

# Estabilidad:
# Un algoritmo es estable si mantiene el orden relativo de elementos iguales.
# Ejemplo: [(2,a), (1,b), (2,c)] → Estable: [(1,b), (2,a), (2,c)]
#                                  Inestable: [(1,b), (2,c), (2,a)]

# Cuándo usar cada algoritmo:
# Bubble/Selection/Insertion: 
#   - Arreglos muy pequeños (< 10 elementos)
#   - Datos casi ordenados (Insertion)
#   - Educativo/simplicidad
#
# Merge Sort:
#   - Necesitas estabilidad
#   - Complejidad garantizada O(n log n)
#   - Sorting externo (datos en disco)
#   - Linked lists
#
# Quick Sort:
#   - Performance general (caso promedio)
#   - In-place importante (poco espacio)
#   - Datos aleatorios
#   - Implementación de sorted() en muchos lenguajes

# Optimizaciones comunes:
# - Quick Sort: pivote aleatorio o mediana de tres
# - Hybrid: Quick/Merge + Insertion para subarreglos pequeños
# - TimSort (Python): Merge + Insertion optimizado

# Buenas prácticas:
# Usa sorted() de Python en producción (TimSort optimizado)
# Implementa sorting para aprender, no reinventar
# Considera estabilidad si importa orden de iguales
# Para objetos, usa key function: sorted(lista, key=lambda x: x.precio)
# Profiling antes de optimizar

# Errores comunes:
# No considerar estabilidad cuando importa
# Quick Sort con pivote fijo en datos ordenados (O(n²))
# No considerar uso de memoria (Merge Sort usa O(n))
# Reinventar sorting en producción
# No aprovechar optimizaciones de built-ins

# Ejemplo práctico - Bubble Sort:

def bubble_sort(arr):
    """
    Ordena arreglo usando Bubble Sort.
    Optimizado: detiene si no hay intercambios
    """
    n = len(arr)
    for i in range(n):
        intercambiado = False
        # Últimos i elementos ya están ordenados
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambiado = True
        # Si no hubo intercambios, ya está ordenado, esto es para no hacer iteraciones innecesarias
        if not intercambiado:
            break
    return arr

# Ejemplo - Merge Sort:

def merge_sort(arr):
    """Ordena usando Merge Sort (Divide & Conquer)."""
    if len(arr) <= 1:
        return arr
    # Dividir
    mid = len(arr) // 2
    izq = merge_sort(arr[:mid])
    der = merge_sort(arr[mid:])
    
    # Conquistar (fusionar)
    return merge(izq, der)

def merge(izq, der):
    """Fusiona dos arreglos ordenados."""
    resultado = []
    i = j = 0
    
    # Mezclar mientras ambos tengan elementos
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:  # <= para estabilidad
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    
    # Agregar elementos restantes
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    
    return resultado

# Ejemplo - Quick Sort:

def quick_sort(arr):
    """Ordena usando Quick Sort."""
    if len(arr) <= 1:
        return arr
    
    pivote = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    
    # Ordenar recursivamente y combinar
    return quick_sort(menores) + iguales + quick_sort(mayores)

# Ejemplo - Quick Sort in-place:

def quick_sort_inplace(arr, bajo=0, alto=None):
    """Quick Sort in-place (modifica arreglo original)."""
    if alto is None:
        alto = len(arr) - 1
    
    if bajo < alto:
        pi = partition(arr, bajo, alto)
        quick_sort_inplace(arr, bajo, pi - 1)
        quick_sort_inplace(arr, pi + 1, alto)
    
    return arr

def partition(arr, bajo, alto):
    """Particiona arreglo y retorna índice del pivote."""
    pivote = arr[alto]
    i = bajo - 1
    
    for j in range(bajo, alto):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    return i + 1

# Documentación: https://docs.python.org/3/howto/sorting.html


# 💻 Ejercicios Acumulativos

# Ejercicio 1: Implementación de Bubble Sort
# Contexto: Entender funcionamiento de algoritmos simples.
def Bubble_sort(Data):
    n = len(Data)
    for i in range(n):
        swap = False
        for j in range(0, n - i - 1):
            if Data[j] > Data[j + 1]:
                Data[j], Data[j + 1] = Data[j + 1], Data[j]
                swap = True
        if not swap:
            break
    return Data

import random
Datas = [random.randint(0, 1000) for _ in range(800)]
print(Bubble_sort(Datas))


# Ejercicio 2: Implementación de Merge Sort
# Contexto: Algoritmo divide & conquer fundamental.
def Merge_sort2(Darr):
    if len(Darr) <= 1:
        return Darr
    medium = len(Darr) // 2
    left = Darr[:medium]
    right = Darr[medium:]
    left_sort = Merge_sort2(left)
    right_sort = Merge_sort2(right)
    return new_merge(left_sort, right_sort)

def new_merge(list1, lits2):
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(lits2):
        if list1[i] <= lits2[j]:
            result.append(list1[i])
            i = i + 1
        else:
            result.append(lits2[j])
            j = j + 1
            
    result.extend(list1[i:])
    result.extend(lits2[j:])
    return result

print(Merge_sort2(Datas))


# Ejercicio 3: Implementación de Quick Sort
# Contexto: Algoritmo in-place muy eficiente.
def Quick_sort2(Xarr):
    if len(Xarr) <= 1:
        return Xarr
    Pivot = Xarr[len(Xarr) // 2]
    left = [ x for x in Xarr if x < Pivot]
    medium = [ x for x in Xarr if x == Pivot]
    right = [ x for x in Xarr if x > Pivot]
    return Quick_sort2(left) + medium + Quick_sort2(right)
print(Quick_sort2(Datas))
    

# Ejercicio 4: Análisis Comparativo de Algoritmos
# Contexto: Benchmarking de diferentes algoritmos de busqueda.
# Requisitos: Implementa sistema de benchmarking:
def Benchmark(data):
    import time
    start = time.time()
    Bubble_sort(data.copy())
    end = time.time()
    results = end - start
    print(f"Bubble Sort:, {results}, seconds")
    
    start = time.time()
    Merge_sort2(data.copy())
    end = time.time()
    results2 = end - start
    print(f"Merge Sort:, {results2}, seconds")
    
    start = time.time()
    Quick_sort2(data.copy())
    end = time.time()
    results3 = end - start
    print(f"Quick Sort:, {results3}, seconds")
    
Benchmark(Datas)


# Ejercicio 5: Sistema de Ordenamiento de Objetos (Integrador)
# Contexto: Ordenar estructuras complejas con múltiples criterios.
# Requisitos: Implementa sistema completo de sorting para objetos:

class Producto:
    """Representa un producto."""
    def __init__(self):
        self.warhouse = []
        self.next_id = 1
    
    def Storage(self, name, price, stock, category):
        if not name or not price or not stock or not category:
            return "There is a missing piece of information"
        name = name.lower()
        category = category.lower()
        self.warhouse.append({"ID": self.next_id, "Name": name, "Price": price, "Stock": stock, "Category": category})
        result_id = self.next_id
        self.next_id += 1
        return f"The Product: {name} with a ID: {result_id} was successfuly added"
        
    def Sorting(self, obj):
        if not obj:
            return "I need a item to sort"
        new_list = sorted(self.warhouse, key=lambda x:x[obj])
        return new_list

data = Producto()
data.Storage("telephone", 256, 5, "tecnology")
data.Storage("hax", 25, 10, "tools")
data.Storage("garbage", 6, 15, "home")
data.Storage("stove", 2560, 2, "home")
print(data.Sorting("Price"))


# 📖 Ejercicios de Lectura de Código

# Ejercicio 6: Identificar Algoritmo y Problemas
# Analiza estos códigos:

# Código 1: ¿Qué algoritmo es?
def misterio_sort_1(arr):
    """¿Bubble, Selection o Insertion?"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
# Respuesta: Es el algoritmo de ordenamiento burbuja

# Código 2: Quick Sort problemático
def quick_sort_malo(arr):
    """¿Qué problema tiene?"""
    if len(arr) <= 1:
        return arr
    pivote = arr[0]  # Siempre primer elemento
    # implementacion correcta pivot = arr[len(arr) // 2]
    menores = [x for x in arr[1:] if x < pivote]
    mayores = [x for x in arr[1:] if x >= pivote]
    
    return quick_sort_malo(menores) + [pivote] + quick_sort_malo(mayores)
# ¿Qué pasa con arr = [1, 2, 3, 4, 5]? el pivote no puede ser el primer elemento si no que es el elemento del medio de la lista,
# para que el pueda agrupar los elementos de la derecha y izquierda, en este caso arr lo podra agrupar los elementos de la izquierda,
# porque no los tiene.

# Código 3: Merge ineficiente
def merge_malo(izq, der):
    """¿Qué problema de eficiencia tiene?"""
    resultado = []
    while izq and der:  # Mientras ambos tengan elementos
        if izq[0] <= der[0]:
            resultado.append(izq.pop(0))  # pop(0) es O(n)
        else:
            resultado.append(der.pop(0))
    resultado.extend(izq)
    resultado.extend(der)
    return resultado
# Tiene varios problemas de eficiencia, 1- si la lista esta vacia la implementacion igualmente usara recursos.
# 2- si no hay una variable i y j con sus contadores la implementacion causara un stackoverflow

# Código 4: Recursión sin límite
def merge_sort_peligroso(arr):
    """¿Qué pasa con listas muy grandes?"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    izq = merge_sort_peligroso(arr[:mid])
    der = merge_sort_peligroso(arr[mid:])
    
    return merge(izq, der)
# ¿Stack overflow? ¿Cuándo?
# Cuando implementa mergesort se tiene que tener encuenta la memoria porque recursion usa mucha memoria y puede llegar a un punto, 
# en el que se puede provocar stackoverflow por el numero de llamadas ilimitadas que la funcion se llama a si misma.

# Preguntas:
# ¿Cómo identificar cada algoritmo por su estructura?
# bubble sort se puede identifcar porque se comparan los 2 numeros y se intercambian si el primero es mayor que el segundo.
# Merge Sort se reconoce facilmente por la frase divide y venceras, se implementan 2 funciones y para funcionar una llama a la otra.
# QuickSort se idendifica porque divide en 3 bloques la lista(menor, igual, mayor) y al final los une

# ¿Qué hace que un algoritmo sea estable o inestable?
# Lo que hace estable a un algoritmo es el numero de veces que su entrada crece y su metodo para ordenar

# ¿Cuál es el peor caso para Quick Sort?
# El peor caso para quicksort es cuando se implementa con 2 bucles for o con recursividad


# Ejercicio 7: Refactorización y Optimización
# Refactoriza estos códigos:

# Código 1: Bubble Sort sin optimización
def bubble_sin_optimizar(arr):
    """Siempre hace n² comparaciones."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
# Agrega: detención temprana, reducir rango
def bubble_optimizar(arr):
    """Siempre hace n² comparaciones."""
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break
    return arr

# Código 2: Quick Sort con pivote fijo
def quick_sort_mejorable(arr):
    """Pivote siempre último."""
    if len(arr) <= 1:
        return arr
    pivote = arr[-1]
    menores = [x for x in arr[:-1] if x <= pivote]
    mayores = [x for x in arr[:-1] if x > pivote]
    return quick_sort_mejorable(menores) + [pivote] + quick_sort_mejorable(mayores)
# Mejora: pivote aleatorio o mediana de tres
def quick_sort(arr):
    """Pivote siempre último."""
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivote]
    igual = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    return quick_sort_mejorable(menores) + igual + quick_sort_mejorable(mayores)

# Código 3: Merge Sort que crea muchas listas
def merge_sort_v1(arr):
    """Crea nuevas listas constantemente."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    izq = merge_sort_v1(arr[:mid])
    der = merge_sort_v1(arr[mid:])
    return merge(izq, der)
# Considera: versión in-place o híbrida
def merge_sort_v3(arr):
    """Crea nuevas listas constantemente."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    izq = merge_sort_v1(arr[:mid])
    der = merge_sort_v1(arr[mid:])
    return merge3(izq, der)
def merge3(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result



# 🧪 Evaluación Teórica

# Pregunta 1
# Compara Merge Sort y Quick Sort. ¿Cuáles son las ventajas y desventajas de cada uno?
# ¿Cuándo usarías Merge Sort sobre Quick Sort y viceversa?
# las ventajas de merge sort es que es un algoritmo estable, tiene una complejidad de O(n log n) en el peor caso y es eficiente para ordenar listas enlazadas o grandes cantidades de datos que no caben en memoria. 
# Las desventajas son que requiere espacio adicional O(n) para la fusión y puede ser más lento que Quick Sort en la práctica debido a la sobrecarga de la fusión.
# Usaria Merge Sort sobre Quick Sort cuando necesito estabilidad, cuando estoy ordenando listas enlazadas o cuando estoy trabajando con grandes cantidades de datos que no caben en memoria. Usaría Quick Sort sobre Merge Sort cuando necesito un algoritmo in-place, cuando estoy ordenando arreglos pequeños o cuando quiero un rendimiento promedio más rápido.

# Pregunta 2
# Explica qué significa que un algoritmo de sorting sea "estable".
# Un algoritmo de sorting es estable si mantiene el orden relativo de los elementos iguales. Es decir, si dos elementos antes y despues de ordenarse tienen el mismo valor a la par. Esto es importante cuando se ordenan objetos con múltiples atributos.

# Pregunta 3
# ¿Por qué Quick Sort puede ser O(n²) en el peor caso? Que es un algoritmo de ordenamiento in-place, y que es un algoritmo de ordenamiento no in-place?
# Quick Sort puede ser O(n²) en el peor caso cuando el pivote elegido es el elemento más pequeño o más grande en cada partición.
# Un algoritmo de ordenamiento in-place es aquel que ordena los elementos sin usar espacio adicional(los ordena en la misma lista). 
# Un algoritmo de ordenamiento no in-place, requiere espacio adicional a la hora de ordenar, como Merge Sort que necesita espacio O(n) para la fusión osea otra lista para hacer la funsion..



# 🎯 Objetivo de mañana (Día 16): Binary Search - Búsqueda eficiente en datos ordenados

# Conexión con proyectos finales:
# 💰 Cost Optimizer: Ordenar recursos por costo, buscar eficientemente, top N más caros
# 🔐 SecureVault: Ordenar secrets por prioridad, búsqueda rápida en logs ordenados por timestamp