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
from flask_mail import Mail


# db = connect_db()
db = SQLAlchemy()
celery = Celery(broker=Config.CELERY_BROKER_URL,backend=Config.CELERY_RESULT_BACKEND)
mail = Mail()

# Connect Redis db
redis_db = redis.Redis(
    host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=1, charset="utf-8", decode_responses=True
)

# Initialize timer in redis
redis_db.mset({"minute": 0, "second": 0})

def create_app(config=Config):
    """
    end point of the app
    """
    # Initiate flask object and its config
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    db.init_app(app)
    mail.init_app(app)

    from app.routes import page_not_found
    app.register_error_handler(404, page_not_found)

    # run route from the app context
    with app.app_context():
        # Import routes
        from app.routes import app_bp
        app.register_blueprint(app_bp)
        
        return app
