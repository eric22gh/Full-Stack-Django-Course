Markdown
# 🌐 DÍA 25: MÓDULO 0 - HTTP/HTTPS a Fondo, APIs REST y CORS

**📦 Dependencias del Módulo:**
* **Entorno:** Máquina Virtual con Ubuntu.
* **Comandos:** `curl`, `openssl`.

## 📖 FASE 1: TEORÍA 
La web moderna no lee páginas estáticas, consume datos dinámicos. Para que sistemas distintos (como n8n, React y Django) se comuniquen sin problemas, deben seguir una arquitectura llamada **REST**. Además, como los datos que viajan pueden ser contraseñas o transacciones financieras, deben ir blindados con criptografía (**HTTPS**).


## DOCUMENTACIÓN OFICIAL
*🔗 **Doc Oficial:** [MDN: CORS](https://developer.mozilla.org/es/docs/Web/HTTP/CORS) / [Let's Encrypt: How it works](https://letsencrypt.org/howitworks/)*

### 🎯 El Propósito
Cuando termines tu "Finance Tracker" y lo subas a producción, si alguien intercepta el cable de internet de tu cliente, no debe poder leer qué está enviando. Aprenderás cómo los Certificados SSL/TLS evitan esto. Además, cuando React intente pedirle datos a Django, el navegador lo bloqueará por seguridad (Error de CORS). Hoy entenderás qué es eso para que sepas arreglarlo en 5 minutos en lugar de perder 3 días buscando en foros.


### 🎯 Puntos Clave: Stateless, TLS y CORS
1.  **HTTP es "Stateless" (Sin Estado):** El servidor tiene amnesia severa. Cada petición HTTP es independiente. Si haces login y luego pides ver tu perfil, el servidor ya olvidó quién eres. *Solución:* Usar **Tokens (JWT)**. Le envías tu carnet digital en la "Cabecera" (`Header: Authorization`) en absolutamente cada petición.
2.  **HTTPS (SSL/TLS) y Llaves Asimétricas:** HTTPS no es un protocolo nuevo, es HTTP metido dentro de un tubo seguro de TLS. 
    * Usa **Llaves Públicas y Privadas**. El servidor le da a todo el mundo un candado abierto (Llave Pública). Tu computadora mete los datos en una caja, le pone ese candado y la envía. Ahora, **solo** el servidor tiene la Llave Privada para abrirla.
    
3.  **CORS (Cross-Origin Resource Sharing):** Es un mecanismo de seguridad de los navegadores web (Chrome, Firefox). Si tu frontend está en `miapp.com` y tu API de Django está en `api.miapp.com`, son "orígenes distintos". Por defecto, el navegador bloquea la petición. Django tiene que enviar una cabecera que diga: *"Tranquilo Chrome, yo autorizo a miapp.com a leerme"*.


### ⚠️ Buenas y Malas Prácticas
* **✅ Buenas Prácticas:** Usar **Let's Encrypt** para generar certificados SSL gratuitos y auto-renovables en tus servidores de producción.
* **❌ El Error Típico (Mala Práctica):** Construir una API que envía datos sensibles por `HTTP` o crear rutas confusas (ej. en lugar de usar el verbo `DELETE /usuarios/1`, crear una ruta rara como `POST /borrarUsuario1`).


### 💻 Implementación Oficial (Guía de Comandos CLI)
curl -v [https://google.com](https://google.com)            # El flag -v (verbose) te muestra TODO el saludo secreto del SSL/TLS
openssl s_client -connect github.com:443                    # Extrae y audita el certificado de seguridad de una página
curl -X POST -H "Content-Type: application/json" -d '{"nombre":"Eric"}' [https://api.com/users](https://api.com/users) 
                                                            # Simula a React enviando datos



💻 FASE 2: PRÁCTICA
⚙️ Ejercicio 1: Lógica Base CLI (Auditoría Criptográfica)
# Contexto: Un cliente sospecha que el certificado de seguridad de su página expiró porque
# los usuarios ven una alerta roja en Chrome. Quieres ver la fecha de expiración desde la terminal.
# Requisitos:
# 1. Ejecuta este comando profesional de SysAdmin para extraer las fechas del certificado de github.com:
#    echo | openssl s_client -connect github.com:443 2>/dev/null | openssl x509 -noout -dates
# 2. Analiza el resultado. Anota mentalmente cuál es la fecha 'notAfter' (cuándo expira).

# --- TUS COMANDOS AQUÍ ---
1- echo | openssl s_client -connect github.com:443 2> /dev/null | openssl x509 -noout -dates, 2- notafter=Aug 2 23:59:59 2026 GMT



🚀 Ejercicio 2: Proyecto Real (Simulando a React con JSON)
# Contexto: Antes de programar tu formulario en React, quieres probar si la API externa acepta 
# crear nuevos registros usando el método POST y un cuerpo en formato JSON.
# Requisitos:
# 1. Usa 'curl' para hacer un POST a la API de pruebas: [https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts)
# 2. Debes incluir una Cabecera (-H) indicando que el contenido es JSON: "Content-Type: application/json"
# 3. Debes incluir los Datos (-d) en formato JSON puro: '{"title": "Automatizacion", "body": "Prueba desde Limon", "userId": 1}'
# 4. (Verás en la terminal que la API te responde con un "id", simulando que guardó el dato).

# --- TUS COMANDOS AQUÍ ---
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"title": "Automatizacion", "body": "Prueba desde Limon", "userId": 1}' \
  https://jsonplaceholder.typicode.com/posts
2- {
  "title": "Automatizacion",
  "body": "Prueba desde Limon",
  "userId": 1,
  "id": 101
}

🚀 Ejercicio 3: Proyecto Real (El Error de CORS - Simulación Mental)
# Contexto: Abres la consola de Chrome (F12) en la web de un cliente y ves un error gigante en rojo:
# "Access to fetch at '[https://api.agenciaflow.com/data](https://api.agenciaflow.com/data)' from origin '[https://www.agenciaflow.com](https://www.agenciaflow.com)' 
# has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource."
#
# Requisitos (Responde en texto):
# 1. Según la teoría que leíste, ¿quién está bloqueando la petición, el servidor de Django o el navegador Chrome del usuario?
# 2. ¿Qué cabecera exacta le falta enviar al backend de Django para que el error desaparezca?

# --- TU RESPUESTA AQUÍ ---
# El error de CORS se repara en el BACKEND (Django), diciéndole al servidor que agregue esta línea en sus respuestas de cabecera:
Access-Control-Allow-Origin: https://www.agenciaflow.com, que en resumen le dice al navegador que el backend de Django autoriza a la web de agenciaflow.com a leer sus datos.


🐛 Ejercicio 4: Lectura de Código y Debugging (Seguridad API)
# Contexto: Estás auditando una automatización de n8n creada por otro desarrollador. 
# El flujo se conecta al banco del cliente para descargar un reporte financiero. 
# Al revisar la configuración del nodo HTTP Request en n8n, notas lo siguiente:
#
# URL: [http://banco-api.local/reportes/descargar](http://banco-api.local/reportes/descargar)
# Method: GET
# Headers: 
#   - Authorization: Bearer jwT3kR...
# Query Parameters:
#   - id_cuenta: 123456789
#   - pin_seguridad: 4455
#
# Hay al menos DOS errores críticos de seguridad (nivel despido inmediato) en cómo se diseñó
# o se consumió esta petición hacia la API del banco. Identifícalos basándote en la teoría de HTTP/HTTPS.

# --- EXPLICACIÓN DE LOS 2 ERRORES Y TU CORRECCIÓN AQUÍ ---
Primeramnete usar http en un tema financiero es una gran mala practica, que ya informacion a muy vulnerable al robo de datos. seguidamente me parece que la cabecera 'Authorization: Bearer jwT3kR...' no es el correcto y como ultimo me parece que datos sencible como un pin de seguridad no deberian estar en una query.
curl -X POST https://banco-api.local/reportes/descargar \
  -H "Authorization: Bearer jwT3kR..." \
  -H "Content-Type: application/json" \
  -d '{"id_cuenta": 123456789, "pin_seguridad": 4455}'


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA (Cierre del Día)
❓ Pregunta Teórica 1:
Tu backend (Django) procesa pagos, por lo que usa arquitectura REST estricta. Si un usuario quiere "actualizar" su dirección de envío, ¿qué verbo HTTP (GET, POST, PUT/PATCH o DELETE) debería usar la petición que envía React y por qué?
El verbo que deberia usar la peticion es PUT ya que se usa para actualizar algun contenido, se podria confundir con POST, pero hay que tener claro que post se usa unicamente para crear un nuevo contenido y GET se usa para obtener informacion y DELETE para eliminar X recurso. 

❓ Pregunta Teórica 2:
Explicaste que HTTP es "Sin Estado" (Stateless) y tiene amnesia severa. Cuando tú inicias sesión en Amazon, cierras la pestaña y vuelves a entrar al día siguiente, sigues logueado. Si HTTP no tiene memoria, ¿dónde está guardando tu computadora esa "memoria temporal" o "Token" para enviársela a Amazon y no tener que pedirte la clave de nuevo?
La informacion se estaria guardando en una gran solucion llamada JSON WEB TOKEN(JWT) el guarda sus crendenciales y las envia a la cabecera cada vez que se realiza una peticion.

🗣️ Prueba de Feynman (Explicación):
Escenario: Un cliente escucha que vas a proteger su tienda online con encriptación asimétrica (Llaves Públicas y Privadas) pero no entiende cómo funciona eso si el hacker puede ver los datos viajando por los cables de fibra óptica.
Explícale, usando la analogía de un candado abierto que repartes por la calle y una única llave maestra que guardas en tu casa, cómo funciona la encriptación SSL/TLS al momento de que un cliente envía los datos de su tarjeta de crédito.
La encriptación SSL/TLS funciona como un candado abierto que distribuyes a varias personas por la calle. Cuando un cliente quiere enviar sus datos de tarjeta de crédito, toma ese candado  y lo usa para cerrar una caja donde pone su información. Luego, envía esa caja cerrada a través de la red. Aunque un hacker pueda interceptar la caja mientras viaja por los cables de fibra óptica, no podrá abrirla porque solo tú tienes la llave maestra que habre todos los candados y está guardada en tu casa (el servidor). Así, los datos permanecen seguros y privados hasta que llegan a ti, donde puedes abrir la caja con tu llave y acceder a la información.