# 🚀 DÍA 17: MÓDULO 0 - El Sistema de Archivos y Navegación Estricta en Linux

## 📖 FASE 1: TEORÍA 
El **FHS (Filesystem Hierarchy Standard)** es el acuerdo oficial gestionado por la Linux Foundation que define cómo deben organizarse los directorios en un sistema operativo tipo Unix. Sin este estándar, cada distribución (Ubuntu, RedHat, Alpine) guardaría los archivos donde quisiera, imposibilitando la automatización y la creación de scripts portables.

## DOCUMENTACIÓN OFICIAL
*🔗 **Doc Oficial:** [Linux Filesystem Hierarchy Standard (FHS)](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html)*

### 🎯 El Propósito
Cuando automatices tareas con Python o n8n en un servidor en la nube (AWS), no tendrás una pantalla con carpetas para hacer doble clic. Tu única ventana al mundo será una terminal de texto. Dominar la navegación estricta te permite moverte por el sistema a ciegas, con precisión, y entender exactamente dónde guarda Linux las configuraciones, los logs y tus proyectos.

### 🎯 ¿Qué problema resuelve el FHS?
Resuelve el caos de la gestión de software y estados del sistema. El FHS separa de forma estricta los archivos según dos ejes críticos:
1.  **Estáticos vs. Variables:** Los archivos estáticos (como los binarios de un programa o las configuraciones) no cambian sin la intervención del administrador. Los archivos variables (como bases de datos, colas de correo o logs) cambian constantemente por la ejecución del sistema.
2.  **Compartibles vs. No Compartibles:** Los compartibles pueden alojarse en un servidor de red y ser usados por varias máquinas (ej: `/usr`). Los no compartibles contienen datos específicos del hardware local(solo son de ese server) (ej: `/etc` o `/boot`).


### 📁 Desglose Anatómico del Árbol de Directorios 

| Directorio | Tipo según FHS | Propósito Técnico Real e Importancia |
| `/` | **Raíz (Root)** | El punto de partida. Todo el sistema. El FHS exige que sea lo más pequeño posible para que el sistema pueda arrancar y repararse incluso si otros discos fallan. |
| `/bin` | Estático / Compartible | Binarios de comandos esenciales para **todos** los usuarios (ej: `cat`, `ls`, `cp`). Tradicionalmente eran los necesarios para arrancar el sistema en modo de emergencia. |
| `/sbin` | Estático / Compartible | Binarios de administración del sistema (System Binaries). Comandos destinados al superusuario `root` para tareas de mantenimiento y red (ej: `iptables`, `fdisk`, `reboot`). |
| `/etc` | Estático / No Compartible | **El cerebro de la configuración local.** Aloja archivos de texto puro que controlan el comportamiento de los programas del sistema. Aquí configurarás servicios, usuarios locales y redes. No debe contener binarios. donde se guardan las configuraciones globales |
| `/var` | Variable / No Compartible(estan en local) | **Datos variables (Variable Data).** Espacio diseñado para archivos cuyo tamaño cambia continuamente: archivos de registro (`/var/log`), cachés (`/var/cache`) y colas de tareas. |
| `/home` | Variable / Compartible | Directorios personales de los usuarios del sistema. Es tu entorno seguro de trabajo. Tus proyectos, configuraciones personalizadas (`.bashrc`) y entornos virtuales de Python deben vivir aquí. |
| `/root` | Variable / No Compartible | El directorio `home` específico para el superusuario (administrador). Está separado de `/home` para garantizar que, si la partición de los usuarios se corrompe o no se monta, el administrador aún pueda iniciar sesión y reparar el sistema. |
| `/tmp` | Variable / No Compartible | Archivos temporales. Los programas escriben aquí datos que necesitan por poco tiempo. nOTA: El FHS dicta que **el sistema puede borrar este directorio en cada reinicio**, por lo que nunca debes guardar nada persistente aquí. |


