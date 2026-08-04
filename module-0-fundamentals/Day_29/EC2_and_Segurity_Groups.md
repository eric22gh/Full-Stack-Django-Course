# ☁️ DÍA 29: MÓDULO 0 - EC2 y Security Groups 

**📦 Dependencias del Módulo:**
* **Entorno:** Máquina Virtual con Ubuntu en VirtualBox.
* **Herramientas:** `awscli`.

## 📖 FASE 1: TEORÍA 
Hasta ahora, hemos usado tu máquina virtual local de VirtualBox. Pero si tu laptop se apaga, tu sitio web se cae. Para eso existe **Amazon EC2 (Elastic Compute Cloud)**. Es el servicio que te permite alquilar computadoras virtuales (Instancias) en los centros de datos de Amazon, elegir cuánta memoria RAM tienen, cuántos procesadores y qué sistema operativo usan.

Y lo más crítico: vienen protegidas por un **Security Group (Grupo de Seguridad)**, que es un Firewall virtual que bloquea absolutamente todo el tráfico por defecto hasta que tú digas lo contrario.

## DOCUMENTACIÓN OFICIAL
*🔗 **Doc Oficial:** [¿Qué es Amazon EC2?](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) / [Security Groups para EC2](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)*


### 🎯 Puntos Clave: Instancias y Escudos de Fuego
1.  **Tipos de Instancias (Familias y Tamaños):** AWS tiene nombres clave para sus computadoras. 
    * `t2.micro` o `t3.micro`: Son las más baratas (a veces gratuitas el primer año), ideales para pruebas, con 1 CPU y 1GB de RAM. La letra ('t') es la familia, el número ('3') es la generación, y el final ('micro') es el tamaño.
    
| Categoría            | Ejemplos principales | Optimización          | Casos de uso clave        |
| ---                  | ---               | ---                     | ---                       |
| General Purpose      | M5, M6, T3, Mac2  | Balance CPU/memoria/red | Web apps, DBs medianas    |
| Burstable Performance| T2, T3, T4g       | CPU variable            | Tráfico irregular         |
| Compute Optimized    | C5–C9             | CPU intensivo           | Batch, gaming, ML         |
| Memory Optimized     | R5–R8, X1, U7i    | RAM masiva              | In-memory DBs, big data   |
| Storage Optimized    | I3, I4, D2, H1    | IOPS altos              | DBs, logs, data lakes     |
| Accelerated Computing| P3, G5, Trn1, Inf1| GPUs/FPGAs              | IA, gráficos, simulaciones|
| HPC Optimized        | Hpc6a, Hpc7g      | HPC escalable           | Simulaciones científicas  |
| Previous Generation  | M4, C4, R4, I2    | Compatibilidad          | Software legado           |


2.  **AMI (Amazon Machine Image):** Es el "CD de instalación". Cuando creas un EC2, le dices qué AMI usar: Ubuntu 24.04, Amazon Linux 2023, Windows Server, etc.
3.  **Security Groups (SG):** Es el muro de fuego alrededor de tu servidor. 
    * Operan a nivel de **Instancia**, no de red completa.
    * Tienen **Reglas de Entrada (Inbound)** y **Reglas de Salida (Outbound)**.
    * Son **Stateful (Con estado):** Esto es magia pura. Si abres el puerto 80 para que un cliente pida una página web (Inbound), el Security Group recuerda esa conexión y automáticamente deja salir la respuesta web hacia el cliente, sin necesidad de que tú abras reglas de salida.
4. stateful vs stateless: Los Security Groups son stateful, lo que significa que si permites una conexión entrante (inbound), la respuesta saliente (outbound) se permite automáticamente. En cambio, los Network ACLs son stateless, por lo que debes configurar reglas tanto de entrada como de salida.
5. ACL (Access Control List): Es un firewall a nivel de red, que opera a nivel de subred. Es stateless, lo que significa que si permites una conexión entrante, debes permitir manualmente la salida correspondiente.
6. **Puertos y Protocolos:** Cada servicio de red usa un puerto específico. Por ejemplo, HTTP usa el puerto 80, HTTPS usa el 443, SSH usa el 22, PostgreSQL usa el 5432, SQL Server usa el 1433, RDP usa el 3389, etc. Los Security Groups permiten abrir o cerrar estos puertos según tus necesidades.
7. Load Balancer: Es un servicio que distribuye el tráfico entrante entre varias instancias EC2, para mejorar la disponibilidad y escalabilidad de tu aplicación. Se coloca delante de tus servidores web y puede manejar miles de conexiones simultáneas.

