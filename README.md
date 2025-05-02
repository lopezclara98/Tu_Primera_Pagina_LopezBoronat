Proyecto Django - Página Web de Gestión de Velas y Perfil de Usuario
Este es un proyecto basado en Django que permite gestionar velas personalizadas, incluyendo la creación, visualización, edición y eliminación de velas. Además, incorpora funcionalidades de gestión de usuario, como el inicio de sesión, el registro, la visualización y edición del perfil del usuario.

Funcionalidades
Gestión de velas: Permite crear, listar, editar, eliminar y ver detalles de velas.

Autenticación de usuario: Los usuarios pueden registrarse, iniciar sesión, cerrar sesión y acceder a su perfil.

Perfil de usuario: Los usuarios pueden ver y editar su perfil, que incluye campos como nombre, apellido, email y avatar.

Herencia de templates: Se utiliza herencia de plantillas en Django para una estructura modular y reutilizable.

Formularios con imágenes: Se maneja correctamente la carga y visualización de imágenes en los formularios de creación y edición de velas y perfiles.

Mensajes de error y éxito: Se muestran mensajes en caso de no encontrar resultados en el listado de velas o en el buscador.

Requerimientos
Este proyecto utiliza las siguientes tecnologías y bibliotecas:

Python 3.x

Django 4.x

Bootstrap 5 (para los estilos)

SQLite (base de datos predeterminada)

Dependencias
Asegúrate de tener un archivo requirements.txt con las dependencias necesarias:

shell
Copiar
Editar
Django>=4.0
gunicorn
Pillow
Para instalar las dependencias, utiliza el siguiente comando:

bash
Copiar
Editar
pip install -r requirements.txt
Instrucciones de uso
Clonación del repositorio:

Clona el repositorio en tu máquina local usando el siguiente comando:

bash
Copiar
Editar
git clone https://github.com/lopezclara98/Tu_Primera_Pagina_LopezBoronat.git
cd Tu_Primera_Pagina_LopezBoronat
Configuración de la base de datos:

Asegúrate de haber creado la base de datos con el siguiente comando:

bash
Copiar
Editar
python manage.py migrate
Archivos estáticos:

El proyecto hace uso de archivos estáticos (CSS, JS) cargados desde Bootstrap. Asegúrate de haber configurado la carga de estáticos correctamente en settings.py y ejecuta el siguiente comando para recolectar los archivos estáticos:

bash
Copiar
Editar
python manage.py collectstatic
Ejecutar el servidor de desarrollo:

Para iniciar el servidor de desarrollo, usa el siguiente comando:

bash
Copiar
Editar
python manage.py runserver
Luego, abre tu navegador y navega a http://127.0.0.1:8000 para ver la página.

Estructura de Archivos
models.py: Define los modelos de la base de datos, incluyendo el modelo Vela y el modelo Usuario personalizado.

views.py: Define las vistas para manejar las operaciones de CRUD (crear, leer, actualizar, eliminar) en las velas, además de las vistas relacionadas con el usuario.

urls.py: Define las rutas para cada vista, incluyendo la página de inicio, listado de velas, detalles, creación, edición y eliminación, así como las vistas de login, logout y registro.

templates/: Contiene las plantillas HTML, que utilizan Bootstrap para los estilos y permiten la herencia de plantillas.

base.html: Plantilla base con la estructura común de la página.

crear_vela.html, listado_de_velas.html, detalle_vela.html: Plantillas para la gestión de velas.

editar_perfil.html: Plantilla para la edición de perfil del usuario.

static/: Contiene los archivos estáticos, como los archivos de estilo de Bootstrap.

Funcionalidades Importantes
Página de inicio:

Proporciona una vista de bienvenida y enlaces a las principales secciones del sitio.

Vista de listado de velas:

Muestra un listado de velas con un resumen de sus atributos.

Permite buscar velas.

Si no hay velas disponibles, se muestra un mensaje de error.

Vista de detalle de vela:

Muestra la información completa de una vela seleccionada, incluida su imagen si está disponible.

Creación, edición y eliminación de velas:

Permite crear, editar y eliminar velas desde vistas específicas.

Los formularios de creación y edición incluyen soporte para imágenes.

Vista de perfil del usuario:

Muestra información del usuario, como nombre, apellido, email y avatar.

Permite la edición del perfil y cambio de contraseña.

Autenticación de usuario:

Los usuarios pueden registrarse, iniciar sesión y cerrar sesión.
