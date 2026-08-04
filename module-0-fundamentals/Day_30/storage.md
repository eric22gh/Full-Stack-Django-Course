# ☁️ DÍA 30: MÓDULO 0 - Amazon S3 (El Disco Duro Infinito)

**📦 Dependencias del Módulo:**
* **Entorno:** Máquina Virtual con Ubuntu en VirtualBox.
* **Herramientas:** `awscli`.


## 📖 FASE 1: TEORÍA 
Amazon S3 es un servicio de **Almacenamiento de Objetos**. A diferencia del disco duro de tu computadora portátil (que guarda archivos en carpetas dentro de otras carpetas de forma jerárquica), S3 guarda "Objetos" en contenedores planos llamados "Buckets" (Baldes).

Es el lugar perfecto para alojar los archivos estáticos de tu web (HTML, CSS, imágenes, videos) o guardar copias de seguridad de bases de datos de forma masiva.

## DOCUMENTACIÓN OFICIAL
*🔗 **Doc Oficial:** [Conceptos de Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) / [AWS CLI S3 Commands](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html)*

### 🎯 Puntos Clave: Buckets, Objetos y Seguridad
1.  **Buckets (Baldes):** Es el contenedor principal. **REGLA DE ORO:** El nombre de un bucket debe ser *globalmente único* en todo el mundo. Si alguien en China ya le puso "mis-fotos" a su bucket, tú no puedes usar ese nombre. Suele usarse el dominio de la empresa (ej. `agenciaflow-produccion-assets`).
2.  **Objetos y Llaves (Keys):** En S3 no hay "carpetas" reales, aunque la interfaz gráfica te lo haga creer. S3 usa "Keys" (Llaves) que son el nombre completo del archivo. Un archivo llamado `logo.png` guardado "dentro" de la carpeta `img` en realidad tiene un Key llamado `img/logo.png`.
3.  **Almacenamiento de Bloques vs. Objetos:** 
    * *Bloques (EBS - Elastic Block Store):* Es el disco duro normal que conectas a tu servidor EC2. Sirve para instalar un Sistema Operativo (Ubuntu) o una base de datos de lectura/escritura muy rápida.
    * *Objetos (S3):* Sirve para guardar un archivo completo (como una foto) y leerlo por internet. No puedes instalar Ubuntu en S3.
4.  **Seguridad (Block Public Access):** Por defecto, S3 bloquea todo el acceso público. Si intentas abrir una foto subida a S3 con el navegador, te dará un error `Access Denied` (XML). Para que una imagen sea pública, debes cambiar la configuración del bucket o generar una "URL Prefirmada".

### ⚠️ Buenas y Malas Prácticas
* **✅ Buenas Prácticas:** Mantener siempre encendida la opción **"Block all public access"** a nivel de cuenta y usar Roles de IAM para que solo tu servidor EC2 pueda acceder al bucket.
* **❌ El Error Típico (Mala Práctica):** Hacer público un bucket entero de la empresa solo porque querías que un cliente pudiera descargar un logo. Un bot que escanea internet podría encontrar facturas, copias de seguridad de contraseñas y datos sensibles de clientes en ese mismo bucket expuesto.


### 💻 Implementación Oficial (Guía de Comandos CLI)
# Crear un bucket nuevo (mb = make bucket)
aws s3 mb s3://agenciaflow-assets-2026

# Listar todos los buckets en tu cuenta
aws s3 ls

# Subir (copiar) un archivo local hacia S3
aws s3 cp "C:/Users/EAedw/Downloads/Justificacion de horario.pdf" s3://agenciaflow-produccion-assets-2026

# Descargar un archivo de S3 a tu computadora
aws s3 cp s3://agenciaflow-assets-2026/Justificacion\ de\ horario.pdf "C:/Users/EAedw/Downloads/Justificacion de horario.pdf"

# Mágia pura: Sincronizar toda una carpeta local con S3 (Sube solo los archivos nuevos o modificados)
aws s3 sync "C:/Users/EAedw/Documents/Proyecto Web/build" s3://agenciaflow-assets-2026/

# Borrar un archivo de S3
aws s3 rm s3://agenciaflow-assets-2026/foto.jpg


💻 FASE 2: PRÁCTICA
⚙️ Ejercicio 1: Lógica Base CLI (Creación y Subida)
# Contexto: Tienes el logo oficial de la agencia en tu servidor local (logo_flow.png) 
# y necesitas guardarlo en la nube.
# Requisitos:
# Escribe los dos comandos exactos de AWS CLI para:
# 1. Crear un bucket en S3. Invéntate un nombre que creas que nadie en el mundo haya usado.
# 2. Copiar un archivo ficticio llamado "logo_flow.png" (que está en tu directorio actual) 
#    hacia la raíz de ese nuevo bucket.

# --- TUS COMANDOS AQUÍ ---
1- aws s3 mb s3://agencia-flow-git-hub-2030, 
2- aws s3 cp "C:/Users/EAedw/Documents/logo_flow.png"  s3://agencia-flow-git-hub-2030


🚀 Ejercicio 2: Proyecto Real (Sincronización de Frontend)
# Contexto: En el Módulo 4 de tu curso, crearás una página web en React. 
# Al compilar la página, React te genera una carpeta llamada "build" con todo tu HTML, CSS y JS final.
# Subir archivo por archivo a mano es trabajo de novatos.
#
# Requisitos:
# Escribe el comando de AWS CLI que utilizarías para sincronizar toda la carpeta local llamada "build/" 
# hacia tu bucket de S3 llamado "s3://agenciaflow-frontend-prod".
# (Pista: Usa el comando que compara archivos y solo sube las diferencias).

