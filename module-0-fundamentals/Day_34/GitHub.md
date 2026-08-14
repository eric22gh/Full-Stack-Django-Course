☁️ DÍA 34: MÓDULO 0 - GitHub, SSH Keys y Repositorios Remotos
📦 Dependencias del Módulo:
Entorno: VS Code + Terminal Linux, Navegador Web.
Herramientas: Cuenta gratuita en GitHub.com.

📖 FASE 1: TEORÍA
Muchos confunden Git con GitHub. Git es el motor (el software en tu terminal que toma las fotos). GitHub es simplemente una página web (propiedad de Microsoft) que funciona como un disco duro en la nube para guardar los álbumes de fotos de Git y compartirlos con tu equipo.

Para que tu terminal pueda enviar código a GitHub sin pedirte la contraseña cada 5 minutos, usaremos el mismo protocolo de seguridad que usamos para entrar a los servidores de AWS: Llaves Asimétricas SSH.


DOCUMENTACIÓN OFICIAL
🔗 Doc Oficial: Generar llave SSH para GitHub / Adding a remote


🎯 El Propósito
¿Qué problema resolvemos hoy? La colaboración y el respaldo en la nube. Si a tu laptop le cae un vaso de agua encima, tu repositorio local de Git muere con ella. Al hacer "Push" (empujar) hacia GitHub, tu código queda respaldado en los servidores de la nube.


🔑 Puntos Clave: Push, Pull y Remote
Remote (El Destino): Tu Git local no sabe que GitHub existe. Debes agregar un "Control Remoto" (una URL) y bautizarlo. Por convención mundial, el servidor principal siempre se bautiza con la palabra origin.

Push (Empujar): Es el acto de subir tus commits locales hacia GitHub.

Pull (Halar/Tirar): Es el acto de descargar los cambios que otro programador subió a GitHub hacia tu máquina local.

Clone (Clonar): Descargar un repositorio completo de internet por primera vez.


⚠️ Buenas y Malas Prácticas
✅ Buena Práctica: Ejecutar SIEMPRE git pull a primera hora de la mañana antes de empezar a programar. Así te aseguras de tener los cambios que tus compañeros hicieron la noche anterior.

❌ Mala Práctica: Autenticarse en GitHub usando el formato HTTPS en la terminal (te pedirá usuarios y tokens constantemente). El estándar de la industria es usar formato SSH.


💻 Implementación Oficial (Comandos Core)
# 1. Vincular tu carpeta local con un repositorio vacío creado en la página de GitHub
git remote add origin git@github.com:TuUsuario/agencia-flow.git

# 2. Renombrar la rama principal a "main" (buena práctica moderna)
git branch -M main

# 3. Empujar tu código a GitHub por primera vez (el -u vincula tu rama local con la remota)
git push -u origin main

# 4. Descargar cambios nuevos desde la nube
git pull origin main


# 5. Clonar el proyecto de otra persona (o tuyo en una PC nueva)
git clone git@github.com:OtroUsuario/su-proyecto.git

# 6. aplica tus commits encima de los que ya existen en el remoto, manteniendo un historial más limpio.
git pull origin main --rebase

#7. despues de hacer el rebase hay que editar archivos en conflicto
git add .
git rebase --continue


💻 FASE 2: PRÁCTICA DIARIA
(Instrucción: Hoy necesitas abrir tu cuenta de GitHub en el navegador y usar tu terminal).


⚙️ Ejercicio 1: Implementación - Lógica Base (Autenticación SSH)
# Contexto: Vas a conectar tu computadora a GitHub de forma segura usando criptografía,
# justo como aprendiste en el módulo de Redes.
#
# Requisitos Ejecutables:
# 1. En tu terminal de Linux, genera una llave SSH nueva ejecutando: 
#    ssh-keygen -t ed25519 -C "tu_correo_de_github@email.com" (Presiona Enter a todo).
# 2. Imprime tu llave pública en la terminal con: cat ~/.ssh/id_ed25519.pub
# 3. Entra a GitHub.com -> Settings -> SSH and GPG keys -> New SSH Key, y pega ahí la llave.
# 4. Ejecuta el comando de prueba: ssh -T git@github.com
# 5. Pega aquí el mensaje final de saludo que te arroja la terminal de GitHub.

# --- TU OUTPUT DE CONSOLA AQUÍ ---
1- ssh-keygen -t ed25519 -C "ferali.eh@gmail.com"
2- cat ~/.ssh/id_ed25519.pub = ssh-ed25519 AAAAC3NzaC1lZDI1NTE5XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
3- añadida correctamente la clave SSH a GitHub
4- ssh -T git@github.com
5- Hi eric22gh! You've successfully authenticated, but GitHub does not provide shell access.


🚀 Ejercicio 2: Implementación - Escenario Real (Tu Primer Push)
# Contexto: Tienes tu carpeta 'agencia_flow_pruebas' del Día 33 llena de commits, pero 
# solo existe en tu laptop. Vamos a respaldarla en la nube.
#
# Requisitos Ejecutables:
# 1. Ve a GitHub.com y crea un repositorio nuevo (vacío) llamado "agencia_flow_repo".
# 2. Copia la URL que te da GitHub en formato SSH (empieza con git@github.com...).
# 3. En tu terminal (dentro de tu carpeta local), ejecuta el comando para agregar ese 'remote' (origin).
# 4. Sube tu código con 'git push -u origin main'.
# 5. Refresca la página de GitHub en tu navegador. ¡Tu código ya debería estar ahí!
# Escribe en tu respuesta los 2 comandos exactos que usaste en los pasos 3 y 4.

