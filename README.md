# LISTA DE TAREAS
Con esta aplicación se gestionan tareas ordenadas por categorías
## Procedimiento de arranque

### Ajustes iniciales
Abra un terminal en el directorio del proyecto y ejecute este comando para crear un entorno virtual:
```
python -m virtualenv .venv
```
.venv es el nombre que se le da al entorno virtual

Ahora active el entorno virtual presionando en la parte inferior izquierda de su Visual Studio Code que aparecera como "Python (version de python que tenga ejemplo: 3.8.10 ) ('.venv: venv')"

Si no aparece cierre el Visual Studio Code y vuelvalo a abrir

Instale las dependencias:
```
pip install -r requirements.txt
```
El entorno virtual debe estar activo y el comando ejecutarlo desde la carpeta del proyecto

Abra el archivo **inventario/settings.py** y modifique todos lo datos necesarios en  'DATABASES' para conectarlo a su base de datos
```python
DATABASES = {
        'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'mydb',
		'USER': 'root',
		'PASSWORD': 'root',
		'HOST':'localhost',
		'PORT':'3306',
    }
}
```
Añadir en **settings.py** Installed_Apps la carpeta, en este caso **tareas**


Ejecutar el siguiente comando:
``` 
python manage.py makemigrations
```
Ejecutar el siguiente comando para instalar 
el Mysql
```
pip install Mysql
```

Para exportar la base de datos ejecute el siguiente comando:
```
python manage.py migrate
```

Ahora se creará un usuario administrador con el siguiente comando:
```
python manage.py createsuperuser
```
Siga las instrucciones para crear su usuario administrador
### Puesta en marcha
Asegurese que la base de datos está en funcionamiento

Inicie el entorno virtual presionando en la parte inferior izquierda del Visual Studio Code y abra un terminal nuevo para comprobar que aparece (.venv) antes de la dirección en el terminal

Compruebe que esta en la carpeta raíz del proyecto para que la aplicación funcione correctamente cuando la ejecute

NOTA: En Windows puede fallar con el PowerShell

Ejecute el proyecto desde **manage.py** con 'F5' o desde el terminal escriba:
```
python manage.py runserver
```
Seleccione la opción de **Django** si se le pregunta

Puede acceder a la aplicación con un navegador en la siguiente dirección:

http://127.0.0.1:8000/admin/

### Estructura del proyecto

El modulo principal se llama **manage.py**

Las vistas se encuentran en **tareas/templates**

Los archivos de estilos se encuentran en **tareas/static**

Todas las dependencias se encuentran en el archivo **requirements.txt**