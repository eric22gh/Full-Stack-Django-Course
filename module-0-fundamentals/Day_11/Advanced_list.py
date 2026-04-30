# 🚀 DÍA 11 - Módulo 0: Listas Avanzadas y Operaciones Eficientes

# 📚 Teoría Concisa

# Operaciones Avanzadas con Las listas son la estructura de datos más versátil de Python, pero su uso eficiente requiere
# conocer sus operaciones internas y complejidades.

# Slicing avanzado:
# lista[inicio:fin:paso]
# lista[::-1]  # Invertir lista
# lista[::2]   # Elementos en posiciones pares
# lista[1::2]  # Elementos en posiciones impares

# Operaciones in-place vs creación de nuevas listas:
# lista.sort() vs sorted(lista)
# lista.reverse() vs lista[::-1]
# lista.extend(otra) vs lista = lista + otra

# Métodos importantes y sus complejidades:
# append(x)      - O(1) - agrega al final
# insert(i, x)   - O(n) - inserta en posición i
# pop()          - O(1) - elimina último
# pop(i)         - O(n) - elimina el dato en la posición i
# remove(x)      - O(n) - elimina primera ocurrencia
# index(x)       - O(n) - busca posición de x
# count(x)       - O(n) - cuenta ocurrencias
# sort()         - O(n log n) - ordena in-place
# reverse()      - O(n) - invierte in-place

# List unpacking:
# a, b, c = [1, 2, 3]
# primero, *resto = [1, 2, 3, 4, 5]
# *inicio, ultimo = [1, 2, 3, 4, 5]

# Técnicas avanzadas:
# Two pointers: usar dos índices para recorrer
# Sliding window: ventana deslizante para subarreglos
# In-place modifications: modificar sin crear nueva lista
# List as stack: append() y pop() para LIFO
# List as queue: usar collections.deque para FIFO eficiente

# Operaciones con múltiples listas:
# zip(): combina listas elemento por elemento
# zip(*listas): transpose (descomprime)
# itertools.chain(): concatena múltiples iterables

# Buenas prácticas:
# Usa list comprehensions para transformaciones simples
# Evita modificar lista mientras iteras sobre ella
# Para búsquedas frecuentes, convierte a set o dict
# append() es O(1), insert(0, x) es O(n) - usa deque para queue
# Usa slicing para copiar: nueva = original[:]
# Ordena una vez y reutiliza si es posible

# Errores comunes:
# Modificar lista durante iteración
# Usar insert(0, x) repetidamente (ineficiente)
# Comparar listas grandes con in (usa set)
# No considerar que slicing crea copias
# Copiar listas con = en vez de [:] o copy()

# Ejemplo práctico - Two Pointers:

def eliminar_duplicados_ordenada(lista):
    """Elimina duplicados de lista ordenada in-place(no crea otra lista) usando two pointers."""
    if not lista: # si la lista esta vacia
        return 0
    # Puntero de escritura
    write = 1
    # Puntero de lectura
    for read in range(1, len(lista)): # read es el indice
        if lista[read] != lista[read - 1]:
            lista[write] = lista[read]
            write += 1
    return write  # Nueva longitud


# Ejemplo - Sliding Window:
def max_suma_subarray(lista, k):
    """Encuentra suma máxima de subarray de longitud k."""
    if len(lista) < k:
        return None
    # Suma de la primera ventana 
    suma_ventana = sum(lista[:k]) # crea otra lista
    max_suma = suma_ventana
    # Deslizar ventana
    for i in range(len(lista) - k):
        suma_ventana = suma_ventana - lista[i] + lista[i + k]
        max_suma = max(max_suma, suma_ventana)
    
    return max_suma

# Ejemplo - List Unpacking:

# Básico
numeros = [1, 2, 3, 4, 5]
primero, segundo, *resto = numeros
print(primero)  # 1
print(resto)    # [3, 4, 5]

# Intercambiar valores sin variable temporal
a, b = 10, 20
a, b = b, a  # a=20, b=10

# Desempaquetar en funciones
def procesar(x, y, z):
    return x + y + z

datos = [1, 2, 3]
resultado = procesar(*datos)  # Desempaqueta lista como argumentos

# Documentación oficial: https://docs.python.org/3/tutorial/datastructures.html

# 💻 Ejercicios Acumulativos

