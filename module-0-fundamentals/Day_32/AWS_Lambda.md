# ☁️ DÍA 32: MÓDULO 0 - AWS Lambda y el Mundo Serverless

**📦 Dependencias del Módulo:**
* **Entorno:** Máquina Virtual con Ubuntu en VirtualBox.
* **Herramientas:** `awscli`, `zip` (apt install zip).

## 📖 FASE 1: TEORÍA 
Hasta ahora hemos hablado de EC2. Tener un EC2 es como tener el motor de un carro encendido las 24 horas del día. Si alguien entra a tu web, el motor responde. Si es de madrugada y no hay nadie, el motor sigue gastando gasolina (dinero) sin hacer nada.

¿Qué pasaría si pudieras decirle a Amazon: *"Aquí está mi código en Python. Mantenlo apagado. Pero si ocurre un EVENTO (como que alguien suba una foto), enciende una mini-computadora, ejecuta el código en 2 segundos, y apágala inmediatamente"*?
Eso es **AWS Lambda**. A esto se le llama **Serverless (Sin Servidor)**. (Spoiler: Sí hay servidores físicos, pero tú no los administras, ni los actualizas, ni los ves).

## DOCUMENTACIÓN OFICIAL
*🔗 **Doc Oficial:** [¿Qué es AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) / [AWS CLI Lambda Commands](https://docs.aws.amazon.com/cli/latest/reference/lambda/index.html)*


### 🎯 Puntos Clave: Eventos, Handlers y Roles de Ejecución
1.  **Event-Driven (Basado en Eventos):** Una función Lambda no hace nada hasta que algo la "dispara" (Trigger). Los triggers pueden ser:
    * Un archivo que se sube a un bucket S3.
    * Un usuario llamando a un Endpoint HTTP (API Gateway).
    * Un reloj que se activa todos los días a las 8:00 a.m. (EventBridge / Cron).
2.  **El Execution Role (Rol de IAM):** Lambda es un código fantasma. Si ese código intenta leer algo de S3, AWS le dirá "Acceso Denegado". Debes crear un **Rol en IAM** y ponérselo a Lambda para darle permisos de hablar con otros servicios.
3.  **Pago por Milisegundo:** Con EC2 pagas por hora. Con Lambda pagas por el tiempo exacto de ejecución, medido en milisegundos. AWS te regala **1 millón de ejecuciones gratis al mes**.


### ⚠️ Buenas y Malas Prácticas
* **✅ Buenas Prácticas:** Usar Lambda para tareas cortas y explosivas (ej. redimensionar una imagen, procesar un pago, enviar un correo). Mantener el código lo más liviano posible para evitar el "Cold Start" (el milisegundo de retraso al despertar la función).
* **❌ El Error Típico (Mala Práctica):** Intentar usar Lambda para un proceso que tarda 2 horas en terminar (ej. entrenar una Inteligencia Artificial). Lambda tiene un **límite máximo de vida de 15 minutos**. Si tu código no termina en 15 minutos, AWS lo asesina automáticamente.


### 💻 Implementación Oficial (Guía de Comandos CLI)
# 1. Todo código de Lambda debe empaquetarse en un archivo ZIP antes de subirse
zip function.zip index.py

# 2. Crear la función Lambda subiendo el ZIP y asignándole un Rol de IAM
aws lambda create-function --function-name MiPrimerLambda \
    --zip-file fileb://function.zip \
    --handler index.lambda_handler \
    --runtime python3.11 \
    --role arn:aws:iam::123456789012:role/MiLambdaRole

# 3. Invocar (ejecutar) la función manualmente desde la terminal para probarla
aws lambda invoke --function-name MiPrimerLambda output.txt


💻 FASE 2: PRÁCTICA
⚙️ Ejercicio 1: Lógica Base CLI (El Empaquetado)
# Contexto: En el próximo módulo crearás un script en Python llamado 'bot_facturas.py'.
# Quieres subirlo a AWS Lambda para que corra de forma Serverless, pero la consola de 
# AWS CLI requiere que subas el archivo en formato comprimido.
#
# Requisitos:
# Escribe el comando exacto de Linux (usando la herramienta 'zip') que usarías para 
# comprimir el archivo 'bot_facturas.py' dentro de un archivo llamado 'codigo.zip'.

# --- TU COMANDO AQUÍ ---
1- zip codigo.zip bot_facturas.py



🚀 Ejercicio 2: Proyecto Real (Automatización con Triggers)
# Contexto: Un cliente (un fotógrafo en Limón) sube fotos en ultra-alta resolución (40MB cada una)
# a su bucket de S3 llamado 'flow-fotos-raw'. El problema es que esas fotos pesan mucho para 
# mostrarlas en su página web.
# 
# Quieres crear una arquitectura Serverless donde cada vez que caiga una foto nueva en 'flow-fotos-raw', 
# una función Lambda se active automáticamente, comprima la foto a 2MB y la guarde en otro bucket 
# llamado 'flow-fotos-web'.
#
# Requisitos:
# En esta arquitectura, ¿quién actúa como el "Trigger" (Disparador), quién actúa como el 
# "Procesador de Cómputo" y qué permisos exactos de IAM (Lectura/Escritura) necesitaría tener 
# el "Execution Role" de esa Lambda sobre los buckets?

# --- TU DISEÑO ARQUITECTÓNICO AQUÍ --- 
# disparador: bucket(flow-fotos-raw)
# quién actúa como el 
# "Procesador de Cómputo": Lambda
# permisos exactos de IAM (Lectura/Escritura) que necesitaría tener el "Execution Role" de esa Lambda sobre los buckets:
# - Permiso de lectura (s3:GetObject) sobre el bucket 'flow-fotos-raw'
# - Permiso de escritura (s3:PutObject) sobre el bucket 'flow-fotos-web'


🚀 Ejercicio 3: Proyecto Real (EC2 vs Lambda)
# Contexto: Tienes un bot en Python que revisa el precio del dólar en el Banco Central de Costa Rica 
# todos los días a las 6:00 a.m. El bot tarda exactamente 10 segundos en correr, envía un mensaje 
# de Telegram y termina.
#
# El desarrollador Junior te dice: "Hay que alquilar un EC2 t3.micro ($8 al mes) encendido 24/7 
# para correr este bot de 10 segundos diario".
#
# Requisitos:
# Explícale al Junior, en términos de costos y mantenimiento, por qué AWS Lambda es 
# infinitamente superior para este caso de uso específico.

# --- TU JUSTIFICACIÓN AQUÍ ---
Lambda es una mejor opcion ya que en primera instancia tenemos un activador que serian la 6 de la mañana, por lo que no es necesario tener un servidor encendido 24/7, ya que el bot solo se ejecuta una vez al día, ponemos un cron job que active la lambda con el script a las 6 de la mañana, despues para finalizar, se le puede enviar un mensaje de telegram con la libreria de python, y al finalizar la lambda se apaga, por lo que no hay costos de mantenimiento ni de electricidad, ya que solo se paga por el tiempo de ejecucion del script, que en este caso es de 10 segundos. En cambio con un EC2, se tendria que pagar por el tiempo que este encendido, aunque no se este usando, lo cual es un gasto innecesario.



🐛 Ejercicio 4: Lectura de Código y Debugging (La Muerte de los 15 Minutos)
# Contexto: Emocionado por el poder Serverless, decides migrar un programa viejo de la agencia 
# a AWS Lambda. El programa se encarga de procesar 50,000 registros en una base de datos 
# y suele tardar unos 25 minutos en completarse cuando lo corrías en tu laptop.
#
# Lo subes a Lambda, lo ejecutas, y notas que siempre procesa los primeros 30,000 registros, 
# pero luego la función muere repentinamente arrojando un error de "Task timed out".
#
# Analiza y explica técnicamente por qué AWS está matando tu proceso a la mitad, 
# y cuál sería la solución arquitectónica correcta (Pista: volver a la infraestructura clásica).

# --- EXPLICACIÓN DEL ERROR Y TU CORRECCIÓN AQUÍ ---
El error ocurre porque AWS Lambda tiene un límite máximo de tiempo de ejecución de 15 minutos por invocación. Dado que tu programa tarda aproximadamente 25 minutos en procesar los 50,000 registros, la función Lambda se agota antes de completar su tarea, resultando en el error "Task timed out". Lo que loe recomiendo es dividir el procesamiento en lotes más pequeños que puedan completarse dentro del límite de tiempo de Lambda, o bien, considerar volver a una infraestructura clásica como EC2, donde puedes ejecutar procesos de larga duración sin restricciones de tiempo. Otra opción sería utilizar servicios como AWS Step Functions para orquestar la ejecución de múltiples funciones Lambda en secuencia, permitiendo así procesar todos los registros sin exceder el límite de tiempo.


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA (Cierre del Día y del Módulo)
❓ Pregunta Teórica 1:
En Lambda, existe un concepto llamado "Cold Start" (Arranque en Frío). Si una función no ha sido llamada en varias horas, AWS "destruye" el contenedor subyacente para ahorrar espacio. Cuando alguien vuelve a llamar la función, hay un pequeño retraso de 1 o 2 segundos mientras AWS la vuelve a preparar.
Sabiendo esto, ¿usarías Lambda para el sistema de control de frenos automáticos de un vehículo autónomo? Justifica por qué.
Bajo esta premisa no usaria lambda para esta implemntacion ya que 1 o 2 son vitales en prevenir accidentes de transito, y el cold start de lambda podria poner en riesgo la vida de las personas, por lo que no es recomendable usar lambda para este caso de uso.


❓ Pregunta Teórica 2:
Si subes una función en Python a Lambda y necesitas que guarde un archivo temporalmente mientras hace cálculos, ¿puedes contar con que ese archivo siga guardado en el disco duro de Lambda al día siguiente? (Piensa en la naturaleza efímera/Stateless del modelo Serverless).
AWS lambda no es un servicio de alamacenamiento en aws, su funcion es ejecutar codigo, por lo que no se puede contar con que el archivo siga guardado en el disco duro de lambda al dia siguiente, ya que lambda es un servicio efimero y stateless, por lo que no guarda ningun tipo de informacion entre ejecuciones. Una posibke solucion seria guardar el archivo en un bucket de S3, que es un servicio de almacenamiento persistente en AWS, y luego acceder a ese archivo desde Lambda cuando sea necesario.


🗣️ Prueba de Feynman (Explicación):
Escenario: El cliente no entiende por qué le propones una "Arquitectura Serverless". Te dice: "Pero si no hay servidor, ¿dónde corre mi código? ¿En el aire?".
Explícale el concepto de Serverless / Lambda vs. EC2 usando la analogía de comprar/alquilar un carro propio (EC2) vs. pedir un Uber (Lambda). Enfatiza en quién maneja, quién da mantenimiento y cómo se cobra.
AWS lambda es como pedir un Uber. Cuando necesitas ir a algún lugar, simplemente llamas al Uber y el conductor te lleva a tu destino. No tienes que preocuparte por mantener el carro, pagar gasolina, ni hacerle mantenimiento. Solo pagas por el viaje que realizas. De manera similar, con Lambda, subes tu código y AWS se encarga de ejecutarlo cuando ocurre un evento, sin que tengas que preocuparte por servidores o infraestructura. En cambio , tener un EC2 es como comprar tu propio carro. Tienes que preocuparte por el mantenimiento, la gasolina, los seguros y todo lo relacionado con el carro, incluso si no lo estás usando. Con EC2, pagas por el tiempo que el servidor está encendido, independientemente de si tu código se está ejecutando o no.