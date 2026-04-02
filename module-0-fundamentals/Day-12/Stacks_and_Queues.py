# 🚀 DÍA 12 - Módulo 0: Stacks y Queues - Implementación y Aplicaciones

# 📚 Teoría Concisa
# Stacks (Pilas) - LIFO (Last In, First Out)
# Una pila es una estructura donde el último elemento agregado es el primero en salir.
# Piensa en una pila de platos: solo puedes tomar el de arriba.

# Operaciones principales:
# push(item): agregar agregar a la pila - O(1)
# pop(): remover el elemento arriba de la pila - O(1)
# peek()/top(): ver los elementos de la pila - O(1)
# is_empty(): verificar si la pila está vacía - O(1)
# size(): obtener el tamaño de la pila - O(1)

# Implementación en Python:
# Con lista: stack = [], stack.append(x), stack.pop(), return stack[-1]( el menos -1 es el último elemento), return stack(peek()), len(stack) == 0, len(stack)

# Queues (Colas) - FIFO (First In, First Out)
# Una cola es una estructura donde el primer elemento agregado es el primero en salir.
# Piensa en una fila de banco: el primero en llegar es el primero atendido.

# Operaciones principales:
# enqueue(item): agregar al final/ append() - O(1)
# dequeue(): remover del frente/pop(0) - O(1)
# front()/peek(): ver primer elemento sin remover/queque[0] - O(1)
# is_empty(): verificar si está vacía/ len(queque) == 0 - O(1)
# size(): obtener tamaño/ len(queque) - O(1)

# Implementación en Python:
# Con lista (INEFICIENTE): queue.append(x) agregar, queue.pop(0) - O(n) para eliminar el primer elemento pop(0)
# Con deque (EFICIENTE): from collections import deque
#                        queue = deque()
#                        queue.append(x), queue.popleft() - O(1) ambas
                        # queue[0] para front/peek, len(queue) == 0 para is_empty, len(queue) para size

# Aplicaciones prácticas de Stacks:
# - Validación de paréntesis/corchetes
# - Historial de navegación (back button)
# - Undo/Redo en editores
# - Evaluación de expresiones matemáticas
# - Call stack en recursión
# - Parsing de HTML/XML

# Aplicaciones prácticas de Queues:
# - Procesamiento de tareas (task queue)
# - BFS (Breadth-First Search)
# - Manejo de requests en servidores
# - Print spooling
# - Buffer de datos
# - Sistemas de mensajería

# Buenas prácticas:
# Usa list para stacks (append/pop)
# Usa collections.deque para queues (NO list con pop(0))
# Encapsula en clases para mejor API
# Valida operaciones (no hacer pop en estructura vacía)
# Documenta qué representa cada estructura

# Errores comunes:
# Usar list.pop(0) para queues (O(n) - muy lento)
# No validar si está vacía antes de pop/dequeue
# Confundir cuándo usar stack vs queue
# No usar deque cuando se necesita queue eficiente

# Ejemplo práctico - Stack:
class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        """Agrega item al tope."""
        self._items.append(item)
    
    def pop(self):
        """Remueve y retorna item del tope."""
        if self.is_empty(): # Validación para evitar error al hacer pop en stack vacío
            raise IndexError("Pop de stack vacío")
        return self._items.pop()
    
    def peek(self):
        """Retorna item del tope sin remover."""
        if self.is_empty():
            raise IndexError("Peek de stack vacío")
        return self._items[-1]
    
    def is_empty(self):
        """Verifica si está vacía."""
        return len(self._items) == 0
    
    def size(self):
        """Retorna tamaño."""
        return len(self._items)

# Ejemplo - Queue con deque:

from collections import deque
class Queue:
    def __init__(self):
        self._items = deque() # deque es una estructura de datos optimizada para operaciones en ambos extremos (append y popleft)
    
    def enqueue(self, item):
        """Agrega item al final."""
        self._items.append(item)
    
    def dequeue(self):
        """Remueve y retorna item del frente."""
        if self.is_empty():
            raise IndexError("Dequeue de queue vacía")
        return self._items.popleft()  # O(1) con deque
    
    def front(self):
        """Retorna primer item sin remover."""
        if self.is_empty():
            raise IndexError("Front de queue vacía")
        return self._items[0]
    
    def is_empty(self):
        """Verifica si está vacía."""
        return len(self._items) == 0
    
    def size(self):
        """Retorna tamaño."""
        return len(self._items)