# --- TUS COMANDOS AQUÍ ---
1- git remote add origin git@github.com:eric22gh/agencia_flow_repo.git
2- git push -u origin main


🚀 Ejercicio 3: Implementación - Escenario Real (Trabajo en Equipo Simulando Clonación)
# Contexto: Contrataste a un desarrollador nuevo para la Agencia Flow. Él necesita 
# el código en su propia computadora para empezar a trabajar. Vas a simular ser él.
#
# Requisitos Ejecutables:
# 1. En tu terminal, sal de tu carpeta actual (comando: `cd ..`) y ve a tu Escritorio.
# 2. Ejecuta el comando 'git clone' usando la URL SSH de tu repositorio.
# 3. Verás que se descargó una carpeta idéntica con tu proyecto.
# Escribe aquí el comando de clonación exacto que utilizaste.

# --- TU COMANDO AQUÍ ---
1- cd ..
2- git clone git@github.com:eric22gh/agencia_flow_repo.git



🐛 Ejercicio 4: Lectura de Código y Debugging (El Rechazo del Push)
# Contexto: Estás trabajando en VS Code y haces un commit. Intentas subirlo ejecutando 
# `git push origin main`. git push -u origin main

# Sin embargo, la terminal se pone en rojo y te escupe este error:
#
# ! [rejected]        main -> main (fetch first)
# error: failed to push some refs to 'github.com:agencia/proyecto.git'
# hint: Updates were rejected because the remote contains work that you do
# hint: not have locally. This is usually caused by another repository pushing
# hint: to the same ref.
#
# Pregunta Debugging: Analizando el error de arriba (lee el "hint" en inglés), 
# ¿qué fue lo que pasó en GitHub mientras tú programabas, y qué comando EXACTO 
# debes ejecutar en tu terminal antes de intentar hacer Push otra vez?

# --- TU EXPLICACIÓN Y CORRECCIÓN AQUÍ ---
Esto sucede porque el repositorio remoto ya tiene commits o codigo que no esta en mi repositorio local, al yo escribir codigo nuevo a el le falta el anterior, entonces antes de trabajar tengo que sincronizarme con el repo de git hub y despues subir mi codigo o aporte nuevo. La solucion correcta a este problema es el coamando git pull origin main --rebase o solo git pull origin main para asi traer el codigo en remoto a mi repo local y asi editar lo que ocupo y ya finalmente un git push -u origin main.


🧠 FASE 3: CONSOLIDACIÓN TEÓRICA
❓ Pregunta Teórica 1:
Si tu computadora portátil se destruye hoy por completo, pero aplicaste correctamente el flujo de Git y GitHub (Commit -> Push) a las 5:00 p.m., ¿cuánto trabajo/código perdiste de tus proyectos? Justifica tu respuesta entendiendo el rol de origin.
Afortunadamente en este caso el codigo que se pierde es nulo, al yo realizar los pasos correctos, git add ., git commit -m "Autentificaciion de usuarios" y finalmente rl git push -u origin main ya git hub se sincroniza con mi repo local y a la nube, lo siguiente seria ya con computadora nueva, implementar el comando para mi llave ssh, luego añadir esa llave ssh a git hub, luego crear una nueva carpeta en mi computadora, donde seguire trabajando en mi proyecto y realizar el git clone con shh a la carpeta por medio de vs code.



❓ Pregunta Teórica 2:
Configuramos la conexión usando llaves SSH (git@github.com...) en lugar de usar la URL tradicional de HTTPS ([https://github.com/](https://github.com/)...). Desde una perspectiva de seguridad y automatización (pensando en el futuro Módulo de CI/CD), ¿por qué las llaves SSH son una mejor práctica profesional?
Hoy en dia https es muy seguro ya que lo usamos dia con dia y va mejorando cada vez mas, pero no esta excento de ataques de intervencion en su transporte de contraseñas o tokens, en cambio ssh usa la criptografia de clave publica y sin en dado caso algun hacker la quiere interceptar ocupara de las 2 llavez y una de esas permanece en mi dispositivo entonces se disminuyen los riegos de intercepcion exitosas.


🗣️ Prueba de Feynman (Explicación):
Escenario: Un familiar te ve usando la terminal y te pregunta qué es la diferencia entre Git y GitHub, porque los nombres suenan igual.
Explícaselo usando la analogía de editar un video en tu computadora (Git) versus subir ese video a YouTube para que el mundo lo vea (GitHub).
Te lo voy a explicar de una forma facil, git es como una herramienta de edicion de video, en ella encontraras todo para editar el video io en este caso el codigo, ya que con ella realizamos comandos, para recuperar, editar, unir o ver el historial del codigo. Del otro lado tenmos a git hub que seria una plataforma de streaming como you tube en ella se suben los video y se pueden ver o descargar y usar desde cualquier parte del mundo al igual con git hub, yo desde costa rica inicio un repo y le doy a git push porque finalize una funcion y mi compañero en sigapur al instante puede descargar el repo y seguir trabajando en otra funcionalidad aparte.