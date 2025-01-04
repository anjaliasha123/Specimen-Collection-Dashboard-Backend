#!/bin/bash

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to be ready..."
python /app/check_postgres.py

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate --noinput

# # Execute SQL import after migrations
# echo "Executing import_data.sql..."
# psql -U $POSTGRES_USER -d $POSTGRES_DB -f /docker-entrypoint-initdb.d/import_data.sql


# Collect Static files
echo "Collect Static Files"
python manage.py collectstatic --noinput

# Import CSV data after migrations are complete
echo "Importing CSV data into PostGIS..."
python manage.py import_csv

# Start server
echo "Starting server"
gunicorn --worker-tmp-dir /dev/shm dashboard_api.wsgi:application --bind "0.0.0.0:8000"