# Documentación oficial: https://docs.python.org/3/library/collections.html#collections.deque

# 💻 Ejercicios Acumulativos
# Ejercicio 1: Implementación Completa de Stack
# Contexto: Sistema que necesita estructura Stack robusta.
# Requisitos: Implementa clase Stack con estos métodos:

class Stack:
    def __init__(self, max_size: int = None):
        self.warhouse = []
        self.max_size = max_size
        
    def push(self, item) -> None:
        """ Agrega item al tope. Raises: OverflowError: Si stack está lleno (max_size alcanzado) """
        if self.is_full():
            raise OverflowError("max_size alcanzado")
        else:
            self.warhouse.append(item)
    
    def pop(self):
        """ Remueve y retorna item del tope.
        Raises: IndexError: Si stack está vacío
        """
        if self.is_empty():
            raise IndexError("The stack is empty")
        return self.warhouse.pop()
    
    def peek(self):
        """Retorna tope sin remover."""
        if self.is_empty():
            raise IndexError("The stack is empty")
        return self.warhouse[-1]
    
    def is_empty(self) -> bool:
       return len(self.warhouse) == 0
    
    def is_full(self) -> bool:
        """Verifica si está lleno (solo si max_size definido)."""
        return len(self.warhouse) == self.max_size
    
    def size(self) -> int:
        """Retorna cantidad de elementos."""
        return len(self.warhouse)
    
    def clear(self) -> None:
        """Vacía el stack."""
        self.warhouse.clear()
    
    def to_list(self) -> list:
        """Retorna copia como lista (tope al final)."""
        if self.is_empty():
            raise ValueError("The stack is empty so there is nothing to copy")
        return self.warhouse.copy()
        
    def __str__(self) -> str:
        """Representación string: Stack[bottom -> top]"""
        return f"Stack[bottom -> top]: {self.warhouse}"
    
Complete = Stack(max_size=5)
Complete.push(10)
Complete.push(2)
Complete.push(3)
print(Complete)
print(Complete.peek())
print(Complete.is_empty())
print(Complete.is_full())
print(Complete.size())
Complete.pop()

# Ejercicio 2: Validador de Paréntesis/Corchetes
# Contexto: Parser que valida sintaxis de código.
# Requisitos: Implementa estas funciones usando Stack:

# 1. validar_parentesis(expresion: str) -> bool
#    - Valida que paréntesis (), corchetes [] y llaves {} estén balanceados
#    - Ejemplos válidos: "()", "()[]{}", "({[]})"
#    - Ejemplos inválidos: "(", "([)]", "(()"
#    - Usa Stack para tracking
def validar_parentesis(expresion: str) -> bool:
    stack = Stack()
    pares = {')': '(', ']': '[', '}': '{'}
    
    for char in expresion:
        if char in pares.values():  # Si es un paréntesis de apertura
            stack.push(char)
        elif char in pares:  # Si es un paréntesis de cierre
            if stack.is_empty() or stack.pop() != pares[char]:
                return False  # No coincide o stack vacío
    return stack.is_empty()  # Al final, stack debe estar vacío

# 2. encontrar_errores_parentesis(expresion: str) -> list[dict]
#    - Encuentra y reporta todos los errores
#    - Retorna lista de: [{"posicion": int, "tipo": str, "caracter": str}]
#    - Tipos de error: "sin_cerrar", "sin_abrir", "mal_anidado"

def encontrar_errores_parentesis(expresion: str) -> list[dict]:
    stack = Stack()
    errores = []
    pares = {')': '(', ']': '[', '}': '{'}
    
    for i, char in enumerate(expresion):
        if char in pares.values():  # Paréntesis de apertura
            stack.push((char, i))  # Guardamos el carácter y su posición
        elif char in pares:  # Paréntesis de cierre
            if stack.is_empty():
                errores.append({"posicion": i, "tipo": "sin_abrir", "caracter": char})
            else:
                top_char, top_pos = stack.pop()
                if top_char != pares[char]:
                    errores.append({"posicion": i, "tipo": "mal_anidado", "caracter": char})
    
    # Cualquier paréntesis que quede en el stack es un error de sin cerrar
    while not stack.is_empty():
        _, pos = stack.pop()
        errores.append({"posicion": pos, "tipo": "sin_cerrar", "caracter": expresion[pos]})
    return errores

