<h1>Documentación de Despliegue Proyecto Django Tutorial</h1>

<h2>1. Entorno de Desarrollo (Local)</h2>

<h3>Configuración Inicial</h3>
1.  **Repositorio**: Fork de `https://github.com/josedom24/django_tutorial` en `https://github.com/serjaii/django_tutorial`.
2.  **Entorno Virtual**: Creación (`python3 -m venv venv`) e instalación de dependencias (`pip install -r requirements.txt`).
3.  **Base de Datos**: SQLite por defecto. Migraciones aplicadas (`manage.py migrate`).
4.  **Datos**: Creación de superusuario (`admin`/`admin`) y preguntas de prueba mediante script `populate.py`.

<h3>Despliegue con Apache2</h3>
*   **Servidor**: Apache2 con módulo `libapache2-mod-wsgi-py3`.
*   **Configuración**: Archivo `/etc/apache2/sites-available/django_tutorial.conf`.
*   **Estáticos**: `collectstatic` hacia `STATIC_ROOT`.
*   **Resultados**:
    *   Polls: `pantallazos/polls_page_1765870256768.png`
    *   Admin: `pantallazos/admin_dashboard_1765870283885.png`

<hr>

<h2>2. Entorno de Producción (VPS)</h2>

<h3>Preparación del Servidor</h3>
1.  **Dependencias**: Instalación de `python3-venv`, `python3-dev`, `libmariadb-dev` , `build-essential`, `mariadb-server`, `nginx`, `git`.
2.  **Código**: Clonado del repositorio en `/home/serjaii/django_tutorial`.
3.  **Entorno Virtual**: Creación y activación e instalación de dependencias + `mysqlclient` y `uwsgi`.

<h3>Base de Datos (MariaDB)</h3>
1.  **Creación**: Base de datos `myproject` y usuario `myprojectuser`.
2.  **Configuración Django**: Modificación de `settings.py` para usar el motor `django.db.backends.mysql`.
3.  **Migración de Datos**:
    *   Exportación local: `python manage.py dumpdata --exclude auth.permission --exclude contenttypes > data.json`
    *   Carga en VPS: `python manage.py migrate` y `python manage.py loaddata data.json`.

<h3>Servidor de Aplicaciones (uWSGI)</h3>
1.  **Configuración**: `uwsgi.ini` en la raíz del proyecto (socket en `django_tutorial.sock`).
2.  **Servicio Systemd**: `/etc/systemd/system/django_uwsgi.service` para ejecución automática.

<h3>Servidor Web (Nginx) y SSL</h3>
1.  **Configuración**: Archivo `/etc/nginx/sites-available/django_tutorial`.
2.  **Proxy Inverso**: Redirección de peticiones `/` al socket uWSGI.
3.  **Archivos Estáticos**: Servidos directamente por Nginx desde `/static/`.
4.  **SSL**: Generación de certificado autofirmado para `python.sergiojimenez.org` (ya que el dominio no apuntaba correctamente para Let's Encrypt).
5.  **Redirección HTTP a HTTPS**: Configurada en Nginx.

<h3>Verificación Final</h3>
La aplicación es accesible vía HTTPS en `https://82.165.10.178/`.
*   **Debug**: `DEBUG = False` configurado en producción.
*   **Estilos**: Admin se visualiza correctamente.

<h3>Pantallazos Producción</h3>
*   **Encuestas**: `pantallazos/produccion_polls.png`
*   **Admin Dashboard**: `pantallazos/produccion_admin.png`
