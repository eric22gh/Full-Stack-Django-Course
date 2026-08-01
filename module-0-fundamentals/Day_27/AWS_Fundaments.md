# ☁️ DÍA 27: MÓDULO 0 - Arquitectura Cloud y Navegación (El Mapa del Tesoro)

**📦 Dependencias del Módulo:**
* **Entorno:** Máquina Virtual con Ubuntu en VirtualBox.
* **Herramientas:** `awscli` (Lo instalaremos hoy).

## 📖 FASE 1: TEORÍA 
Hasta hace unos años, si querías poner una página web o una base de datos para una empresa, tenías que comprar un servidor físico (On-Premise), conectarlo a la corriente, ponerle aire acondicionado y rezar para que no se fuera la luz o el disco duro fallara. 

El **Cloud Computing (La Nube)** cambió esto por completo. AWS (Amazon Web Services) te permite "alquilar" pedacitos de sus supercomputadoras repartidas por todo el mundo, cobrándote por segundo de uso. Cuando ya no lo ocupas, lo apagas y dejas de pagar.

## DOCUMENTACIÓN OFICIAL
*🔗 **Doc Oficial:** [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) / [What is AWS CLI?](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)*

### 🎯 El Propósito
Como ingeniero de la Agencia Flow, no puedes simplemente darle clic a "Crear Servidor" sin saber dónde se está creando. Tienes que elegir estratégicamente el país (para que la carga sea rápida) y diseñar tu sistema para que sobreviva a desastres naturales. Además, debes saber moverte entre la interfaz visual (Consola Web) y la consola de comandos (CLI), ya que la automatización solo vive en la terminal.

### 🎯 Puntos Clave: Regiones y Zonas de Disponibilidad (AZs)
Para entender AWS, imagina un mapa mundial. Amazon no tiene un solo edificio gigante, tiene su infraestructura dividida en tres niveles de tamaño:

1.  **Región (Region):** Es un área geográfica del mundo. Por ejemplo, `us-east-1` (Norte de Virginia), `sa-east-1` (São Paulo, Brasil), o `ap-northeast-1` (Tokio, Japón). Al elegir una región, defines las leyes bajo las que están tus datos y la latencia (velocidad) para tus usuarios. En AWS hay 37 regiones en total, y cada una tiene un nombre único. de las cuales son: 
Américas (9 regiones)
US East (N. Virginia) – us-east-1
US East (Ohio) – us-east-2
US West (N. California) – us-west-1
US West (Oregon) – us-west-2
Canada (Central) – ca-central-1
Canada West (Calgary) – ca-west-1
South America (São Paulo) – sa-east-1
Mexico (Querétaro) – mx-central-1
Chile (Santiago) – cl-south-1

Europa (10 regiones)
Ireland – eu-west-1
London (UK) – eu-west-2
Paris (France) – eu-west-3
Frankfurt (Germany) – eu-central-1
Stockholm (Sweden) – eu-north-1
Milan (Italy) – eu-south-1
Spain (Madrid) – eu-south-2
Zurich (Switzerland) – eu-central-2
Warsaw (Poland) – eu-central-3
Helsinki (Finland) – eu-north-2

Asia Pacífico (14 regiones)
Tokyo (Japan) – ap-northeast-1
Osaka (Japan) – ap-northeast-3
Seoul (South Korea) – ap-northeast-2
Singapore – ap-southeast-1
Sydney (Australia) – ap-southeast-2
Melbourne (Australia) – ap-southeast-4
Jakarta (Indonesia) – ap-southeast-3
Malaysia – ap-southeast-5
New Zealand – ap-southeast-6
Thailand – ap-southeast-7
Hong Kong – ap-east-1
Taipei (Taiwán) – ap-east-2
Mumbai (India) – ap-south-1
Hyderabad (India) – ap-south-2

Medio Oriente (2 regiones)
Bahrain – me-south-1
UAE (Dubai) – me-central-1

