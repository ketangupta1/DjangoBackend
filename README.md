# Django-Course
Starting the Django framework

## Install Django
    python3 -m pip install django

## Creating Django project
    django-admin startproject my_django_project
- Change the directory to my_django_project

## Start the server by running the command
    python3 manage.py runserver

## Create your app(named my_app here) by using command:
    python3 manage.py startapp my_app
- Now register your app to the INSTALLED_APPS section of the setting.py(my_django_project) file, the name of the app can be found in the app.py file of my_app.
