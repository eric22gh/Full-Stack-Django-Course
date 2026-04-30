# 🚀 DÍA 14 - Módulo 0: BFS y DFS - Algoritmos de Búsqueda

# 📚 Teoría

# BFS (Breadth-First Search) - Búsqueda en Anchura; 
# Explora el grafo/árbol nivel por nivel, visitando todos los vecinos de un nodo antes de pasar al siguiente nivel.

# Características de BFS (Busqueda en anchura):
# - Usa Queue (FIFO)
# - Explora por niveles
# - Encuentra el camino más corto en grafos no ponderados
# - Complejidad: O(V + E) donde V=vértices, E=aristas
# - Complejidad espacial: O(V) - puede usar mucha memoria

# DFS (Depth-First Search) - Búsqueda en Profundidad
# Explora tan profundo como sea posible antes de retroceder.

# Características de DFS:
# - Usa Stack (LIFO) o recursión (call stack implícito)
# - Explora una rama completamente antes de otra
# - Útil para detectar ciclos, topological sort
# - Complejidad: O(V + E)
# - Complejidad espacial: O(h) donde h=altura (mejor que BFS en árboles)

# Implementación de BFS:
# 1. Encolar nodo inicial
# 2. Mientras queue no esté vacía:
#    a. Desencolar nodo
#    b. Procesar/visitar nodo
#    c. Encolar vecinos no visitados
#    d. Marcar como visitados

# Implementación de DFS:
# Recursivo:
#   1. Marcar nodo como visitado
#   2. Procesar nodo
#   3. Para cada vecino no visitado, llamar DFS recursivamente
#
# Iterativo:
#   1. Push nodo inicial a stack
#   2. Mientras stack no esté vacío:
#      a. Pop nodo
#      b. Si no visitado: procesar y marcar
#      c. Push vecinos no visitados

# Cuándo usar cada uno:
# BFS:
# - Encontrar camino más corto (no ponderado)
# - Level-order traversal porque con este se usan queue y con DFS se usan stack
# - Encontrar vecinos cercanos
# - Redes sociales (conexiones)
#
# DFS:
# - Detectar ciclos
# - Topological sort
# - Resolver laberintos
# - Backtracking problems
# - Cuando la solución está lejos de la raíz

# Aplicaciones prácticas:
# BFS:
# - GPS (camino más corto)
# - Crawlers web
# - Redes sociales (amigos cercanos)
# - Broadcasting en redes
#
# DFS:
# - Análisis de dependencias
# - Sudoku solver
# - Pathfinding en juegos
# - Compiladores (análisis sintáctico)

# Buenas prácticas:
# Usa set para tracking de visitados (O(1) lookup)
# En grafos con ciclos, SIEMPRE marca visitados
# BFS para caminos mínimos, DFS para exploración completa
# Considera espacio: DFS usa menos memoria en árboles
# Documenta qué representa cada nodo/grafo

# Errores comunes:
# No marcar nodos como visitados (bucle infinito en grafos con ciclos)
# Marcar visitados muy tarde (duplicar trabajo)
# Confundir cuándo usar BFS vs DFS
# No considerar grafos desconectados
# Recursión DFS sin límite de profundidad (stack overflow)

# Ejemplo práctico - BFS(busqueda en anchura) en árbol:

from collections import deque
def bfs_arbol(raiz):
    """BFS en árbol binario."""
    if not raiz:
        return []
    resultado = []
    queue = deque([raiz])
    while queue:
        nodo = queue.popleft()
        resultado.append(nodo.valor)
        
        if nodo.izquierdo:
            queue.append(nodo.izquierdo)
        if nodo.derecho:
            queue.append(nodo.derecho)
    
    return resultado

# Ejemplo - DFS recursivo en árbol:

def dfs_preorder(nodo, resultado=None):
    """DFS preorder recursivo."""
    if resultado is None:
        resultado = []
    
    if nodo is None:
        return resultado
    
    resultado.append(nodo.valor)
    dfs_preorder(nodo.izquierdo, resultado)
    dfs_preorder(nodo.derecho, resultado)
    
    return resultado

# Ejemplo - DFS iterativo en árbol:

def dfs_iterativo(raiz):
    """DFS iterativo usando stack."""
    if not raiz:
        return []
    
    resultado = []
    stack = [raiz]
    
    while stack:
        nodo = stack.pop()
        resultado.append(nodo.valor)
        
        # Push derecho primero para que izquierdo se procese primero
        if nodo.derecho:
            stack.append(nodo.derecho)
        if nodo.izquierdo:
            stack.append(nodo.izquierdo)
    
    return resultado

# Ejemplo - BFS en grafo (representado como diccionario):

