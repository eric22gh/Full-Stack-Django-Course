# ☁️ DÍA 28: MÓDULO 0 - IAM (Identity and Access Management) y Seguridad Cloud

**📦 Dependencias del Módulo:**
* **Entorno:** Máquina Virtual con Ubuntu en VirtualBox.
* **Herramientas:** `awscli`.

## 📖 FASE 1: TEORÍA 
En AWS, la seguridad no es opcional, es el cimiento de todo. Cuando abres una cuenta en AWS usando tu correo y tarjeta de crédito, te conviertes en el **Usuario Raíz (Root User)**. Este usuario tiene el poder de borrar toda la cuenta, cancelar la facturación y destruir bases de datos enteras. **NUNCA DEBES USAR EL USUARIO RAÍZ PARA TRABAJAR.**

Para el trabajo diario, para tu código de Django o para tus automatizaciones de n8n, usarás **IAM** para crear identidades con permisos limitados.

## DOCUMENTACIÓN OFICIAL
*🔗 **Doc Oficial:** [AWS IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) / [Understanding IAM Policies (JSON)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)*


### 🎯 Puntos Clave: Los 4 Elementos de IAM
1.  **Usuarios (Users):** Personas (Eric) o Programas (n8n, React) que necesitan acceder a AWS. 
2.  **Grupos (Groups):** Colecciones de usuarios. En lugar de darle permisos a 10 programadores uno por uno, creas un grupo llamado "Desarrolladores", le das permisos al grupo y metes a los 10 ahí.
3.  **Políticas (Policies):** Son documentos escritos en formato **JSON** que definen exactamente QUÉ se puede hacer. Siguen una estructura lógica: `Effect` (Permitir/Denegar), `Action` (Qué verbo: Leer, Escribir, Borrar) y `Resource` (En qué servicio específico).
4.  **Roles (Roles):** Son "sombreros mágicos" temporales. **Lección de oro:** Una máquina virtual (EC2) jamás debe tener credenciales quemadas en su código. En su lugar, le "pones el sombrero" (Rol) al servidor EC2 para que Amazon lo reconozca internamente y le dé permiso de hablar con S3 o RDS sin usar contraseñas.


### ⚠️ Buenas y Malas Prácticas
* **✅ Buenas Prácticas:** El **Principio de Menor Privilegio (PoLP)**. Si n8n solo necesita subir facturas a S3, le das una política que diga `"Action": "s3:PutObject"`. Si intentan leer o borrar, AWS los bloqueará. Activar MFA (Autenticación de 2 factores) para todos los humanos.
* **❌ El Error Típico (Mala Práctica):** Asignar la política predeterminada `AdministratorAccess` (Acceso total) a las llaves de un script en Python solo para "evitar dolores de cabeza de permisos". Si ese script se filtra, entregaste las llaves del reino.


### 💻 Implementación Oficial (Guía de Comandos CLI)
aws iam create-user --user-name n8n_bot                     # Crea un usuario nuevo
aws iam create-access-key --user-name n8n_bot               # Le genera las llaves (Access Key y Secret Key) al usuario
aws iam create-group --group-name Developers                # Crea un grupo
aws iam add-user-to-group --user-name eric --group-name Developers # Mete al usuario en el grupo
aws iam attach-group-policy --group-name Developers --policy-arn arn:aws:iam::aws:policy/AdministratorAccess # Le da permisos al grupo
aws iam list-users                                          # Muestra todos los usuarios de la cuenta
# elimar un usuario, grupo y access key
aws iam remove-user-from-group --user-name eric --group-name Developers # Saca al usuario del grupo
aws iam detach-group-policy --group-name Developers --policy-arn arn:aws:iam::aws:policy/AdministratorAccess # Quita permisos al grupo
aws iam delete-group --group-name Developers               # Elimina un grupo
aws iam delete-access-key --user-name n8n_bot --access-key-id ACCESS_KEY_ID # Elimina las llaves del usuario
aws iam delete-user --user-name n8n_bot                     # Elimina un usuario