África (2 regiones)
Cape Town (Sudáfrica) – af-south-1
Kenya (Nairobi) – af-east-1  

   
3.  **Zona de Disponibilidad (Availability Zone - AZ):** Dentro de cada Región hay varias AZs. Por ejemplo, dentro de Virginia (`us-east-1`) existen `us-east-1a`, `us-east-1b`, `us-east-1c`. **Una AZ es un conjunto de 1 o más centros de datos físicos separados por kilómetros.** Tienen energía e internet independientes. Si un huracán inunda la AZ "A", la AZ "B" sigue intacta, aws tiene mas de 120 zonas de disponibilidad.

4.  **Centro de Datos (Data Center):** Es un edificio físico con servidores, aire acondicionado, generadores eléctricos y seguridad. Cada AZ tiene al menos un centro de datos, pero puede tener varios.  

5.  **Edge Locations:** Puntos pequeñitos repartidos en muchísimos más países (incluyendo a veces nodos cercanos en Centroamérica) que sirven solo como memoria caché para cargar fotos y videos más rápido (Servicio CloudFront).

### Nota: AWS actualmente cuenta con 37 regiones activas en el mundo, distribuidas en 5 continentes, con más de 120 zonas de disponibilidad. Estas regiones permiten desplegar servicios cerca de los usuarios para reducir latencia y cumplir requisitos legales 
### AWS GovCloud (US): regiones especiales para clientes gubernamentales en EE. UU.
### AWS China: regiones independientes en Beijing y Ningxia, operadas en colaboración local.
### Opt-in: algunas regiones requieren habilitación manual en la cuenta (ej. Hong Kong, Malasia, Nueva Zelanda).

### ⚠️ Buenas y Malas Prácticas
* **✅ Buenas Prácticas:** Diseñar **Alta Disponibilidad (High Availability - HA)**. Si creas una base de datos crítica, le dices a AWS que ponga el servidor principal en la AZ "A" y un clon automático en la AZ "B". Si se quema el edificio "A", tu web sigue viva.
* **❌ El Error Típico (Mala Práctica):** Crear todos los servidores para un cliente de Costa Rica en la región de Sídney, Australia (`ap-southeast-2`). Los datos tendrán que cruzar cables submarinos a través de todo el Océano Pacífico, generando un *lag* (retraso) enorme en cada clic, el mmejor lugar para implementar losa seria en virginia o ohia.
  

### 💻 Implementación Oficial (Guía de Comandos y Conceptos)
*   **Consola de Administración de AWS (GUI):** Es la página web bonita de Amazon. Ideal para ver reportes visuales o cuando estás aprendiendo un servicio nuevo.
*   **AWS CLI (Command Line Interface):** Es la herramienta que instalas en tu Ubuntu. Te permite hacer **todo** lo que hace la web, pero escribiendo comandos. Es obligatorio para crear *scripts* y automatizar infraestructuras.


sudo apt update && sudo apt install awscli -y   # Instala el cliente de AWS en tu terminal Linux
aws --version                                   # Verifica que el CLI se instaló correctamente

## comandos en windows
# Para instalar AWS CLI en Windows, puedes descargar el instalador desde la página oficial de AWS y seguir las instrucciones. Una vez instalado, abre PowerShell o CMD y ejecuta: 1- `aws --version` para verificar la instalación.
2- `aws configure` para configurar tus credenciales de AWS (Access Key ID y Secret Access Key).
3- `aws s3 ls` para listar los buckets de S3 en tu cuenta, por ejemplo.
4- `aws ec2 describe-instances` para listar las instancias EC2 en tu cuenta.
5- `aws help` para obtener ayuda sobre los comandos disponibles y su uso.
6- `aws configure list` para ver la configuración actual de AWS CLI, incluyendo la región predeterminada y el formato de salida.
7- `aws s3 cp localfile.txt s3://mybucket/` para copiar un archivo local a un bucket de S3.
8- `aws s3 sync localfolder/ s3://mybucket/` para sincronizar un directorio local con un bucket de S3.
9- `aws ec2 start-instances --instance-ids i-1234567890abcdef0` para iniciar una instancia EC2 específica.
10- `aws ec2 stop-instances --instance-ids i-1234567890abcdef0` para detener una instancia EC2 específica.


