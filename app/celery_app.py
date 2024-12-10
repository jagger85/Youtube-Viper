from celery import Celery
from .config import Config

def make_celery():
    celery = Celery(
        __name__,
        broker=Config().CELERY_BROKER_URL,
        backend=Config().CELERY_RESULT_BACKEND
    )
    return celery

celery = make_celery()
