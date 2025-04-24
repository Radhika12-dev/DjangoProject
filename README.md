# DjangoProject
This is a django project tutorial

# Command to create virtual env and activate it
python -m pip install virtualenv
python -m virtualenv venv
venv\Scripts\activate

# Command to create a new project
django-admin startproject name_of_project

# Command to create an app
python manage.py startapp app_name

# Command to run the server
python manage.py runserver

# Command to create superuser
python manage.py createsuperuser

# Command to get help
python manage.py --help

# Command to migrate the chnages to DB
python manage.py migrate
python manage.py makemigrations

Run pip install django-environ for handling environment variables.