# Ejercicio 1: Operaciones Avanzadas de Slicing
# Contexto: Procesamiento de lotes de datos.
# Requisitos: Dada esta lista de transacciones:
transacciones = [
    {"id": 1, "monto": 100, "tipo": "ingreso"},
    {"id": 2, "monto": 50, "tipo": "egreso"},
    {"id": 3, "monto": 200, "tipo": "ingreso"},
    {"id": 4, "monto": 75, "tipo": "egreso"},
    {"id": 5, "monto": 150, "tipo": "ingreso"},
    {"id": 6, "monto": 30, "tipo": "egreso"},
    {"id": 7, "monto": 120, "tipo": "ingreso"},
    {"id": 8, "monto": 90, "tipo": "egreso"},
]

# Usa slicing para obtener:
# 1. ultimas_3: últimas 3 transacciones
print(transacciones[5:])
# 2. primeras_5: primeras 5 transacciones
print(transacciones[:5])
# 3. cada_dos: cada segunda transacción (índices pares: 0, 2, 4...)
print(transacciones[1::2])
# 4. invertida: transacciones en orden inverso
transacciones.reverse()
print(transacciones)
# 5. mitad_inferior: primera mitad de la lista
mitad = len(transacciones) // 2
print(transacciones[mitad:])
# 6. mitad_superior: segunda mitad de la lista
print(transacciones[:mitad])
# 7. sin_extremos: todas menos primera y última
print(transacciones[1:7][::-1])

# Crea función procesar_lote(transacciones: list, operacion: str) -> list:
#   - Recibe lista y tipo de operación ("ultimas_3", "invertida", etc.)
#   - Retorna el slice apropiado según la operación
#   - Usa match/case o if/elif
def process(transactions : list, opr : str) -> list | None:
    if not isinstance(transactions, list) and not isinstance(opr, str):
        return "transactions list and opr, must be list and string"
    elif opr.lower() == "last three":
        return transactions[5:]
    elif opr.lower() == "firt three":
        return transactions[:5]
    elif opr.lower() == "each two":
        return transactions[1::2]
    elif opr.lower() == "reverse":
        return transactions[::-1]
    elif opr.lower() == "first half":
        half = len(transactions) // 2
        return transactions[:half]
    elif opr.lower() == "last half":
        return transactions[half:]
    elif opr.lower() == "without extremes":
        return transactions[1:7][::1]
    else:
        return f"I dont recognize that operation: {opr}"
    
print(process(transacciones, "reverse"))

# Ejercicio 2: Two Pointers - Fusión de Listas Ordenadas
# Contexto: Combinar resultados ordenados de múltiples fuentes.
# Requisitos: Implementa estas funciones usando técnica de two pointers:

# 1. fusionar_ordenadas(lista1: list[int], lista2: list[int]) -> list[int]
#    - Ambas listas vienen ordenadas
#    - Fusiona manteniendo orden
#    - Usa dos punteros (índices) para recorrer ambas listas
#    - O(n + m) - no uses sort()
def funsion(list1 : list[int], list2 : list[int]) -> list[int]:
    list1.extend(list2)
    if not list1:
        return 0
    writer = 1
    for read in range(1, len(list1)):
        if list1[read] < list1[read - 1]:
            list1[writer] = list1[read]
            writer += 1
    return list1

# 2. eliminar_duplicados_inplace(lista: list[int]) -> int
#    - Lista está ordenada
#    - Elimina duplicados modificando la lista original
#    - Retorna nueva longitud
#    - Usa two pointers: read y write
def delete_duplicades(list1 : list[int]) -> int:
    if not list1:
        return 0
    list1.sort()
    writer = 1
    for read in range(1, len(list1)):
        if list1[read] != list1[read - 1]:
            list1[writer] = list1[read]
            writer += 1
    return len(list1)

# 3. mover_ceros_al_final(lista: list[int]) -> None
#    - Mueve todos los 0 al final manteniendo orden de no-ceros
#    - Modifica in-place
#    - Usa two pointers
def move_zeros(list1 : list[int]) -> list[int] | None:
    if not list1:
        return []
    writer = 0
    for read in range(len(list1)):
        if list1[read] != 0: # mueve los numeros diferentes a 0 al inicio de la lista
            list1[writer] = list1[read]
            writer += 1
    for i in range(writer, len(list1)):
        list1[i] = 0
    return list1