💻 FASE 2: PRÁCTICA

⚙️ Ejercicio 1: Lógica Base CLI (Preparando las Herramientas)
# Contexto: Como SysAdmin, tu principal herramienta para gobernar la nube será tu propia terminal.
# Requisitos:
# 1. Abre tu terminal de Ubuntu.
# 2. Actualiza los repositorios de apt e instala el AWS CLI usando el comando correspondiente.
# 3. Verifica la instalación ejecutando 'aws --version' y anota la versión de Python que el 
#    sistema te muestra que usa el CLI por debajo.

# --- TUS COMANDOS Y RESPUESTAS AQUÍ ---
1- `sudo apt update && sudo apt install awscli -y`, 2- `aws --version` 3- aws -- version: aws-cli/2.36.12 y Python/3.14.6 

🚀 Ejercicio 2: Proyecto Real (Decisiones de Arquitectura y Latencia)
# Contexto: La Agencia Flow acaba de cerrar un contrato con una cadena de supermercados en Limón. 
# El cliente necesita que el sistema de facturación en la nube responda lo más rápido posible 
# para no hacer fila en las cajas.
# Tienes dos opciones principales de Regiones en AWS que el equipo está debatiendo:
# Opción A: us-east-1 (Norte de Virginia, EE. UU.)
# Opción B: eu-central-1 (Fráncfort, Alemania)
#
# Requisitos:
# Escribe tu decisión y justifica técnicamente por qué elegiste esa región basándote 
# en el concepto de la Capa de Red y la geografía (Latencia).

# --- TU DECISIÓN ARQUITECTÓNICA AQUÍ ---
AWS tiene al rededor de 37 regions y 120 edge location, ala hora de implementar una infraestructura tenemos que tener esto contemplado ya que unos de los detalles mas importantes que pide el cliente es la baja latencia, para el no negociable. Bajo este criterio la mejor region para este cliente es la us-east-1 o norte de virginia ya que posee la mejor latencia. Nota: ni siempre la menor distancia es la mejor opcion, por ejemplo una de las regiones mas cercanas a limon es la mx-central-1(queretaro mexico) pero debido asu infraestructura basica tiene una mayor latencia que la region de virgiania.


🚀 Ejercicio 3: Proyecto Real (Diseño de Alta Disponibilidad)
# Contexto: El sistema del supermercado del Ejercicio 2 no se puede caer nunca. 
# Decides alquilar 2 servidores EC2 (máquinas virtuales) para que se repartan el trabajo.
#
# Requisitos:
# 1. Ya elegiste la Región. Ahora, dentro de esa región existen las Zonas de Disponibilidad 
#    'a', 'b', 'c', 'd', 'e' y 'f'.
# 2. Explica cómo distribuirías esos dos servidores entre las Zonas de Disponibilidad para 
#    asegurarte de que si un incendio destruye un centro de datos entero de Amazon, 
#    tu cliente en Limón pueda seguir facturando.

# --- TU DISEÑO DE DISPONIBILIDAD AQUÍ ---
Anteriormente selecionamos la region de virgiania, a continiacion vamos con la alta disponibilidad. Cuando se desplega infraestructura en aws siempre y siempre tenemos que pensar de que las cosas van a fallar, por ese motivo hay que utilizar 2 o mas AZ(availability zones), yo selecionaria us-east-1a y us-east-1c o inclusive una mas us-east-1e.


