FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /codigo
WORKDIR /codigo
COPY requirements.txt /codigo/
RUN yum install apache2
RUN yum install apache2-dev
RUN pip install -r requirements.txt
COPY . /codigo/
RUN chmod 777 subida/migrations/
RUN chmod 777 ejecutar.sh
CMD ["./ejecutar.sh"]
