#!/usr/bin/env bash
echo waiting for db ...

while ! nc -z postgresql 5432; do
  sleep 0.1
done

echo SQL started

python manage.py migrate

exec gunicorn --bind 0.0.0.0:8000 django_demo.wsgi --threads 4 --preload