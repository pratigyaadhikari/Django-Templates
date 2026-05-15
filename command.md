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