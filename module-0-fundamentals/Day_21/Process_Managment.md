Markdown
# 🚀 DÍA 21: MÓDULO 0 - Gestión de Procesos, Recursos y Variables


## 📖 FASE 1: TEORÍA 
Un servidor Linux no es solo un montón de archivos estáticos; es un ecosistema vivo donde decenas de programas (procesos) se ejecutan simultáneamente en la memoria RAM y compiten por el tiempo del procesador (CPU). Saber administrar este tráfico es la principal responsabilidad de un SysAdmin. Además, el sistema utiliza "Variables de Entorno", que son pequeños letreros invisibles en la memoria que le dicen a los procesos dónde buscar cosas o cómo comportarse.

## DOCUMENTACIÓN OFICIAL
*🔗 **Doc Oficial:** [Linux man pages: ps(1)](https://man7.org/linux/man-pages/man1/ps.1.html) / [kill(1)](https://man7.org/linux/man-pages/man1/kill.1.html)*


### 🎯 El Propósito
Cuando tu script automatizado de Python en AWS se quede congelado (en un *loop* infinito) o tu servidor de PostgreSQL colapse porque el disco duro se llenó al 100%, no podrás usar el "Administrador de Tareas" visual de Windows. Tienes que saber cómo diagnosticar qué programa está consumiendo la memoria, cómo asesinar ese proceso de forma segura y cómo leer el espacio del disco desde la terminal de texto antes de que todo el sistema caiga.

### 🎯 ¿Qué problema resuelve la Gestión de Procesos y Recursos?
1.  **Evitar caídas de servidor (Downtime):** Detectar picos de consumo de CPU/RAM y detener procesos rebeldes antes de que el servidor se congele.
2.  **Configuración de Entornos (Variables):** Permitir que herramientas como Python, Django o n8n sepan en qué modo están corriendo (ej. `PRODUCCION` o `DESARROLLO`) sin tener que cambiar el código fuente.


### 📁 Desglose Anatómico de Herramientas y Señales
| Comando / Concepto | Propósito Técnico Real e Importancia |
| :--- | :--- |
| `top` / `htop` | Monitores interactivos en tiempo real. Muestran los procesos ordenados por consumo de CPU o RAM. (`htop` es la versión moderna y colorida, pero a veces requiere instalación con `sudo apt install htop`). |
| `ps aux` | Toma una "fotografía" estática de todos los procesos corriendo en este exacto milisegundo. Ideal para combinarlo con `grep` y buscar un programa específico. |
| `PID` | Process ID. El número de cédula único (identificador) de cada programa en ejecución. Lo necesitas obligatoriamente para detenerlo. |
| `kill -15` (SIGTERM) | **Cierre amable.** Le pide al programa que guarde sus datos, cierre sus archivos y se apague de forma segura. Es la forma correcta y profesional de detener un proceso. |
| `kill -9` (SIGKILL) | **Asesinato forzado.** El sistema operativo aniquila el programa instantáneamente. Solo debe usarse si `kill -15` falló, ya que puede corromper bases de datos. |
| `df -h` | Muestra el espacio libre y usado de los **discos duros** (particiones) en formato humano (MB, GB). |
| `du -sh` | Calcula cuánto pesa una **carpeta específica** y todo lo que tiene adentro. |
| `$PATH` | La variable de entorno más importante. Es una lista de rutas donde Linux busca los comandos. Si escribes `python3`, Linux lo busca en las carpetas listadas en tu `$PATH`. |


### 🔑 Puntos Clave (Bajo el capó)
* **Procesos en Segundo Plano (Background):** Si ejecutas un script que tarda mucho y quieres seguir usando la terminal, agregas un ampersand `&` al final del comando. El proceso se irá al fondo y te devolverá tu consola.
* **Variables de Entorno Temporales vs Permanentes:** Si escribes `export ENTORNO="produccion"`, la variable existirá solo hasta que cierres esa ventana de la terminal. Para hacerla permanente en cada inicio de sesión, el comando debe guardarse dentro de archivos ocultos como `~/.bashrc`.


### ⚠️ Buenas y Malas Prácticas
* **✅ Buenas Prácticas:** Monitorizar periódicamente el espacio en disco con `df -h` en tus servidores cloud. Un disco que llega al 100% hará que bases de datos como PostgreSQL se corrompan y dejen de arrancar.
* **❌ El Error Típico (Mala Práctica):** Encontrar un proceso bloqueado y lanzarle directamente un `kill -9` sin intentar primero un `kill -15`. Esto es el equivalente a apagar tu computadora arrancando el cable de la pared en lugar de usar el botón de "Apagar sistema".


### 💻 Implementación Oficial (Guía de Comandos Básicos)
top                                  # Abre el monitor en vivo (presiona 'q' para salir de la pantalla)
ps aux | grep "python"               # Busca el PID de cualquier script de python que esté corriendo
kill 1234                            # Envía SIGTERM (amable) al proceso con PID 1234 (por defecto kill usa -15)
kill -9 1234                         # Envía SIGKILL (forzado) al proceso con PID 1234
df -h                                # Muestra el espacio de las particiones (h = human readable)
du -sh /home/eric/agencia_flow       # Muestra el peso total de la carpeta (s = summary, h = human)
echo "export MI_VARIABLE="valor"" >> ~/.bashrc crear una variable de entorno permantente
source ~/.bashrc   # aplicar los cambios sin reiniciar
printenv                             # Muestra todas las variables de entorno actuales del sistema
echo $PATH                           # Muestra el contenido exclusivo de la variable PATH
htop                                 # monitor de procesos al igual que top, pero con colores.


💻 FASE 2: PRÁCTICA
Nota: Ejecuta estos comandos dentro de tu Ubuntu en VirtualBox. 

⚙️ Ejercicio 1: Lógica Base CLI (Cacería de Procesos)
# Contexto: Un script de automatización se quedó colgado en segundo plano y está consumiendo recursos.
# Requisitos:
# 1. Ejecuta este comando para simular un proceso congelado en segundo plano: sleep 3000 &
# 2. La terminal te devolverá un número entre corchetes y otro número al lado (ej: [1] 5432). El segundo número es el PID.
# 3. Usa 'ps aux' combinado con 'grep' (usando la tubería |) para buscar el proceso de nombre "sleep" y confirmar su PID.
# 4. Envíale la señal de cierre amable (SIGTERM) usando el comando kill y su PID.
# 5. Vuelve a hacer la búsqueda con grep para confirmar que el proceso ya no está corriendo.

# --- TUS COMANDOS AQUÍ ---
1- sleep 3000 & = [1] 19760, 2- ps aux | grep "sleep" = 19760, 3- kill -15 19760, 4- ps aux | grep "sleep", 5- No se encuentra


🚀 Ejercicio 2: Proyecto Real (Auditoría de Almacenamiento Cloud)
# Contexto: AWS te envía una alerta indicando que tu disco virtual (EBS) de 20GB está casi lleno.
# Requisitos:
# 1. Usa el comando adecuado para ver el porcentaje de uso de la partición principal de tu disco duro 
#    (suele llamarse /dev/sda1 o /dev/mapper/... y está montada en la ruta '/'). Anota mentalmente qué % de uso tiene.
# 2. Ve a tu Home y usa el comando adecuado para ver cuánto pesa exactamente la carpeta 'agencia_flow' 
#    y todo su contenido resumido en formato humano (MB/KB).

# --- TUS COMANDOS AQUÍ ---
1- df -h, 2- = 27%, 2- cd /home/eric/Escritorio, 3- du -sh agencia_flow = 52kb agencia_flow/


🚀 Ejercicio 3: Proyecto Real (Inyección de Variables para Django)
# Contexto: Tu backend de Django en el Proyecto 1 necesita saber si debe conectarse 
# a la base de datos de pruebas o a la de producción sin que tú tengas que tocar el código de Python.
# Requisitos:
# 1. Crea una variable de entorno en tu terminal llamada 'DJANGO_ENV' y asígnale el valor "produccion" usando el comando 'export'.
# 2. Verifica que el sistema operativo haya guardado la variable imprimiéndola en pantalla con 'echo $DJANGO_ENV'.
# 3. Usa el comando 'printenv' combinado con 'grep' para buscar "DJANGO" y comprobar que la variable existe en la memoria global de la terminal.

# --- TUS COMANDOS AQUÍ ---
1- cd /home/eric/Escritorio, 2- export DJANGO_ENV="produccion", 3- echo $DJANGO_ENV, 4- printenv | grep "DJANGO"


🐛 Ejercicio 4: Lectura de Código y Debugging
# Contexto: Un compañero tiene un script de scraping en Python que extrae datos de hoteles en Limón, 
# pero el script falló y se quedó "zombie" (congelado). Te muestra el comando que piensa usar para matarlo.
# Analiza por qué su enfoque es destructivo y reescribe la rutina correcta que debe hacer un SysAdmin.

# --- COMANDOS DEL COMPAÑERO ---
# Él vio en top que el PID del script es 8842 y quiere ejecutar directo en la terminal:
kill -9 8842
primero debe de verificar si 8842 es el proceso que quiere matar puede ser con: ps aux o htop.
segundo ya cuando tenga el PID del proceso el comando que tiene que ingresar es el kill -15 8842.
lo que hara este comando es que se pide al sistema que guarde sus datos, cierre sus archivos y despues se apague, es una buena practica yt el kill -9 es un cierre forzado, por eso no se recomienda.

🧠 FASE 3: CONSOLIDACIÓN TEÓRICA (Cierre del Día)
❓ Pregunta Teórica 1:
¿Cuál es la diferencia técnica y el caso de uso real entre tomar una "fotografía" de los procesos con ps aux | grep palabra versus abrir el monitor interactivo con top? ¿Cuándo usarías uno y cuándo el otro?
Con ps aux se toma una fotografia de los procesos de x o y momento, yo lo usaria si no requiero tanos datos para remediar el problema...
top es mas completo, muestra los procesos en tiempo real y continua mostrandolos hasta que el usuario lo cierre, yo lo usaria en una situacion en la que ocupo estar monitoriando los procesos frecuentemente y en tiempo rea.

❓ Pregunta Teórica 2:
Imagina que escribes el comando python3 script.py y la terminal te dice "Comando no encontrado", pero tú sabes que Python sí está instalado en una carpeta rara del sistema. ¿Qué papel juega la variable de entorno $PATH en este error?
Con el comando echo $PATH se muestra todo el contenido de la variable de entorno, path le dice al terminal donde buscar los programas o en este caso el script, si el script no esta creado en path la terminal no lo va a reconocer y le aparecera en pantalla: Comando no encontrado

🗣️ Prueba de Feynman (Explicación):
Escenario: Un amigo que usa Windows no entiende por qué los usuarios de Linux hablan de matar procesos con -15 o -9. Explícale en un párrafo corto, usando la analogía de sacar a un cliente problemático de un restaurante, cuál es la diferencia exacta entre aplicarle un kill -15 y un kill -9.
Te lo explico facilmente, ala hora de sacar a un cliente de un restaurante por disturbios ocasionados, podemos hacerlo de 2 maneras: de una forma rapida, ruda y no darle el tiempo de recojer sus pertenecias que esto seria un ejemplo de kill -9 8893 o de una forma gentil y segura en el que se le diga que comprende su molestia pero ocupo que salga del restaurante y darle tiempo al cliente de recoger sus pertenencias, que vendria siendo un kill -15 8893... Este ultimo es una buena practica ya que el sistema le dice al proceso que guarde sus datos y cierre archivos.