### ⚠️ Comandos CLI Útiles
* Crear una instancia EC2: `aws ec2 run-instances --image-id ami-12345678 --count 1 --instance-type t2.micro --key-name MyKeyPair --security-groups MySecurityGroup`
* Listar instancias EC2: `aws ec2 describe-instances`
* Crear un Security Group: `aws ec2 create-security-group --group-name "NombreDelSG" --description "Descripción"`
* listar Security Groups: `aws ec2 describe-security-groups`
* Agregar regla Inbound: `aws ec2 authorize-security-group-ingress --group-name "NombreDelSG" --protocol tcp --port 80 --cidr 0.0.0.0/0`
* attachar un Security Group a una instancia: `aws ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --groups sg-12345678 sg-87654321`
* aws ec2 authorize-security-group-ingress --group-name "Web-SG" --protocol tcp --port 80 --cidr 0.0.0.0/0
# Autorizar entrada por SSH (Puerto 22) SOLO a tu IP (Cambia la IP de ejemplo por la tuya)
# aws ec2 authorize-security-group-ingress --group-name "Web-SG" --protocol tcp --port 22 --cidr 190.21.34.12/32


### ⚠️ Buenas y Malas Prácticas
* **✅ Buenas Prácticas:** El puerto 22 (SSH) **NUNCA** debe estar abierto al mundo (`0.0.0.0/0`). Solo debe estar abierto hacia la IP pública de tu casa o la VPN de la Agencia Flow. Los puertos 80 (HTTP) y 443 (HTTPS) sí pueden estar abiertos al mundo.
  
* **❌ El Error Típico (Mala Práctica):** Crear un solo Security Group llamado "sg-general", abrir todos los puertos del 1 al 65535, y asignárselo a todos los servidores web y bases de datos para "evitarse dolores de cabeza". Acabas de invitar a todos los hackers de internet a entrar a tu base de datos.


### 💻 Implementación Oficial (Guía de Comandos CLI)
# Listar las instancias que tienes corriendo
aws ec2 describe-instances 
# Crear un Security Group
aws ec2 create-security-group --group-name "Web-SG" --description "Permitir HTTP y SSH"
# Autorizar entrada por el puerto 80 (HTTP) a todo el mundo
aws ec2 authorize-security-group-ingress --group-name "Web-SG" --protocol tcp --port 80 --cidr 0.0.0.0/0
# Autorizar entrada por SSH (Puerto 22) SOLO a tu IP (Cambia la IP de ejemplo por la tuya)
aws ec2 authorize-security-group-ingress --group-name "Web-SG" --protocol tcp --port 22 --cidr 190.21.34.12/32


💻 FASE 2: PRÁCTICA
⚙️ Ejercicio 1: Lógica Base CLI (Forjando el Escudo)
# Contexto: Vas a preparar el terreno para tu futuro servidor de Django. 
# Lo primero es crearle su escudo de seguridad.
# Requisitos:
# Escribe la secuencia de comandos AWS CLI para:
# 1. Crear un Security Group llamado "Django-SG" con la descripción "Firewall para App Backend".
# 2. Agregarle una regla Inbound para permitir tráfico al puerto 8000 (el de desarrollo de Django) 
#    desde cualquier parte del mundo (0.0.0.0/0).

# --- TUS COMANDOS AQUÍ ---
1- aws ec2 create-security-group --group-name Django-SG --description "Firewall para App Backend"
2- aws ec2 authorize-security-group-ingress --group-name "Django-SG" --protocol tcp --port 8000 --cidr 0.0.0.0/0


🚀 Ejercicio 2: Proyecto Real (Seguridad Militar en SGs)
# Contexto: Acabas de instalar una base de datos PostgreSQL dentro de un EC2 privado 
# para un cliente de finanzas de la Agencia Flow. 
# El puerto de la base de datos es el 5432. Tu servidor web de Django tiene la IP interna 10.0.0.50.
#
# Requisitos:
# Escribe el comando de AWS CLI que agrega la regla al Security Group de la Base de Datos 
# para permitir que el puerto 5432 sea accesible ÚNICAMENTE desde el servidor de Django, 
# y que bloquee todo lo demás.
# (Pista: Usa la notación CIDR exacta /32 para apuntar a una sola IP).

# --- TUS COMANDOS AQUÍ ---
1- aws ec2 authorize-security-group-ingress --group-name "Django-SG" --protocol tcp --port 5432 --cidr IP del lugar donde se conecta/32


