# ☁️ DÍA 31: MÓDULO 0 - RDS y Conexión Total (El Motor de Datos)

**📦 Dependencias del Módulo:**
* **Entorno:** Máquina Virtual con Ubuntu en VirtualBox / Windows Terminal.
* **Herramientas:** `awscli`.
  

## 📖 FASE 1: TEORÍA 
Las bases de datos son el corazón de cualquier aplicación (Django, n8n, WordPress). Tienes dos formas de tener una base de datos en AWS:
1. **No Gestionada (Hazlo tú mismo):** Creas un servidor EC2, entras por SSH, instalas PostgreSQL a mano, configuras el firewall, haces tus propios backups y rezas para que no se corrompa el disco. (Es más barato, pero consume todo tu tiempo).
2. **Gestionada (Amazon RDS):** Le dices a Amazon: *"Dame una base de datos PostgreSQL versión 15"*. Amazon la crea, la actualiza por ti, hace copias de seguridad automáticas todos los días y, si se cae, la levanta sola. (Es más caro, pero te da paz mental).


## DOCUMENTACIÓN OFICIAL
*🔗 **Doc Oficial:** [¿Qué es Amazon RDS?](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) / [AWS CLI Configuración](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)*


### 🎯 Puntos Clave: Endpoints, Multi-AZ y Credenciales
1.  **Endpoints (Puntos de enlace):** A diferencia de un servidor EC2 al que te conectas mediante una dirección IP, a RDS te conectas mediante un "Endpoint" (una URL larga, ej. `midatabase.c3x...us-east-1.rds.amazonaws.com`). AWS usa esto para poder mover tu base de datos de un servidor físico a otro sin que la IP cambie y rompa tu código.
2.  **Multi-AZ (Alta Disponibilidad):** Si activas esto, AWS crea una copia oculta de tu base de datos en otra Zona de Disponibilidad. Si el centro de datos principal se incendia, AWS cambia el Endpoint hacia la copia oculta en menos de 60 segundos. Tus usuarios ni se enteran de que hubo un desastre.
3.  **Ventana de Mantenimiento:** Tú le defines a AWS a qué hora (ej. domingos a las 3:00 a.m.) tiene permiso de apagar la base de datos por 5 minutos para instalarle parches de seguridad.
4.  **Conexión Total (`aws configure`):** Para que tu terminal deje de decir *"Unable to locate credentials"*, debes registrar las llaves IAM que creaste en el Día 28 usando el comando global de configuración.


### ⚠️ Buenas y Malas Prácticas
* **✅ Buenas Prácticas:** Mantener la base de datos **Privada** (Publicly Accessible: NO). Solo tu servidor EC2 (Django) debería poder hablar con RDS. Nadie desde el internet exterior debería siquiera ver la base de datos.
* **❌ El Error Típico (Mala Práctica):** Crear la base de datos como "Pública" y permitir que el puerto 5432 esté abierto a `0.0.0.0/0`. Esto invita a todos los bots del mundo a intentar adivinar tu contraseña (ataques de fuerza bruta).


### 💻 Implementación Oficial (Guía de Comandos CLI)
# El comando más importante de AWS CLI (Te pedirá 4 datos)
aws configure

# Listar todas tus bases de datos RDS
aws rds describe-db-instances

# crear una base de datos RDS PostgreSQL (ejemplo)
aws rds create-db-instance \
    --db-instance-identifier midatabase \
    --db-instance-class db.t3.micro \
    --engine postgres \
    --db-username admin \
    --db-password MiPassword123 \
    --allocated-storage 20 \
    --backup-retention-period 7 \
    --no-publicly-accessible \
    --vpc-security-group-ids sg-0123456789abcdef0 \
    --db-subnet-group-name mi-subnet-group \
    --storage-type gp2 \
    --multi-az \
    --auto-minor-version-upgrade \
    --publicly-accessible false \
    --tags Key=Environment,Value=Dev


