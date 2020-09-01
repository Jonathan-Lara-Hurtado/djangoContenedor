#!/bin/bash

chmod 777 almacenamiento

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput -c
python3 manage.py collectstatic --noinput

REDHATOPENSHIFT=true
ARGS=""
ARGS="$ARGS --log-to-terminal"
ARGS="$ARGS --port 8080"
if $REDHATOPENSHIFT
then
  ARGS="$ARGS --url-alias /static $OPENSHIFTDATADIR/ArchivosEstaticos/"
  ARGS="$ARGS --url-alias /ArchivosMedia $OPENSHIFTDATADIR/ArchivosMedia/"
  ARGS="$ARGS --url-alias /favicon.ico $OPENSHIFTDATADIR/ArchivosEstaticos/"
#ARGS="$ARGS --httpd-executable /usr/sbin/apache2"
else
  ARGS="$ARGS --url-alias /static ArchivosEstaticos/"
  ARGS="$ARGS --url-alias /ArchivosMedia ArchivosMedia/"
  ARGS="$ARGS --url-alias /favicon.ico ArchivosEstaticos/"
fi
exec mod_wsgi-express start-server $ARGS pagina/wsgi.py