🚀 Ejercicio 3: Proyecto Real (Selección de Arquitectura)
# Contexto: Tienes dos proyectos nuevos. 
# 1. Un blog de noticias estático hecho en WordPress con muy poco tráfico.
# 2. Un sistema de renderizado de videos en 3D que requiere procesadores brutalmente potentes.
#
# Requisitos:
# Basado en la teoría de "Tipos de Instancias", dime qué familia y tamaño de instancia (ej. t2.micro, c5.xlarge, etc.) 
# le asignarías a cada proyecto para optimizar los costos del cliente sin sacrificar rendimiento.

# --- TUS RESPUESTAS ARQUITECTÓNICAS AQUÍ ---
1- Al primer cliente yo le recoemdaria una t2.micro o t3.micro, ya que es para web basica y de poco trafijo, entonces esa le quedaria excelente.
2- Al segundo cliente yo le recomendaria la familia C, ya sea de la c5 - c9.largue, ya que son procesadores que son hechos para el gaming, machine learning


🐛 Ejercicio 4: Lectura de Código y Debugging (El Muro Invisible)
# Contexto: Un junior en tu equipo crea un servidor EC2 con Ubuntu en AWS. Le asigna un Security Group 
# llamado "Test-SG". 
# Luego, abre su terminal e intenta conectarse por SSH: 
# ssh -i llaves.pem ubuntu@54.120.30.15
#
# La terminal se queda congelada, el cursor parpadea y, después de 2 minutos, arroja el error: 
# "Connection timed out".
#
# El junior te dice: "¡La contraseña de la llave pem está mala, Amazon me está bloqueando!".
#
# Analiza técnicamente qué significa un "Connection timed out" en este contexto y 
# explícale al junior qué regla exacta olvidó agregar en su Security Group "Test-SG".

# --- EXPLICACIÓN DEL ERROR Y TU CORRECCIÓN AQUÍ ---
Amazon no te a bloquedo, el significado de Connection timed out es que no se a logra connectar a la ec2 en el tiempo establecido.. Puede ser por varias razones pero la principal y comun es el olvido de habilitar sh en el inboud del segurity group ya que sin esa regla que permita la entrada al puerto 22(SHH) ABSOLUTAMENTE nadie se podra conectare por shh a la ec2. Se logra con el comando aws ec2 authorize-security-group-ingress --group-name "Django-SG" --protocol tcp --port 22 --cidr 54.120.30.15/32 o tambien desde la consola.


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA (Cierre del Día)
❓ Pregunta Teórica 1:
Cuando apagas y vuelves a encender una instancia EC2 básica, AWS le asigna una IP Pública completamente nueva. Si ya le diste esa IP a un cliente para que se conecte, tendrás un problema. ¿Qué recurso gratuito de AWS EC2 debes asociarle a tu servidor para que su dirección IP pública sea fija y nunca cambie, incluso si reinicias la máquina?
Para este tipo de situaciones aws tiene una excelente y gratuita solucion, la cual se llama elastic IP, a la hora de implementar la ec2 la seleccionamos y la implementamos. A si la ec2 en nuestro proyecto tendra una IP fija sin problemas.


❓ Pregunta Teórica 2:
Explicaste que los Security Groups son "Stateful" (Tienen estado). Si tú abres el puerto 443 (Inbound) para que los usuarios entren a tu página web segura, ¿tienes que crear manualmente una regla de salida (Outbound) para que la página web pueda enviar los datos de regreso al usuario? Justifica tu respuesta.
Los segurity group al ser stateful no ocupan una regla de salida, basta con una regla de entrada(inbound) para el puerto en turno ya sea 22, 443 o 5432 y con dicha regla ya el usuario ingeniero podra hacer uso del puerto.


🗣️ Prueba de Feynman (Explicación):
Escenario: Un cliente está preocupado por los hackers y te pide que le expliques cómo protege Amazon su servidor EC2.
Explícale el concepto de Security Groups usando la analogía de los guardias de seguridad en la entrada de un edificio corporativo que revisan las credenciales de los visitantes y anotan quién entró. Asegúrate de explicar por qué si el guardia te dejó entrar, no te pedirá identificación de nuevo cuando vayas de salida (Stateful).
Las reglas Inbound de los segurity son muy sencillas de entender, te las voy a explicar de la siguiente manera imagina que tienes guardas de seguridad en tu edificio, ellos velan por el registro de credenciales y llaves autenticas, si un usuario no las tiene o tu le dices a los guardas que no permitan a nadie entrar, ellos asi lo haran o sea tienes el control absoluto, una vez ya ingresado el user o sistema a la hora de salir no se le pediran credenciales y pasa sin autentificacion, a eso se le conoce como stafull aunque claro si quieres mas seguridad estan las access control list que son stateless(piden autentificacion en la entrada y salida).