def bfs_grafo(grafo, inicio):
    """
    BFS en grafo.
    grafo = {nodo: [vecinos]}
    """
    visitados = set()
    queue = deque([inicio])
    visitados.add(inicio)
    resultado = []
    
    while queue:
        nodo = queue.popleft()
        resultado.append(nodo)
        
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                visitados.add(vecino)
                queue.append(vecino)
    
    return resultado

# Documentación: https://docs.python.org/3/library/collections.html#collections.deque


# 💻 Ejercicios Acumulativos

# Ejercicio 1: Implementación Básica de BFS y DFS en Árboles
# Contexto: Sistema que explora árbol binario con diferentes estrategias.
# Requisitos: Usando la clase TreeNode del día anterior, implementa:
from Day_13 import TreeNode



# Ejercicio 2: BFS y DFS en Grafos
# Contexto: Sistema de análisis de grafos (redes sociales, mapas).
# Requisitos:
# Implementa funciones para trabajar con grafos representados como diccionarios:
# grafo = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# 1. bfs_grafo(grafo: dict, inicio: str) -> list
#    - BFS desde nodo inicio
#    - Retorna orden de visita

# 2. dfs_grafo_recursivo(grafo: dict, inicio: str, visitados: set = None) -> list
#    - DFS recursivo desde nodo inicio
#    - Retorna orden de visita

# 3. dfs_grafo_iterativo(grafo: dict, inicio: str) -> list
#    - DFS iterativo con Stack
#    - Retorna orden de visita

# 4. encontrar_camino_bfs(grafo: dict, inicio: str, destino: str) -> list | None
#    - Encuentra camino más corto usando BFS
#    - Retorna camino como lista de nodos
#    - None si no hay camino

# 5. encontrar_todos_caminos_dfs(grafo: dict, inicio: str, destino: str) -> list[list]
#    - Encuentra TODOS los caminos posibles usando DFS
#    - Retorna lista de caminos

# 6. es_conexo(grafo: dict) -> bool
#    - Verifica si el grafo es conexo (todos los nodos alcanzables)
#    - Usa BFS o DFS desde cualquier nodo

# 7. contar_componentes_conexas(grafo: dict) -> int
#    - Cuenta componentes conexas separadas
#    - Usa DFS/BFS múltiples veces

# Casos de prueba:
# bfs_grafo(grafo, 'A')  # ['A', 'B', 'C', 'D', 'E', 'F']
# encontrar_camino_bfs(grafo, 'A', 'F')  # ['A', 'C', 'F']
# encontrar_todos_caminos_dfs(grafo, 'A', 'F')  # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]



# Ejercicio 3: Problemas Clásicos con BFS
# Contexto: Resolución de problemas típicos usando BFS.
# Requisitos:
# Implementa estas soluciones:

# 1. nivel_minimo_hoja(raiz: TreeNode) -> int
#    - Encuentra profundidad mínima de cualquier hoja
#    - Usa BFS (detente en primera hoja encontrada)

# 2. es_arbol_simetrico(raiz: TreeNode) -> bool
#    - Verifica si árbol es simétrico (espejo)
#    - Usa BFS nivel por nivel

# 3. encontrar_nodo_mas_lejano(raiz: TreeNode, objetivo) -> tuple
#    - Encuentra nodo más lejano del objetivo
#    - Retorna (nodo, distancia)
#    - Usa BFS desde objetivo

# 4. nivel_con_maxima_suma(raiz: TreeNode) -> int
#    - Encuentra nivel con mayor suma de valores
#    - Usa BFS nivel por nivel

# 5. nodos_a_distancia_k(raiz: TreeNode, objetivo, k: int) -> list
#    - Encuentra todos los nodos a exactamente k de distancia del objetivo
#    - Usa BFS

# 6. reconstruir_arbol_desde_bfs(valores: list) -> TreeNode
#    - Reconstruye árbol binario completo desde recorrido BFS
#    - valores = [1, 2, 3, 4, 5] → construye árbol nivel por nivel

# Casos de prueba:
#       1
#      / \
#     2   3
#    /     \
#   4       5

# nivel_minimo_hoja(raiz)  # 2 (nodos 4 y 5 están a profundidad 2)
# nivel_con_maxima_suma(raiz)  # 1 (nivel 1: 2+3=5)



# Ejercicio 4: Problemas Clásicos con DFS
# Contexto: Resolución de problemas usando DFS.
# Requisitos:
# Implementa estas soluciones:

# 1. tiene_ciclo(grafo: dict, dirigido: bool = False) -> bool
#    - Detecta si grafo tiene ciclos
#    - Usa DFS con tracking de estados (visitando/visitado)

# 2. ordenamiento_topologico(grafo: dict) -> list | None
#    - Genera orden topológico de grafo dirigido acíclico
#    - Retorna None si tiene ciclos
#    - Usa DFS