# 3. balancear_expresion(expresion: str) -> str
#    - Agrega los cierres faltantes al final
#    - "(()" -> "((()))"
#    - "[{" -> "[{}]"
def balancear_expresion(expresion: str) -> str:
    stack = Stack()
    pares = {')': '(', ']': '[', '}': '{'}
    apertura = set(pares.values())
    
    for char in expresion:
        if char in apertura:
            stack.push(char)
        elif char in pares:
            if not stack.is_empty() and stack.peek() == pares[char]:
                stack.pop()
    
    # Agregar cierres faltantes
    resultado = expresion
    while not stack.is_empty():
        resultado += next(key for key, value in pares.items() if value == stack.pop())
    return resultado


# Ejercicio 3: Implementación de Queue Eficiente
# Contexto: Sistema de procesamiento de tareas.
# Requisitos: Implementa clase Queue usando deque:

from collections import deque 
new_queue = deque()
class Queue:
    def __init__(self):
        pass
       
    def enqueue(self, task : str, priority : int) -> None:
        """Agrega item al final."""
        if not isinstance(task, str) and not isinstance(priority, int):
            return "The task must be a text and the priority a number"
        else:
            new_queue.append((task, priority))
    
    def dequeue(self):
        """ Remueve y retorna item del frente. Raises: IndexError: Si queue está vacía """
        if self.is_empty():
            raise IndexError("There is nothing to delete")
        else:
            new_queue.popleft()
            return f"The task {new_queue[0][0]} with priority {new_queue[0][1]} is the next to process"
            
    def front(self):
        """Retorna primer item sin remover."""
        if self.is_empty():
            raise ValueError("There is nothing infront of the queue")
        else:
            return list(new_queue)[0]
        
    def rear(self):
        """Retorna último item sin remover."""
        if self.is_empty():
            raise ValueError("There is nothing behind the queue")
        else:
            return list(new_queue)[-1]
    
    def is_empty(self) -> bool:
        """Verifica si está vacía."""
        return len(list(new_queue)) == 0
    
    def size(self) -> int:
        """Retorna cantidad de elementos."""
        if self.is_empty():
            raise ValueError("The queue is empty")
        else:
            return f"The size of the queue is: {len(list(new_queue))}"
    
    def clear(self) -> None:
        """Vacía la queue."""
        new_queue.clear()
        return "The queue is succesfuly clear"
    
    def to_list(self) -> list:
        """Retorna copia como lista (frente al inicio)."""
        if self.is_empty():
            raise ValueError("The queue is empty so there is nothing to copy")
        else:
            return list(new_queue)
    
    def __str__(self) -> str:
        """Representación: Queue[front -> rear]"""
        return f"Queue[front -> rear]: {list(new_queue)}"
    
    
data = Queue()
data.enqueue("task1", 1)
data.enqueue("task2", 2)
print(data)
print(data.front())
print(data.rear())
print(data.size())
print(data.dequeue())
print(data)


# Ejercicio 4: Historial de Navegación (Browser Back/Forward)
# Contexto: Implementar funcionalidad de navegador web.
# Requisitos: Implementa clase BrowserHistory usando dos Stacks:

class BrowserHistory:
    """Simula historial de navegación con back/forward."""
    def __init__(self, homepage: str):
        """ Inicializa con homepage. Usa dos stacks: back_stack y forward_stack."""
        self.current = homepage
        self.back_stack = Stack()
        self.forward_stack = Stack()
    
    def visit(self, url: str) -> None:
        """ Visita nueva URL, Agrega URL actual a back_stack, Limpia forward_stack (nueva rama de navegación), Actualiza URL actual"""
        self.back_stack.push(self.current)
        self.current = url
        self.forward_stack.clear()
    
    def back(self, steps: int = 1) -> str:
        """ Retrocede 'steps' páginas, Mueve URLs de back_stack a forward_stack, Retorna URL resultante,Si steps > páginas disponibles, va hasta donde pueda """
        for _ in range(steps):
            if self.back_stack.is_empty():
                break  # No hay más páginas para retroceder
            self.forward_stack.push(self.current)  # Mueve la URL actual al forward_stack
            self.current = self.back_stack.pop()  # Actualiza la URL actual con la del back_stack
        return self.current
    
    def forward(self, steps: int = 1) -> str:
        """ Avanza 'steps' páginas, Mueve URLs de forward_stack a back_stack, Retorna URL resultante """
        for _ in range(steps):
            if self.forward_stack.is_empty():
                break  # No hay más páginas para avanzar
            self.back_stack.push(self.current)  # Mueve la URL actual al back_stack
            self.current = self.forward_stack.pop()  # Actualiza la URL actual con la del forward_stack
        return self.current
    
    def current_url(self) -> str:
        """Retorna URL actual."""
        return self.current
    
    def get_history(self) -> list[str]:
        """Retorna historial completo [más antiguo -> actual]."""
        history = self.back_stack.to_list() + [self.current] + self.forward_stack.to_list()[::-1]
        return history
    
    def can_go_back(self) -> bool:
        """Verifica si puede retroceder."""
        return not self.back_stack.is_empty()
    
    def can_go_forward(self) -> bool:
        """Verifica si puede avanzar."""
        return not self.forward_stack.is_empty()
    
