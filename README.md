# Django Rest framework Auth Setup (dj-rest-auth & django-allauth)

This project implements how to use dj-rest-auth and django-allauth
to sign up, sign in, authenticate users in drf applications.

> **TIP**
> 
> This project uses "poetry" to manage dependencies. Ensure you have "poetry" already installed.
> 
> Read documentation here on how to install "poetry": https://python-poetry.org/docs/
>
> You can still use "pip" to install the dependencies in the *requirements.txt* file

-----------

## Project Structure

See this repository on how the environment setup was achieved:
[django_env_settings][reference]

[reference]:https://github.com/cla-bit/django_env_settings.git

```text

└── root/
    ├── loggings/
    │   ├── __init__.py
    │   ├── base.py
    │   └── local.py
    ├── manage.py
    ├── pyproject.toml
    ├── ruff.toml
    ├── requirements.txt
    └── drfauth/
        ├── libs_config/
        │   └── __init__.py
        ├── __init__.py
        ├── asgi.py
        ├── env.py
        ├── urls.py
        ├── wsgi.py
        └── settings/
            ├── __init__.py
            ├── base.py
            └── local.py

```

------------

## Installation & Setup


#### Installation

- Clone the repository

```git
git clone https://github.com/cla-bit/drf-auth-setup.git
cd <your_project>
```

- Create your virtual environment

```shell
python -m venv <your_venv>
```
> **NOTE**
> 
> If using linux/MacOS terminal, use "python3".

- Activate your virtual environment

```shell
<your_venv>\Scripts\activate
```

*Linux/MacOS terminal*
```shell
source <your_venv>/bin/activate
```

- Install the dependencies using *poetry* or *pip*

```shell
poetry install
```

or using pip

```shell
pip install -r requirements.txt
```

#### Start up the application

- Make migrations
```python
python manage.py makemigrations
```

- Migrate to the database
```python
python manage.py migrate
```

- Start the django project
```python
python manage.py runserver
```

- Open the server on your browser and view the API endpoints

![Example 1](/static/img/drf_auth_setup1.png "drf-auth-setup api endpoints example")

![Example 2](/static/img/drf_auth_setup2.png "drf-auth-setup api endpoints example")

---------

## Workflow

This project uses a CustomUser object instead of the default django User object.

With this knowledge, you will be able to setup completely and customize your django project to 
authenticate custom users.

> **TIP**
> 
> drf-spectacular library was installed and setup for API documentation.