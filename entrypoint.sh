#!/bin/sh

if [ "$DATABASE" = "jublia" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py create_db
python manage.py seed_db
# Run Celery worker
celery -A app.celeryconf.celery worker --loglevel=INFO --detach --pidfile=''

# Run Celery Beat
celery -A app.celeryconf.celery beat --loglevel=INFO --detach --pidfile=''

exec "$@"

# flask run --eager-loading