# Listar todas tus bases de datos RDS en formato tabla
aws rds describe-db-instances --output table

# Listar todas tus bases de datos RDS en formato JSON
aws rds describe-db-instances --output json

# Ver solo los Endpoints de tus bases de datos (usando filtros avanzados)
aws rds describe-db-instances --query "DBInstances[*].[DBInstanceIdentifier,Endpoint.Address]" --output table

# eliminar una base de datos RDS (ejemplo)
aws rds delete-db-instance \
    --db-instance-identifier midatabase \
    --skip-final-snapshot 



💻 FASE 2: PRÁCTICA
⚙️ Ejercicio 1: Lógica Base CLI (El Enlace Global)
# Contexto: Tienes en un papel las Access Keys que creaste para tu usuario IAM administrador.
# Ahora vas a vincular tu terminal local definitivamente con tu cuenta de AWS.
#
# Requisitos:
# Simula que ejecutas el comando 'aws configure'. Escribe en el bloque de abajo 
# exactamente qué responderías a las 4 preguntas que te hará la terminal.
# (Inventa un Access Key y Secret Key ficticios, pero usa la región que elegiste 
# en el Día 27 y el formato de salida recomendado por defecto 'json').

# --- TUS RESPUESTAS A 'aws configure' AQUÍ ---
# AWS Access Key ID [None]: KHDBVLJACLJADSCVÑQSKN
# AWS Secret Access Key [None]: KJCBSJLASASJBCLJASBCLJASBCJLSBCVLJ
# Default region name [None]: us-east-1
# Default output format [None]: json


🚀 Ejercicio 2: Proyecto Real (Arquitecto de Costos vs. Tiempo)
# Contexto: Un cliente te pide crear el sistema interno de la Agencia Flow. Tienen presupuesto ajustado.
# Opción A: Levantar un EC2 t3.micro ($8/mes) e instalarle PostgreSQL a mano.
# Opción B: Usar Amazon RDS t3.micro ($18/mes) con PostgreSQL gestionado.
#
# Requisitos:
# Como Arquitecto Cloud, debes justificar cuándo vale la pena pagar esos $10 extra al mes.
# Escribe 3 ventajas automáticas que te da RDS por las que recomendarías la Opción B 
# a pesar de ser más cara.

# --- TU JUSTIFICACIÓN ARQUITECTÓNICA AQUÍ ---
1- la alta disponibilidad llamada multi-AZ, en ec2 tambien tenemos alta disponibilidad si lo empleamos correctamente, pero si una az falla tendremos que cambiar el endpoint manualmente y eso seria un costo extra de la empresa hacia su persona.
2- En temas de implementacion en RDS es mucho mas sencilla, aws se encaerga de automatizar la infraestructura como backups, actualizaciones de seguridad y mantenimiento, mientras que en EC2 tendriamos que hacerlo manualmente.
3- Si bien es cierto que a corto plazo ec2 es mas barato, a la larga el costo del mantenimiento lo va ser mas costoso, caso contrario en RDS que es mucho mas sencillo y automatizado, por lo que a largo plazo es mas barato y seguro.



🚀 Ejercicio 3: Proyecto Real (Uniendo EC2 y RDS)
# Contexto: Tienes tu servidor EC2 (Django) con el Security Group "Django-SG".
# Acabas de crear tu base de datos RDS con el Security Group "Database-SG".
#
# Requisitos:
# Para que EC2 se comunique con RDS, ¿qué regla de Inbound (Entrada) exacta debes 
# poner en el "Database-SG" de la base de datos RDS? 
# (Menciona el Protocolo, el Puerto y cuál debería ser el "Origen/Source" de esa regla).

# --- TU REGLA DE FIREWALL AQUÍ ---
El protocolo es TCP, el puerto es 5432 y el origen/source es el Security Group de Django-SG, para que solo las instancias EC2 con ese Security Group puedan acceder a la base de datos RDS.


