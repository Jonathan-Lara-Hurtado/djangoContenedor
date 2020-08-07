#!/bin/bash



echo OPENSHIFTDATADIR='/opt/app-root/src'
echo $OPENSHIFTDATADIR

echo "migrations"
python manage.py makemigrations

echo "migrate"
python manage.py migrate

echo "runserver"
python manage.py runserver 0.0.0.0:8000