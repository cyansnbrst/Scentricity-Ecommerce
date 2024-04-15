FROM python:3.10-alpine3.16

WORKDIR /backend
EXPOSE 8000

COPY requirements.txt /temp/requirements.txt

RUN apk add postgresql-client build-base postgresql-dev
RUN pip install -r /temp/requirements.txt
RUN adduser --disabled-password scents-user

COPY scentricity_backend /backend

# docker-compose run --rm backend sh -c "python manage.py migrate"
