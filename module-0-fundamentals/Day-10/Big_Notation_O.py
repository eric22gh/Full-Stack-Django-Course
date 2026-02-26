# 🚀 DÍA 10 - Módulo 0: Big O Notation Aplicado a Queries y Algoritmos

# 📚 Teoría: Big O Notation
# La notación Big O (O(...)) o lista[i] describe el comportamiento del algoritmo en el peor de los casos.
# Es una notación matemática que describe la complejidad de un algoritmo:
# - Tiempo de ejecución (cuánto tarda)
# - Espacio en memoria (cuánta memoria usa)

# Se enfoca en el PEOR CASO y en cómo crece con el tamaño de entrada (n)

# ✅ # Complejidad temporal: Número de operaciones que el algoritmo realiza conforme n(la entrada) crece.
# conocido como tiempo lineal O(n)

# Complejidad Temporal
# | Notación  | Descripción                      | Ejemplo común                    | Eficiencia  |
# |-----------|----------------------------------|----------------------------------|-------------|
# | O(1)      | Tiempo constante                  | Acceso a un elemento en una lista| Excelente   |
# | O(log n)  | Tiempo logarítmico               | Búsqueda binaria, se reduce a la mitad | Muy buena   |
# | O(n)      | Tiempo lineal                    | Recorrer una lista                | Buena       |
# | O(n log n)| Tiempo casi lineal               | Algoritmos de ordenación como Merge Sort y Quicksort | Aceptable |
# | O(n²)     | Tiempo cuadrático                | Doble bucle anidado              | Pobre       |
# | O(2ⁿ)     | Tiempo exponencial               | Algoritmo recursivo de Fibonacci  | Mala        |


# ✅ Complejidad Espacial: cantidad de memoria que utiliza conforme n(la entrada) crece
# Esto incluye variables y estructuras de datos.

# | Notación  | Descripción                      | Ejemplo común                    | Eficiencia  |
# |-----------|----------------------------------|----------------------------------|-------------|
# | O(1)      | Espacio constante                | Variables temporales             | Excelente   |
# | O(n)      | Espacio lineal                   | Almacenar una lista de n elementos| Buena       |
# | O(n²)     | Espacio cuadrático               | Matrices bidimensionales         | Pobre       |
# | O(2ⁿ)     | Espacio exponencial              | Algoritmos recursivos con muchas llamadas | Mala |
#

# ✅ Notación Big O: Se centra en cómo el tiempo de ejecución o el uso de memoria crece a medida que aumenta el tamaño de la entrada. 
# La notación Big O se utiliza para clasificar algoritmos según su rendimiento y eficiencia.

# Reglas para calcular Big O:
# 1. Ignora constantes: O(2n) → O(n)
# 2. Toma el término dominante: O(n² + n) → O(n²)
# 3. Variables diferentes para inputs diferentes: O(a + b), no O(n)
# 4. Drop non-dominant terms: O(n + log n) → O(n)

# Big O en operaciones comunes de Python:
# Lista:
#   - Acceso por índice: O(1)
#   - Búsqueda (in): O(n)
#   - append(): O(1)
#   - insert(0, x): O(n)
#   - pop(): O(1)
#   - pop(0): O(n)
#   - sort(): O(n log n)

# Diccionario:
#   - Acceso por clave: O(1)
#   - Inserción: O(1)
#   - Búsqueda de clave: O(1)
#   - Iteración: O(n)

# Set:
#   - Búsqueda (in): O(1)
#   - Inserción: O(1)
#   - Union/Intersección: O(n)

# Complejidad espacial:
# - O(1): No crea estructuras nuevas proporcionales a n
# - O(n): Crea lista/dict del tamaño de entrada

# Aplicación práctica en Django ORM:
# - select_related(): O(1) queries (JOIN en DB)
# - sin select_related: O(n) queries (N+1 problem)
# - Filtrado con índices: O(log n)
# - Filtrado sin índices: O(n)


# Buenas prácticas:
# Prefiere O(1) y O(log n) cuando sea posible
# Evita bucles anidados (O(n²)) con datos grandes
# Usa estructuras correctas: set para búsquedas, dict para lookups
# Piensa en escalabilidad: ¿funciona con 1M de registros?
# En Django: usa select_related/prefetch_related siempre

