FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/

RUN pip install pipenv && pipenv install --system

COPY . .

RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D myuser
USER myuser

CMD gunicorn iron_project.wsgi:application --bind 0.0.0.0:8000