data = BrowserHistory("home.com")
data.visit("page1.com")
data.visit("page2.com")
print(data.current_url())  # page2.com
print(data.back())  # page1.com
print(data.back())  # home.com
print(data.forward())  # page1.com
print(data.get_history())  # ['home.com', 'page1.com', 'page2.com']


# Ejercicio 5: Sistema de Procesamiento de Tareas (Integrador)
# Contexto: Sistema que procesa tareas con diferentes estrategias.
# Requisitos: Implementa sistema completo de gestión de tareas:

from collections import deque
from datetime import datetime
from typing import Literal # literal: se usa para indicar que una variable solo puede tomar ciertos valores específicos (en este caso, "fifo", "lifo", "prioridad")

class Tarea:
    def __init__(self, id: int, nombre: str, prioridad: int = 0, tiempo_estimado: int = 1):
        self.id = id
        self.nombre = nombre
        self.prioridad = prioridad
        self.tiempo_estimado = tiempo_estimado
        self.timestamp_creacion = datetime.now()
    
    def __str__(self):
        return f"Tarea({self.id}: {self.nombre}, P{self.prioridad})"

class GestorTareas:
    def __init__(self, estrategia: Literal["fifo", "lifo", "prioridad"] = "fifo", Task: list[Tarea] = None):
        self.estrategia = estrategia
        self.tareas = Task if Task is not None else []
        pass
    
    def agregar_tarea(self, tarea: Tarea) -> None:
        """Agrega tarea según estrategia."""
        self.tareas.append(tarea)
        self.cambiar_estrategia(self.estrategia)  # Reorganiza
    
    def procesar_siguiente(self) -> Tarea | None:
        """ Procesa siguiente tarea según estrategia.
        Retorna la tarea procesada o None si no hay.
        """
        if self.estrategia == "fifo":
            return deque.popleft(self.tareas) if self.tareas else None
        elif self.estrategia == "lifo":
            return self.tareas.pop() if self.tareas else None
        elif self.estrategia == "prioridad":
            if not self.tareas:
                return None
            # Encuentra tarea con mayor prioridad (y más antigua en caso de empate)
            tarea_prioritaria = max(self.tareas, key=lambda t: (t.prioridad, -t.timestamp_creacion.timestamp()))
            self.tareas.remove(tarea_prioritaria)
            return tarea_prioritaria
            
    def ver_siguiente(self) -> Tarea | None:
        """Ve siguiente tarea sin procesarla."""
        if self.Is_empty():
            return None
        if self.estrategia == "fifo":
            return self.tareas[0]
        elif self.estrategia == "lifo":
            return self.tareas[-1]
        elif self.estrategia == "prioridad":
            return max(self.tareas, key=lambda t: (t.prioridad, -t.timestamp_creacion.timestamp()))
    
    def listar_pendientes(self) -> list[Tarea]:
        """Retorna lista de tareas pendientes."""
        return self.tareas.copy()
    
    def procesar_todas(self) -> list[Tarea]:
        """ Procesa todas las tareas pendientes.
        Retorna lista en orden de procesamiento.
        """
        procesadas = []
        while not self.Is_empty():
            procesadas.append(self.procesar_siguiente())
        return procesadas
    
    def cambiar_estrategia(self, nueva_estrategia: Literal["fifo", "lifo", "prioridad"]) -> None:
        """
        Cambia estrategia manteniendo tareas actuales.
        Reorganiza tareas según nueva estrategia.
        """
        self.estrategia = nueva_estrategia
        if nueva_estrategia == "fifo":
            self.tareas.sort(key=lambda t: t.timestamp_creacion)  # Más antiguas primero
        elif nueva_estrategia == "lifo":
            self.tareas.sort(key=lambda t: t.timestamp_creacion, reverse=True)  # Más recientes primero
        elif nueva_estrategia == "prioridad":
            self.tareas.sort(key=lambda t: (t.prioridad, -t.timestamp_creacion.timestamp()), reverse=True)  # Mayor prioridad y más reciente primero
    
    def Is_empty(self) -> bool:
        """Verifica si no hay tareas pendientes."""
        return self.listar_pendientes() == 0
    
    
