# 🚀 DÍA 18: MÓDULO 0 - Flujos de Datos, Redirecciones y Visores


## 📖 FASE 1: TEORÍA 
En Linux, los comandos no son islas aisladas; están diseñados bajo la filosofía Unix: *"Haz una sola cosa, hazla bien, y prepárate para conectarte con otros programas"*. Para lograr esta conexión, Linux trata la información como flujos de datos continuos (Streams). Cada vez que abres una terminal, el sistema operativo le asigna automáticamente tres "canales" invisibles a cada programa para comunicarse con el teclado y la pantalla.
## DOCUMENTACIÓN OFICIAL
*🔗 **Doc Oficial:** [GNU Coreutils - Redirections](https://www.gnu.org/software/bash/manual/html_node/Redirections.html)*


### 🎯 El Propósito
Cuando tu script de Python en AWS falle a las 3:00 a.m. o tu contenedor Docker se detenga, no estarás ahí para verlo en vivo. Necesitas obligar al sistema a que desvíe esos mensajes de error hacia archivos de texto permanente (logs). Además, si un archivo de log pesa 4 GB, abrirlo con un editor de texto normal colapsará la memoria de tu servidor. Dominar los visores y flujos te permite extraer la línea exacta del error en segundos sin sobrecargar el hardware.

### 🎯 ¿Qué problema resuelve la Redirección y los Visores?
Evita la pérdida de información crítica del sistema y el desperdicio de memoria RAM. Nos permite:
1.  **Separar el éxito del fracaso:** Enviar los datos correctos de una automatización a un reporte `.csv` y los errores de ejecución a un archivo `errores.log` de forma independiente.
2.  **Encadenar comandos:** Usar la salida de un programa como la materia prima del siguiente, creando tuberías de procesamiento de datos en tiempo real.


### 📁 Desglose Anatómico de los Descriptores de Archivo (File Descriptors)
| Descriptor | Nombre Estándar | ID Numérico | Dispositivo por Defecto | Propósito Técnico Real |
| :--- | :--- | :--- | :--- | :--- |
| `stdin` | Entrada Estándar | `0` | Teclado | El canal por donde el programa recibe instrucciones o datos del usuario. |
| `stdout` | Salida Estándar | `1` | Pantalla | El canal donde el programa imprime los resultados exitosos de su ejecución. |
| `stderr` | Error Estándar | `2` | Pantalla | El canal exclusivo para imprimir mensajes de error o alertas críticas. |


### 🔑 Puntos Clave 
*   **Operadores de Redirección:** 
    *   `>` (Sobrescribir): Borra todo el contenido actual del archivo de destino y escribe la nueva salida.
    *   `>>` (Anexar): No borra nada; añade la nueva información al final de la última línea del archivo.
    *   `2>` (Redirección de Errores): Captura exclusivamente el canal `stderr` (ID 2) y lo desvía a un archivo.(osea captura los errores y los envia a un archivo)
*   **La Tubería o Pipe (`\|`):** Toma la salida estándar (`stdout`) del comando de la izquierda y la conecta directamente como la entrada estándar (`stdin`) del comando de la derecha. Es un puente de datos en memoria.


### ⚠️ Buenas y Malas Prácticas
*   **✅ Buenas Prácticas:** Usar siempre `>>`(añadir al final) por defecto cuando guardes logs históricos de tus automatizaciones, para evitar borrar días enteros de registros por accidente.
*   **❌ El Error Típico (Mala Práctica):** Usar el comando `cat` para ver archivos inmensos de texto. Ejecutar `cat log_gigante.txt` escupirá millones de líneas en la pantalla a toda velocidad, saturando el búfer de la terminal y congelando la interfaz por varios minutos.


### 💻 Implementación Oficial (Guía de Comandos Básicos)
echo "Iniciando servicio de automatización" > output.log # Crea/Sobrescribe el archivo con el msj entre ""
echo "Conexión exitosa con Django" >> output.log        # Anexa información sin borrar
for i in {1..30}; do echo "Línea de log número $i" >> auditoria.log; done  # para escribir multiples textos a un archivo de prueba
ls /carpeta/inexistente 2> errores.log                 # Captura el error en el archivo
ls /carpeta/vacia > reporte.log 2>&1                   # captura tanto el error como el contenido si lo hay


cat archivo_corto.txt                                  # Muestra todo el contenido (solo usar en archivos pequeños)
less log_extenso.txt                                   # Abre un visor interactivo (usa flechas para bajar, 'q' para salir)
head -n 5 sistema.log                                  # Muestra únicamente las PRIMERAS 5 líneas del archivo
tail -n 10 sistema.log                                 # Muestra únicamente las ÚLTIMAS 10 líneas (ideal para ver fallos recientes)
tail -f sistema.log                                    # Modo "Live Watch": se queda abierto mostrando cambios en tiempo real    

💻 FASE 2: PRÁCTICA
Nota: Ejecuta estos comandos dentro de tu Ubuntu en VirtualBox.


⚙️ Ejercicio 1: Lógica Base CLI (Control de Canales)
# Contexto: Estás probando cómo reacciona la terminal ante comandos exitosos y comandos fallidos.
# Requisitos:
# 1. Ve a tu Home y genera un comando 'ls' hacia tu carpeta personal, pero redirige su salida exitosa a un archivo llamado 'exito.txt'.
# 2. Ejecuta un comando intencionalmente erróneo (por ejemplo, 'ls /no_existe') y redirige su error al archivo 'falla.txt'.
# 3. Comprueba el contenido de ambos archivos usando 'cat' para verificar qué canal capturó cada uno.

# --- TUS COMANDOS AQUÍ ---
1- cd Escritorio, 2- touch exito.txt, 3- cd .., 4- ls Escritorio/ >> exito.txt, 5- touch falla.txt, 6- ls /no_existe 2> falla.txt
7- cat exito.txt(ls: no se puede acceder a Escritorio/: no existe el archivo o el directorio )
8 - cat falla.txt (ls: no se puede acceder a /no_existe: no existe el archivo o el directorio )

🚀 Ejercicio 2: Proyecto Rea6- cat exito.txt()
l (Historial del Portafolio)
# Contexto: Quieres simular un sistema de registro de visitas manual para la landing page de tu agencia de desarrollo.
# Requisitos:
# 1. Crea una estructura en tu Home: 'agencia_flow/logs/'.
# 2. Escribe una línea que diga "Usuario de Limón visitó la web" y guardala en un archivo llamado 'accesos.log' dentro de la carpeta anterior.
# 3. Agrega una segunda línea que diga "Usuario de Cartago visitó la web" al MISMO archivo, asegurándote de no borrar la visita de Limón.
# 4. Usa un comando para verificar que ambas líneas coexisten dentro del archivo.

# --- TUS COMANDOS AQUÍ ---
1- cd Escritorio/agencia_flow/, 2- mkdir logs, 3- cd logs/ 4- touch accesos.log, 5- echo "Usuario de Limón visitó la web" > accesos.log, 
6- echo "Usuario de Cartago visitó la web" >> accesos.log, 7- tail -n 5 accesos.log


🚀 Ejercicio 3: Proyecto Real (Análisis de Logs de Automatizaciones)
# Contexto: Tu flujo de n8n generó un archivo de auditoría masivo del sistema. Necesitas inspeccionar puntos específicos sin romper la memoria.
# Requisitos:
# 1. Genera un archivo simulado con 30 líneas de texto ejecutando este comando exacto en tu terminal:
#    for i in {1..30}; do echo "Línea de log número $i" >> auditoria.log; done
# 2. Usa el comando visor adecuado para inspeccionar únicamente las primeras 3 líneas de 'auditoria.log'.
# 3. Usa otro comando para extraer en pantalla exclusivamente las últimas 5 líneas del archivo (donde están los eventos más recientes).

# --- TUS COMANDOS AQUÍ ---
1- touch auditoria.log, 2- for i in {1..30}; do echo "Línea de log número $i" >> auditoria.log; done, 3- head -n 3 auditoria.log
4- tail -n 5 auditoria.log


🐛 Ejercicio 4: Lectura de Código y Debugging
# Contexto: El script bash de respaldo automático de un compañero de equipo está vaciando 
# el reporte histórico de la base de datos cada vez que se ejecuta a la medianoche, en lugar de acumularlo.
# Además, cuando el script falla, el error se muestra en pantalla y no se guarda en ningún registro de auditoría.
# Analiza los comandos del script defectuoso y refactorízalos.

# --- COMANDOS DEFECTUOSOS DEL COMPAÑERO ---
echo "--- Iniciando Respaldo PostgreSQL ---" > /home/user/backup.log
pg_dump database_prod > /home/user/db_backup.sql
echo "Respaldo finalizado con éxito" > /home/user/backup.log

# --- CORRECCIÓN AQUÍ ---

# Corrección del Script:
echo "--- Iniciando Respaldo PostgreSQL ---" >> /home/user/backup.log
cd /home/user/
touch errores_backup.log
pg_dump database_prod >> /home/user/db_backup.sql 2>> /home/user/errores_backup.log
echo "Respaldo finalizado con éxito" >> /home/user/backup.log


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA 
❓ Pregunta Teórica 1:
Si ejecutas el comando ls /carpeta/vacia > reporte.log 2>&1, ¿qué significa técnicamente la expresión 2>&1 al final del comando y qué terminará guardado dentro de reporte.log?
Es un comando muy usado en linux para capturar todo ya que ls /carpeta/vacia > reporte.log sobre escribe el resultado(positivo) en la carpeta, pero si da error no lo va a capturar, ahi es donde entra reporte.log 2>&1 ya que captura el error en dado caso de no existir o que la carpeta este vacia...Resumen captura todo tipo de reacciones del comando en el archivo reporte.log

❓ Pregunta Teórica 2:
Estás monitoreando en vivo el archivo de logs de Django (access.log) en un servidor de producción mientras los usuarios interactúan con tu portafolio web. ¿Cuál es la diferencia operativa entre usar less access.log y tail -f access.log para esta tarea específica?
Con less access.log puedo ver con menor datalle los logs del servidor, en cambio tail -f access.log es un comando completamente diferente ya que con el puedo ver los logs del servidor completamente en vivo

🗣️ Prueba de Feynman (Explicación):
Escenario: Estás trabajando en tu proyecto final y tu novia te ve concentrado tirando comandos con flechas (>) y barras (|) en la pantalla negra de VirtualBox. Ella te pregunta con curiosidad: "¿Qué significan esos símbolos raros que le pones a los comandos?". Explícale en un párrafo corto, usando la analogía de la tuberías de agua de una casa (grifos, desagües y uniones), qué hacen los operadores >, >> y el pipe |.

Te explico facilmente el este simbolo > redirige el agua a un estañon pero el problema es que ese estañon tiene un desague entonces no se puede llenar completamente osea siempre va a tener agua limpia, por el contrario con >> el estañon no tiene desague y se puede llenar(anexar/añadir) perfectamente agua al estañon. Ahora bien se ocupa alimentacion(agua y tuberia) aqui es donde entra "|" el asu vez viene siendo un grifo que en su parte izquierda recive el agua y su parte derecha es la salida por donde pasa el agua(datos), entrada(izquierda)/salida(derecha).