# Errores comunes:
# Buscar en lista cuando deberías usar set
# Bucles anidados innecesarios
# No considerar N+1 problem en ORMs
# Optimización prematura (optimiza cuando sea necesario)

# Ejemplo práctico - Comparación de complejidades:

# O(1) - Constante
def obtener_primero(lista):
    """Siempre toma el mismo tiempo, sin importar tamaño de lista."""
    return lista[0] if lista else None

# O(n) - Lineal
def buscar_elemento(lista, objetivo):
    """Revisa cada elemento hasta encontrar objetivo."""
    for elemento in lista:
        if elemento == objetivo:
            return True
    return False

# O(n²) - Cuadrática
def encontrar_duplicados_malo(lista):
    """Compara cada elemento con todos los demás."""
    duplicados = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                duplicados.append(lista[i])
    return duplicados

# O(n) - Lineal optimizado
def encontrar_duplicados_bueno(lista):
    """Usa set para O(1) lookups."""
    vistos = set()
    duplicados = set()
    for elemento in lista:
        if elemento in vistos:
            duplicados.add(elemento)
        vistos.add(elemento)
    return list(duplicados)

# Ejemplo - N+1 Problem (común en Django):

# ❌ Malo - O(n) queries a la base de datos
# for producto in productos:  # 1 query
#     print(producto.categoria.nombre)  # N queries adicionales
# Total: 1 + N queries

# ✅ Bueno - O(1) queries
# productos = Producto.objects.select_related('categoria')  # 1 query con JOIN
# for producto in productos:
#     print(producto.categoria.nombre)  # Sin queries adicionales
# Total: 1 query

# Documentación: https://wiki.python.org/moin/TimeComplexity


# 💻 Ejercicios Acumulativos

