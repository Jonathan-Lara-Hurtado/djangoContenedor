#!/bin/bash

#echo "Iniciando proceso"

echo "migrations"
python manage.py makemigrations

echo "migrate"
python manage.py migrate

python manage.py migrate collectstatic

ARGS=""
ARGS="$ARGS --log-to-terminal"
ARGS="$ARGS --port 8080"
ARGS="$ARGS --url-alias /static $OPENSHIFTDATADIR/ArchivosEstaticos/"
ARGS="$ARGS --url-alias /ArchivosMedia $OPENSHIFTDATADIR/ArchivosMedia/"
ARGS="$ARGS --url-alias /favicon.ico $OPENSHIFTDATADIR/ArchivosEstaticos/"
#ARGS="$ARGS --httpd-executable /usr/sbin/apache2"
exec mod_wsgi-express start-server $ARGS pagina/wsgi.py

#echo "Iniciando proceso"

#echo "migrations"
#python manage.py makemigrations

#echo "migrate"
#python manage.py migrate

#echo "runserver"
#python manage.py runserver 0.0.0.0:8000