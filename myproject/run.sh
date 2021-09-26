#!/bin/bash
rm db.sqlite3
rm -rf myproject/login/migrations/
python manage.py makemigrations 
python manage.py migrate
exec ./manage.py runserver 0.0.0.0:8000