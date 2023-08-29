# Django and DRF with Docker (Udemy Course)
Building a functional API with Docker, Celery, Redis, Flower, Nginx, Nginx Proxy manager, Portainer and more...

# Content

On this course we will be building a production ready, detailed Django REST API, running on a web server powered by NGINX, on a custom domain name and served securely over HTTPS with SSL Certificates from Letsencrypt.

We shall achieve our goal by leveraging tools such as Docker, Celery, Redis, Flower, Nginx, Nginx Proxy manager, Portainer, shell scripts and more...

The concepts we shall cover include:

- Docker and running multiple containers

- Securing a Django REST API with HTTPS using SSL Certificates

- REST APIs with Django and Django Rest Framework

- Class Based Views.

- Shell Scripting.

- Asynchronous tasks with Celery and Redis

- Asynchronous tasks monitoring with Flower

- Introduction to API testing with Pytest using factories and fixtures.

- Token based authentication

- Working with email in development with Mailhog and in production with Mailgun

- Python Test coverage

- Serving static and media files with NGINX and whitenoise

- Makefiles and how they make working with Docker easier.


# Project Setup

Some of the things I did while setting up the project :

- Created requirements folder with a file with the required packages for each environment ( dev vs production = base.txt and local.txt vs production.txt )
- Added a .gitignore
- Created setup.cfg, configuring ```flake8``` and ```isort```
- Changed the ```settings.py``` file into a folder with a file for each environment ( dev vs production = base.txt and local.txt vs production.txt )
- Changed the ```wsgi.py``` file to point to the new settings location
  ```py
    file: wsgi.py

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authors_api.settings.local")
  ```
- Created the ```core_apps``` folder and store my django apps there. THe ones created with ```python manage.py startapp```

# Logging In Django

Logging is important for debugging and trouble shoorint our application.

I will use the python ```logging``` module in this course.

```Loggers``` are the fundamental building blocks of this framework. THey are tipically associated with a specific component or module.

The key components of loggers are :

- Log Levels
- Handlers
- Filters
- Formatters

### Setting Up logging

On our settings/local , I have added :
```py
LOGGING = {
    "version" : 1,
    "disable_existing_loggers": False,
    "formatters" : {
        "verbose" : {
            "format" : "%(levelname)s %(name)-12s %(asctime)s %(module)s"
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers" : {
        "console" : {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter" : "verbose",
        }
    },
    "root": {
        "level": "INFO",
        "handlers" : ["console"]
    },
}
```