# 4. encontrar_par_suma(lista: list[int], objetivo: int) -> tuple | None
#    - Lista está ordenada
#    - Encuentra par de números que sumen objetivo
#    - Usa two pointers: uno al inicio, otro al final
#    - O(n) - no uses bucles anidados

def find_for_sum(list1 : list[int], obj : int) -> tuple | None:
    if not list1:
        return []
    list1.sort()
    writer = 1
    result = []
    for read in range(1, len(list1)):
        if list1[read] + list1[read - 1] == obj:
            result.append([list1[writer], list1[writer + 1]])
            writer += 1
    return result
print(funsion([1, 3, 5], [2, 4, 6]))
print(delete_duplicades([1, 1, 2, 3, 3, 4]))
print(move_zeros([0, 1, 0, 3, 12]))
print(find_for_sum([1, 2, 3, 4, 5], 5))  



# Ejercicio 3: Sliding Window - Análisis de Subarrays
# Contexto: Análisis de métricas en ventanas de tiempo.
# Requisitos: Dada lista de ventas diarias:
ventas_diarias = [120, 150, 200, 180, 90, 110, 160, 140, 190, 210, 170, 130]

# Implementa usando sliding window:

# 1. max_promedio_ventana(ventas: list[float], k: int) -> float
#    - Encuentra ventana de k días con mayor promedio
#    - Retorna el promedio máximo
#    - O(n) - no recalcules suma completa cada vez
def max_average_window(list1 : list[float], k : int) -> float | None:
    if len(list1) < k:
        return None
    sum_window = sum(list1[:k])
    max_average = sum_window / k
    for i in range(len(list1) - k):
        sum_window = sum_window - list1[i] + list1[i + k]
        max_average = max(max_average, sum_window / k)
    return max_average

# 2. ventana_suma_mayor_objetivo(ventas: list[int], objetivo: int) -> int
#    - Encuentra longitud mínima de ventana cuya suma >= objetivo
#    - Retorna longitud (0 si no existe)
#    - Usa ventana de tamaño variable
def window_sum_greater_than_obj(list1 : list[int], obj : int) -> int:
    left = 0
    sum_window = 0
    min_length = float('inf')
    for right in range(len(list1)):
        sum_window += list1[right]
        while sum_window >= obj:
            min_length = min(min_length, right - left + 1)
            sum_window -= list1[left]
            left += 1
    return min_length if min_length != float('inf') else 0

# 3. contar_ventanas_positivas(valores: list[int], k: int) -> int
#    - Cuenta cuántas ventanas de tamaño k tienen suma positiva
#    - Retorna el conteo
def count_positive_windows(list1 : list[int], k : int) -> int:
    if len(list1) < k:
        return 0
    sum_window = sum(list1[:k])
    count = 1 if sum_window > 0 else 0
    for i in range(len(list1) - k):
        sum_window = sum_window - list1[i] + list1[i + k]
        if sum_window > 0:
            count += 1
    return count

# 4. mejor_periodo_ventas(ventas: list[int], k: int) -> tuple[int, int]
#    - Encuentra índices [inicio, fin] de ventana con mayor suma
#    - Retorna tupla (indice_inicio, indice_fin)
def best_sales_period(list1 : list[int], k : int) -> tuple[int, int] | None:
    if len(list1) < k:
        return None
    sum_window = sum(list1[:k])
    max_sum = sum_window
    best_start = 0
    for i in range(len(list1) - k):
        sum_window = sum_window - list1[i] + list1[i + k]
        if sum_window > max_sum:
            max_sum = sum_window
            best_start = i + 1
    return (best_start, best_start + k - 1)

print(max_average_window(ventas_diarias, 3))
print(window_sum_greater_than_obj(ventas_diarias, 500))
print(count_positive_windows(ventas_diarias, 3))
print(best_sales_period(ventas_diarias, 3))

# Ejercicio 4: Rotación y Manipulación In-Place
# Contexto: Operaciones eficientes sin crear copias.
# Requisitos: Implementa estas funciones que modifican listas in-place:

# 1. rotar_derecha(lista: list, k: int) -> None
#    - Rota lista k posiciones a la derecha
#    - [1,2,3,4,5] con k=2 → [4,5,1,2,3]
#    - Modifica in-place, no crea nueva lista
#    - O(n) tiempo, O(1) espacio

def rotate_right(list1 : list, k : int) -> None:
    k = k % len(list1)
    list1[:] = list1[-k:] + list1[:-k]
    list1.reverse()
    list1[:k] = list1[:k][::-1]
    return list1

