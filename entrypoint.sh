# #!/bin/sh

# if [ "$DATABASE" = "delman" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi

# python manage.py create_db

# exec "$@"
#!/bin/sh

# Run Celery worker
celery -A app.celery worker --loglevel=INFO --detach --pidfile=''

# Run Celery Beat
celery -A app.celery beat --loglevel=INFO --detach --pidfile=''

flask run --eager-loading