💻 FASE 2: PRÁCTICA
⚙️ Ejercicio 1: Lógica Base CLI (El Nacimiento de una Identidad)
# Contexto: Vas a conectar n8n (tu plataforma de automatización) a AWS para que guarde 
# reportes automáticos de la Agencia Flow. No usarás tu usuario personal.
# Requisitos:
# Escribe la secuencia de comandos (basada en la guía oficial de arriba) para:
# 1. Crear un usuario de IAM llamado 'agencia_flow_n8n'.
# 2. Generarle a ese usuario sus llaves programáticas (Access Key y Secret Key) para que n8n las use.

# --- TUS COMANDOS AQUÍ ---
1- aws iam create-user --user-name agencia_flow_n8n, 2- aws iam create-access-key --user-name agencia_flow_n8n


🚀 Ejercicio 2: Proyecto Real (Traducción de Políticas JSON)
# Contexto: El equipo de ciberseguridad te envía la siguiente política en JSON que se 
# le va a asignar a un nuevo pasante (Junior). 
#
# {
#   "Version": "2012-10-17",
#   "Statement": [
#     {
#       "Effect": "Allow",
#       "Action": [
#         "ec2:DescribeInstances",
#         "ec2:StartInstances",
#         "ec2:StopInstances"
#       ],
#       "Resource": "*"
#     },
#     {
#       "Effect": "Deny",
#       "Action": "ec2:TerminateInstances",
#       "Resource": "*"
#     }
#   ]
# }
#
# Requisitos:
# Como Ingeniero Cloud, debes saber leer JSON fluido. Explica en español sencillo:
# 1. ¿Qué tres cosas exactas SÍ puede hacer el pasante con los servidores (EC2)?
# 2. ¿Cuál es la única acción que AWS le bloqueará rotundamente (Deny) aunque lo intente?

# --- TU TRADUCCIÓN DEL JSON AQUÍ ---
Estos 4 permisos se basan correctamente en la regla del menor privilegio en aws, DescribeInstances: lo que permite es listar y ver informacion de todas las instancias en la cuenta de aws, lo consderi muy importante. StartInstances: se utiliza para poner a funcionar las instancias y su contra parte StopInstances se utiliza para detenerñas. Por ultimo tenemos a la accion deny en TerminateInstances, que basicamente nos dice que no tenemos permiso de terminar o borrar ninguna ec2 en nuestra consola. 


🚀 Ejercicio 3: Proyecto Real (Roles vs. Usuarios)
# Contexto: Tienes tu aplicación de Django (Módulo 3) corriendo en un servidor EC2 en Virginia.
# Django necesita guardar las fotos de perfil de los usuarios en S3 (El disco duro en la nube).
#
# Un colega te dice: "Crea un usuario IAM llamado 'django_user', genérale un Access Key y Secret Key,
# guárdalos en el archivo .env de Ubuntu y que Django los use para subir las fotos".
#
# Requisitos:
# Como aprendiste hoy, eso es un riesgo innecesario cuando ambos servicios (EC2 y S3) están dentro de AWS.
# Explica a tu colega qué componente de IAM (Users, Groups, Policies, o Roles) deberías usar en 
# su lugar para que el servidor EC2 tenga permisos de forma automática y mucho más segura, sin manejar llaves físicas.

# --- TU RESPUESTA ARQUITECTÓNICA AQUÍ ---
En aws la seguridad es primero y con mucha razon con el asunto de las access y secret key ya que no se debe de dar a ninguna implementacion en la consola, para esa tarea o problema estan lo roles que son mas efectivos. Se tratan de permisos temporales que se les puede dar a un servicio en aws para que realize dicha funcion. Es mal seguro y eficiente ya que si al servicio que le damos las access key sufre un hackeo, la empresa estaria en graves problemas.


