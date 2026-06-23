Markdown
# 🚀 DÍA 24: MÓDULO 0 - Servicios del Sistema y Capas Superiores (5, 6, 7)

**📦 Dependencias del Módulo:**
* **Entorno:** Máquina Virtual con Ubuntu en VirtualBox.
* **Comandos:** `systemctl`, `journalctl`.

## 📖 FASE 1: TEORÍA 
Ya dominas la IP (Capa 3 - la dirección) y el Puerto (Capa 4 - la puerta). Pero una vez que los datos cruzan esa puerta, entran al territorio de las **Capas Superiores del Modelo OSI (5, 6 y 7)**. Aquí es donde los ceros y unos se convierten en texto, se encriptan de forma segura y finalmente son entregados a la aplicación final (como tu API de Django). 

Pero, ¿quién se encarga de mantener esa aplicación encendida 24/7 en tu servidor Linux? El administrador de servicios: **Systemd**.



## DOCUMENTACIÓN OFICIAL
*🔗 **Doc Oficial:** [Systemd / Systemctl](https://man7.org/linux/man-pages/man1/systemctl.1.html) / [OSI Model Upper Layers](https://www.cloudflare.com/learning/ddos/glossary/open-systems-interconnection-model-osi/)*

### 🎯 El Propósito
Si la luz de tu servidor en Limón se va y la máquina se reinicia, no vas a estar ahí a las 3:00 a.m. para escribir `python manage.py runserver`. Necesitas decirle a Linux: *"Django es un servicio crítico; si el servidor se reinicia, enciéndelo automáticamente. Si el programa crashea por un error, reinícialo tú solo"*. Esto se logra convirtiendo tus scripts en **Servicios (Daemons)** usando `systemd`.

### 🎯 Puntos Clave: Las Capas Superiores y Systemd
1.  **Capa 5 (Sesión):** Mantiene la conversación abierta. Si estás bajando un archivo pesado y el internet parpadea, esta capa intenta mantener el "hilo" de la conexión para no empezar desde cero.
2.  **Capa 6 (Presentación):** El traductor y guardaespaldas. Aquí ocurre la magia del **Certificado SSL**. Los datos llegan encriptados y esta capa los descifra. También formatea los datos (ej. convierte todo a JSON o a texto legible).
3.  **Capa 7 (Aplicación):** Es la interfaz final. HTTP (navegadores web), SSH (terminal remota) y FTP (transferencia de archivos). **Tus automatizaciones de n8n y tu código de Django viven aquí.**
4.  **Systemd (`systemctl`):** Es el proceso número 1 de Linux (PID 1). Es el padre de todos los demás procesos. Controla qué aplicaciones (Capa 7) deben iniciar cuando el sistema operativo arranca.



### ⚠️ Buenas y Malas Prácticas
* **✅ Buenas Prácticas:** Usar `systemctl reload` en lugar de `restart` cuando modificas la configuración de un servidor web (como Nginx). El `reload` aplica los cambios sin botar las conexiones de los usuarios que están navegando en ese momento.
* **❌ El Error Típico (Mala Práctica):** Ejecutar una API en producción usando herramientas de terminal (como `screen`, `tmux` o el símbolo `&` al final del comando). Si el sistema se reinicia, el proceso muere para siempre. En producción, **todo** debe ser un servicio configurado en `/etc/systemd/system/`.


### 💻 Implementación Oficial (Guía de Comandos CLI)
sudo systemctl status ssh        # Revisa si el servicio SSH está corriendo, si falló o si está apagado
sudo systemctl status ssh -l     # Muestra el estado completo del servicio, incluyendo la ruta de su archivo de configuración
sudo systemctl stop ssh          # Apaga el servicio (Nadie podrá conectarse remotamente)
sudo systemctl start ssh         # Enciende el servicio
sudo systemctl restart ssh       # Lo apaga y lo enciende inmediatamente
sudo systemctl enable ssh        # LECCIÓN CRÍTICA: Le dice a Linux que encienda este servicio al arrancar la PC
sudo systemctl disable ssh       # Evita que el servicio arranque automáticamente al reiniciar
sudo systemctl reload ssh        # Aplica cambios de configuración sin botar las conexiones activas
sudo systemctl reload sshd       # Aplica cambios de configuración sin botar las conexiones activas (para el demonio SSH)
sudo systemctl is-enabled ssh    # Verifica si el servicio está habilitado para arrancar al inicio
sudo systemctl is-active ssh     # Verifica si el servicio está activo en este momento
sudo systemctl list-units --type=service  # Lista todos los servicios activos en el sistema
journalctl -u ssh -n 20          # Muestra los últimos 20 logs de errores específicos de ese servicio


💻 FASE 2: PRÁCTICA
⚙️ Ejercicio 1: Lógica Base CLI (El Jefe de los Servicios)
# Contexto: Quieres auditar el servicio 'cron', que es el reloj interno de Linux encargado de 
# ejecutar tareas programadas (lo usarás mucho en automatización).
# Requisitos:
# 1. Usa 'systemctl' para verificar el estado (status) del servicio 'cron'. Observa si dice "active (running)".
# 2. Usa 'systemctl' con privilegios 'sudo' para detener (stop) el servicio 'cron'.
# 3. Vuelve a verificar el estado para confirmar que ahora dice "inactive (dead)".
# 4. Vuelve a iniciarlo (start) para no dejar tu sistema sin reloj de tareas.

# --- TUS COMANDOS AQUÍ ---
1- systemctl status cron, 2- respuesta: running, 3- sudo systemctl stop cron, 4- systemctl status cron 5- respuesta: inactive, 6- sudo systemctl start cron, 7- sudo systemctl status cron, 8-respuesta: active.


🚀 Ejercicio 2: Proyecto Real (Prevención de Caídas - Enable vs Start)
# Contexto: Instalaste un motor de base de datos para la Agencia Flow. Actualmente está corriendo, 
# pero quieres asegurarte de que si el servidor de AWS se reinicia, la base de datos vuelva a encender sola.
# Requisitos:
# 1. En Ubuntu, el firewall viene como un servicio llamado 'ufw'. 
#    Usa el comando 'systemctl' necesario para "habilitar" (enable) que el servicio 'ufw' 
#    arranque automáticamente cada vez que la máquina virtual se encienda.
# 2. (Opcional mental) Observa cómo la terminal te responde creando un "symlink" (enlace simbólico), 
#    que es la forma en que Linux anota en su libreta de arranque qué cosas debe encender.

# --- TUS COMANDOS AQUÍ ---
1- sudo systemctl status ufw, 2- sudo systemctl enable ufw, 3- sudo systemctl status ufw, 4- respuesta: activate


🚀 Ejercicio 3: Proyecto Real (Lectura de Logs de Servicios)
# Contexto: Un cliente no puede conectarse por SSH. En lugar de buscar en el archivo global de logs 
# y usar múltiples tuberías con 'grep', systemd tiene su propio lector ultra-eficiente llamado 'journalctl'.
# Requisitos:
# 1. Usa 'journalctl' con el flag '-u' (unit) para especificar que solo quieres ver los logs 
#    del servicio 'cron'.
# 2. Combínalo con el flag '-n 10' para ver únicamente las últimas 10 líneas de ese registro.
# Nota: en ubuntu el ssh lo cambie a cron para terner logs ya que en ssh no veia ningun log

# --- TUS COMANDOS AQUÍ ---
1- journalctl -u cron -n 10, 2- logs: uno de los logs decia: session closed for user root, session opened for user root


🐛 Ejercicio 4: Lectura de Código y Debugging
# Contexto: Un desarrollador Junior de la Agencia Flow terminó de programar el bot de Telegram 
# en Python y lo dejó corriendo en el servidor usando este comando: 
# python3 bot.py &
# 
# A las 2:00 a.m. el servidor hizo una actualización de seguridad automática y se reinició. 
# A la mañana siguiente, el cliente llama furioso porque el bot lleva 6 horas apagado.
#
# Analiza técnicamente por qué el comando del Junior fue una mala práctica para un entorno 
# de producción y explica qué herramienta de Linux debió usar para evitar esta catástrofe.

# --- EXPLICACIÓN DEL ERROR Y TU CORRECCIÓN AQUÍ ---

Primeramente el comando python3 bot.py & si se usa para correr un servicio, el problema es, lunix no puede reinicia archivos .py, sin embarga hay una solucion la cual es crear un archivo de configuracion en la carpeta system que tenga unas configuraciones y luego usar en el servidor el comando sudo systemctl enable (nombre del archivo config), asi el servidor sabe que cada vez que se reinicie tiene que agregar ese script a su reinicio automatico y finalmente iniciar el servicio con un sudo systemctl start bot.service.

# PASO 1: No habilitas el .py, creas un archivo de servicio
# El archivo usualmente se crea en /etc/systemd/system/bot.service
# Adentro lleva instrucciones como:
# ExecStart=/usr/bin/python3 /home/eric/bot.py
# Restart=always

# PASO 2: Ahora sí, le dices a Systemd que lea el nuevo archivo y lo active para siempre
sudo systemctl daemon-reload   # Recarga la lista de servicios
sudo systemctl enable bot.service
sudo systemctl start bot.service

🧠 FASE 3: CONSOLIDACIÓN TEÓRICA (Cierre del Día)
❓ Pregunta Teórica 1:
Cuando compras un certificado de seguridad SSL en la web, la información del usuario de tu cliente viaja encriptada para evitar que los hackers la lean. Basado en el Modelo OSI, ¿qué capa (5, 6 o 7) es la responsable directa de tomar esa información ilegible y "traducirla/desencriptarla" para que tu API la reciba como texto normal?
La capa donde ocurre esta magia es la Capa 6(presentacion), a ella llegados los datos cifrados y ella se encarga de descifralos que a su vez los transforma en JSON o texto legible.


❓ Pregunta Teórica 2:
Si ejecutas sudo systemctl start nginx, el servidor web se enciende hoy. Pero si la máquina se apaga, no volverá a encender. ¿Cuál es la diferencia conceptual exacta entre start y enable en el mundo de systemd?
Con systemctl start nginx tendriamos el mismo problema de la pregunta anterior, tendriamos que estar introduciendo el comando cada vez que se reinicia el servidor en pocas palabras no es escalable. En cambio con el coamndo systemctl enable nginx el programa se reiniciaria automaticamente cada vez que el servidor se encienda.


🗣️ Prueba de Feynman (Explicación):
Escenario: Un cliente, dueño de una panadería local, escucha que configuras sus automatizaciones como "Servicios (Daemons)" y te pregunta qué significa eso y por qué le cobras el mantenimiento de los mismos.
Explícale el concepto de un Servicio (Daemon) en Linux usando la analogía de la diferencia entre contratar a un jornalero por horas (script manual) vs. contratar a un guarda de seguridad nocturno (Daemon) para su local.
En los servidores de linux un reinicio puede ocurrir por cualquier cosa y cualquier hora, en el caso de una finca un incidente puede ocurrir a cualquier hora e incluisive cuando usted duerme señor, si usted solo pone a un guarda de seguridad de dia no sabra que pasa de noche, tendria que revisar si hay rastros de un posible hurto(logs), en cambio si coloca guardas de seguridad a toda hora ante la enventualidad de algun hurto o percanse(reinicio del server) se dara cuanta y hasta se le podra informar en el mismo instante en el que ocurra.