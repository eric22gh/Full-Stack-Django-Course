# 🌐 DÍA 23: MÓDULO 0 - Redes Profundas: Capa de Transporte y Puertos (El Motor)

**📦 Dependencias del Módulo:**
* **Entorno:** Máquina Virtual con Ubuntu en VirtualBox.
* **Comandos:** `ss`, `nc` (Netcat), `telnet`.


## 📖 FASE 1: TEORÍA 
En el Día 22 vimos que la IP es la dirección de la casa (Capa 3) y HTTP es el idioma que hablan al llegar (Capa 7). Pero falta algo en el medio: **La Capa de Transporte (Capa 4)**. 
Una vez que los datos llegan a tu servidor (la casa), ¿por qué puerta entran? Un servidor tiene 65,535 "puertas" llamadas **Puertos**. Además, los datos no viajan de golpe, viajan en pequeños paquetes, y hay dos formas de enviarlos: asegurándose de que lleguen (TCP) o lanzándolos lo más rápido posible (UDP).

## DOCUMENTACIÓN OFICIAL
*🔗 **Doc Oficial:** [Comando ss (Socket Statistics)](https://man7.org/linux/man-pages/man8/ss.8.html) / [Netcat Manual](https://linux.die.net/man/1/nc)*


### 🎯 El Propósito
Cuando corras tu servidor de Django, te dirá: `Starting development server at http://127.0.0.1:8000/`. Ese `:8000` es el puerto. Si intentas levantar otro proyecto al mismo tiempo, la terminal te gritará "Port already in use" (Puerto ya en uso). Tienes que saber cómo auditar tus puertos, cerrarlos y probar si están abiertos hacia el mundo exterior.


### 🎯 Puntos Clave: TCP, UDP y Puertos
1.  **TCP (Transmission Control Protocol):** Es el protocolo formal y seguro. Antes de enviar datos, hace un saludo de 3 pasos (3-way handshake: *"¿Estás ahí?", "Sí, estoy aquí", "Perfecto, te envío el dato"*). Si un paquete se pierde, TCP lo vuelve a enviar. Es lento pero 100% confiable. Lo usan la web (HTTP), correos y SSH.
2.  **UDP (User Datagram Protocol):** Es el protocolo rápido y temerario. Lanza los paquetes sin preguntar si el otro está listo y no le importa si se pierden por el camino. Lo usan los videojuegos online, las videollamadas (Zoom) y el streaming en vivo.
3.  **Puertos (Los Apartamentos):** Si la IP es la dirección del edificio, el Puerto es el número del apartamento. 
    * `Puerto 80`: Tráfico Web Inseguro (HTTP).
    * `Puerto 443`: Tráfico Web Seguro (HTTPS).
    * `Puerto 22`: Conexiones remotas de consola (SSH).
    * `Puerto 5432`: Base de datos PostgreSQL.
    * `Puerto 3306`: Base de datos MySQL.
    * `Puerto 53`: DNS (resolución de nombres de dominio).
    * `Puerto 21`: FTP (Transferencia de archivos).
    * `Puerto 6379`: Base de datos Redis.
    * `Puerto 27017`: Base de datos MongoDB.
    * `Puerto 3389`: Escritorio remoto (RDP).
    * Puerto 631: Impresión en red (IPP).
    * `Puerto 25`: Envío de correos (SMTP).
    * `Puerto 110`: Recepción de correos (POP3).
    * `Puerto 143`: Recepción de correos (IMAP).
    * `Puerto 23`: Telnet (conexión remota insegura).
    * `Puerto 8000 / 8080`: Puertos de desarrollo (Django / React).
4.  **Sockets:** Es la combinación de una IP y un Puerto (ej. `192.168.1.5:22`). Es la conexión final.


### ⚠️ Buenas y Malas Prácticas
* **✅ Buenas Prácticas:** La regla de oro del SysAdmin: **Cerrar todo por defecto**. Si tu servidor solo aloja una web, un escaneo de puertos solo debería mostrar el 80 y el 443 abiertos. El resto debe estar bloqueado por un Firewall.
* **❌ El Error Típico (Mala Práctica):** Dejar el puerto de tu base de datos (ej. 5432) abierto al internet público (`0.0.0.0`). Las bases de datos solo deben escuchar conexiones internas (`127.0.0.1` o `localhost`).


### 💻 Implementación Oficial (Guía de Comandos CLI)
ss -tuln                          # Lista todos los puertos TCP/UDP que están Abiertos/Escuchando en tu servidor
ss -tulnp                         # Igual que el anterior, pero te dice qué Programa (PID) está usando cada puerto
nc -zv google.com 443             # Netcat: Intenta tocar la puerta 443 de Google para ver si está abierta
sudo ufw status                   # Revisa el estado del Firewall de Ubuntu (Uncomplicated Firewall)


💻 FASE 2: PRÁCTICA
⚙️ Ejercicio 1: Lógica Base CLI (Escaneo de Puertos Locales)
# Contexto: Quieres saber qué "puertas" tiene abiertas tu máquina virtual Ubuntu en este momento.
# Requisitos:
# 1. Usa el comando 'ss' con las banderas para listar puertos TCP (t), UDP (u), 
#    que estén en estado de escucha/listening (l) y que muestre números en lugar de nombres (n).
# 2. Revisa la lista y anota mentalmente si ves el puerto 22 (SSH) o el 53 (DNS local) abiertos.

# --- TUS COMANDOS AQUÍ ---
1- ss -tuln, 2- puestos abiertos: 631 y 53


🚀 Ejercicio 2: Proyecto Real (Tocar la puerta con Netcat)
# Contexto: En el futuro, tu API de Django intentará conectarse a una base de datos externa. 
# Si falla, no sabrás si es un error de contraseña o si el puerto está cerrado por un Firewall. 
# Netcat (nc) es la ganzúa del SysAdmin para probar puertas.
# Requisitos:
# 1. Usa 'nc' con los flags '-zv' (z = solo escanear, v = verbose/detallado) para verificar 
#    si el puerto 443 (HTTPS) del dominio 'github.com' está abierto.
# 2. Intenta hacer lo mismo hacia el puerto 22 (SSH) de 'github.com'. 
#    Nota la diferencia en la respuesta (GitHub tiene el puerto 22 abierto para operaciones con Git).

# --- TUS COMANDOS AQUÍ ---
1- nc -zv github.com 22, 2- respuesta: 22 port [tcp/ssh] succeeded, 3- nc -zv github.com 5432 4- respuesta: 5432 port (tcp) failed: connection refused, 5- nc -zv github.com 443, 6- respuesta: 443 port [tcp/https] succeeded


🚀 Ejercicio 3: Proyecto Real (Resolución de Conflictos de Puertos)
# Contexto: Intentas iniciar tu servidor de pruebas en el puerto 8080, pero el sistema 
# te da un error diciendo que el puerto "ya está en uso". Necesitas encontrar al culpable.
# Requisitos:
# 1. Simula un programa "secuestrando" el puerto 8080 abriendo una terminal y ejecutando 
#    un servidor de escucha con Netcat: nc -l 8080 & 
#    (El '&' lo manda a segundo plano, simulando que es un proceso oculto).
# 2. Ahora, usa 'ss -tulnp' combinado con 'grep' para buscar qué proceso (PID) tiene secuestrado el puerto 8080.
# 3. Usa el comando 'kill' con el PID que encontraste para liberar el puerto.

# --- TUS COMANDOS AQUÍ ---
1- nc -l 8080 &, 2- 5609, 3- ss -tulnp | grep 8080, 4- kill -15 5609, 5- ss -tulnp | grep 8080, 6- terminado nc -l 8080


🐛 Ejercicio 4: Lectura de Código y Debugging
# Contexto: Configuras tu servidor PostgreSQL en la nube para el Proyecto 1 (Finance Tracker). 
# Desde tu computadora local en Limón, intentas conectarte a la base de datos usando el puerto 5432, 
# pero la conexión se queda "cargando" indefinidamente hasta que da un error de "Timeout".
#
# Un compañero te dice: "Seguro escribiste mal la contraseña de la base de datos, revisa tu .env".
#
# Analiza por qué un error de "Timeout" descarta automáticamente que sea un problema de contraseña, 
# y explica, basándote en la Capa de Transporte, cuál es la causa real del problema.

# --- EXPLICACIÓN DEL ERROR Y TU CORRECCIÓN AQUÍ ---
El error timeout se refiere a que el tiempo de coneccion despues de ingresar las credenciales se vencio, pero tenemos una pista clave y es la misma palabras (timeout) esto se refiere aque no se realizo la coneccion a la base de datos atravez del puerto, muy posiblemente el puerto 5432 que es el de la base de datos de popstgress esta cerrado y no esta escuchando, para confirmarlo podemos ingresar el comando ss -tulnp para verificar que puertos estan escuchando y asi poner a escuchar el puerto 5432 para que la coneccion se realice.


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA (Cierre del Día)
❓ Pregunta Teórica 1:
Tu cliente necesita transmitir cámaras de seguridad en vivo desde su comercio hacia su teléfono móvil. No le importa si en la transmisión la imagen sufre un "glitch" de un milisegundo por perder un cuadro, pero sí necesita que no haya retraso (lag). ¿Qué protocolo se debería usar bajo el capó para esta transmisión de video, TCP o UDP, y por qué?
Como ingeniero en informatica le recomendaria UDP(User Datagram Protocolo) brindandole los pros como una transmicion de datos rapida y de poco retraso ya que la usan en sistemas como videojuegos en linea y plataforma de video llamada como zoom sin embargo le abvertiria sobre los contras ya que este protocolo tiene baja seguridad y su envio de paquetes no es tan eficiente com el de TCP debido a esto es propenso a cyber ataques.


❓ Pregunta Teórica 2:
Si abres tu navegador y escribes http://www.nacion.com, ¿a qué puerto de destino exacto se está intentando conectar el navegador por defecto, aunque tú no hayas escrito el número?
Por defecto se estaria estableciendo coneccion con el puerto 80(http)

🗣️ Prueba de Feynman (Explicación):
Escenario: Un cliente no entiende por qué su página web necesita un "Certificado de Seguridad SSL" para pasar del puerto 80 al puerto 443.
Explícale, usando la analogía de enviar una carta por correo en un sobre transparente vs. enviar la carta en una caja fuerte portátil con llave, la diferencia entre navegar por el Puerto 80 (HTTP) y el Puerto 443 (HTTPS).
Al enviar un correo de suma importacion por el protocolo http seria como enviar una carta con un sobre transparente, el correo seria propenso a robos, duplicado de informacion crucial para sus empresa señor como por ejemplo sus credenciales para la caja fuerte. En camio el protocolo https es altamente eficiente y seguro para el transporte de datos, ya que gracias al SSL(Certificado de seguridad) sus datos viajaran encryptado y de una forma mas segura, que en este caso seria enviar las credenciales de su caja fuerte con un carro blindado, vidrio anti balas y poralizado a su destino.