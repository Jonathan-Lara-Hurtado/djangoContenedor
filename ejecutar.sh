#!/bin/bash
echo "variable"
export OPENSHIFTDATADIR="/opt/app-root/src/data"

echo $OPENSHIFT_DATA_DIR

echo "migrations"
python manage.py makemigrations

echo "migrate"
python manage.py migrate

echo "runserver"
python manage.py runserver 0.0.0.0:8000