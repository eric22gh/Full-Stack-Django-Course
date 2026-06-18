# 🌐 DÍA 22: MÓDULO 0 - Fundamentos de Redes (TCP/IP, DNS y HTTP)

**📦 Dependencias del Módulo:**
* **Entorno:** Máquina Virtual con Ubuntu en VirtualBox.
* **Herramientas de red:** `curl`, `ping`, `nslookup` (ya vienen en Ubuntu).

## 📖 FASE 1: TEORÍA 
Internet no es magia; son cables, direcciones matemáticas y reglas estrictas de comunicación. Como "Fullstack Automation Engineer" de la Agencia Flow, vas a conectar sistemas (ej. un formulario web con una base de datos). Para que esos sistemas se hablen, utilizan el protocolo HTTP, que es el idioma universal de la web.


## DOCUMENTACIÓN OFICIAL
*🔗 **Doc Oficial:** [MDN Web Docs: HTTP](https://developer.mozilla.org/es/docs/Web/HTTP) / [CURL Manual](https://curl.se/docs/manpage.html)*

### 🎯 El Propósito
Cuando construyas la API de tu "Finance Tracker" en Django (Módulo 3), esta vivirá en una dirección IP. Cuando React (Módulo 4) quiera pedirle los datos de los gastos, enviará una carta digital (Petición HTTP). Si esa carta se pierde o devuelve un error, necesitas saber exactamente en qué parte del trayecto falló: ¿Fue el internet (TCP/IP)? ¿Fue el nombre del dominio (DNS)? ¿O fue un error de código en tu API (HTTP 500)?


### 🎯 Puntos Clave de la Arquitectura de Red
1.  **IP y TCP (Las Carreteras):** Cada dispositivo tiene una IP (ej. `192.168.1.10`). TCP es el protocolo que asegura que los datos lleguen completos y en orden, sin que se pierdan paquetes en el camino.
2.  **DNS (El Directorio Telefónico):** Los humanos no memorizan IPs como `142.250.190.46`, memorizan `google.com`. El DNS (Domain Name System) traduce el nombre a la IP real del servidor. Si el DNS falla, la red funciona, pero los nombres no resuelven.

3.  **HTTP (El Idioma de las APIs):** * **Verbos (Métodos):** `GET` (dame datos), `POST` (guarda estos datos nuevos), `PUT` (actualiza datos), `DELETE` (borra datos).
    * **Cabeceras (Headers):** Metadatos invisibles que acompañan tu petición. Aquí van los *Tokens JWT* de seguridad o el formato de los datos (`Content-Type: application/json`).
    * **Códigos de Estado:** * `200 OK`: Todo perfecto.
        * `400 Bad Request`: El cliente (ej. React) mandó datos mal formateados.
        * `401 Unauthorized`: Te falta el token de seguridad.
        * `404 Not Found`: La ruta de la API no existe.
        * `500 Internal Server Error`: Tu código de Python en Django falló y explotó.


### ⚠️ Buenas y Malas Prácticas
* **✅ Buenas Prácticas:** Usar siempre códigos de estado HTTP semánticos en tus APIs. Si un usuario intenta borrar un archivo que no es suyo, devuelve un `403 Forbidden`, no un genérico `400` o `500`.
* **❌ El Error Típico (Mala Práctica):** Asumir que si una página no carga es porque "el servidor está caído". A menudo es un error de DNS local o un bloqueo de un Firewall (puertos cerrados).


### 💻 Implementación Oficial (Guía de Comandos CLI)
ping google.com                # Envía paquetes básicos para ver si hay conexión (Ctrl+C para detener)
nslookup amazon.com            # Consulta al DNS para que te diga qué IP tiene amazon.com
curl [http://example.com](http://example.com)        # Hace una petición HTTP GET y descarga el código HTML a la consola
curl -I [http://example.com](http://example.com)     # El flag -I (i mayúscula) trae SOLO las cabeceras HTTP y el código de estado
curl -X POST https://api...    # Forzar una petición POST en lugar de GET



💻 FASE 2: PRÁCTICA
⚙️ Ejercicio 1: Lógica Base CLI (Resolución y Latencia)
# Contexto: Un cliente te dice que su portal web no funciona. Quieres descartar problemas de red básicos.
# Requisitos:
# 1. Usa el comando 'nslookup' apuntando a 'github.com' y anota mentalmente una de las direcciones IP que te devuelve el DNS.
# 2. Usa el comando 'ping' con el flag '-c 4' (count 4) apuntando a esa IP exacta que obtuviste.
# Esto asegura que le estás haciendo ping directamente al servidor por su número, saltándote el DNS.

# --- TUS COMANDOS AQUÍ ---
1- nslookup github.com, 2- Address: 140.82.113.3, 3- ping 140.82.113.3 -c 4, 5- envio exactamente los 4 paquetes


🚀 Ejercicio 2: Proyecto Real (Inspección de Cabeceras HTTP)
# Contexto: Quieres saber qué tipo de servidor web usa una página famosa y confirmar que responde bien.
# Requisitos:
# 1. Usa 'curl' para hacer una petición a '[https://www.github.com](https://www.github.com)'.
# 2. Obligatorio: Usa un flag específico para que curl NO descargue el código HTML, sino que SOLO te muestre 
#    las cabeceras (Headers) y el Código de Estado HTTP.
# 3. Observa la primera línea de la respuesta (debería ser el código 200) y busca en las cabeceras qué "server" utilizan.

# --- TUS COMANDOS AQUÍ ---
1- curl -I [https://www.github.com], 2- efectivamente codigo 200 y server: github.com


🚀 Ejercicio 3: Proyecto Real (Consumiendo una API REST desde Linux)
# Contexto: En n8n o React vas a consumir APIs JSON. Aquí vas a simularlo desde la terminal de Ubuntu.
# Existe una API pública gratuita para pruebas llamada JSONPlaceholder.
# Requisitos:
# 1. Usa el comando 'curl' para hacer un GET a la siguiente URL: 
#    [https://jsonplaceholder.typicode.com/users/1](https://jsonplaceholder.typicode.com/users/1)
# 2. La respuesta será un objeto JSON puro (con nombre, email, etc.). 
# 3. Haz la misma petición, pero esta vez conéctala (Pipe |) al comando 'grep' para extraer únicamente la línea que contiene la palabra "email".

# --- TUS COMANDOS AQUÍ ---
1- curl https://jsonplaceholder.typicode.com/users/1, 2- curl https://jsonplaceholder.typicode.com/users/1 | grep "email", 3- "email": "Sincere@april.biz"


🐛 Ejercicio 4: Lectura de Código y Debugging
# Contexto: Estás desarrollando el frontend en React (Módulo 4) y tratas de enviar un nuevo 
# gasto a tu API de Django (Módulo 3). Al enviar el formulario, la consola te arroja el siguiente error:
# "HTTP Error: 401 Unauthorized"
#
# Tu compañero desarrollador Junior entra en pánico y dice: 
# "¡Hay que reiniciar el servidor de AWS! ¡La base de datos o el código de Django explotaron!"
#
# Analiza por qué la conclusión de tu compañero es técnicamente incorrecta basándote en el significado
# de la familia de códigos HTTP y explica cuál es el verdadero problema que debes revisar en React.

# --- EXPLICACIÓN DEL ERROR Y TU CORRECCIÓN AQUÍ ---
De primera mi compañero carece de conocer el codigo de errores web, entonces atacaria ese problema porque es la raiz de todo, en general se sabe que los errores 400 son errores de permisos, accesos, etc... y los 500 son errores del servidor. como en este caso es un 401 Unauthorized y se debe a falla en el token de seguridad, el servidor para una responder a una peticion se necesita credenciales, al no encontrarlas sucede este error 401... la solucion mas rapida y eficiente es añadir el token correcto al encabezado de la peticion.


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA (Cierre del Día)
❓ Pregunta Teórica 1:
¿Cuál es la diferencia arquitectónica principal entre un error de la familia 4xx (como 400, 403, 404) y un error de la familia 5xx (como 500, 502, 503)? ¿A quién debes "culpar" en cada caso?
De forma clara y asertiva los errores 400, 403 y 404 son errores de permisos, seguridad, accesos o peticiones al servidor. Los errores 500, 502, 503 son errores del servidor si en algun momento tu pagina wed registra un error 500 la culpa es del servidor ve y revisalo ya que puede ser que tu server este de baja y si tu pagina web registra un error 400 ya sabemos que los problemas son permisos.

❓ Pregunta Teórica 2:
Si el servicio de DNS de tu proveedor de internet falla por completo, ¿todavía sería posible acceder a la página web de un comercio local desde tu computadora? Si es así, ¿cómo tendrías que escribir la dirección en el navegador?
Domain name system o conocido popularmente como DNS es un sistema transforma las largas direcciones IP en nombres mas amenos para memorizar, si en algun momento esto dejara de funcionar, continuariamos con la navegacion por internet y poder acceder a facebook, sim embargo tendriamos que apuntar o memorizar la direccion IP de facebook, IG, TIKTOK o en mi caso la IP de la tienda de mi negocio.

🗣️ Prueba de Feynman (Explicación):
Escenario: Un cliente al que le estás ofreciendo una automatización con n8n te pregunta qué son esas "APIs" y "Cabeceras (Headers)" de las que hablas.
Explícale el concepto de las Cabeceras HTTP usando la analogía de un paquete que se envía por Correos de Costa Rica. (¿Qué representa la caja, qué representa la etiqueta externa y qué función cumplen esas etiquetas invisibles?).
Las Cabeceras HTTP son fragmentos de informacion que acompañan cada peticion y respuesta entre cliente y servidor. permiten que el navegador y el servidor sepan como manejar los datos...
Un ejemplo de estos es el servicio de correos de CR, el cliente hace una peticion y los metadatos serian: nombre completo del emisor y del destinatario, cedula de ambos, provincia, tipo de objeto, numero de telefono listo para enviar al servidor que en este caso es correos, ellos reciben estos datos los interpretan y hacen el envio de la encomienda que seria la respuesta del servidor.