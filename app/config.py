import os

class Config(object):
    """
    class Config to store credential information
    """
    SECRET_KEY = '\xce\xcc\x9eV\x978\xafpbdO@J\x92\xcc\x80\xa8\xc5\xa0\xbbu&\x84\xba'
    DB_USERNAME = 'postgres'
    DB_PASSWORD = 'postgres'
    DB = 'jublia'
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:postgres@localhost:5432/jublia")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = os.getenv("REDIS_PORT", "6379")
    CELERY_BROKER_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND = os.getenv("REDIS_URL", "redis://localhost:6379/0")
