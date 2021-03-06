# Flask

## Requirements

- Python 3.7
- IDE

## Set Up

- Create an virtual enviroment and make sure to run inside it
- Run `pip install -r requirements.txt` to install the dependencies
- create database named `jublia`
- Run redis in port 6379

## Set Up environment variables (Linux)

Set up environment variable from root project directory
Set for development mode

```bash
export FLASK_ENV=development
export FLASK_APP=manage.py
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/jublia
```

## Set Up database

Set up environment variable from root project directory
Set for development mode

```bash
python manage.py create_db
python manage.py seed_db
```

## Run the scheduler

```bash
celery -A app.celeryconf.celery worker --loglevel=INFO --detach --pidfile=''

celery -A app.celeryconf.celery beat --loglevel=INFO --detach --pidfile=''
```

## Run tests

Run this command and access the web app at `localhost:5000`

```bash
pytest -vv
```

## Run

Run this command and access the app app at `localhost:5000`. You can check curl.sh to access di API

```bash
python manage.py run -h 0.0.0.0
```

## Run in docker

P.S. Currently not working, please run locally without docker

```bash
docker-compose up -d --build
```

App running on `localhost:5000`. You can check curl.sh to access di API

## Post email with curl

```bash
curl -X POST -H "Content-Type: application/json"  http://localhost:5000/save_emails --data '{"event_id": "1", "email_subject": "A good seminar", "email_content": "You should come to this seminar", "timestamp": "2021-12-14 20:02:00"}'
```

## Scheduler

The scheduler will run every 4 seconds and check if any email need to send on the time based on the `timestamp` data in database, email sent simulates by updating `status` field in `emails` table from `Unsend` to `sent`

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
