# Proyecto Django Hospital
## Daniel Leonardo Restrepo Vela
### Pasos para usarlo
1. Clonamos el repositorio y vamos a la rama developer
```
git clone https://github.com/AlejoVela/django-hospital.git
git checkout -b developer
git pull origin developer
```
2. Creamos el ambiente virutal con el siguiente comando
```
python -m venv env
env\Scripts\activate
```
3. Descargamos las dependencias del proyecto
```
pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install psycopg2
```
4. Revisamos las dependencias para instaladas para ver que todo se instalo correctamente
```
pip freeze
```
5. Montamos el proyecto
```
python manage.py runserver
```