# 3. encontrar_todas_hojas(raiz: TreeNode) -> list
#    - Encuentra todos los nodos hoja usando DFS
#    - Retorna lista de valores

# 4. diametro_arbol(raiz: TreeNode) -> int
#    - Calcula diámetro del árbol (camino más largo entre dos hojas)
#    - Usa DFS recursivo

# 5. suma_maxima_camino_raiz_hoja(raiz: TreeNode) -> int
#    - Encuentra suma máxima de cualquier camino raíz-hoja
#    - Usa DFS

# 6. serializar_arbol(raiz: TreeNode) -> str
#    - Serializa árbol a string usando DFS preorder
#    - Usa marcador para None (ej: "#")
#    - Ejemplo: "1,2,4,#,#,5,#,#,3,#,#"

# 7. deserializar_arbol(data: str) -> TreeNode
#    - Reconstruye árbol desde string serializado
#    - Usa DFS

# Casos de prueba:
# grafo_dag = {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': ['D'],
#     'D': []
# }
# ordenamiento_topologico(grafo_dag)  # ['A', 'C', 'B', 'D'] (uno de los posibles)
#
# arbol = TreeNode(1)
# # ... construir arbol
# serializado = serializar_arbol(arbol)  # "1,2,4,#,#,5,#,#,3,#,#"
# nuevo_arbol = deserializar_arbol(serializado)



# Ejercicio 5: Sistema de Análisis de Redes Sociales (Integrador)
# Contexto: Plataforma que analiza conexiones entre usuarios.
# Requisitos:
# Implementa sistema completo de análisis de red social:

class RedSocial:
    """Sistema de análisis de red social usando grafos."""
    
    def __init__(self):
        """
        Inicializa red.
        grafo: {usuario: [amigos]}
        """
        self.grafo = {}
    
    def agregar_usuario(self, usuario: str) -> None:
        """Agrega usuario a la red."""
        pass
    
    def agregar_amistad(self, usuario1: str, usuario2: str) -> None:
        """
        Crea amistad bidireccional.
        Agrega usuarios si no existen.
        """
        pass
    
    def eliminar_amistad(self, usuario1: str, usuario2: str) -> None:
        """Elimina amistad bidireccional."""
        pass
    
    def obtener_amigos(self, usuario: str) -> list:
        """Retorna lista de amigos directos."""
        pass
    
    def grado_separacion(self, usuario1: str, usuario2: str) -> int | None:
        """
        Calcula grados de separación (distancia más corta).
        Usa BFS.
        Retorna None si no están conectados.
        """
        pass
    
    def amigos_en_comun(self, usuario1: str, usuario2: str) -> list:
        """
        Encuentra amigos que ambos usuarios tienen en común.
        """
        pass
    
    def sugerencias_amistad(self, usuario: str, max_sugerencias: int = 5) -> list:
        """
        Sugiere amigos potenciales (amigos de amigos que no son amigos).
        Usa BFS nivel 2.
        Ordena por cantidad de amigos en común.
        """
        pass
    
    def encontrar_influencers(self, top_n: int = 5) -> list[tuple]:
        """
        Encuentra usuarios más conectados.
        Retorna [(usuario, cantidad_amigos), ...]
        Ordenado descendente.
        """
        pass
    
    def comunidades_conexas(self) -> list[list]:
        """
        Identifica comunidades separadas en la red.
        Usa DFS para encontrar componentes conexas.
        Retorna lista de comunidades (cada una es lista de usuarios).
        """
        pass
    
    def camino_mas_corto(self, inicio: str, destino: str) -> list | None:
        """
        Encuentra camino de amistades más corto.
        Usa BFS.
        Retorna camino o None.
        """
        pass
    
    def usuarios_a_distancia_n(self, usuario: str, distancia: int) -> list:
        """
        Encuentra usuarios a exactamente n conexiones de distancia.
        Usa BFS.
        """
        pass
    
    def es_red_conexa(self) -> bool:
        """
        Verifica si todos los usuarios están conectados (directa o indirectamente).
        """
        pass
    
    def obtener_estadisticas(self) -> dict:
        """
        Genera estadísticas de la red.
        Retorna: {
            "total_usuarios": int,
            "total_amistades": int,
            "grado_promedio": float,
            "usuario_mas_popular": str,
            "comunidades": int,
            "es_conexa": bool,
            "diametro": int  # máxima distancia entre dos usuarios
        }
        """
        pass
    
    def visualizar_conexiones(self, usuario: str, profundidad: int = 2) -> dict:
        """
        Obtiene subgrafo de conexiones hasta cierta profundidad.
        Usa BFS.
        Retorna: {usuario: [amigos]} del subgrafo
        Para visualización.
        """
        pass

