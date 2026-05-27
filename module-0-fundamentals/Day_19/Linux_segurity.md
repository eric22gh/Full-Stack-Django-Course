# 🚀 DÍA 19: MÓDULO 0 - Seguridad en Linux: Usuarios, Permisos y SSH

**📦 Dependencias del Módulo:**
*   **Entorno:** Máquina Virtual con Ubuntu en VirtualBox operativa.
*   **Terminal:** Consola nativa de Ubuntu.
---

## 📖 FASE 1: TEORÍA 
Linux nació desde sus raíces como un sistema multiusuario. Esto significa que decenas de personas (o procesos de software) pueden estar conectadas al mismo servidor a la vez. Para evitar que un usuario borre el trabajo de otro o altere los archivos del sistema, Linux implementa una matriz de seguridad estricta basada en tres identidades (Dueño, Grupo, Otros) y tres acciones (Lectura, Escritura, Ejecución).

## DOCUMENTACIÓN OFICIAL
*🔗 **Doc Oficial:** [GNU Coreutils - File Permissions](https://www.gnu.org/software/coreutils/manual/html_node/File-permissions.html)*

### 🎯 El Propósito
Cuando subas tu API de Django a AWS o configures n8n, tus scripts van a interactuar con el sistema de archivos. Si dejas un archivo con permisos totalmente abiertos, cualquier atacante que explote una vulnerabilidad web podrá secuestrar tu servidor. Dominar los permisos te permite aplicar el "Principio del Menor Privilegio": dar el acceso mínimo necesario para que tu software funcione de forma segura.

### 🎯 ¿Qué problema resuelve la Matriz de Permisos y SSH?
1.  **Protección de datos críticos:** Evita que procesos externos (como un servidor web público) modifiquen archivos de configuración del sistema (`/etc`) o lean variables de entorno secretas.
2.  **Acceso remoto seguro:** SSH reemplaza los protocolos antiguos que mandaban contraseñas en texto plano por la red, permitiéndote gobernar servidores en cualquier parte del mundo de forma encriptada usando llaves matemáticas.

### 📁 Desglose Anatómico de la Matriz de Permisos (rwx)

Cuando ejecutas `ls -l`, verás una cadena de 10 caracteres al inicio (ej: `-rwxr-xr--`). Así se descifra:

| Posición | Símbolo | Significado Técnico | Valor Octal (Numérico) |
| :--- | :--- | :--- | :--- |
| `0` | `-` o `d` | Tipo de archivo (`-` = archivo común, `d` = directorio). | No aplica |
| `1-3` | `rwx` | Permisos del **Dueño** (User): puede leer, escribir y ejecutar. | r=4, w=2, x=1 (Suma: 7) |
| `4-6` | `r-x` | Permisos del **Grupo** (Group): puede leer y ejecutar, no modificar. | r=4, w=0, x=1 (Suma: 5) |
| `7-9` | `r--` | Permisos de **Otros** (Others): el resto del mundo solo puede leer. | r=4, w=0, x=0 (Suma: 4) |

### 🔑 Puntos Clave 
*   **Representación Octal:** Los permisos se pueden cambiar usando números. La suma de los valores define el permiso final. `7` es control total (4+2+1), `5` es lectura y ejecución (4+1), `4` es solo lectura. Un permiso `755` es el estándar para scripts ejecutables.
*   **El Superusuario (`sudo`):** El usuario `root` tiene el poder de saltarse todas las reglas de permisos. Usar `sudo` antes de un comando te otorga temporalmente ese poder de "Dios".
*   **Criptografía Asimétrica (SSH):** Funciona con un par de llaves. Tu máquina local tiene una **Llave Privada** (tu contraseña secreta que nunca dejas salir) y el servidor tiene tu **Llave Pública** (el candado). Si encajan, entras sin pedir contraseña.

### ⚠️ Buenas y Malas Prácticas
*   **✅ Buenas Prácticas:** Mantener tus archivos de credenciales y llaves SSH privadas con el permiso estricto `600` (solo el dueño lee y escribe, nadie más puede hacer nada).
*   **❌ El Error Típico (Mala Práctica):** Ejecutar `chmod 777` en carpetas de proyectos para solucionar problemas de "Permission Denied". Esto abre las puertas de par en par a nivel de seguridad y es motivo de rechazo inmediato en auditorías de IT.

### 💻 Implementación Oficial (Guía de Comandos Básicos)
```bash
ls -l archivo.py                     # Visualiza los permisos detallados de un archivo
chmod +x script.sh                   # Añade permiso de ejecución de forma simbólica
chmod 755 automatizacion.py          # Asigna rwxr-xr-x de forma octal (numérica)
chmod 600 llaves.pem                 # Asigna rw------- (máxima seguridad para archivos secretos)
sudo chown eric:developers app.log   # Cambia el dueño a 'eric' y el grupo a 'developers'
ssh-keygen -t rsa -b 4000            # Genera un par de llaves SSH de alta seguridad

💻 FASE 2: PRÁCTICA
Nota: Ejecuta estos comandos dentro de tu Ubuntu en VirtualBox.

⚙️ Ejercicio 1: Lógica Base CLI (Cálculo Octal)
Bash
# Contexto: Tienes un script de Python que limpia reportes viejos y necesitas asignarle permisos exactos.
# Requisitos:
# 1. Crea un archivo en tu Home llamado 'limpiador.py'.
# 2. Configura sus permisos usando el modo octal para que:
#    - Tú (Dueño) puedas Leer, Escribir y Ejecutar.
#    - Los de tu equipo (Grupo) puedan Leer y Ejecutar.
#    - El resto del mundo (Otros) NO pueda hacer absolutamente nada (ni ver que existe).
#    - Ejecuta un 'ls -l limpiador.py' 

# --- TUS COMANDOS Y RESULTADOS AQUÍ ---
1- cd Escritorio/, 2- touch limpiador.py, 3- chmod 750 limpiador.py, ls -l limpiador.py

🚀 Ejercicio 2: Proyecto Real (Aislamiento de Credenciales de la Agencia)
Bash
# Contexto: Vas a crear el archivo donde guardarás las API Keys de n8n y los accesos a la base de datos PostgreSQL de tus clientes de Limón.
# Requisitos:
# 1. En la carpeta 'agencia_flow', crea un archivo llamado '.env' (el punto al inicio lo hace oculto).
# 2. Escribe dentro la línea: "DB_PASSWORD=Limon2026" (puedes usar un redireccionador o el editor nano).
# 3. Quítale absolutamente todos los permisos al Grupo y a Otros, dejando que SOLO tú puedas leerlo y escribirlo.
# 4. Haz un 'ls -la' para verificar que los permisos quedaron exactamente como: -rw-------

# --- TUS COMANDOS AQUÍ ---
1- cd Escritorio/agencia_flow/, 2- touch .env, 3-  echo "DB_PASSWORD=Limon2026" > .env, 4- head -n 5 .env, 5- DB_PASSWORD=Limon2026, 
6- chmod 600 .env, 7- ls -l .env, 8- -rw-------
# NOTA: El permiso 600 (rw-------) es el estándar de oro en ciberseguridad para proteger contraseñas en entornos de producción.

🚀 Ejercicio 3: Proyecto Real (Simulación de Conexión AWS SSH)
Bash
# Contexto: Para conectarte a tus futuras instancias EC2 en AWS, necesitas dominar la generación de llaves criptográficas.
# Requisitos:
# 1. Genera un par de llaves SSH dentro de tu máquina virtual usando el comando 'ssh-keygen'.
# 2. Cuando te pida la ruta, dale ENTER para que use la ruta por defecto (~/.ssh/id_rsa). No le pongas passphrase por ahora.
# 3. Entra a la carpeta oculta '.ssh' y lista su contenido. Identifica cuál es tu llave pública (el candado para los servidores) y cuál tu llave privada.

# --- TUS COMANDOS AQUÍ ---
1- ssh-keygen -t rsa -b 4000, 2- ENTER, 3- cd ~/.ssh/, 4- ls -l, 5- id_rsa # llave privada, id_rsa.pub # llave publica


🐛 Ejercicio 4: Lectura de Código y Debugging
Bash
# Contexto: Tu cliente de una tienda en retail intentó correr un script de carga de inventario en Python 
# que tú le programaste, pero la terminal le muestra el error: "bash: ./inventario.py: Permission denied".
# El cliente, buscando en internet, vio que ejecutando "sudo" o "chmod 777" se arregla.
# Analiza por qué esas opciones son peligrosas y escribe la solución correcta que deberías guiar al cliente a hacer.

# --- PROPUESTAS PELIGROSAS DEL CLIENTE ---
Opción A: sudo python3 inventario.py
Opción B: chmod 777 inventario.py

# --- TU EXPLICACIÓN Y CORRECCIÓN AQUÍ ---
# Explicación de los riesgos de la Opción A y B:
la mejor solucion para el cliente es que yo me conecte via remota al servidor y ver que permisos tiene el archivo inventario.py con ls -l y luego proceder a cambiarle los permisos aplicando las buenas practicas con un chmod 755, ya que le va a permitir al cliente si esta en un grupo o es un usuario comun leer y ejecutar el archivo.
La opción A: sudo python3 inventario.py es altamente peligroso porque le da temporalmente permisos completos a un usuario que no conoces el sistema o el script, en este otro caso la Opción B: chmod 777 inventario.py le daria los permisos permanentes lo que es aun mas peligroso.
Nota: el permiso 711 (rwx--x--x) falla en el lenguaje de python. Porque cuando el cliente ejecuta ./inventario.py, el sistema operativo necesita leer el archivo de texto para pasárselo al intérprete de Python. Si le quitas el permiso de lectura (r) al grupo o a otros, el sistema arrojará un error. Por eso, el estándar para scripts de Python siempre debe ser 755 (rwxr-xr-x).

# Comando correcto que debe ejecutar el cliente para dar solo el permiso necesario:
chmod 711 inventario.py o chmod 755 inventario.py

🧠 FASE 3: CONSOLIDACIÓN TEÓRICA (Cierre del Día)
❓ Pregunta Teórica 1:
Si un directorio tiene asignados los permisos numéricos 644, ¿qué problema experimental ocurrirá cuando intentes usar el comando cd para entrar a él, incluso si eres el dueño del directorio? (Pista: Analiza qué significa la ejecución 'x' en una carpeta).
R/ El permiso chmod 644 otorga permisos al super user para leer y escribir y no para ejecutarlo(abrirlo) por eso es que si se realiza dicha operacion dara un error de permission denied, tambien le da permiso al grupo para leer y a otros tambien para leer

❓ Pregunta Teórica 2:
En el contexto de automatizaciones corporativas en la nube, ¿por qué es una mala práctica de seguridad extrema utilizar la clave de tu usuario "Root" de AWS para conectar tus scripts locales en lugar de generar un usuario IAM con permisos restringidos?
R/ El principio de menor privilegio se aplica para todo este tema de permisos y usarios. Utilizar el usuario root en AWS es una mala practica y una gran brecha de seguridad ya que es un usuario que tiene los privilegios maximos sobre la plataforma o infraestructura, lo correcto es crear un usario IAM y otorgarle solo los permisos necesarios, por ejemplo si la empresa va a implementar redes y servicios de almacenamiento, nosotros como buenos profesionales solo le otorgaremos esos permisos.

🗣️ Prueba de Feynman (Explicación):
Escenario: Helen te ve generando las llaves SSH en VirtualBox y te pregunta para qué sirve esa "llave pública" y "llave privada" de la que tanto hablan en seguridad informática. Explícales en un párrafo corto, utilizando la analogía de un candado y su llave física, cómo funciona esta tecnología para entrar a un servidor remoto sin que nadie pueda clonar tus accesos.
R/ En este caso el servidor es el porton grande de acceso que tiene una llave publica que en este caso es el candado y todo el mundo puede ver, y el servidor las posee. El servidor tambien tiene una llave privada la cual seria la llave fisica que nosotros tenemos y guardamos con seguridad para abrir el candado(llave publica), cuando vamos a conectarnos via remota al servidor las 2 llaves(candado y llave) tienen que coincidir para que el porton habra(conectarse via remota exitosamente) de lo contrario la coneccion fallara o el porton no se abrira.