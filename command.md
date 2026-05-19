# install virtual environment
pip install virtualenv

# create virtual environment
virtualenv name
pythin -m venv name

# activate virtual env
env\Scripts\activate
source env\Scripts\activate

source env/bin/activate. (Mac ko lagi)

# Django: Python based Full stack framework(backend, frontend)
# MVT architecture (follow garxa DJANGO la)
Model: data, database, table, fields, datatypes
view: logic: request-response, Model data httprequest, template building
Templates: frontend(html,css)

(projects create garera app create garni
)
- projects: core configurations haru basxa
- app: functionalities

# start project
django-admin startproject project_name .   (. is optional)

# start app
python manage.py startapp app_name

# run server
python manage.py runserver


# Templates 

#load .env file
pip install python-dotenv

#stored all installed packages
pip freeze > requirements.txt

#install later( other can install same packages)
pip install -r requirements.txt

# uninstall
pip uninstall -r requirements.txt


# MODELS
# model -> makemigrations -> migration file created -> migrate -> database reflect

# migration file created
python manage.py makemigrations

python manage.py migrate

# create superuser
python manage.py createsuperuser


# ( These commands are used through the terminal to manage and store data on the server/database, instead of adding everything manually from the admin panel in the browser)

# shell
python manage.py shell
# then (import garni)
from app_name.models import model_name

# CRUD : Create, Retrieve, Update, Delete
# get all data
model_name.objects.all()

# create data
model_name.objects.create(field1 = "...", field2 = "...", ....)

# Retrieve: single data
a = model_name.objects.get(id = 1) 
a.field1 
a.field2

# Update
We first fetch object into variable, then modify it.
a.field1 = new_data 
a.field2 = new data 
a.field3 = new data 
a.save()

# Delete:
retrieve a data
a.delete()

# Filter
model_name.objects.filter(field1= "...", field2 = "...", field3 = "...", ......)