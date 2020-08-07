#!/bin/bash
echo "Iniciando proceso"

chmod 777 subida/migrations

echo "migrations"
python manage.py makemigrations

echo "migrate"
python manage.py migrate

echo "runserver"
python manage.py runserver 0.0.0.0:8000