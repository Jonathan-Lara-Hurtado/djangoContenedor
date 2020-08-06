FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /codigo
WORKDIR /codigo
COPY requirements.txt /codigo/
RUN pip install -r requirements.txt
COPY . /codigo/
CMD ["python","manage.py","makemigrations"]
CMD ["python","manage.py","migrate"]
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
