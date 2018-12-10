#!/usr/bin/env bash
#python manage.py migrate
gunicorn api.wsgi \
    --name munchy \
    --bind unix:/opt/django_app.sock \
    --workers 3 \
    --log-level=info \
    --log-file=/var/log/gunicorn.log \
    --access-logfile=/var/log/access.log &
service nginx start
tail -f /var/log/nginx/error.log