🐛 Ejercicio 4: Lectura de Código y Debugging (El Misterio del Servidor Fantasma)
# Contexto: Un desarrollador Junior de la agencia creó un servidor para hacer pruebas el viernes. 
# El lunes en la mañana, entra a la Consola Web de AWS (el sitio web), 
# va a la sección de EC2 y ve con terror que dice: "Instancias en ejecución: 0".
# 
# Él entra en pánico y te escribe: "¡Nos hackearon! ¡Alguien borró el servidor el fin de semana!".
#
# Tú, conociendo cómo funciona la Consola de AWS, sabes que el 90% de las veces que un junior 
# "pierde" un servidor, no ha sido borrado, solo está mirando mal el Mapa.
#
# Analiza y explica cuál fue el error de novato exacto que cometió el desarrollador en la 
# interfaz de AWS al buscar su servidor.

# --- EXPLICACIÓN DEL ERROR Y TU CORRECCIÓN AQUÍ ---
Con mi experiencia me atreveria a decir que el esta buscaNDO INSTANCIAS en la region incorrecta, como consejo es importante tener presente en que region se esta trabajando y segundo no es necesario ingresar a la consola de aws para ver las instancias, desde vs code con el comando aws describe-instances vemos un listado de instancias que tenemos en la cuenta.
# --- Cómo listar instancias EC2 sin importar la región desde la terminal ---
# Si no sabes en qué región el Junior dejó la máquina encendida, puedes forzar
# al CLI a buscar en una región específica agregando la bandera --region:

aws ec2 describe-instances --region us-west-2
aws ec2 describe-instances --region us-east-1


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA (Cierre del Día)
❓ Pregunta Teórica 1:
En el mundo de los servidores físicos tradicionales, se habla del modelo CapEx (Gasto de Capital = pagar $5,000 de un solo golpe por un servidor). En el Cloud Computing (AWS), usamos el modelo OpEx (Gastos Operativos). Explica con tus palabras cuál es la ventaja financiera para una empresa de pasarse al modelo OpEx de AWS.
Con el modelo de pago OpEx de AWS solo se paga por lo que se usa esto es una gran ventaja a la hora de iniciar un proyecto ya que la empresa puede destinar eso dinero hacia otro lado, aws solo pide informacion de los que se va a implementar, las necesidades y el tipo de proyecto que se va a realizar. a diferencia de ompremise que supone un gasto inicial grande y a su vez es poco escalable.

❓ Pregunta Teórica 2:
Si la "Consola Web" de AWS tiene botones visuales muy agradables para crear cosas, ¿por qué los Ingenieros Cloud y DevOps prefieren usar la terminal oscura con el awscli para crear servidores y bases de datos?
Actualmente el mundo entero esta viviendo una transicion hacia la automatizacion por la razon de que todo se nececita mas rapido y eficiente, por esta razon y otras como comandos agiles para hacer varios recursos en aws a la vez los ingenieros y devops prefieren usar la terminal oscura.


🗣️ Prueba de Feynman (Explicación):
Escenario: Un cliente que vende zapatos por internet tiene su página web alojada en una laptop vieja en el cuarto trasero de su tienda. Te dice que no entiende por qué debería pagarle a Amazon (AWS) si él ya tiene su propia computadora. Explícale el concepto de Cloud Computing y Alta Disponibilidad usando la analogía de comprar y mantener tu propio generador eléctrico de gasolina en el patio trasero vs. conectarte a la red eléctrica del ICE.
A la hora de abastecer nuestra vievienda o local con luz electrica obtener con una empresa como el use es una gran ventaja ya que si requerimos mas potencia ya sea 110 a 220 y hasta mas el ice le proveera de dicha potencia y usted pagara por su uso y listo, no conlleva manteniiento de maquinas o otras cosas, en cambio con tu generardor electrico es una maquina a la sele debe de dar mantenimiento periodicamente, combustible, si no ocupas energia tienes que ir a apagar el generardor electrico. son muchos los procesos que con lleva y finalmente si requieres mas potencia vas a tener que hacer un gasto enorme por otro generador electrico... asi mismo es aws, solo pagas lo que usas y ellos se encargan del resto.