🐛 Ejercicio 4: Lectura de Código y Debugging (El Error de $50,000)
# Contexto: Revisando el código que un cliente subió a su repositorio PÚBLICO de GitHub,
# notas que en su archivo de configuración de AWS tienen asociada esta política:
#
# {
#   "Version": "2012-10-17",
#   "Statement": [
#     {
#       "Effect": "Allow",
#       "Action": "*",
#       "Resource": "*"
#     }
#   ]
# }
#
# Analiza y explica, basándote en la teoría de seguridad de AWS, por qué ese asterisco ("*") 
# es considerado una bomba de tiempo. Nombra al menos una cosa catastrófica que un hacker
# podría hacer si encuentra las llaves de este usuario en GitHub.

# --- EXPLICACIÓN DEL ERROR Y TU CORRECCIÓN AQUÍ ---
Como anteriormente explicamos en aws el principio de menor privilegio es sumamente importante, para evitar futuras catastrofes como las que vemos aqui. Analizando detenidamente aqui vemos 2 errores de tamaños astronomico 1- en github no se suben credenciales es una norma, se debe usar el archivo git ignore para no subirlas. 2- en este permiso se encuentra la llave para hacer de todo en la cosa a la que pertenece ese proyecto.. Un hacker que llegue y vea esa informacion tan valiosa ya que es una mina de oro para el y en el peor de los casos eliminaria el proyecto.


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA (Cierre del Día)
❓ Pregunta Teórica 1:
¿Cuál es la diferencia principal entre Autenticación y Autorización en AWS IAM? (Pista: Una responde "¿Quién eres?" y la otra "¿Qué puedes hacer?").
La autenticacion en aws es uno de los primeros filtros de seguridad en aws, sirve para decidir si X usuario esta en mi base de datos por ejemplo quien eres "user-1", si estas en la base de datos, puedes entrar a la consola. Pero no solo por entrar ya puedes usar en implementar infraestructura en la consola, ya que el usuario que se identifica tiene que tener policies adecuadas para la labor encomenda, simpre basandonos en el concepto de menor privilegio.


❓ Pregunta Teórica 2:
Imagina que la Agencia Flow tiene 50 programadores. Mañana todos necesitan permiso para acceder a una nueva base de datos RDS. Según las buenas prácticas de IAM, ¿deberías ir a los 50 usuarios uno por uno a adjuntarles una Política JSON, o existe una forma arquitectónicamente más limpia de hacerlo de un solo golpe?
Lo correcto es crear un grupo llamado RDS-DEVS y a ese grupo añadirle permisos de rds, puede ser full-access a rds siempre y cuando se analice que es y como van a implementar. Despues a esos 50 usuarios les enviaria por correo el link para que se unan al grupo.


🗣️ Prueba de Feynman (Explicación):
Escenario: Tienes que explicarle al gerente de la empresa por qué debe implementar el Principio de Menor Privilegio (PoLP) en los sistemas del personal.
Explícaselo usando la analogía de las llaves de un hotel y el personal de limpieza. ¿Qué pasa si al conserje que solo debe limpiar el piso 1 le das una "Llave Maestra" (AdministratorAccess) que abre la caja fuerte del gerente, la cocina y todas las habitaciones del hotel?
Cuando hablamos de seguridad en aws el tema de menor privilegio es innegociable en la implementacion de sus infraestructuras, por ejemplo teniendo un hotel con 4 pisos, 4 conserjes y un sotano, lo correcto seria al conserje 1 su mision es velar por el sotano y el primer entonces lo correcto y seguro es darle las llaves del sotano y las del primer piso solamente y asi sucesivamente con las demas conserjes. Jamas ni nunca se le debe de dar la llave maestra(AdministratorAccess) a un conserje ya que esa solo la tendras tu que eres el dueño del hotel osea tu eres el usuario root de tu consola.