# 2. rotar_izquierda(lista: list, k: int) -> None
#    - Rota lista k posiciones a la izquierda
#    - [1,2,3,4,5] con k=2 → [3,4,5,1,2]

def rotate_left(list1 : list, k : int) -> None: 
    k = k % len(list1)
    list1[:] = list1[k:] + list1[:k]
    list1.reverse()
    list1[:len(list1) - k] = list1[:len(list1) - k][::-1]
    return list1

# 3. invertir_rango(lista: list, inicio: int, fin: int) -> None
#    - Invierte elementos entre índices inicio y fin (inclusivo)
#    - [1,2,3,4,5] con inicio=1, fin=3 → [1,4,3,2,5]

def reverse_range(list1 : list, start : int, end : int) -> None:
    while start < end:
        list1[start], list1[end] = list1[end], list1[start]
        start += 1
        end -= 1
    return list1

# 4. intercalar_mitades(lista: list) -> None
#    - Intercala primera y segunda mitad
#    - [1,2,3,4,5,6] → [1,4,2,5,3,6]
#    - Asume lista de longitud par
def intercalate_halves(list1 : list) -> None:
    mid = len(list1) // 2
    first_half = list1[:mid]
    second_half = list1[mid:]
    intercalated = []
    for i in range(mid):
        intercalated.append(first_half[i])
        intercalated.append(second_half[i])
    list1[:] = intercalated
    return list1

# 5. reorganizar_pares_impares(lista: list[int]) -> None
#    - Mueve pares al inicio, impares al final
#    - Mantiene orden relativo dentro de cada grupo
#    - [1,2,3,4,5,6] → [2,4,6,1,3,5]
def reorganize_even_odd(list1 : list[int]) -> None:
    even = [x for x in list1 if x % 2 == 0]
    odd = [x for x in list1 if x % 2 != 0]
    list1[:] = even + odd
    return list1

print(rotate_right([1, 2, 3, 4, 5], 2))
print(rotate_left([1, 2, 3, 4, 5], 2))
print(reverse_range([1, 2, 3, 4, 5], 1, 3))
print(intercalate_halves([1, 2, 3, 4, 5, 6]))
print(reorganize_even_odd([1, 2, 3, 4, 5, 6]))



# Ejercicio 5: Procesador de Logs con Operaciones Avanzadas (Integrador)
# Contexto: Sistema que procesa y analiza logs de servidor.
# Requisitos: Dada esta estructura de logs:
logs = [
    {"timestamp": 1000, "nivel": "INFO", "mensaje": "Servidor iniciado", "usuario": "system"},
    {"timestamp": 1001, "nivel": "ERROR", "mensaje": "Fallo en DB", "usuario": "admin"},
    {"timestamp": 1002, "nivel": "INFO", "mensaje": "Request procesado", "usuario": "user1"},
    {"timestamp": 1003, "nivel": "WARNING", "mensaje": "Memoria alta", "usuario": "system"},
    {"timestamp": 1004, "nivel": "ERROR", "mensaje": "Timeout", "usuario": "user2"},
    {"timestamp": 1005, "nivel": "INFO", "mensaje": "Request procesado", "usuario": "user1"},
] * 100  # 600 logs

