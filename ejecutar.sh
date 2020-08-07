#!/bin/bash
echo "variable"
export OPENSHIFT_DATA_DIR = '/opt/app-root/src/data'

echo "migrations"
python manage.py makemigrations

echo "migrate"
python manage.py migrate

echo "runserver"
python manage.py runserver 0.0.0.0:8000