# 🛡️ DÍA 26: MÓDULO 0 - Diagnóstico de Redes Avanzado y Acceso Seguro (SSH)

**📦 Dependences del Módulo:**
* **Entorno:** Máquina Virtual con Ubuntu en VirtualBox.
* **Herramientas:** `ssh`, `ssh-keygen`, `traceroute`, `mtr`.

## 📖 FASE 1: TEORÍA 
Administrar la nube requiere operar computadoras a miles de kilómetros de distancia. Para hacerlo de forma segura sin que nadie intercepte tus comandos en el camino, se creó el protocolo **SSH**. Además, para diagnosticar problemas de conectividad global, los ingenieros no se quedan en el simple `ping`; rastrean la ruta física de los datos salto por salto a través de los routers del mundo.


## DOCUMENTACIÓN OFICIAL
*🔗 **Doc Oficial:** [OpenSSH Documentation](https://www.openssh.com/manual.html) / [Traceroute Man Page](https://man7.org/linux/man-pages/man1/traceroute.1.html)*

### 🎯 El Propósito
Cuando crees tu servidor EC2 en AWS para la Agencia Flow, Amazon no te dará una contraseña (las contraseñas son inseguras y fáciles de hackear). Te dará un archivo de llave criptográfica. Aprenderás cómo usar tus llaves públicas y privadas para conectarte al servidor instantáneamente sin escribir una sola contraseña, y cómo diagnosticar si la red entre Costa Rica y el servidor de AWS tiene problemas de latencia o pérdida de paquetes.

### 🎯 Puntos Clave: Autenticación por Llaves y Rastreo de Rutas
1.  **¿Cómo funciona SSH? (Puerto 22):** SSH encripta todo el tráfico entre tu terminal local y el servidor remoto. Puedes conectarte de dos formas:
    * **Por contraseña:** Insegura, propensa a ataques de fuerza bruta.
    * **Por llaves SSH (Asimétrica):** Generas un par de llaves en tu laptop. La **Llave Privada** (`id_rsa`) se queda en tu máquina y nunca, bajo ninguna circunstancia, se comparte. La **Llave Pública** (`id_rsa.pub`) se copia en el servidor remoto. Si las llaves encajan, entras.
2.  **Traceroute / MTR (El Mapa del Viaje):** Cuando haces `ping`, solo sabes si el servidor destino responde o no. Con `traceroute`, ves una lista de todos los routers (saltos) por los que pasa tu paquete desde el módem de tu casa, pasando por tu proveedor de internet (ISP), los cables submarinos, hasta llegar al centro de datos de AWS. Si hay un fallo en el camino, verás exactamente en qué país o proveedor se detuvo.



### ⚠️ Buenas y Malas Prácticas
* **✅ Buenas Prácticas:** Deshabilitar por completo el login por contraseña en el archivo de configuración de tu servidor SSH (`/etc/ssh/sshd_config`) y permitir **únicamente** el acceso mediante llaves SSH autorizadas.
* **❌ El Error Típico (Mala Práctica):** Perder tu llave privada o darle permisos muy abiertos en Linux. SSH es tan estricto con la seguridad que si dejas tu llave privada con permisos de lectura para otros usuarios (ej. permisos 777), se negará a conectarse y te arrojará un error de *"Unprotected Private Key File"*.


### 💻 Implementación Oficial (Guía de Comandos CLI)
ssh-keygen -t rsa -b 4000            # Genera un par de llaves SSH ultra-seguras (puedes dar Enter a todo)
ssh-keygen -t rsa -b 4096            # Genera un par de llaves SSH publica y privada (puedes dar Enter a todo)
cat ~/.ssh/id_rsa.pub                # Muestra tu llave pública (esta es la que se copia en los servidores)
ssh -i llaves.pem ubuntu@10.0.0.5    # Conectarse a un servidor remoto usando una llave específica (.pem)
traceroute google.com                # Muestra los saltos que da el paquete en la red (requiere: sudo apt install traceroute)
mtr google.com                       # Mi herramienta favorita: un ping + traceroute en tiempo real e interactivo (presiona 'q' para salir)


💻 FASE 2: PRÁCTICA
⚙️ Ejercicio 1: Lógica Base CLI (Fábrica de Llaves Criptográficas)
# Contexto: Vas a preparar tu entorno local para poder conectarte a futuros servidores de AWS sin usar contraseñas.
# Requisitos:
# 1. Genera un par de llaves SSH en tu terminal usando el comando: ssh-keygen -t rsa -b 4096
#    (Cuando te pregunte en qué archivo guardarlo o que le pongas una contraseña/passphrase, presiona ENTER a todo para dejarlo por defecto).
# 2. Usa el comando 'ls -la ~/.ssh/' para listar el contenido de la carpeta oculta de SSH.
# 3. Identifica y escribe en tus respuestas cuál es el archivo de tu llave PRIVADA y cuál es el de tu llave PÚBLICA.

# --- TUS COMANDOS Y RESPUESTAS AQUÍ ---
1- ssh-keygen -t rsa -b 4000 , ssh-keygen -t rsa -b 4096, 3- ls -la ~/.ssh/ , 4- llave publieca: id_rsa.pub, llave privada: id_rsa


🚀 Ejercicio 2: Proyecto Real (Mapeando la Carretera de Internet)
# Contexto: Un cliente en Limón se queja de que el sistema de la Agencia Flow se siente "lento" hoy. 
# Quieres verificar si hay un problema en los cables internacionales de internet.
# Requisitos:
# 1. Instala las herramientas de diagnóstico ejecutando: sudo apt update && sudo apt install traceroute mtr -y
# 2. Ejecuta un 'traceroute' apuntando a un servidor lejano, por ejemplo: traceroute wikipedia.org
# 3. Observa las líneas del resultado (cada una es un router en el mundo). 
#    Anota en tu respuesta cuántos "saltos" (hops/líneas) le tomó a tu internet llegar hasta el servidor de Wikipedia.

# --- TUS COMANDOS Y RESPUESTAS AQUÍ ---
1- sudo apt update && sudo apt install traceroute mtr -y, 2- traceroute wikipedia.org, 3- Saltos: 12


🚀 Ejercicio 3: Proyecto Real (Simulando un Servidor Remoto en Local)
# Contexto: Quieres practicar cómo conectarte por SSH, pero como no tenemos otra computadora física, 
# te conectarás a tu propia máquina virtual simulando que es un servidor remoto. (A esto se le llama conectarse a localhost).
# Requisitos:
# 1. Asegúrate de tener el servidor SSH instalado en tu Ubuntu con: sudo apt install openssh-server -y
# 2. Intenta conectarte a ti mismo usando tu nombre de usuario actual y la dirección de bucle local:
#    ssh eric@127.0.0.1   (o cambia 'eric' por el nombre de tu usuario en la terminal si es distinto).
# 3. La terminal te dará un mensaje de advertencia de seguridad (ECDSA key fingerprint) preguntando si confías en la conexión.
#    Escribe 'yes' y presiona Enter. Luego introduce tu contraseña de Ubuntu.
# 4. ¡Listo! Estás dentro de un túnel SSH. Escribe el comando 'exit' para cerrar la sesión remota y volver a tu terminal local.

# --- TUS COMANDOS AQUÍ ---
1- sudo apt install openssh-server -y, 2- ssh ericAE@127.0.0.1 3- yes, 4- contraseña de Ubuntu, 5- exit


🐛 Ejercicio 4: Lectura de Código y Debugging (El Bloqueo de la Llave)
# Contexto: Descargaste la llave de acceso de tu nuevo servidor EC2 de AWS llamada 'agencia_key.pem'.
# Abres la terminal e intentas conectarte de inmediato usando el comando oficial:
# ssh -i agencia_key.pem ubuntu@54.210.43.12
#
# Pero la terminal se niega a conectar y te escupe el siguiente error crítico en la pantalla:
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Permissions 0777 for 'agencia_key.pem' are too open.
# It is required that your private key files are NOT accessible by others.
# This private key will be ignored.
# Load key "agencia_key.pem": bad permissions
# Permission denied (publickey).
#
# Analiza técnicamente por qué SSH bloqueó la conexión y escribe el comando exacto 
# de Linux (que aprendiste en los Días 17 y 18) para corregir los permisos de ese archivo y poder entrar al servidor.

# --- EXPLICACIÓN DEL ERROR Y TU CORRECCIÓN AQUÍ ---
El primer error es que el archivo de la llave privada 'agencia_key.pem' tiene permisos demasiado abiertos (0777), lo que significa que cualquier usuario en el sistema puede leer, escribir y ejecutar ese archivo. SSH requiere que las llaves privadas sean accesibles solo por el propietario para garantizar la seguridad. Para corregir esto, debes cambiar los permisos del archivo a 600, lo que permite solo al propietario leer y escribir el archivo.
El comando exacto para corregir los permisos es: `chmod 600 agencia_key.pem`


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA (Cierre del Día)
❓ Pregunta Teórica 1:
Acabas de generar tu llave pública (id_rsa.pub) y tu llave privada (id_rsa). Si vas a configurar un servidor en AWS o quieres conectarte de forma segura a tu cuenta de GitHub, ¿cuál de las dos llaves debes subir a internet y cuál debes ocultar celosamente en tu computadora?
La respuesta correcta es: Debes subir la llave pública (id_rsa.pub) a internet (por ejemplo, a tu servidor en AWS o a tu cuenta de GitHub) y debes ocultar celosamente la llave privada (id_rsa) en tu computadora, ya que esta es la que garantiza tu acceso seguro y no debe ser compartida con nadie.


❓ Pregunta Teórica 2:
Estás ejecutando mtr google.com para diagnosticar la red. Notas que en el salto número 3 (un router de tu proveedor local) hay un 15% de pérdida de paquetes (Loss%), y a partir de ahí la latencia se dispara. ¿Qué significa esto en el mundo real y qué acción deberías tomar?
En este caso, un 15% de pérdida de paquetes en el salto número 3 indica que hay un problema en la red de tu proveedor local, lo que está afectando la calidad de la conexión hacia Google. Esto podría traducirse en una experiencia de navegación lenta o intermitente para los usuarios. La acción recomendada sería contactar a tu proveedor de servicios de internet (ISP) para informarles del problema y solicitar que lo solucionen, ya que es un fallo fuera de tu control.


🗣️ Prueba de Feynman (Explicación):
Escenario: Tu socio comercial de la Agencia Flow no entiende mucho de servidores y te pregunta: "¿Por qué nos complicamos creando llaves SSH públicas y privadas si con una contraseña de 20 caracteres con mayúsculas y símbolos estaríamos igual de seguros?".
Explícales, usando la analogía de una cerradura física en la puerta de la oficina donde tú repartes copias del molde de la llave a tus empleados, pero nadie puede falsificar la cerradura, por qué las llaves SSH destruyen por completo la seguridad basada en contraseñas tradicionales.

Te explico: Imagina que la puerta de tu oficina tiene una cerradura muy especial que solo puede ser abierta con un molde de llave único. Tú repartes copias de este molde a tus empleados, quienes pueden abrir la puerta sin problemas. Sin embargo, si alguien logra obtener una copia de la llave (como una contraseña), podría entrar fácilmente a la oficina y causar problemas.