data = GestorTareas(estrategia="prioridad")
data.agregar_tarea(Tarea(1, "Tarea 1", prioridad=2))
data.agregar_tarea(Tarea(2, "Tarea 2", prioridad=1))
data.agregar_tarea(Tarea(3, "Tarea 3", prioridad=3))
print(data.ver_siguiente())


# 📖 Ejercicios de Lectura de Código
# Ejercicio 6: Analiza y corrige estos errores:

# Error 1: Queue ineficiente
class QueueMala:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)  # ¿Qué problema tiene? no es la mejor opción para implementar una queue,
# ya que pop(0) es O(n) porque tiene que mover todos los elementos restantes una posición hacia adelante. 
# Esto hace que el rendimiento de dequeue sea lento a medida que la queue crece.


# Error 2: Confunde cuándo usar stack vs queue
# def procesar_tareas_malo(tareas):
#     """Procesa tareas FIFO pero usa stack."""
#     stack = []
#     for tarea in tareas:
#         stack.append(tarea)
    
#     while stack:
#         procesar(stack.pop())  # ¿Es FIFO o LIFO?
# ¿Qué estructura debería usar? ahi esta usando lifo, pero si queremos procesar en orden de llegada (FIFO), deberíamos usar una queue, no un stack.

# Error 3: Reinventa la rueda
class MiDeque:
    """Intenta reimplementar deque con listas."""
    def __init__(self):
        self.items = []
    
    def append_left(self, item):
        self.items.insert(0, item)  # O(n) - ineficiente
# ¿Por qué no usar collections.deque?
# Usar insert no es eficinte ya que tiene complejidad o(n) y si loque se quiere es efiiciencia es mejor usar deque ya que es una estructura optimizada 0(1)

# Preguntas:
# ¿Por qué list.pop(0) es O(n)?
# porque al eliminar el primer elemento de la lista, los demas tienen que recorer una poscion en la lista y conforme la lista crece los movimientos van a aumentar. 

# ¿Cuándo es aceptable NO validar operaciones?
# En contextos controlados donde se garantiza que no habrá operaciones inválidas (ej. uso interno de una clase bien diseñada).

# ¿Cómo decides entre Stack y Queue para un problema?
# Dependiendo del tipo de procesamiento de la app, si es una app web o tareas es mejor usar una queue, 
# pero si es un historial de navegacion o undo/redo es mejor usar un stack.


# Ejercicio 7: Refactoriza estos códigos usando estructuras apropiadas:

# Código 1: Invertir string (usa Stack)
def invertir_string_v1(texto):
    """Sin usar estructuras de datos."""
    resultado = ""
    for i in range(len(texto) - 1, -1, -1):
        resultado += texto[i]
    return resultado
print(invertir_string_v1("Hola Mundo"))  # "odnuM aloH"
# Refactoriza usando Stack explícito
def invertir_string_v2(texto):
    """Usando Stack."""
    stack = Stack()
    for char in texto:
        stack.push(char)
    
    resultado = ""
    while not stack.is_empty():
        resultado += stack.pop()
    return resultado

# Código 2: Procesar en orden de llegada (usa Queue)
# def procesar_pedidos_v1(pedidos):
#     """Procesa pero no garantiza FIFO."""
#     while pedidos:
#         pedido = pedidos[0]
#         procesar(pedido)
#         pedidos.remove(pedido)  # O(n)
#     return True
# Refactoriza con Queue eficiente
from collections import deque
def procesar_pedidos_v2(pedidos):
    """Procesa en orden de llegada usando Queue."""
    procesar = deque(pedidos)  # Convertir a deque para eficiencia
    while procesar:
        procesado = procesar.popleft()  # O(1)
        return f"Pedido {procesado} procesado"

# Código 3: Undo/Redo (usa dos Stacks)
class EditorSimple:
    def __init__(self):
        self.texto = ""
        self.cambios = []  # Lista simple
    
    def escribir(self, texto):
        self.cambios.append(self.texto)
        self.texto += texto
    
    def undo(self):
        if self.cambios:
            self.texto = self.cambios.pop()
