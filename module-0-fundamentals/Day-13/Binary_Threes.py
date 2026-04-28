# 🚀 DÍA 13 - Módulo 0: Árboles Básicos - Conceptos y Recorridos

# 📚 Teoría

# Árboles - Estructura de Datos Jerárquica: es una estructura de datos no lineal compuesta por nodos conectados
# en una relación jerárquica (padre-hijo).

# Terminología:
# - Nodo: elemento que contiene datos y referencias a otros nodos( en si son todos son nodos que contienen datos)
# - Raíz (root): nodo superior del árbol (sin padre, el primer nodo)
# - Padre: nodo que tiene 2 nodos hijos
# - Hijo: nodo que desciende de otro nodo
# - Hoja (leaf): nodo sin hijos
# - Nivel: distancia desde la raíz (raíz = nivel 0)
# - Altura: nivel máximo del árbol
# - Subárbol: árbol formado por un nodo(padre) y sus descendientes

# Árbol Binario:
# Cada nodo tiene como máximo 2 hijos (izquierdo y derecho)

# Estructura básica de un nodo:
# class TreeNode:
#     def __init__(self, valor):
#         self.valor = valor
#         self.izquierdo = None
#         self.derecho = None

# Tipos de árboles binarios:
# - Árbol binario completo: todos los niveles llenos excepto último
# - Árbol binario perfecto: todos los niveles completamente llenos
# - Árbol binario de búsqueda (BST): izquierdo < padre < derecho

# Recorridos de árboles:
# 1. Inorder (Izquierdo-Raíz-Derecho): 
#    - En BST da elementos ordenados
#    - Recursivo: inorder(izq), visitar(raíz), inorder(der)
#
# 2. Preorder (Raíz-Izquierdo-Derecho):
#    - Útil para copiar árbol
#    - Recursivo: visitar(raíz), preorder(izq), preorder(der)
#
# 3. Postorder (Izquierdo-Derecho-Raíz):
#    - Útil para eliminar árbol
#    - Recursivo: postorder(izq), postorder(der), visitar(raíz)
#
# 4. Level-order (por niveles):
#    - Usa Queue (BFS)
#    - No recursivo generalmente

# Complejidad de operaciones básicas:
# - Búsqueda: O(h) donde h = altura (O(n) peor caso, O(log n) balanceado)
# - Inserción: O(h)
# - Eliminación: O(h)
# - Recorridos: O(n) - visita todos los nodos

# Aplicaciones prácticas:
# - Sistema de archivos (carpetas y subcarpetas)
# - DOM de HTML
# - Expresiones matemáticas
# - Bases de datos (índices B-tree)
# - Compresión (Huffman coding)
# - Decisiones (árboles de decisión)

# Buenas prácticas:
# Usa recursión para recorridos (más limpio)
# Valida si nodo es None antes de acceder
# Para level-order usa Queue explícita
# Documenta qué representa cada árbol
# Considera casos base en recursión

# Errores comunes:
# No validar nodos None
# Confundir orden de recorridos
# Recursión sin caso base (stack overflow)
# No considerar árboles vacíos
# Modificar árbol durante recorrido sin cuidado

# Ejemplo práctico - Nodo y recorridos básicos:

class TreeNode:
    """Nodo de árbol binario."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.valor)

# Recorrido Inorder (recursivo)
def inorder(nodo):
    """Recorre: Izquierdo -> Raíz -> Derecho"""
    if nodo is None:
        return "the node is empty"
    inorder(nodo.left)
    print(nodo.value, end=" ")
    inorder(nodo.right)

# Recorrido Preorder (recursivo)
def preorder(nodo):
    """Recorre: Raíz -> Izquierdo -> Derecho"""
    if nodo is None:
        return "the node is empty"
    print(nodo.value, end=" ")
    preorder(nodo.left)
    preorder(nodo.right)

# Recorrido Postorder (recursivo)
def postorder(nodo):
    """Recorre: Izquierdo -> Derecho -> Raíz"""
    if nodo is None:
        return "the node is empty"
    postorder(nodo.left)
    postorder(nodo.right)
    print(nodo.value, end=" ")

# Recorrido Level-order (iterativo con Queue)
from collections import deque
def level_order(root):
    """Recorre por niveles usando Queue."""
    if root is None:
        return "the tree is empty"
    queue = deque([root])
    while queue:
        nodo = queue.popleft()
        print(nodo.value, end=" ")
        if nodo.left:
            queue.append(nodo.left)
        if nodo.right:
            queue.append(nodo.right)

# Ejemplo de árbol:
#       8
#     /   \
#   3     10
#  / \   /  \
# 1   6  9    14
# 8, 3, 10, 1, 6, 9, 14
# este es un bst perfecto porque todos los niveles estan llenos, nivel 0 tiene 1 nodo, nivel 1 tiene 2 nodos, nivel 2 tiene 4 nodos, y no hay nodos en el nivel 3
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right.left = TreeNode(9)
root.right.right = TreeNode(14)

print("Inorder: ", end="")
inorder(root)     # 1 3 6 8 9 10 14
print("\nPreorder: ", end="")
preorder(root)    # 8 3 1 6 10 9 14

# inorder(raiz)     # 1 3 6 8 9 10 14 da primero todos los de la izquierda, luego la raiz, y luego los de la derecha
# preorder(raiz)    # 8 3 1 6 10 9 14 da primero la raiz, luego los de la izquierda, y luego los de la derecha
# postorder(raiz)   # 1 6 3 9 14 10 8 da primero los de la izquierda, luego los de la derecha, y luego la raiz
# level_order(raiz) # 8 3 10 1 6 9 14 da primero el nivel 0, luego el nivel 1, y luego el nivel 2

# ejemplo
class Node:
    def __init__(self, value:int):
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self, value:int):
        self.root = Node(value)
        
    def Insert(self, value:int):
        if self.root is None:
            self.root = Node(value)
        else:
            self.Insertions(self.root, value) 
            
    def Insertions(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.Insertions(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.Insertions(node.right, value)
                  
    def SeeInordeer(self, Node):
        if Node is not None:
            self.SeeInordeer(Node.left)
            print(Node.value, end=" ")
            self.SeeInordeer(Node.right)
            
            
list_of_values = [13, 3, 7, 11, 14, 18, 20, 10, 16, 9, 12, 15, 19]
#             13
#        /         \
#       10           16
#    /    \        /  \
#   9       12    15   19
# /  \    /   \  /  \  /  \
# 3   7  11     14    18  20

data = BST(list_of_values[0])
for value in list_of_values[1:]:
    data.Insert(value)
print("Inorder: ", end="")
data.SeeInordeer(data.root)


# Documentación: https://docs.python.org/3/library/collections.html#collections.deque


# 💻 Ejercicios Acumulativos

# Ejercicio 1: Implementación de TreeNode y Operaciones Básicas
# Contexto: Construcción de árbol binario básico.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BST1:
    def __init__(self, value):
        self.root = TreeNode(value)
        
    def Insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.Insertions1(self.root, value)
            
    def Insertions1(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self.Insertions1(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self.Insertions1(node.right, value)
            
    def Seethree(self, node):
        if node is not None:
            self.Seethree(node.left)
            print(node.value)
            self.Seethree(node.right)
            
    def is_empty(self):
        return self.root is None
            
            
data1 = BST1(8)
data1.Insert(7)
data1.Insert(15)
data1.Insert(6)
data1.Insert(14)
data1.Insert(5)
data1.Seethree(data1.root)


# Ejercicio 2: Implementación de Recorridos
# Contexto: Sistema que necesita recorrer árbol de diferentes formas.
# Requisitos: Implementa estas funciones de recorrido:

class Node2:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BST2:
    def __init__(self, value):
        self.root = Node2(value)
        
    def Insert(self, value):
        if self.root is None:
            self.root = Node2(value)
        else:
            self.Insertions(self.root, value)
            
    def Insertions(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node2(value)
            else:
                self.Insertions(node.left, value)
        else:
            if node.right is None:
                node.right = Node2(value)
            else:
                self.Insertions(node.right, value)
                
    def Inorder(self, node):
        if node is not None:
            self.Inorder(node.left)
            print(node.value, end=" ")
            self.Inorder(node.right)
        
    def Preorder(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.Preorder(node.left)
            self.Preorder(node.right)
            
    def Postorder(self, node):
        self.Postorder(node.left)
        self.Postorder(node.right)
        print(node.value, end=" ")
        
    def Level_order(self, root):
        from collections import deque 
        if root is None:
            return "the tree is empty"
        queue = deque([root])
        while queue:
            nodex = queue.popleft()
            print(nodex.value, end=" ")
            if nodex.left:
                queue.append(nodex.left)
            if nodex.right:
                queue.append(nodex.right) # este es el recorrido por niveles, primero se visita el nodo raiz, luego los nodos del nivel 1, luego los nodos del nivel 2, etc.

data = BST2(16)
data.Insert(10)
data.Insert(20)
data.Insert(8)
data.Insert(12)
data.Insert(18)
data.Insert(25)
print("Inorder: ", end="")
data.Inorder(data.root)     # 8 10 12 16 18 20 25
print("\nPreorder: ", end="")
data.Preorder(data.root)    # 16 10 8 12 20 18 25
print("\nLevel-order: ", end="")
data.Level_order(data.root) # 16 10 20 8 12 18 25


# Ejercicio 3: Búsquedas y Validaciones en Árboles
# Contexto: Sistema que busca y valida información en árboles.
# Requisitos: Implementa estas funciones:

class Node3:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BST3:
    def __init__(self, value):
        self.root = Node3(value)
        
    def Insert(self, value):
        if self.root is None:
            self.root = Node3(value)
        else:
            self.Insertions(self.root, value)
            
    def Insertions(self, node, value):
            if value < node.value:
                if node.left is None:
                    node.left = Node3(value)
                else:
                    self.Insertions(node.left, value)
            else:
                if node.right is None:
                    node.right = Node3(value)
                else:
                    self.Insertions(node.right, value)
                    
    def Search_value(self, root, value):
        search = self.Search_value_recursive(root, value)
        return f" The Value {value} founded"
    
    def Search_value_recursive(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node.value
        if value < node.value:
            return self.Search_value_recursive(node.left, value)
        else:
            return self.Search_value_recursive(node.right, value)

    def They_are_same(self, raiz1, raiz2):
        if raiz1 is None and raiz2 is None:
            return True
        if raiz1 is None or raiz2 is None:
            return False
        if raiz1.value != raiz2.value:
            return False
        return self.They_are_same(raiz1.left, raiz2.left) and \
               self.They_are_same(raiz1.right, raiz2.right)
               
    
data1 = BST3(8)
data1.Insert(7)
data1.Insert(15)
data1.Insert(6)
data1.Insert(14)
data1.Insert(5)
data2 = BST3(8)
data2.Insert(7)
data2.Insert(15)
data2.Insert(6)
data2.Insert(14)
print(data1.Search_value(data1.root, 14)) # 14
print(data1.They_are_same(data1.root, data2.root))


# Ejercicio 4: Sistema de Árbol de Expresiones Matemáticas (Integrador)
# Contexto: evalúa expresiones usando árboles.
# Requisitos: Implementa sistema completo de árbol de expresiones:

class ExpressionNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def evaluate(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return int(node.value)
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)
    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val / right_val
    
# Ejemplo: (3 + 5) * (2 - 4)
root = ExpressionNode('*')
root.left = ExpressionNode('+')
root.right = ExpressionNode('-')
root.left.left = ExpressionNode('3')
root.left.right = ExpressionNode('5')
root.right.left = ExpressionNode('2')
root.right.right = ExpressionNode('4')
print(evaluate(root)) # (3 + 5) * (2 - 4) = 8 * -2 = -16


# 📖 Ejercicios de Lectura de Código

# Ejercicio 5: Analiza estos códigos e identifica problemas:

# Código 1: Sin validación de None
def contar_nodos_malo(nodo):
    """¿Qué pasa si nodo es None?"""
    return 1 + contar_nodos_malo(nodo.izquierdo) + contar_nodos_malo(nodo.derecho)
# ¿Qué error da? ¿Cómo arreglarlo? si el valor del nodo es none, puede dar un error al intentar acceder a sus atributos izquierdo y derecho. Se debe agregar validación al inicio de la función y verificar si el nodo es None y retornar 0, ya que un nodo None no contribuye al conteo de nodos.

# Código 2: Recursión sin caso base
def altura_malo(nodo):
    """Falta caso base."""
    return 1 + max(altura_malo(nodo.izquierdo), altura_malo(nodo.derecho))
# ¿Qué problema causa? El problema es que si el nodo es None, la función seguirá llamándose a sí misma indefinidamente, lo que resultará en un error de stack overflow.
# Para corregirlo, se debe agregar un caso base al inicio de la función que verifique si el nodo es None y retornar -1.

# Código 3: Confusión de recorridos
def imprimir_inorder(nodo):
    """¿Realmente es inorder?"""
    if nodo:
        print(nodo.valor)
        imprimir_inorder(nodo.izquierdo)
        imprimir_inorder(nodo.derecho)
# ¿Qué recorrido es? ¿Cómo corregirlo? el de la implementacioon es preorder, ya que se visita primero el nodo raiz, para arreglarlo y que sea inorder, 
# se debe cambiar el orden de las llamadas recursivas, primero el nodo izquierdo, luego el nodo raiz, y luego el nodo derecho.

# Código 4: Level-order sin Queue
def level_order_malo(raiz):
    """Intenta level-order con recursión simple."""
    if raiz:
        print(raiz.valor)
        level_order_malo(raiz.izquierdo)
        level_order_malo(raiz.derecho)
# ¿Por qué no funciona? ¿Qué hace realmente? es una mala implemmentacion ya que el recorrido es preorder y el level order visitita los los nodos por niveles y se implementa con deque.

# Código 5: Modificar durante recorrido
def eliminar_hojas_malo(nodo):
    """Elimina hojas durante recorrido."""
    if nodo:
        if nodo.izquierdo and nodo.izquierdo.es_hoja():
            nodo.izquierdo = None
        if nodo.derecho and nodo.derecho.es_hoja():
            nodo.derecho = None
        eliminar_hojas_malo(nodo.izquierdo)
        eliminar_hojas_malo(nodo.derecho)
# ¿Qué problema tiene? el problema es que al eliminar las hojas durante el recorrido, se puede modificar la estructura del árbol, 
# lo que puede causar que se pierdan nodos o errores al intentar acceder a nodos que ya han sido eliminados.

# Preguntas:
# ¿Por qué validar None es crítico?
# es importante implementar la validacion de none ya que si no se hace, una funcion puede llamarse a si misma infinitamente y a la hora de acceder a los atributos de izquierda o derecha, puede dar error.

# ¿Qué recorrido es más fácil: recursivo o iterativo?
# El recorrido recursivo es generalmente más fácil de entender y escribir, ya que sigue la estructura natural del árbol. 
# Sin embargo, el recorrido iterativo con una Queue puede ser más eficiente en términos de memoria, especialmente para árboles muy grandes, ya que evita la sobrecarga de llamadas recursivas.

# ¿Cuándo NO deberías usar recursión?
# No deberías usar recursión cuando el árbol es muy grande, ya que puede causar un error de stack overflow.


# Ejercicio 7: Refactorización de Código con Árboles
# Refactoriza estos códigos para mejorarlos: 

# Código 1: Búsqueda lineal en árbol
def buscar_v1(raiz, objetivo):
    """Convierte a lista y busca."""
    valores = []
    def extraer(nodo):
        if nodo:
            valores.append(nodo.valor)
            extraer(nodo.izquierdo)
            extraer(nodo.derecho)
    extraer(raiz)
    return objetivo in valores
# Refactoriza para buscar directamente sin lista 

def buscar_v2(raiz, objetivo):
    """Busca directamente con recursión."""
    if raiz is None:
        return False
    if raiz.valor == objetivo:
        return True
    return buscar_v2(raiz.izquierdo, objetivo) or buscar_v2(raiz.derecho, objetivo)

# Código 2: Suma de valores
def sumar_valores_v1(raiz):
    """Usa recorrido y lista."""
    valores = level_order(raiz)
    return sum(valores)
# Refactoriza para sumar directamente con recursión
def sumar_valores_v2(raiz):
    """Suma directamente con recursión."""
    if raiz is None:
        return 0
    return raiz.valor + sumar_valores_v2(raiz.izquierdo) + sumar_valores_v2(raiz.derecho)

# Código 3: Encontrar profundidad
def profundidad_v1(raiz, objetivo, nivel=0):
    """Busca profundidad pero no valida."""
    if raiz.valor == objetivo:
        return nivel
    return profundidad_v1(raiz.izquierdo, objetivo, nivel+1) or \
           profundidad_v1(raiz.derecho, objetivo, nivel+1)
# Refactoriza agregando validaciones
def profundidad_v2(raiz, objetivo, nivel=0):
    """Busca profundidad con validación."""
    if raiz is None:
        return -1
    if raiz.valor == objetivo:
        return nivel
    izquierda = profundidad_v2(raiz.izquierdo, objetivo, nivel+1)
    if izquierda != -1:
        return izquierda
    return profundidad_v2(raiz.derecho, objetivo, nivel+1)



# 🧪 Evaluación Teórica

# Pregunta 1
# Explica la diferencia entre los recorridos Inorder, Preorder y Postorder. y ¿Cuál usarías para copiar un árbol? ¿Y para eliminarlo?
# Inorder: Izquierdo -> Raíz -> Derecho. En un BST da elementos ordenados(menor a mayor). No es ideal para copiar o eliminar.
# Preorder: Raíz -> Izquierdo -> Derecho. Es ideal para copiar un árbol, ya que visita primero la raíz y luego los hijos, lo que permite reconstruir la estructura del árbol.
# Postorder: Izquierdo -> Derecho -> Raíz. Es ideal para eliminar un árbol, ya que inicia con los hijos y luego la raíz, lo que permite eliminar los nodos sin perder referencias a los hijos.

# Pregunta 2
# ¿Qué es la altura de un árbol? ¿Cómo se calcula recursivamente? y ¿Cuál es la diferencia entre altura y profundidad de un nodo?
# La altura de un árbol es la longitud del camino más largo desde la raíz hasta una hoja. Se calcula recursivamente como 1 + el máximo entre la altura del subárbol izquierdo y la altura del subárbol derecho. 
# La profundidad de un nodo es la distancia desde la raíz hasta ese nodo específico.
# Mientras que la altura se refiere a la distancia desde ese nodo hasta la hoja más lejana.

# Pregunta 3
# Explica cómo funciona el recorrido level-order (por niveles). ¿Por qué necesitas una Queue? ¿Podrías hacerlo con recursión simple?
# level-order visita los nodos del árbol por niveles, comenzando desde la raíz y luego visitando los nodos de cada nivel antes de pasar al siguiente.
# Se necesita una Queue para mantener el orden de los nodos a visitar, ya que se agregan los hijos de cada nodo a la Queue y se procesan en el orden en que fueron agregados.
# no se puede hacer un recorrido level order con recursion simple.

# 🎯 Objetivo de mañana (Día 14): BFS y DFS - Algoritmos de búsqueda en grafos y árboles

# Conexión con proyectos finales:
# 💰 Cost Optimizer: Árbol de dependencias de recursos AWS, jerarquía de costos
# 🔐 SecureVault: Árbol de permisos jerárquicos, estructura de secrets organizados