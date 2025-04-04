#!/bin/sh

echo "[entrypoint] Running Django migrations..."
python manage.py migrate

echo "[entrypoint] Creating superuser if needed..."
python manage.py create_superuser

echo "[entrypoint] Starting Gunicorn..."
exec gunicorn app.wsgi:application --bind 0.0.0.0:8000
