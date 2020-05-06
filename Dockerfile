FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/

RUN pip install pipenv && pipenv install --system

COPY . /code/

RUN python manage.py collectstatic --noinput

CMD gunicorn hello_django.wsgi:application --bind 0.0.0.0:8000