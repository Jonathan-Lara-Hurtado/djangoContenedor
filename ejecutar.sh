#!/bin/bash

ARGS=""
ARGS="$ARGS --port 8080"
#ARGS="$ARGS --url-alias /static ArchivosEstaticos/"
#ARGS="$ARGS --url-alias /ArchivosMedia ArchivosMedia/"
#ARGS="$ARGS --url-alias /favicon.ico ArchivosEstaticos/"

exec mod_wsgi-express start-server $ARGS pagina/wsgi.py

#echo "Iniciando proceso"

#echo "migrations"
#python manage.py makemigrations

#echo "migrate"
#python manage.py migrate

#echo "runserver"
#python manage.py runserver 0.0.0.0:8000