# Refactoriza con Stack para undo y Stack para redo
class EditorConUndoRedo:
    def __init__(self):
        self.texto = ""
        self.undo_stack = Stack()
        self.redo_stack = Stack()
    
    def escribir(self, texto):
        self.undo_stack.push(self.texto)  # Guardar estado actual para undo
        self.texto += texto
        self.redo_stack.clear()  # Limpiar redo al hacer nuevo cambio
    
    def undo(self):
        if not self.undo_stack.is_empty():
            self.redo_stack.push(self.texto)  # Guardar estado actual para redo
            self.texto = self.undo_stack.pop()  # Revertir a estado anterior
    
    def redo(self):
        if not self.redo_stack.is_empty():
            self.undo_stack.push(self.texto)  # Guardar estado actual para undo
            self.texto = self.redo_stack.pop()  # Revertir a estado siguiente

# 🧪 Evaluación Teórica

# Pregunta 1
# Explica la diferencia entre Stack (LIFO) y Queue (FIFO). Da 3 ejemplos del mundo real de cada uno.
# ¿Por qué deque es mejor que list para implementar Queue?
# Stack (LIFO - Last In, First Out): El último elemento agregado es el primero en salir. Ejemplos: Pila de platos, Historial de navegación (back button), Undo/Redo en editores.
# Queue (FIFO - First In, First Out): El primer elemento agregado es el primero en salir. Ejemplos: Fila de banco, Procesamiento de tareas, Buffer de datos.
# Deque es mejor que list para implementar Queue porque deque está optimizado para operaciones en ambos extremos.

# Pregunta 2
# ¿Cómo usarías un Stack para validar paréntesis balanceados? Describe el algoritmo paso a paso.
# ¿Qué complejidad temporal y espacial tiene?
# Algoritmo para validar paréntesis balanceados usando Stack:
# 1. Crear un stack vacío.
# 2. Iterar sobre cada carácter en la expresión:
#    a. Si el carácter es un paréntesis de apertura ( (, [, { ), empujarlo al stack.
#    b. Si el carácter es un paréntesis de cierre ( ), ], } ), verificar si el stack está vacío. Si está vacío, la expresión no es balanceada. Si no está vacío, hacer pop del stack y verificar si el paréntesis de apertura coincide con el de cierre. Si no coincide, la expresión no es balanceada.
# 3. Al final de la iteración, si el stack está vacío, la expresión es balanceada. Si no está vacío, la expresión no es balanceada.
# Complejidad temporal: O(n), donde n es la longitud de la expresión, ya que se itera una vez sobre la expresión.
# Complejidad espacial: O(n) en el peor caso, si todos los caracteres son paréntesis de apertura, el stack podría contener todos ellos.

# Pregunta 3
# Explica cómo implementarías funcionalidad de "back" y "forward" de un navegador usando Stacks.
# ¿Qué pasa con el forward stack cuando visitas una nueva página?
# Para implementar la funcionalidad de "back" y "forward" de un navegador usando Stacks, se pueden usar dos stacks: uno para el historial de páginas visitadas (back_stack) y otro para las páginas a las que se puede avanzar (forward_stack).
# - Cuando visitas una nueva página, empujas la página actual al back_stack y limpias el forward_stack, ya que estás creando una nueva rama de navegación.
# - Cuando haces "back", haces pop del back_stack para obtener la página anterior y empujas la página actual al forward_stack.
# - Cuando haces "forward", haces pop del forward_stack para obtener la página siguiente y empujas la página actual al back_stack.


# Reflexión personal:
# ¿Qué fue lo más difícil?
# como implemntar back y forward en el navegador

# ¿Entendiste cuándo usar Stack vs Queue?
# si me quedo sumamente claro, el stack es para cosas como historial de navegacion o undo/redo, 
# mientras que la queue es para procesamiento de tareas o manejo de requests en servidores.   

# ¿Cuánto tiempo real te tomó?
# aproximadamente 4 dias


# 🎯 Objetivo de mañana (Día 13): Árboles básicos - Conceptos y recorridos

# Conexión con proyectos finales:
# 💰 Cost Optimizer: Queue para procesamiento de tareas AWS, Stack para historial de operaciones
# 🔐 SecureVault: Queue para procesamiento de rotación de secrets, Stack para audit trail/undo