# Implementa clase ProcesadorLogs:
class ProcesadorLogs:
    def __init__(self, logs: list[dict]):
        """Inicializa con lista de logs."""
        self.logs = logs
    
    def filtrar_por_nivel(self, nivel: str) -> list[dict] | str:
        """ Filtra logs por nivel.Usa list comprehension."""
        if not isinstance(nivel, str):
            return "nivel must be a string"
        elif nivel.upper() not in {"INFO", "ERROR", "WARNING"}:
            return f"nivel must be one of INFO, ERROR, WARNING. Received: {nivel}"
        elif not self.logs:
            return "No logs to filter"
        else:
            return [log for log in self.logs if log["nivel"] == nivel]
        
    
    def ultimos_n_logs(self, n: int) -> list[dict]:
        """ Retorna últimos n logs usando slicing."""
        if not isinstance(n, int) or n < 0:
            return "n must be a non-negative integer"
        elif not n:
            return []
        elif not self.logs:
            return "No logs available"
        else:
            return self.logs[-n:] # si n es mayor a la longitud de logs, retornará todos los logs 
    
    def logs_en_rango(self, inicio: int, fin: int) -> list[dict]:
        """ Retorna logs entre timestamps inicio y fin. Asume logs ordenados por timestamp."""
        if not isinstance(inicio, int) or not isinstance(fin, int):
            return "inicio and fin must be integers"
        elif inicio > fin:
            return "inicio must be less than or equal to fin"
        elif not self.logs:
            return "No logs available"
        else:
            return [log for log in self.logs if inicio <= log["timestamp"] <= fin]
    
    def agrupar_por_usuario(self) -> dict[str, list[dict]]:
        """ Agrupa logs por usuario.Retorna: {usuario: [logs_del_usuario]}"""
        if not self.logs:
            return "No logs available"
        else:
            resultado = {}
            for log in self.logs:
                usuario = log["usuario"]
                if usuario not in resultado:
                    resultado[usuario] = []
                resultado[usuario].append(log)
            return resultado
    
    
    def estadisticas_por_nivel(self) -> dict[str, dict]:
        """Calcula estadísticas por nivel.
        Retorna: { "INFO": {"cantidad": int, "usuarios_unicos": set, "primero": timestamp, "ultimo": timestamp}, "ERROR": {...},}"""
        if not self.logs:
            return "No logs available"
        else:
            resultado = {}
            for log in self.logs:
                nivel = log["nivel"]
                if nivel not in resultado:
                    resultado[nivel] = {"cantidad": 0, "usuarios_unicos": set(), "primero": log["timestamp"], "ultimo": log["timestamp"]}
                resultado[nivel]["cantidad"] += 1
                resultado[nivel]["usuarios_unicos"].add(log["usuario"])
                resultado[nivel]["primero"] = min(resultado[nivel]["primero"], log["timestamp"])
                resultado[nivel]["ultimo"] = max(resultado[nivel]["ultimo"], log["timestamp"])
            return resultado
    
    def resumen_completo(self) -> dict:
        """Genera resumen completo de logs """
        if not self.logs:
            return "No logs available"
        else:
            return {
                "total_logs": len(self.logs),
                "por_nivel": self.estadisticas_por_nivel(),
                "por_usuario": self.agrupar_por_usuario(),
                "logs en rango 1000-1003": self.logs_en_rango(1000, 1003),
                "ultimos 5 logs": self.ultimos_n_logs(5),
                "logs ERROR": self.filtrar_por_nivel("ERROR"),
            }
            

data = ProcesadorLogs(logs)
print(data.resumen_completo())

# 📖 Ejercicios de Lectura de Código

# Ejercicio 6: Análisis de Operaciones de Lista
# Analiza el código e identifica problemas de eficiencia:

# Código 1: Insertar al inicio repetidamente
def construir_lista_malo(n):
    """¿Qué complejidad tiene esto?"""
    resultado = []
    for i in range(n):
        resultado.insert(0, i)  # O(n) cada vez recorre la lista para insertar al inicio
    return resultado
# Complejidad total: O(n) - cada insert es O(n) y se hace n veces
# ¿Cómo optimizar?
# Solución: usar append() y luego reverse() o construir al revés

# Código 2: Modificar lista durante iteración
def eliminar_negativos_malo(lista):
    """¿Qué problema tiene?"""
    for num in lista:
        if num < 0:
            lista.remove(num)  # Modifica mientras itera
    return lista
# ¿Qué puede salir mal?
# Solución: iterar sobre una copia o usar list comprehension para crear nueva lista sin negativos

# Código 3: Copias innecesarias
def procesar_lista_malo(lista):
    """Crea muchas copias."""
    temp1 = lista[:]
    temp2 = temp1[:]
    temp3 = temp2[:]
    resultado = temp3[:]
    return resultado
# ¿Cómo simplificar?
# Solución: si no necesitas modificar, simplemente retorna lista o una copia directa si necesitas modificar sin afectar original

# Código 4: Búsquedas repetidas en lista
def contar_ocurrencias_malo(items, buscar):
    """O(n²) innecesario."""
    resultado = {}
    for item in buscar:
        resultado[item] = items.count(item)  # O(n) cada vez
    return resultado
# ¿Cómo optimizar a O(n)?
# Solución: usar un diccionario para contar ocurrencias en una sola pasada


# Ejercicio 7: Refactorización de Operaciones Ineficientes
# Refactoriza estos códigos usando técnicas eficientes:

