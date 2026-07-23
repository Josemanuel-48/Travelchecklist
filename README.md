# TravelChecklist

Aplicación web desarrollada con Django para gestionar viajes y las tareas asociadas a cada uno.

## Funcionalidades
- página de inicio (pública)
- registro de usuario, login y logout
- CRUD de viajes (crear, ver, editar, eliminar)
- CRUD de tareas asociadas a cada viaje
- búsqueda, filtros, orden y paginación en el listado de viajes
- mensajes de confirmación tras crear, editar o eliminar un viaje
- panel de administración de Django

## Tecnologías
- Python
- Django
- SQLite
- HTML / CSS
- Git y GitHub

## Puesta en marcha

1. Clonar el repositorio.

2. Crear y activar el entorno virtual:

   python -m venv .venv
   .venv\Scripts\Activate.ps1

3. Instalar dependencias:

   pip install -r requirements.txt

4. Aplicar migraciones:

   python manage.py migrate

5. Crear superusuario (para acceder al panel de administración):

   python manage.py createsuperuser

6. Lanzar el servidor:

   python manage.py runserver

## Usuario de prueba

Para probar la aplicación sin necesidad de registrarte, puedes usar:

- Usuario: demo
- Contraseña: demo1234

También puedes crear tu propio usuario desde /signup/.

## Ejemplos de URLs con parámetros

El listado de viajes (/trips/) admite búsqueda, filtro, orden y paginación combinados mediante parámetros GET:

/trips/?q=Amazonas&destination=Roma&order=destination_asc
/trips/?page=2&q=&destination=&order=destination_asc

## Nota sobre privacidad

Aunque el enunciado sugiere que el listado y el detalle de viajes sean públicos, en esta aplicación esas vistas se mantienen protegidas con @login_required. Los viajes son información personal de cada usuario, por lo que deben ser visibles únicamente para la persona que ha iniciado sesión y no para cualquier visitante. La parte pública de la navegación es la página de inicio (home).

## Estructura básica

- config/ → configuración general del proyecto
- trips/ → app principal
- templates/ → plantillas HTML

## Autoría

- Jose Manuel Gómez León

## Fecha

- 2026