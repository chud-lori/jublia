from celery import Celery
from app import create_app
from app import redis_db, db
from app.models import Email
from sqlalchemy import text, cast, Date, func
from flask import current_app, g
from datetime import datetime, date
from app.config import Config


app = create_app()

celery_beat_schedule = {
    "time_scheduler": {
        "task": "send_email",
        # Run every second
        "schedule": 4.0,
    }
}

def make_celery(app):
    celery = Celery(
        __name__,
        result_backend=Config.CELERY_RESULT_BACKEND,
        broker_url=Config.CELERY_BROKER_URL,
        broker=Config.CELERY_BROKER_URL,
        backend=Config.CELERY_RESULT_BACKEND,
        timezone="UTC",
        task_serializer="json",
        accept_content=["json"],
        result_serializer="json",
        beat_schedule=celery_beat_schedule,
    )
    # celery.conf.update(app.config)

    class ContextTask(celery.Task):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.test_request_context():
                g.in_celery_task = True
                res = self.run(*args, **kwargs)
                return res

    celery.Task = ContextTask
    celery.config_from_object(__name__)
    celery.conf.timezone = 'UTC'
    return celery



celery = make_celery(app)


# @celery.task(name='timer_app')
# def timer():
#     second_counter = int(redis_db.get("second")) + 1
#     print(second_counter)
#     if second_counter >= 59:
#         # Reset the counter
#         redis_db.set("second", 0)
#         # Increment the minute
#         redis_db.set("minute", int(redis_db.get("minute")) + 1)
#     else:
#         # Increment the second
#         redis_db.set("second", second_counter)

@celery.task(name='send_email')
def send_email():
    sql = text('select * from emails where date(timestamp)=current_date')
    result = db.engine.execute(sql) # generator
    nw = datetime.now()
    nw = nw.replace(second=0, microsecond=0)
    for row in result:
        row_timestamp = row[4].replace(second=0, microsecond=0)
        if nw == row_timestamp:
            print(row_timestamp)
            up = Email.query.filter_by(id=row[0]).first()
            up.status = 'sent'
            try:
                db.session.commit()
                print(f"{up.id} sent")
            except:
                print(f"{up} update failed")
    print("Nothing to send")