🐛 Ejercicio 4: Lectura de Código y Debugging (El Endpoint Inalcanzable)
# Contexto: Un colega está intentando conectar el software de contabilidad de su 
# laptop en Costa Rica directamente a una base de datos RDS en AWS.
# El Endpoint es correcto, la contraseña es correcta, y el Security Group tiene 
# abierto el puerto 5432 hacia su IP de Limón.
#
# A pesar de todo esto, la conexión da "Timeout".
#
# Revisas la configuración de la instancia RDS y notas este parámetro:
# "Publicly Accessible: No"
#
# Analiza y explícale a tu colega qué significa ese parámetro, por qué está bloqueando
# su conexión desde Costa Rica, y por qué activar "Yes" (aunque solucionaría el problema 
# inmediato) es una terrible práctica de seguridad.

# --- EXPLICACIÓN DEL ERROR Y TU CORRECCIÓN AQUÍ ---
Si una base de datos dice Publicly Accessible: No, AWS le quita su IP pública por completo. Solo existe en la red privada. Por lo tanto, aunque agregues la IP del colega de Limón en el Security Group, el internet no tiene cómo enrutar los datos hacia la base de datos porque no hay una dirección pública a la cual llegar.
¿Cómo se soluciona en la vida real? Usando un Bastion Host (un pequeño EC2 público al que te conectas por SSH, y desde ahí saltas a la base de datos) o conectando la laptop del colega a una VPN de AWS.


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA (Cierre del Día y del Módulo)
❓ Pregunta Teórica 1:
¿Qué sucede físicamente en la infraestructura de AWS cuando activas la opción Multi-AZ en tu base de datos RDS y el centro de datos principal sufre un apagón masivo?
LO que sucede es que RDS por su naturaleza, siempre y cuando se acgtive la opcion multi-az el sistema automaticamente va a cambiar de AZ, hay personas que se preocuparian por sus datos, pero rds tiene una solucion para ese problema, se puede implementar un backup automatica ya sea semanal o diario para este tipo de sucesos y tambien rds tiene los datos compartidos en las 2 az que se hallan selecionado previamente.


❓ Pregunta Teórica 2:
¿Por qué conectamos el código de nuestras aplicaciones (como Django) usando el Endpoint de RDS en lugar de usar una dirección IP fija como hacíamos con las instancias EC2?
Esto sucede porque el endpoint de RDS es un nombre de dominio que apunta a la dirección IP de la base de datos. Si la base de datos se mueve a otro servidor físico (por mantenimiento o falla), el endpoint sigue siendo el mismo, mientras que una dirección IP fija podría cambiar y romper la conexión. Esto permite una mayor flexibilidad y disponibilidad sin necesidad de actualizar la configuración de la aplicación.


🗣️ Prueba de Feynman (Explicación):
Escenario: Un cliente quiere ahorrar dinero y te dice: "No usemos RDS, mejor instala la base de datos directo en el servidor de la página web (EC2) para tener todo en una sola máquina".
Explícale por qué tener la Base de Datos y la Aplicación Web en la misma computadora es una mala idea. Usa la analogía de tener la caja fuerte con el dinero del negocio en el mismo mostrador de atención al público de la tienda, en lugar de tenerla en una bóveda separada.
La practica de tener la base de datos y la aplicación web en la misma máquina es como tener la caja fuerte con todo el dinero del negocio justo en el mostrador donde atiendes a los clientes. Si alguien entra a robar o si hay un problema con la tienda (como un incendio o un fallo eléctrico), no solo se pierde el dinero, sino también toda la operación del negocio. En cambio, si la caja fuerte (la base de datos) está en una bóveda separada (RDS), incluso si algo le pasa a la tienda (el servidor web), el dinero sigue estando seguro y accesible. Esto asegura que el negocio pueda continuar funcionando sin interrupciones graves.