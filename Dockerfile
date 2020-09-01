FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /codigo
WORKDIR /codigo
COPY requirements.txt /codigo/
RUN apt-get update
RUN apt-get install apache2 -y
RUN apt-get install apache2-dev -y
RUN pip install -r requirements.txt
COPY . /codigo/
RUN chmod 777 subida/migrations/
RUN chmod 777 ejecutar.sh
RUN chmod 777 /codigo/almacenamiento
CMD ["./ejecutar.sh"]