# --- TU COMANDO AQUÍ ---
1- aws s3 mb s3://agenciaflow-frontend-prod
2- aws s3 sync "C:/Users/EAedw/Documents/Proyecto Web/build" s3://agenciaflow-frontend-prod
3- # Sincroniza y elimina de S3 los archivos que ya no existen en tu computadora
aws s3 sync "C:/Users/EAedw/Documents/Proyecto Web/build" s3://agenciaflow-frontend-prod --delete


🚀 Ejercicio 3: Proyecto Real (El Enlace Prefirmado)
# Contexto: Tu bucket de S3 es completamente privado (Block Public Access activado).
# Sin embargo, necesitas que tu cliente vea un contrato en PDF (contrato.pdf) que guardaste ahí.
# No quieres hacer público el bucket entero.
#
# Existe un comando en AWS CLI para generar una "URL Prefirmada" temporal (Presigned URL)
# que le da permiso a cualquiera de descargar ese archivo exacto, pero solo durante un tiempo limitado.
# 
# Requisitos:
# Investiga (o deduce) cómo escribirías el siguiente comando para generar una URL temporal 
# válida por 3600 segundos (1 hora) para el archivo 'contrato.pdf' en el bucket 'agenciaflow-docs'.
# (Pista: el comando empieza con `aws s3 presign ...`)

# --- TU COMANDO AQUÍ ---
1- aws s3 mb s3://agenciaflow-docs
2- aws s3 cp "C:/Users/EAedw/Documents/contrato.pdf" s3://agenciaflow-docs
3- aws s3 presign s3://agenciaflow-docs/contrato.pdf --expires-in 3600
4- lista de la URL generada en la terminal y envíasela al cliente para que pueda descargar el contrato.


🐛 Ejercicio 4: Lectura de Código y Debugging (El Silencio de la Consola)
# Contexto: Un desarrollador recién contratado abre la terminal en su Ubuntu local.
# Él sabe que hay buckets creados porque los vio en la Consola Web. 
# Entonces escribe el comando: aws s3 ls
# 
# Pero la terminal le lanza un error crítico:
# "Unable to locate credentials. You can configure credentials by running 'aws configure'."
#
# El desarrollador dice: "¡La herramienta de awscli está rota en mi computadora!".
#
# Analiza técnicamente el mensaje de error. Explícale al desarrollador qué le falta a 
# su terminal de Ubuntu para poder conectarse a AWS y cómo se relaciona esto con 
# lo que aprendimos ayer en el Día 28 (IAM).

# --- EXPLICACIÓN DEL ERROR Y TU CORRECCIÓN AQUÍ ---
Para conectarse a  aws por medio de la terminal, cada usuario debe de tener una access key, es un metodo de autentificacion cifrado que utiliza aws para una coneccion mas segura entre usuario y plataforma, yo como administrador ingresara a la seccion de iam de la consola y buscare tu usuario para asi poder generarte las access key junto con unas metidas obligatorias que ya deberias de saber, no compartar tu access key con nadie, escribela en un papel y guardalo en un lugar seguro y preferiblemente borra el archivo descargado con las access key
.

🧠 FASE 3: CONSOLIDACIÓN TEÓRICA (Cierre del Día)
❓ Pregunta Teórica 1:
Tu cliente necesita una base de datos PostgreSQL rápida, por lo que alquilarás un servidor EC2. ¿Dónde deberías instalar el motor de la base de datos y guardar sus tablas: en el disco duro EBS (Block Storage) que viene con la instancia EC2, o en un bucket de S3 (Object Storage)? Justifica por qué.
La implementacion correcta seria en ec2 con EBS ya que el es el almacenamiento comun de la ec2 que es el motor de computo que ocupara tu base de datos y asi poder correr perfectamente la base de datos. En cambio s3 no tiene poder de computo, el es solo otra forma de almacenamiento de aws que almacena objetos = archivos.


❓ Pregunta Teórica 2:
¿Por qué AWS exige que el nombre de un bucket (ej. mi-bucket-123) sea único a nivel mundial entre todos los millones de clientes de Amazon, a diferencia de un servidor EC2 donde puedes llamarlo "Servidor Web" sin importar si otra persona usa el mismo nombre?
En s3 es importa el nombre para evitar para evitar subidas de archivos a un bucket que no queremos, la ,mayor parte de los buckets que se implementan en s3 se van a exponer a internet si un usuario por cosa del destino sube un archivo a tu bucket porque el nombre es identico se podrian generar problemas. Al contrario con la ec2 es solo una etiquete que se usa en la plataforma para identificar ya que es imposible que una persona sepa o se acuerde del id de dicha ec2, ese id si es unico.


🗣️ Prueba de Feynman (Explicación):
Escenario: Un cliente quiere guardar un millón de documentos escaneados. No entiende la diferencia entre guardarlos en "el disco duro C: de un servidor en la nube (EBS)" vs. "guardarlos en S3".
Explícale la diferencia usando la analogía de guardar documentos en la gaveta del escritorio de tu oficina (EBS) vs. contratar un almacén gigante de bodegas externas (S3). Menciona ventajas sobre capacidad y pérdida de datos si se incendia la oficina.
S3 en aws es como un almacén gigante de bodegas externas, donde puedes guardar millones de documentos sin preocuparte por el espacio. Incluso si tu oficina se incendia, tus documentos estarán seguros en ese almacén, ya que a la hora de implementarlos se debe selecionar 2 o mas zonas de disponibilidad gracias a esta alta disponibilidad los archivos se guarda en las AZ y si una falla tendras los archivos en la otra AZ. En cambio, EBS es como la gaveta del escritorio de tu oficina: tiene un espacio limitado y si algo le pasa a la oficina, podrías perder todos tus documentos. Además, S3 permite acceder a los documentos desde cualquier lugar y compartirlos fácilmente, mientras que EBS está más limitado a la máquina donde está instalado.