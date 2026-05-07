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
# import sys
# from pathlib import Path

# sys.path.append(str(Path(__file__).resolve().parent.parent))
# from Day_13 import BST1

# # crate three levels of tree
# Three = BST1(12)
# Three.izquierdo = BST1(6)
# Three.derecho = BST1(15)
# Three.izquierdo.izquierdo = BST1(3)
# Three.izquierdo.derecho = BST1(9)
# Three.derecho.izquierdo = BST1(13)
# Three.derecho.derecho = BST1(18)

# # BFS Basico:
# from collections import deque
# def bfs_Three(three):
#     if not three:
#         return [ ]
#     result = []
#     queue = deque([three])
#     while queue:
#         node = queue.popleft()
#         result.append(node.value)
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#     return result
# print(bfs_Three(Three))

# # DFS Recursivo:
# def dfs_preorder(three, result=None):
#     if result is None:
#         result = []
#     if three is None:
#         return result
#     result.append(three.value)
#     dfs_preorder(three.left, result)
#     dfs_preorder(three.right, result)
#     return result

# print(dfs_preorder(Three))


# Ejercicio 2: BFS en Grafos
# Contexto: Sistema de análisis de grafos (redes sociales, mapas).
# Requisitos: Implementa funciones para trabajar con grafos representados como diccionarios:
# grafo = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
def bfs_graft_dict(graft, begin):
    """BFS en grafo representado como diccionario."""
    visited = set()
    queue = deque([begin])
    visited.add(begin)
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graft.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


data = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(bfs_graft_dict(data, 'F'))


# 🎯 Objetivo de mañana (Día 15): Algoritmos de Sorting - Bubble, Merge, Quick Sort

# Conexión con proyectos finales:
# 💰 Cost Optimizer: BFS para encontrar dependencias mínimas entre recursos, DFS para análisis de jerarquías
# 🔐 SecureVault: BFS para permisos en cascada, DFS para validación de políticas anidadas