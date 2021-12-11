"""
initiation file for the app
this file invoked from setup.py outstide
this represent the corpe/ directory
"""

from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
import redis
from celery import Celery


# db = connect_db()
db = SQLAlchemy()
celery = Celery(broker="redis://localhost:6379/0",backend="redis://localhost:6379/0")

# Connect Redis db
redis_db = redis.Redis(
    host="localhost", port="6379", db=1, charset="utf-8", decode_responses=True
)

# Initialize timer in redis
redis_db.mset({"minute": 0, "second": 0})

# Add periodic tasks
# celery_beat_schedule = {
#     "time_scheduler": {
#         "task": "timer_app",
#         # Run every second
#         "schedule": 1.0,
#     }
# }

def create_app(config=Config):
    """
    end point of the app
    """
    # Initiate flask object and its config
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    db.init_app(app)
    # Initialize Celery and update its config
    # celery = Celery(app.name)
    # celery.conf.update(
    #     result_backend=app.config["CELERY_RESULT_BACKEND"],
    #     broker_url=app.config["CELERY_BROKER_URL"],
    #     broker=app.config["CELERY_BROKER_URL"],
    #     backend=app.config["CELERY_RESULT_BACKEND"],
    #     timezone="UTC",
    #     task_serializer="json",
    #     accept_content=["json"],
    #     result_serializer="json",
    #     beat_schedule=celery_beat_schedule,
    # )

    from app.routes import page_not_found
    app.register_error_handler(404, page_not_found)

    # run route from the app context
    with app.app_context():
        # Import routes
        from app.routes import app_bp
        app.register_blueprint(app_bp)
        
        return app