### 🔑 Puntos Clave 
3. **Rutas Absolutas vs. Relativas:**
   * **Absoluta:** El camino completo desde la raíz. Siempre empieza con `/` (ej: `/home/usuario/proyecto`). No importa dónde estés parado, te llevará al mismo lugar.
   * **Relativa:** El camino partiendo de tu ubicación actual. Utiliza los atajos `.` (directorio actual) y `..` (subir un nivel) (ej: `../imagenes`). nota: sirve por si uno no recuerda el nombre ".../module-0-fundamentals"

### ⚠️ Buenas y Malas Prácticas
* **✅ Buenas Prácticas:** Usa siempre el tabulador (`TAB`). Si escribes `cd /e` y presionas `TAB`, la terminal autocompletará a `/etc`. Si no lo hace, es que vas por mal camino. Te ahorra errores de escritura (*typos*).

* **❌ El Error Típico (Mala Práctica):** Trabajar habitualmente dentro de carpetas del sistema como `/var` o `/etc` sin entender que puedes romper la estabilidad del servidor. Tus proyectos de Django y scripts deben vivir estrictamente dentro de tu `/home/tu_usuario/`.

### 💻 Implementación Oficial (Guía de Comandos Básicos)
pwd                        # ¿Dónde estoy? (Print Working Directory)
ls -F                      # Lista archivos añadiendo una '/' al final si es una carpeta
ls -ls                     # lista en formato largo los archivos
ls -la                     # Lista en formato largo mostrando archivos ocultos (. y ..)
cd ~                       # Atajo directo para ir a tu carpeta Home
cd ..                      # retroceder
mkdir -p proyecto/backend  # Crea la carpeta 'proyecto' y, de paso, 'backend' dentro de ella
mkdir -p carpeta/{sub1,sub2,sub3} # Crear una carpeta y varias subcarpetas con `mkdir -p`
cp archivo.txt copia.txt   # Copia un archivo
mv viejo.txt nuevo.txt     # Renombra archivo
mv text.txt destino/       # mueve un archivo a una carpeta
mv archivo1.txt archivo2.txt carpeta/                 # Mover varios archivos
mv foto.jpg home/usuario/Imagenes/ # Mover un archivo a otra ruta(absoluta)

mv reporte.txt home/usuario/docs/reporte_final.txt   # Renombrar el archivo al moverlo
mv -v archivo.txt destino/                            # Ver qué se mueve
sudo mv archivo.txt /ruta/protegida/                  # Usar permisos de administrador
rm -rf carpeta_basura      # Elimina una carpeta y todo su contenido de forma recursiva y forzada (CUIDADO) ~
rm file.txt                # elimina un archivo



💻 FASE 2: PRÁCTICA
Nota: Ejecuta estos comandos dentro de tu WSL 2.

⚙️ Ejercicio 1: Lógica Base CLI (Navegación Quirúrgica)
Bash
# Contexto: Necesitas moverte por el sistema usando atajos sin perder el rumbo.
# Requisitos:
# 1. Ve a tu directorio Home (~).
# 2. Muévete de un solo golpe al directorio del sistema donde se guardan las configuraciones globales.
# 3. Comprueba con un comando que efectivamente estás ahí y lista su contenido en formato largo (-la).
# 4. Regresa al directorio Home usando una ruta relativa de un solo comando (subiendo niveles con '..').

R/ 1- cd ~, 2- cd /etc/, 3- pwd, 4- ls -la, 5- cd ..
nota: El directorio donde se guardan las configuraciones globales es /etc/


🚀 Ejercicio 2: Proyecto Real (Estructura de la Agencia)
Bash
# Contexto: Vas a maquetar la estructura inicial de carpetas para tu portafolio de la "Agencia Flow".
# Requisitos:
# 1. Dentro de tu Home, crea una carpeta llamada 'agencia_flow'.
# 2. Dentro de 'agencia_flow', crea tres carpetas simultáneamente en un solo comando: 'frontend', 'backend' y 'automatizaciones'.
# 3. Entra a la carpeta 'backend' y crea un archivo vacío llamado 'app.py' usando el comando 'touch'.
R/ 1- mkdir agencia_flow, 2- cd agencia_flow/, 3- mkdir Frontend Backend Automatizaciones, 4- cd Backend/, 5- touch app.py


