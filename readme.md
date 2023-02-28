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

## Make a request to the server

```bash
curl http://127.0.0.1:8000/
```

```bash 


## Create an app

```bash
python manage.py startapp api
```

## Create a view

```python
from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Home page")
```