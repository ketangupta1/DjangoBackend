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

## Migrations
- Show migration:

        python3 manage.py showmigrations
- Make migration:
    After creating the models then do the makemigrations.
  
        python3 manage.py makemigrations
- Apply migration:
    To apply that migrations into our DB run command:
  
        python3 manage.py migrate
- Modifying existing table:
  Add the field in the desired table in models.py file and after that use: python3 manage.py makemigrations, you can not add the fields without giving default values. And then apply the migration using command: python3 manage.py migrate.

## User:
- Create superuser:

        python3 manage.py createsuperuser
- If you want to see you model in admin panel then register your model to admin.py 