# Casos de prueba:
# red = RedSocial()
# red.agregar_amistad("Alice", "Bob")
# red.agregar_amistad("Bob", "Charlie")
# red.agregar_amistad("Alice", "David")
# red.agregar_amistad("David", "Charlie")
# red.agregar_amistad("Eve", "Frank")
#
# print(red.grado_separacion("Alice", "Charlie"))  # 2
# print(red.amigos_en_comun("Alice", "Charlie"))  # ["Bob", "David"]
# print(red.sugerencias_amistad("Alice"))  # ["Charlie"]
# print(red.comunidades_conexas())  # [["Alice", "Bob", "Charlie", "David"], ["Eve", "Frank"]]
# print(red.camino_mas_corto("Alice", "Charlie"))  # ["Alice", "Bob", "Charlie"]
# print(red.obtener_estadisticas())



# 📖 Ejercicios de Lectura de Código

# Ejercicio 6: Análisis de Implementaciones BFS/DFS
# Analiza estos códigos e identifica problemas:

# Código 1: BFS sin marcar visitados en grafos con ciclos
def bfs_malo(grafo, inicio):
    """¿Qué problema tiene?"""
    queue = deque([inicio])
    resultado = []
    
    while queue:
        nodo = queue.popleft()
        resultado.append(nodo)
        
        for vecino in grafo[nodo]:
            queue.append(vecino)  # No verifica visitados
    
    return resultado
# ¿Qué pasa con ciclos? ¿Cómo arreglarlo?

# Código 2: DFS recursivo sin límite
def dfs_profundo(grafo, nodo, visitados=None):
    """Puede causar stack overflow."""
    if visitados is None:
        visitados = set()
    
    visitados.add(nodo)
    
    for vecino in grafo.get(nodo, []):
        if vecino not in visitados:
            dfs_profundo(grafo, vecino, visitados)  # Sin límite de profundidad
    
    return visitados
# ¿Cuándo es problema? ¿Cómo limitarlo?

# Código 3: Marcar visitados muy tarde
def bfs_ineficiente(grafo, inicio):
    """Duplica trabajo."""
    queue = deque([inicio])
    resultado = []
    
    while queue:
        nodo = queue.popleft()
        
        if nodo not in resultado:  # Marca DESPUÉS de desencolar
            resultado.append(nodo)
            
            for vecino in grafo[nodo]:
                queue.append(vecino)
    
    return resultado
# ¿Qué problema causa? ¿Cuándo marcar?



# Ejercicio 7: Refactorización y Optimización
# Refactoriza estos códigos usando BFS/DFS apropiadamente:

# Código 1: Encontrar nivel de nodo sin BFS
def encontrar_nivel_v1(raiz, objetivo, nivel=0):
    """Busca linealmente."""
    if not raiz:
        return -1
    if raiz.valor == objetivo:
        return nivel
    
    izq = encontrar_nivel_v1(raiz.izquierdo, objetivo, nivel + 1)
    if izq != -1:
        return izq
    
    return encontrar_nivel_v1(raiz.derecho, objetivo, nivel + 1)
# Refactoriza usando BFS con tracking de nivel

# Código 2: Verificar conectividad sin DFS/BFS
def estan_conectados_v1(grafo, inicio, destino):
    """Busca de forma ineficiente."""
    todos_alcanzables = set()
    
    def alcanzar(nodo):
        if nodo in todos_alcanzables:
            return
        todos_alcanzables.add(nodo)
        for vecino in grafo.get(nodo, []):
            alcanzar(vecino)
    
    alcanzar(inicio)
    return destino in todos_alcanzables
# Refactoriza usando BFS simple

# Código 3: Contar niveles del árbol
def contar_niveles_v1(raiz):
    """Cuenta sin BFS claro."""
    if not raiz:
        return 0
    return 1 + max(contar_niveles_v1(raiz.izquierdo), 
                   contar_niveles_v1(raiz.derecho))
# Refactoriza usando BFS nivel por nivel



# 🧪 Evaluación Teórica

# Pregunta 1
# Explica la diferencia fundamental entre BFS y DFS. ¿Qué estructura de datos usa cada uno?
# Da un ejemplo de problema que se resuelve mejor con BFS y otro con DFS. Justifica.

# Pregunta 2
# ¿Por qué BFS encuentra el camino más corto en grafos no ponderados?
# ¿Funcionaría DFS para esto? ¿Por qué sí o por qué no?

# Pregunta 3
# Explica cómo detectarías un ciclo en un grafo dirigido usando DFS.
# ¿Qué información adicional necesitas tracking además de nodos visitados?


# 🎯 Objetivo de mañana (Día 15): Algoritmos de Sorting - Bubble, Merge, Quick Sort

# Conexión con proyectos finales:
# 💰 Cost Optimizer: BFS para encontrar dependencias mínimas entre recursos, DFS para análisis de jerarquías
# 🔐 SecureVault: BFS para permisos en cascada, DFS para validación de políticas anidadas