# Ejercicio 1: Análisis de Complejidad de Funciones Básicas
# Contexto: Entender complejidad de operaciones comunes.
# Requisitos: Para cada función, determina su complejidad Big O y justifica:
# Función 1:
def sumar_primeros_n(n):
    """Suma números del 1 al n."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
# ¿Complejidad? ¿Por qué?
# Tiempo lineal: o(n) porque tiene que recorrer toda la lista para sumar los numeros.
# espacio constante: o(1) porque esta usando una variable temporal

# Función 2:
def sumar_primeros_n_optimizado(n):
    """Suma números del 1 al n con fórmula."""
    return n * (n + 1) // 2
# ¿Complejidad? ¿Por qué?
# Tiempo constante: O(1) porque siempre realiza la misma cantidad de operaciones sin importar el valor de n.
# Espacio constante: O(1) porque no utiliza nada que la haga crecer, solo variables temporales para el cálculo.

# Función 3:
def buscar_en_matriz(matriz, objetivo):
    """Busca valor en matriz 2D."""
    for fila in matriz:
        for elemento in fila:
            if elemento == objetivo:
                return True
    return False
# ¿Complejidad? 
# tiempo cuadratico: o(n2) porque usa 2 bucles anidados, 1 para volver la primera matriz en una lista y comparar y si no encuentra el resultado, sigue con la otra matriz
# espacio cuadratico: o(n2) porque usa matrices bidimensionales

# Función 4:
def combinar_listas(lista1, lista2):
    """Combina dos listas eliminando duplicados."""
    resultado = []
    for item in lista1:
        if item not in resultado:
            resultado.append(item)
    for item in lista2:
        if item not in resultado:
            resultado.append(item)
    return resultado
# ¿Complejidad? ¿Cómo optimizarla?
# tiempo cuadratico: o(n2) porque usa dos bucles for
# espacio cuadratico: o(n2) porque usa dos bucles para recorrer las 2 listas
def Combine(list1, list2):
    list1.extend(list2)
    return set(list1)

# Función 5:
def es_palindromo(texto):
    """Verifica si texto es palíndromo."""
    return texto == texto[::-1]
# ¿Complejidad?
# tiempo constante o(1): porque es solo un elemento que se esta comparando
# espacio constante o(1): porque esta comparando variables temporales


# Ejercicio 2: Optimización de Búsquedas
# Contexto: Sistema que busca usuarios frecuentemente.
# Requisitos:
# Dada esta lista de usuarios:
usuarios = [
    {"id": i, "nombre": f"Usuario{i}", "email": f"user{i}@email.com", "activo": i % 2 == 0}
    for i in range(10000)
]

# Implementa 3 versiones de búsqueda:

# Versión 1: buscar_por_id_lista(usuarios: list, user_id: int) -> dict | None
#   - Busca linealmente en la lista
#   - Complejidad: O(n)
def Search_id(users : list, user_id : int) -> dict :
    for user in users:
        if user_id == user["id"]:
            return {"id" : user_id, "User" : user_id, "email" : f"User{user_id}@email.com", "Active" : (user_id % 2 == 0)}
 

# Versión 2: buscar_por_id_dict(usuarios_dict: dict, user_id: int) -> dict | None
#   - Primero convierte lista a dict: {id: usuario}
#   - Busca en el diccionario
#   - Complejidad de búsqueda: O(1)
#   - ¿Vale la pena la conversión inicial?
def Search_id_dict(users : list, user_id : int) -> dict :
    users_dict = {user["id"] : user for user in users} # convertir una lista a un diccionario,donde la clave es "id" y valor son los numeros o datos de la lista.
    # ejemplo para que el id sea un numero (1 a 1000) y valor los datos de la list.
    # new = {i : name for i, name in enumerate(users, start=1)}
    return users_dict.get(user_id, None)
    # # no es lo mismo hacer una buscqueda por en una lista que una en un diccionario, porque en la lista se tiene que recorrer toda la lista para encontrar el elemento, 
    # mientras que en el diccionario se puede acceder directamente al elemento usando su clave, 
    # lo que hace que la búsqueda sea mucho más rápida, cuando hay muchos datos.

# Versión 3: buscar_por_id_binaria(usuarios_sorted: list, user_id: int) -> dict | None
#   - Asume lista ordenada por id
#   - Usa búsqueda binaria
#   - Complejidad: O(log n)
def Binary_search(user_s : list, user_id: int, key=lambda x: x["id"]) -> dict:
    new_list = sorted(user_s, key=key)
    left = 0
    right = len(new_list) - 1
    while left <= right:
        medium = (left + right) // 2
        medium_value = key(new_list[medium])
        if user_id == medium_value:
            return new_list[medium]
        elif medium_value < user_id:
            left = medium + 1
        else:
            right = medium - 1
    return None

print(Search_id(usuarios, 7))
print(Search_id_dict(usuarios, 10))
print(Binary_search(usuarios, 22))

# Ejercicio 3: N+1 Problem Simulado
# Contexto: Simular problema N+1 común en ORMs como Django.
# Requisitos: Simula una base de datos en memoria:

# "Tabla" de categorías
categorias_db = {
    1: {"id": 1, "nombre": "Electrónica"},
    2: {"id": 2, "nombre": "Ropa"},
    3: {"id": 3, "nombre": "Alimentos"},
}

# "Tabla" de productos
productos_db = [
    {"id": 1, "nombre": "Laptop", "precio": 1200, "categoria_id": 1},
    {"id": 2, "nombre": "Mouse", "precio": 25, "categoria_id": 1},
    {"id": 3, "nombre": "Camisa", "precio": 30, "categoria_id": 2},
    {"id": 4, "nombre": "Pantalón", "precio": 50, "categoria_id": 2},
    {"id": 5, "nombre": "Manzanas", "precio": 5, "categoria_id": 3},
] * 1000  # Simula 5000 productos

# Implementa dos versiones:
# Versión 1 (MALA): obtener_productos_con_categoria_malo()
#   - Itera sobre productos_db
#   - Para cada producto, hace una "query" a categorias_db[categoria_id]
#   - Simula query con: time.sleep(0.0001) por cada acceso a categorias_db
#   - Cuenta número total de "queries"
#   - Retorna lista de: {"producto": nombre, "categoria": nombre_categoria}
#   - Complejidad: O(n) queries
def Obtain_products(prod : list[dict]) -> dict | str:
    queries = 0
    for products in productos_db:
        if products["categoria_id"] in categorias_db.keys():
            queries += 1
            return {"Product" : products["nombre"], "Category" : categorias_db[1]["nombre"], "Amount of queries" : queries}
        else:
            queries += 1
    return f"I didnt find the product, amount of quieries: {queries}"
# complejidad: tiempo lineal O(n): porque tiene que recorrer toda la lista.

# Versión 2 (BUENA): obtener_productos_con_categoria_bueno()
#   - Hace UNA carga de todas las categorías al inicio
#   - Itera sobre productos y usa diccionario cargado
#   - Simula 1 query inicial: time.sleep(0.0001)
#   - Cuenta número total de "queries"
#   - Retorna misma estructura
#   - Complejidad: O(1) query
def Obtain_products_category(prod : list[dict]) -> dict | str:
    # cargar categorias al inicio
    queries = 1  # Simula 1 query inicial
    categorias_cache = {cat["id"]: cat["nombre"] for cat in categorias_db.values()}  # Carga categorías en un diccionario
    resultado = []
    for products in productos_db:
        categoria_nombre = categorias_cache.get(products["categoria_id"], "Desconocida") # conseguir el nombre de la categoria usando el valor de llave el diccionario la llave es el id de la categoria, 
        # busca con esa llave el nombre de la categoria, si no lo encuentra devuelve "Desconocida"
        queries += 1  # Simula query por cada producto, pero sin acceder a la base de datos
        resultado.append({"Product": products["nombre"], "Category": categoria_nombre})
    return {"Products with category": resultado, "Amount of queries": queries}
# Crea función comparar_n_plus_one() que:
#   - Ejecute ambas versiones
#   - Mida tiempo de ejecución
#   - Muestre número de queries de cada una
#   - Calcule la diferencia de performance

def comparar_n_plus_one():
    import time

    start_time = time.time()
    result_malo = Obtain_products(productos_db)
    end_time = time.time()
    time_malo = end_time - start_time

    start_time = time.time()
    result_bueno = Obtain_products_category(productos_db)
    end_time = time.time()
    time_bueno = end_time - start_time

    print("Resultado Malo:", result_malo)
    print("Tiempo Malo:", time_malo, "segundos")
    
    print("Resultado Bueno:", result_bueno)
    print("Tiempo Bueno:", time_bueno, "segundos")
    
    print("Diferencia de Performance:", time_bueno - time_malo, "segundos")
    
comparar_n_plus_one()

# Ejercicio 4: Estructuras de Datos y Complejidad
# Contexto: Elegir la estructura correcta para cada caso.
# Requisitos: Implementa estas operaciones con diferentes estructuras:

# Caso 1: Sistema de tags únicos
# Implementa con lista y con set:
# - agregar_tag(tag)
# - existe_tag(tag)
# - eliminar_tag(tag)
# - obtener_todos_tags()

# Versión lista:
class TagsLista:
    def __init__(self):
        self.tags = []
    
    def agregar_tag(self, tag: str) -> None:
        if tag not in self.tags:  # ¿Complejidad? O(n) tiempo lineal porque tiene que recorrer toda lista para verificar si no esta.
            self.tags.append(tag)
    
    def existe_tag(self, tag: str) -> bool:
        return tag in self.tags  # ¿Complejidad? O(n) tiempo lineal porque tiene que recorrer toda lista para verificar si el tag existe.
    
    def Delete_tag(self, tag : str) -> str:
        if self.existe_tag(tag) == True:
            self.tags.remove(tag)
            return f"the tag: {tag} succesfuly deleted"
    def Obtain_tag(self):
        return self.tags
    

# Versión set:
class TagsSet:
    def __init__(self):
        self.tags = set()
    
    def agregar_tag(self, tag: str) -> None:
        self.tags.add(tag)  # ¿Complejidad? O(1) tiempo constante porque el set maneja internamente la estructura de datos para permitir inserciones rápidas.
    
    def existe_tag(self, tag: str) -> bool:
        return tag in self.tags  # ¿Complejidad? O(1) tiempo constante porque el set permite búsquedas rápidas, siempre y cuando lo que se busque sea verificar pertenencia.
    
    def Delete_tag(self, tag: str) -> str:
        if self.existe_tag(tag) == True:
            self.tags.remove(tag)
            return f"the tag: {tag} succesfuly deleted"
    # complejidad: O(1) tiempo constante porque primero verifca si el elemento exite en la lista y set permite busquedas rapidas, siempre y cuando lo que se busque sea verificar pertenencia   
    def Obtain_tags(self):
        return self.tags
    # complejidad: O(1) tiempo constante porque primero verifca si el elemento exite en la lista y set permite busquedas rapidas, siempre y cuando lo que se busque sea verificar pertenencia  

# Caso 2: Caché de resultados (key-value)
# Implementa con lista de tuplas y con diccionario:
# - guardar(clave, valor)
# - obtener(clave)

# Crea función benchmark_estructuras() que:
#   - Pruebe ambas implementaciones con 10000 operaciones
#   - Mida tiempo total
#   - Determine cuál es más eficiente para cada caso

def benchmark_estructuras():
    import time
    tags_lista = TagsLista()
    tags_set = TagsSet()

    # Benchmark para TagsLista
    start_time = time.time()
    for i in range(10000):
        tags_lista.agregar_tag(f"tag{i}")
        tags_lista.existe_tag(f"tag{i}")
        tags_lista.Delete_tag(f"tag{i}")
    end_time = time.time()
    print("Tiempo total para TagsLista:", end_time - start_time, "segundos")

    # Benchmark para TagsSet
    start_time = time.time()
    for i in range(10000):
        tags_set.agregar_tag(f"tag{i}")
        tags_set.existe_tag(f"tag{i}")
        tags_set.Delete_tag(f"tag{i}")
    end_time = time.time()
    print("Tiempo total para TagsSet:", end_time - start_time, "segundos")
    
benchmark_estructuras()

# Ejercicio 5: Optimización de Algoritmo Real (Integrador)
# Contexto: Sistema de recomendaciones que encuentra usuarios similares.
# Requisitos: Dada esta estructura:
users_db = [
    {"id": 1, "nombre": "Ana", "intereses": ["python", "django", "aws"]},
    {"id": 2, "nombre": "Carlos", "intereses": ["python", "react", "docker"]},
    {"id": 3, "nombre": "María", "intereses": ["django", "postgresql", "aws"]},
    {"id": 4, "nombre": "Luis", "intereses": ["python", "django", "react"]},
    {"id": 5, "nombre": "Sofia", "intereses": ["aws", "terraform", "docker"]},
] * 200  # 1000 usuarios

# Implementa 3 versiones de buscar usuarios similares:

# Versión 1 (O(n²)): encontrar_similares_v1(usuario_id: int, min_coincidencias: int = 2)
#   - Compara el usuario con TODOS los demás
#   - Cuenta intereses en común usando bucles anidados
#   - Retorna lista de usuarios con >= min_coincidencias en común 
def found_similar_v1(user_id : int, min_coincidences : int = 2) -> list:
    user = next((user for user in users_db if user["id"] == user_id), None)
    # La función next() devuelve el primer elemento que cumple la condición dada (u["id"] == user_id) o None si no se encuentra.
    # Se está utilizando para buscar el usuario con el id especificado en la lista de usuarios_completos. 
    if not user:
        return []
    
    similars = []
    for other in users_db:
        if other["id"] == user_id:
            continue
        coincidences = 0
        for interest in user["intereses"]:
            if interest in other["intereses"]:
                coincidences += 1
        if coincidences >= min_coincidences:
            similars.append(other)
    return similars

# Versión 2 (O(n) con sets): encontrar_similares_v2(usuario_id: int, min_coincidencias: int = 2)
#   - Convierte intereses a sets
#   - Usa intersección de sets para contar coincidencias
#   - Retorna lista de usuarios similares

def found_similar_v2(user_id : int, min_coincidences : int = 2) -> list:
    user = next((user for user in users_db if user["id"] == user_id), None)
    if not user:
        return []
    
    user_interests = set(user["intereses"])
    similars = []
    for other in users_db:
        if other["id"] == user_id:
            continue
        other_interests = set(other["intereses"])
        coincidences = len(user_interests.intersection(other_interests))
        if coincidences >= min_coincidences:
            similars.append(other)
    return similars

# Crea función benchmark_similares() que:
#   - Ejecute las 2 versiones buscando similares de 10 usuarios aleatorios
#   - Mida tiempo promedio de cada versión
#   - Verifique que todas dan el mismo resultado
#   - Muestre tabla comparativa de performance

def benchmark():
    import time
    import random

    user_ids = random.sample(range(1, 1001), 10)  # Selecciona 10 usuarios aleatorios

    # Benchmark para encontrar_similares_v1
    start_time = time.time()
    results_v1 = [found_similar_v1(user_id) for user_id in user_ids]
    end_time = time.time()
    time_v1 = end_time - start_time

    # Benchmark para encontrar_similares_v2
    start_time = time.time()
    results_v2 = [found_similar_v2(user_id) for user_id in user_ids]
    end_time = time.time()
    time_v2 = end_time - start_time

    # Verificar que ambas versiones dan el mismo resultado
    assert results_v1 == results_v2, "Los resultados no coinciden entre versiones"

    print(f"Tiempo promedio para encontrar_similares_v1: {time_v1 / len(user_ids):.4f} segundos")
    print(f"Tiempo promedio para encontrar_similares_v2: {time_v2 / len(user_ids):.4f} segundos")
    
benchmark()


# 📖 Ejercicios de Lectura de Código
# Ejercicio 6: Identificar Complejidad en Código Real, analiza la complejidad Big O de cada fragmento:

# Código 1:
def procesar_datos_1(datos):
    resultado = []
    for item in datos:
        if item > 0:
            resultado.append(item * 2)
    return resultado
# Complejidad: O(n) tiempo lineal; porque tiene q recoerer una lista de elementos y si son mayores a 0, multiplicarlos por 2 y aggregarlos a la nueva lista.
# O(n) espacio lineal: porque tiene que almacenar una lista de n elementos en una lista
# Código 2:
def procesar_datos_2(datos):
    resultado = []
    for i in range(len(datos)):
        for j in range(len(datos)):
            if datos[i] == datos[j] and i != j:
                resultado.append(datos[i])
    return resultado
# Complejidad: O(n2) tiempo cuadratico: porque usa dos bucles for para comparar los items
# complejidad: O(n2) espacio cuadratico: porque tiene matrices bidimensionales

# Código 3:
def procesar_datos_3(datos):
    datos.sort()  # ¿Qué complejidad tiene sort? O(nlog n) tiempo casi lineal: sort utiliza una combinacion de algoritmos de ordenacion, para su funcion.
    # O(n log n) espacio casi lineal
    return datos[len(datos) // 2]
# Complejidad: O(1) tiempo constante: accede al elemento de una lista con el indice.
# O(1) espacio constante: usa variables temporales

# Código 4:
def procesar_datos_4(datos, objetivo):
    izq, der = 0, len(datos) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if datos[medio] == objetivo:
            return medio
        elif datos[medio] < objetivo:
            izq = medio + 1
        else:
            der = medio - 1
    return -1
# Complejidad: O(log n) tiempo logaritmico:  el tiempo se reduce a la mitad por la busqueda binaria.
# O(log n): espacio logaritmico: el espacio que se usa para almacenar, se reduce a la mitad por la busqueda binaria

# Código 5:
def procesar_datos_5(n):
    if n <= 1:
        return 1
    return n * procesar_datos_5(n - 1)
# Complejidad: O(2n) tiempo exponencial: algoritmo recursivo
# O(2n) espacio exponencial: algoritmo recursivo con muchas llamadas

# Código 6:
def procesar_datos_6(datos):
    visto = set()
    for item in datos:
        if item in visto:
            return True
        visto.add(item)
    return False
# Complejidad: O(n) tiempo lineal: recorre una lista de n elementos para verificar si estan en un conjunto.
# o(n) espacio lineal: despues de recorrer y verificar almacena una lista de n elementos.

# Preguntas:
# ¿Cuál es el más eficiente?
# O(1) tiempo constante ya que accede a un elemento de una lista, mediante indices.
# O(1) espacio constante ya que usa variables temporales

# ¿Cuál escala peor con datos grandes?
# las que usan doble bucle anidado O(n2) tiempo  y espacio cuadratico y las que usan recursividad O(2n) tiempo y espacio exponencial.

# ¿Cómo optimizarías el código 2?
# ya que la idea es compara una a una 2 elementos, usaria un algoritmo de busqueda binaria O(log n) ya que se reduce a la mitad el trabajo



# Ejercicio 7: Refactorización para Mejor Complejidad
# Refactoriza estos códigos O(n²) a O(n) o mejor:

# Código 1: Encontrar duplicados
def encontrar_duplicados(lista):
    """O(n²) - Muy lento con listas grandes."""
    duplicados = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados
# Refactoriza a O(n) usando set
def find_duplex(lista : list) -> set | None:
    unique = set()
    duplex = set()
    for index, data in enumerate(lista, start=0):
        if lista[index] in unique:
            duplex.add(data)
        else:
            unique.add(data)
    return duplex
print(find_duplex([1, 22, 3, 10, 22, 3]))
    

# Código 2: Buscar pares que suman el valor del objetivo
def encontrar_pares_suma(lista, objetivo):
    """O(n²) - Compara todos con todos."""
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == objetivo:
                pares.append((lista[i], lista[j]))
    return pares
# Refactoriza a O(n) usando set
def Find_even_numbers(numbers : list, obj : int) -> list[tuple] | None:
    even = []
    for i in range(0, len(numbers) - 1):
        if numbers[i] + numbers[i + 1] == obj:
            even.append((numbers[i], numbers[i + 1]))
    return even
print(Find_even_numbers([5, 2, 4, 3, 1, 10, 2], 7))

# Código 3: Verificar si lista2 es subconjunto de lista1
def es_subconjunto(lista1, lista2):
    """O(n * m) - Para cada elemento de lista2, busca en lista1."""
    for elemento in lista2:
        if elemento not in lista1:
            return False
    return True
# Refactoriza a O(n + m) usando set
def sub(numbers1 : list, number2 : list) -> bool:
    set1 = set(numbers1)
    set2 = set(number2)
    return set2.issubset(set1)
print(sub([1, 2, 3, 4, 5], [2, 3]))


# 🧪 Evaluación Teórica
# Pregunta 1
# Explica qué es Big O Notation y por qué es importante en desarrollo de software.
# ¿Por qué nos enfocamos en el peor caso y no en el caso promedio?
# Big O es una forma de medir el rendimiento de un algoritmo en el pero de los casos, y porque en el peor de los casos, porque una app siempre va a fallar,
# entoces se busca que este fallo no sea tan catastrofico y no se pierdan recursos ni se usen tantos recursos, ya que el gasto y uso excesivo de recursos, 
# es sumamente importante en el desarrollo de software.

# Pregunta 2
# Compara O(n) vs O(n²). Si n = 1000, ¿cuántas operaciones hace cada uno aproximadamente?
# ¿A partir de qué tamaño de datos la diferencia se vuelve crítica?
# si el algoritmo es O(n) el numero de operacion va a crecer conforme a n == 1000, si el algoritmo es O(n2) ese numero se multiplica por 2,
# ese algoritmo usa 2 bubles anidados entonces es doble trabajo para algoritmo y se vuelve critica conforme va creciendo.

# Pregunta 3
# Explica el problema N+1 en ORMs como Django. Da un ejemplo concreto.
# ¿Cómo se soluciona usando select_related() o prefetch_related()?
# N+1 Es un problema de rendimiento que ocurre cuando una app hace una consulta a la bd para obtener una lista de objetos, 
# y luego hace una consulta adicional para cada objeto y asi obtener datos relacionados.
# Ejemplo: Si tienes 100 productos y cada producto tiene una categoría, y haces una consulta para obtener los productos,
# y luego haces una consulta adicional para obtener la categoría del producto, entonces estás haciendo 1 consulta para obtener los productos + 100 consultas para obtener las categorías, lo que resulta en 101 consultas (N+1).
# Para solucionar esto, Usar select_related() para hacer un JOIN y obtener los productos  y sus categorías en una sola consulta, o prefetch_related() para hacer dos consultas optimizadas, una para los productos y otra para las categorías, y luego relacionarlas en memoria.


# Reflexión personal:
# ¿Qué fue lo más difícil?
# entender los distintos tipos de notacion

# ¿Entendiste cómo calcular Big O?
# si correcto, dependiendo de donde se esta almacenando y el tiempo que dura en procesarce

# ¿Cuánto tiempo real te tomó?
# unas 8 horas

# ¿Qué concepto necesitas repasar?
# tipos de notacion big O


# 🎯 Objetivo de mañana (Día 11): Estructuras de datos - Listas avanzadas y operaciones eficientes

# Conexión con proyectos finales:
# 💰 Cost Optimizer: Optimizar queries de recursos AWS, evitar N+1, usar índices para búsquedas rápidas
# 🔐 SecureVault: Búsquedas eficientes de secretos, índices para audit logs, caché con O(1) lookup