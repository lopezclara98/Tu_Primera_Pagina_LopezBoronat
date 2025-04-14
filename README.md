# Tu Primera Página - Proyecto Django 💻

Este es un proyecto realizado como parte del curso de Python de Coderhouse. Se trata de una página web para gestionar velas (crear y listar).

---

## 🚀 ¿Cómo iniciar el proyecto?

1. Cloná el repositorio:
   ```bash
   git clone https://github.com/lopezclara98/Tu_Primera_Pagina_LopezBoronat.git
2: Entrá a la carpeta del proyecto:
cd Tu_Primera_Pagina_LopezBoronat

3: Activá el entorno virtual
.venv\Scripts\activate
4. Instalá dependencias
pip install django
5. Ejecutá el servidor:
python manage.py runserver

Orden sugerido para probar funcionalidades
Inicio

Ruta: http://127.0.0.1:8000/

Vista: inicio → muestra página de bienvenida.

Crear Vela

Ruta: http://127.0.0.1:8000/velas/crear

Vista: crear_vela → formulario para agregar una vela.

Archivo de plantilla: templates/inicio/crear_vela.html

Listar Velas

Ruta: http://127.0.0.1:8000/velas/

Vista: listado_de_velas → muestra lista de todas las velas creadas.

Archivo de plantilla: templates/inicio/listado_de_velas.html
