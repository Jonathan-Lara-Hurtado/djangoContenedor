FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /codigo
WORKDIR /codigo
COPY requirements.txt /codigo/
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install apache2
COPY . /codigo/
RUN chmod 777 subida/migrations/
RUN chmod 777 ejecutar.sh
CMD ["./ejecutar.sh"]
