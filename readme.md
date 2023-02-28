# Installing Django tutorial

## Create a virtual environment

Create a requirements.txt file

```
Django
```

Create a virtual environment and install the requirements

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a .gitignore file

```bash
echo "venv" >> .gitignore
```

## Check the Django version

```bash
import django
print(django.get_version())
```
## Create a project

```bash
django-admin startproject core .
```

## Run the server

```bash
python manage.py runserver
```