# Código 1: Eliminar duplicados manteniendo orden
def eliminar_duplicados_v1(lista):
    """O(n²) - busca en resultado cada vez."""
    resultado = []
    for item in lista:
        if item not in resultado:
            resultado.append(item)
    return resultado
# Refactoriza a O(n) usando set para tracking
def eliminar_duplicados_v2(lista):
    """O(n) - usa set para tracking."""
    resultado = []
    vistos = set()
    for item in lista:
        if item not in vistos:
            resultado.append(item)
            vistos.add(item)
    return resultado

# Código 2: Rotar lista
def rotar_ineficiente(lista, k):
    """Crea muchas listas nuevas."""
    k = k % len(lista)
    return lista[-k:] + lista[:-k]
# Refactoriza para hacerlo in-place
def rotar_eficiente(lista, k):
    """O(n) tiempo, O(1) espacio."""
    k = k % len(lista)
    lista.reverse()
    lista[:k] = lista[:k][::-1]
    lista[k:] = lista[k:][::-1]
    return lista

# Código 3: Encontrar elementos comunes
def elementos_comunes_v1(lista1, lista2):
    """O(n * m) - busca cada elemento."""
    comunes = []
    for item in lista1:
        if item in lista2 and item not in comunes:
            comunes.append(item)
    return comunes
# Refactoriza a O(n + m) usando sets
def elementos_comunes_v2(lista1, lista2):
    """O(n + m) - usa sets."""
    set1 = set(lista1)
    set2 = set(lista2)
    return list(set1.intersection(set2))

# Código 4: Particionar lista
def particionar_v1(lista, pivote):
    """Hace múltiples pasadas."""
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return menores + iguales + mayores
# Refactoriza a una sola pasada
def particionar_v2(lista, pivote):
    """O(n) - una sola pasada."""
    menores = []
    iguales = []
    mayores = []
    for x in lista:
        if x < pivote:
            menores.append(x)
        elif x == pivote:
            iguales.append(x)
        else:
            mayores.append(x)
    return menores + iguales + mayores

# 🧪 Evaluación Teórica

# Pregunta 1
# Explica la diferencia entre operaciones in-place (como sort()) y operaciones que crean nuevas listas (como sorted()).
# ¿Cuándo usarías cada una? ¿Qué ventajas tiene cada enfoque?
# las operaciones in-place como sort() modifican la lista original sin crear una nueva, lo que puede ser mejor para la memoria,
# las operaciones como sorted() crean una nueva lista ordenada, dejando la original intacta. 
# Usaría sort() cuando no necesito conservar el orden original y quiero ahorrar memoria, 
# mientras que usaría sorted() cuando necesito mantener la lista original sin cambios.

# Pregunta 2
# ¿Qué es la técnica de "two pointers" y para qué tipo de problemas es útil?
# Da un ejemplo de un problema que se resuelve eficientemente con two pointers.
# "two pointers" implica usar dos índices para recorrer una lista desde diferentes posiciones (inicio y fin) o en la misma dirección. 
# Es útil para problemas de búsqueda, fusión de listas ordenadas, eliminación de duplicados, etc.

# Pregunta 3
# Explica qué es "sliding window" y cómo funciona.
# ¿Por qué es más eficiente que recalcular desde cero en cada paso?
# "sliding window" es una técnica que mantiene una ventana de tamaño fijo o variable que se desliza a través de la lista.
# En lugar de recalcular la suma o el resultado completo para cada nueva ventana, se actualiza el resultado restando el elemento que sale de la ventana y sumando el nuevo elemento que entra, 
# lo que reduce la complejidad a O(n) en lugar de O(n*k) para recalcular cada vez.


# Reflexión personal:
# ¿Entendiste two pointers y sliding window?
# si, two pointers es una técnica que me parece muy útil para resolver problemas de listas ordenadas o para eliminar duplicados sin crear nuevas listas,
# mientras que sliding window es excelente para problemas de subarrays o métricas en ventanas de tiempo.

# ¿Cuánto tiempo real te tomó?
# unas 8 horas


# 🎯 Objetivo de mañana (Día 12): Stacks y Queues - Implementación y aplicaciones prácticas

# Conexión con proyectos finales:
# 💰 Cost Optimizer: Procesamiento eficiente de listas de recursos AWS, sliding window para análisis temporal
# 🔐 SecureVault: Two pointers para búsquedas en audit logs, operaciones in-place para procesamiento de secrets