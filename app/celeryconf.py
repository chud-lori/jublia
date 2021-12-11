from celery import Celery
import app
from app import redis_db
from app.config import Config

def make_celery(app):
    celery = Celery(
        app.__name__,
        backend=Config.CELERY_RESULT_BACKEND,
        broker=Config.CELERY_BROKER_URL
    )
    # celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery_beat_schedule = {
    "time_scheduler": {
        "task": "timer_app",
        # Run every second
        "schedule": 1.0,
    }
}

celery = make_celery(app)

celery.conf.update(
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

@celery.task(name='timer_app')
def timer():
    second_counter = int(redis_db.get("second")) + 1
    print(second_counter)
    if second_counter >= 59:
        # Reset the counter
        redis_db.set("second", 0)
        # Increment the minute
        redis_db.set("minute", int(redis_db.get("minute")) + 1)
    else:
        # Increment the second
        redis_db.set("second", second_counter)