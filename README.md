# templates_records

Web application for the "Kommerts Group" company

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/outeqa1/template_csv
```


Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```


Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```


After that you have to add apps to `settings.py`:

```sh
INSTALLED_APPS = [
    *** django apps ***
    'templates_records',
]
```


You have to connect django project with DB (I used PostgreSQL):

First method(by adding db to databases in `settings.py`):

```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'templates_records',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    		}
	   }
```


After creating views, models, forms, etc, you have to migrate all the changes to DB: 

```sh
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
```


Finally run your server:

```sh
(venv)$ python manage.py runserver
```


To take admin roots you have to create superuser(edit anything in the web app):

```sh
(venv)$ python manage.py createsuperuser
```

