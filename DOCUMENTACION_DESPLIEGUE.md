# Documentación de Despliegue: Django Tutorial con Apache y WSGI

Esta documentación resume los pasos realizados para desplegar la aplicación `django_tutorial` en un entorno de desarrollo utilizando Apache2 con `mod_wsgi`.

## 1. Configuración del Entorno

1.  **Clonado del Repositorio**: Se utilizó el repositorio `https://github.com/josedom24/django_tutorial`.
2.  **Entorno Virtual**:
    *   Creación: `python3 -m venv venv`
    *   Activación e Instalación: `venv/bin/pip install -r requirements.txt`

## 2. Base de Datos (SQLite)

*   **Identificación**: Se consultó `django_tutorial/settings.py` para verificar que la base de datos es SQLite (`db.sqlite3`).
*   **Migración**: Se ejecutó `venv/bin/python manage.py migrate` para crear las tablas.
*   **Superusuario**: Se creó el usuario `admin` con permisos de administración.
*   **Datos de Prueba**: Se generaron dos preguntas ("¿Cual es tu lenguaje favorito?" y "¿Te gusta Django?") mediante un script de población.

## 3. Verificación de la Aplicación

La aplicación se verificó inicialmente con el servidor de desarrollo (`runserver`) en el puerto 8000.

*   Acceso a Encuestas: `http://localhost:8000/polls/`
*   Acceso a Administración: `http://localhost:8000/admin/`

## 4. Despliegue con Apache2 + WSGI

Se configuró el servidor Apache2 para servir la aplicación en el puerto 80 (HTTP estándar).

### Pasos Realizados:
1.  **Instalación del Módulo**: Verificación de `libapache2-mod-wsgi-py3`.
2.  **Archivos Estáticos**:
    *   Se configuró `STATIC_ROOT` en `settings.py`.
    *   Se ejecutó `collectstatic`: `venv/bin/python manage.py collectstatic`.
3.  **Configuración de Apache (`/etc/apache2/sites-available/django_tutorial.conf`)**:
    *   Se definió un `VirtualHost` en el puerto 80.
    *   Configuración del proceso demonio WSGI (`WSGIDaemonProcess`) apuntando al entorno virtual.
    *   Mapeo de URL WSGI (`WSGIScriptAlias /`).
    *   Alias para archivos estáticos (`/static`).
4.  **Permisos**:
    *   Se ajustaron los permisos de `db.sqlite3` y el directorio del proyecto para que el usuario `www-data` (Apache) pudiera leer y escribir.
5.  **Activación**:
    *   `a2ensite django_tutorial.conf`
    *   `a2dissite 000-default.conf` (para evitar conflictos en el puerto 80).
    *   Reinicio de Apache: `systemctl restart apache2`.

## 5. Pruebas Finales

La aplicación está funcionando correctamente en `http://localhost/`.

### Pantallazos

*   **Página de Encuestas**: `pantallazos/polls_page_1765870256768.png`
*   **Panel de Administración**: `pantallazos/admin_dashboard_1765870283885.png`
