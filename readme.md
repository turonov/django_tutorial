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

## Check the Django version

```bash
import django
print(django.get_version())
```
