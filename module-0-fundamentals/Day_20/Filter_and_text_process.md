# 🚀 DÍA 20: MÓDULO 0 - Procesamiento de Texto y Filtrado (El Poder de Grep)

**📦 Dependencias del Módulo:**
* **Entorno:** Máquina Virtual con Ubuntu en VirtualBox.
* **Terminal:** Consola nativa de Ubuntu.
---

## 📖 FASE 1: TEORÍA 
En un entorno de producción (AWS, Docker, servidores web), n o abres archivos de registro (*logs*) con el bloc de notas, porque suelen pesar gigabytes y colapsarían la memoria RAM. En su lugar, utilizas herramientas de línea de comandos diseñadas para buscar agujas en pajares a la velocidad de la luz. La herramienta reina para esto en el mundo Unix se llama `grep` (Global Regular Expression Print).

## DOCUMENTACIÓN OFICIAL
*🔗 **Doc Oficial:** [GNU Grep Manual](https://www.gnu.org/software/grep/manual/grep.html)*

### 🎯 El Propósito
Si tu flujo de n8n falla o tu API de Django devuelve un error 500, el servidor lo registrará en un archivo de texto con miles de líneas. Necesitas extraer únicamente las líneas que contienen la palabra "Error", "Exception" o "Warning" de forma instantánea. `grep` te permite auditar, filtrar y monitorear la salud de tus sistemas sin leer datos irrelevantes.

### 🎯 ¿Qué problema resuelve Grep y las Expresiones Regulares (Regex)?
1.  **Filtrado Masivo:** Encontrar texto específico dentro de miles de archivos en milisegundos.
2.  **Búsqueda por Patrones (Regex):** No siempre buscas una palabra exacta. A veces buscas "cualquier línea que empiece con un número" o "cualquier texto que parezca un correo electrónico". Las expresiones regulares son el lenguaje matemático para definir esos patrones.

### 📁 Desglose Anatómico de Grep y Regex Básica

| Comando / Símbolo | Función Técnica | Ejemplo de Uso Práctico |
| :--- | :--- | :--- |
| `grep` | Busca coincidencias exactas. | `grep "error" app.log` |
| `grep -i` | *Case Insensitive*: ignora mayúsculas y minúsculas. | `grep -i "django" app.log` (encuentra Django, django, DJANGO) |
| `grep -v` | *Invert Match*: muestra todo EXCEPTO lo que buscas. | `grep -v "éxito" app.log` (muestra solo fallos) |
| `grep -r` | *Recursive*: busca dentro de una carpeta y todas sus subcarpetas. | `grep -r "Limon" /var/log/` |
| `^` (Regex) | Representa el **inicio** de una línea. | `grep "^Error" app.log` (Líneas que *empiezan* con Error) |
| `$` (Regex) | Representa el **final** de una línea. | `grep "200$"` (Líneas que *terminan* con 200) |
| `.` (Regex) | Representa **cualquier** carácter (comodín). | `grep "p.n" texto.txt` (Encuentra pan, pin, pon) |

### 🔑 Puntos Clave (Bajo el capó)
* **Grep no altera archivos:** Es un filtro de lectura. Toma el contenido, busca el patrón y lo escupe en la salida estándar (`stdout`), pero el archivo original se mantiene intacto.
* **Combinación letal (Pipe):** `grep` brilla cuando lo conectas a la salida de otros comandos. Por ejemplo, `ls -la | grep "eric"` listará solo los archivos que te pertenecen.

### ⚠️ Buenas y Malas Prácticas
* **✅ Buenas Prácticas:** Usar comillas `" "` alrededor de la palabra que buscas, especialmente si tiene espacios (ej: `grep "Fallo de conexión" log.txt`).
* **❌ El Error Típico (Mala Práctica):** El infame **"Useless Use of Cat" (UUOC)**. Muchos principiantes escriben `cat archivo.txt | grep "palabra"`. Esto desperdicia recursos porque abres el archivo entero con `cat` para pasárselo a `grep`. La forma correcta y optimizada es simplemente: `grep "palabra" archivo.txt`.

### 💻 Implementación Oficial (Guía de Comandos Básicos)
grep "Timeout" /var/log/syslog         # Busca 'Timeout' en los logs del sistema
grep -i "warning" alertas.txt          # Busca 'warning', 'WARNING', 'Warning'
grep -v "OK" resultados.csv            # Filtra las líneas que digan OK, mostrando el resto
grep -r "DB_PASSWORD" /home/eric/      # Busca en todos los archivos de tu usuario
grep "^Inicio" reporte.txt             # Busca líneas que arranquen con la palabra 'Inicio'
tail -f auditoria.log | grep -i "error" # Ver logs en TIEMPO REAL y filtrar al mismo tiempo / Ctrl+C para salir
grep -i "error" -C 3 auditoria.log     # Ver 3 líneas ANTES y 3 DESPUÉS del error para entender qué pasó

tail -n 5 auditoria.log | grep -i "error"  # Buscar "error" en las últimas 5 líneas
tail -f auditoria.log | grep -E "ERROR|WARNING|Exception" # Versión más potente — buscar en vivo varios patrones a la vez
# -E = expresiones regulares extendidas
# | dentro de grep = OR (busca cualquiera de los tres)

grep -i "error" -B 3 auditoria.log # Ver 3 líneas ANTES del error
# -B = Before
grep -i "error" -A 3 auditoria.log # Ver 3 líneas DESPUÉS del error
# -A = After
grep -c "error" auditoria.log # Retorna solo el número de líneas que contienen "error"

grep -r "error" /var/log/     # Buscar en todos los archivos de un directorio

grep -r "error" /var/log/ -l # Mostrar el nombre del archivo junto al resultado, -l = solo imprime los nombres de archivos que tienen coincidencias

grep "2024-01-15" auditoria.log | grep -i "error" # Primero filtra por fecha, luego por tipo de error

grep "2024-01-15 08:" auditoria.log | grep -i "error" # Buscar errores en una hora específica

grep "2024-01-15" auditoria.log | grep -i "error" | grep "database" # Encadenar tres filtros

grep -i "error" auditoria.log | tail -n 20 # Busca TODOS los errores, muestra solo los últimos 20
# Diferencia clave vs tail primero:
# tail -n 20 | grep → busca en 20 líneas / # grep | tail -n 20 → busca en TODO el archivo, muestra los 20 más recientes

grep -v "ERROR" auditoria.log | grep -v "DEBUG" # Excluir dos patrones a la vez

tail -f /var/log/django/error.log | grep -E "ERROR|WARNING|Exception" ## El Comando Completo de Producción Django

## Resumen por Situación

| Situación                          | Comando                                      |
|------------------------------------|----------------------------------------------|
| Monitoreo en vivo                  | `tail -f app.log \| grep -i "error"`         |
| Entender contexto del error        | `grep -C 3 "error" app.log`                  |
| No sé en qué archivo está          | `grep -r "error" /var/log/`                  |
| Contar errores                     | `grep -c "error" app.log`                    |
| Errores de un día específico       | `grep "2024-01-15" app.log \| grep "error"`  |
| Últimos 20 errores del historial   | `grep "error" app.log \| tail -n 20`         |
| Todo excepto los errores           | `grep -v "error" app.log`                    |
| Buscar varios patrones a la vez    | `grep -E "ERROR\|WARNING" app.log`           |

💻 FASE 2: PRÁCTICA

⚙️ Ejercicio 1: Lógica Base CLI (Sensibilidad y Exclusión)
Bash
# Contexto: Estás auditando una lista de tareas y necesitas aplicar filtros rápidos.
# Requisitos:
# 1. Crea un archivo 'tareas.txt' y agrégale estas 3 líneas (usando echo y >>):
#    "URGENTE: Revisar base de datos"
#    "urgente: Actualizar servidor"
#    "Normal: Responder correos"
# 2. Usa grep para encontrar la palabra "urgente" ignorando si es mayúscula o minúscula.
# 3. Usa grep para mostrar SOLO las tareas que NO contengan la palabra "Normal".

# --- TUS COMANDOS AQUÍ ---
1- cd Escritorio/agencia_flow/logs/, 2- touch tareas.txt, 3- echo "URGENTE: Revisar base de datos" >> tareas.txt, 4- echo  "urgente: Actualizar servidor" >> tareas.txt, 5- echo  "Normal: Responder correos" >> tareas.txt, 6- grep -i "urgente" tareas.txt, 7- grep -v "Normal" tareas.txt

🚀 Ejercicio 2: Proyecto Real (Análisis de Tráfico Web)
Bash
# Contexto: Tu portafolio está recibiendo tráfico y algunos usuarios reportan que la página no carga. 
# Requisitos:
# 1. Crea un archivo 'access.log' y llénalo con estos datos simulados:
#    echo "192.168.1.5 - GET /index.html - 200 OK" >> access.log
#    echo "10.0.0.8 - GET /admin - 403 Forbidden" >> access.log
#    echo "192.168.1.10 - POST /api/login - 500 Internal Server Error" >> access.log
#    echo "172.16.0.2 - GET /imagen.png - 200 OK" >> access.log
# 2. Usa grep para aislar y mostrar en pantalla SOLO la línea donde ocurrió un error en el servidor (código 500).

# --- TUS COMANDOS AQUÍ ---
1- cd Escritorio/agencia_flow/logs/, 2- touch access.log, 3- echo "192.168.1.5 - GET /index.html - 200 OK" >> access.log, 4- echo "10.0.0.8 - GET /admin - 403 Forbidden" >> access.log, 5- echo "192.168.1.10 - POST /api/login - 500 Internal Server Error" >> access.log, 6- echo "172.16.0.2 - GET /imagen.png - 200 OK" >> access.log, grep "500" access.log


🚀 Ejercicio 3: Proyecto Real (El Poder de Regex)
# Contexto: En un archivo de configuración masivo, necesitas encontrar variables específicas 
# que deben estar obligatoriamente al inicio de la línea, ignorando los comentarios.
# Requisitos:
# 1. Crea un archivo 'config.ini' con el siguiente contenido:
#    echo "# Configuracion de DB" > config.ini
#    echo "HOST=localhost" >> config.ini
#    echo "# HOST antiguo = 192.168.0.1" >> config.ini
# 2. Usa grep con la Expresión Regular de "Inicio de línea" (^) para buscar la palabra "HOST", 
#    de modo que solo te devuelva "HOST=localhost" y omita la línea que empieza con "#".

# --- TUS COMANDOS AQUÍ ---
1- cd Escritorio/agencia_flow/logs/, 2- touch confi.ini, 3-  echo "# Configuracion de DB" > config.ini, 4- echo "HOST=localhost" >> config.ini, 5- echo "# HOST antiguo = 192.168.0.1" >> config.ini, 6- grep "^HOST" config.ini


🐛 Ejercicio 4: Lectura de Código y Debugging
# Contexto: Un compañero te muestra este comando que diseñó para buscar tu nombre dentro 
# de un archivo de usuarios del sistema. El comando funciona, pero es ineficiente y es un caso clásico de UUOC (Useless Use of Cat).
# Analiza por qué es ineficiente y refactorízalo a la forma profesional de Linux.

# --- COMANDO DEFECTUOSO DEL COMPAÑERO ---
cat /etc/passwd | grep -i "eric"

# --- EXPLICACIÓN DEL ERROR Y TU CORRECCIÓN AQUÍ ---
# Explicación: Hay 2 grandes errores, usar cat para leer archvos es una mala practica ya que con archivos grandes puede tardar demasiado y seria un uso innecesario de recursos, cat lee archivos y lo que le estas pasando es una ruta de de directorio y grep ocupa la palabra que buscas y el archivo a buscar, en este caso no le esta pasando el archivo.
Lo puedes hacer de esta manera Tail -n 15 auditoria.log | grep -i "Warning|Error|Execption"


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA (Cierre del Día)
❓ Pregunta Teórica 1:
Estás buscando una credencial perdida en tu servidor, pero no recuerdas en qué archivo la guardaste dentro de la carpeta agencia_flow. ¿Qué flag (bandera) de grep utilizarías para buscar dentro de todos los archivos y subcarpetas de ese directorio simultáneamente?
Usaria el comando grep -r "key.rsa" /Home/agencia_flow/logs/

❓ Pregunta Teórica 2:
En la expresión regular grep "2026$" archivo.txt, ¿qué función cumple exactamente el símbolo de dólar $ al final del número?
Si no me equivoco el signo de $ se utiliza para interar un numero de veces, por ejemplo cuando se añada algun comando ese signo le va a dar dinamismo a este tecto, por ejemplo: "20261",  "20262",  "20263" y asi sucesivamente.


🗣️ Prueba de Feynman (Explicación):
Escenario: Un cliente dueño de un hotel ve que usas grep para buscar un error de reservas en sus archivos del servidor. Él te pregunta: "¿Por qué no descargas el archivo y usas el CTRL+F de Word o Excel, no es lo mismo?". Explícale en un párrafo corto la diferencia abismal de rendimiento y capacidad entre grep y el buscador tradicional de un editor de texto de oficina.
Hola te explico de una forma clara, grep busca de una forma mas eficiente y asertiva lo que se requiera en el momento y se usando menos recursos... añadiendole de que el CTRL+F funciona de una mejor manera el w11 y el servidor en el que estamos es linux.