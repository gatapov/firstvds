from celery import Celery
from settings.env import CELERY_BROKER_URL


celery_app = Celery('tasks', broker=CELERY_BROKER_URL)