🚀 Ejercicio 3: Proyecto Real (Despliegue Manual Simulado)
# Contexto: Un flujo de n8n descargó un reporte desordenado en tu Home. Debes organizarlo en la carpeta de la agencia.
# Requisitos:
# 1. Ve a tu Home y crea un archivo llamado 'reporte_leads.csv'.
# 2. Mueve ese archivo directamente a la carpeta 'automatizaciones' que creaste en el Ejercicio 2 (Usa una ruta absoluta).
# 3. Crea una copia de ese archivo dentro de la misma carpeta con el nombre 'reporte_respaldo.csv'.
R/ 1- cd escritorio/, 2- cd agencia_flow, 3- touch reporte_leads.csv, 4- mv reporte_leads.csv automatizaciones/ 
5- cp reporte_leads.csv reporte_respaldo.csv

🐛 Ejercicio 4: Lectura de Código y Debugging
Bash
# Contexto: Un compañero de la UNED te pasa un script en texto plano para automatizar la creación de entornos, 
# pero al ejecutarlo en su WSL 2 le lanza errores de carpetas inexistentes.
# Analiza el porqué falla debido al mal uso de rutas absolutas y relativas, y corrígelo.

# --- COMANDOS DEFECTUOSOS DEL COMPAÑERO ---
cd /home/proyectos
mkdir django_app
cd /django_app
touch settings.py
cd ..
rm -rf /django_app

# --- EXPLICACIÓN DEL ERROR Y TU CORRECCIÓN AQUÍ ---
# Explica brevemente por qué falló el comando 'cd /django_app' y reescribe los comandos de forma limpia y funcional.
1- para acceder ala carpeta seria cd django_app/ ya que con el comando del compañero daria un error, por lo tanto el archivo settings.py se esta creando en la carpera proyectos. Al retroceder con el comando cd.. nos ubicariamos en la carpeta home y a la hora de utilizar el comando rm -rf /django_app nos daria error porque 1- no se necesita el / slash para eliminar una carpeta y 2- la carpeta django_app esta creada en la carpeta proyectos y no en la que estamos ubicados que seria la home.
#### comandos de correccion ###
cd /home/proyectos
mkdir django_app
cd django_app/
touch settings.py
cd ..
rm -rf django_app


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA
❓ Pregunta Teórica 1:
Si estás posicionado en /home/usuario/proyectos/django y ejecutas el comando cd /etc, ¿estás usando una ruta absoluta o una ruta relativa? ¿Por qué?
R/ Estaria usando una ruta absoluta, ya que como la teoria explica una ruta adsoluta inicia desde /(root) y pasa por cada carpeta hasta llegar al archivo o carpeta que se solicita, en cambio la ruta relativa inicia con atajos como "." o ".." y etc es una de las carpetas que continuan despues dela carpeta raiz (/).

❓ Pregunta Teórica 2:
¿Qué diferencia fundamental existe entre ejecutar rm archivo.txt y rm -r carpeta/ a nivel del sistema de archivos?
Los 2 comandos son inicialmente para borrar o eliminar, sin embargo la gran diferencia es que rm fil.txt se usa unicamente para eliminar archivos en donde se encuentre ubicado y rm -r carpeta/ es para eliminar las carpeta escrita y todos los archivos que se encuentren en ella.



🗣️ Prueba de Feynman (Explicación):
Escenario: Imagina que estás configurando un servidor en AWS para un comercio local en Limón. El dueño te pregunta asustado: "¿Cómo sé que las carpetas de mi sistema no se van a mezclar con los archivos de configuración del servidor de Amazon?". Explícale en un párrafo corto, usando la analogía de un edificio de apartamentos, cómo Linux organiza y separa el espacio del usuario (/home) del espacio del sistema (/etc o /var).

Buena tarde señor le comento que linux tiene un sistema de carpetas muy ordenado en que las configuraciones del sistema, configuraciones del servidor los guarda en la carpera raiz, dicha carpeta tiene contenido que no se comparte de forma global y solo administrador puede acceder a ellas. Por otro lado los archivos que va usar el local y sus empleados estan en una carpeta de acceso local llamada home. Como extra tambien se le puede añadir una capa de seguridad a los archivos dentro del home.