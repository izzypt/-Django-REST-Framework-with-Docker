# Django and DRF with Docker (Udemy Course)
Building a functional API with Docker, Celery, Redis, Flower, Nginx, Nginx Proxy manager, Portainer and more...

# Course content

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
