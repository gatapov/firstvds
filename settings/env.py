import os
from .conf import BASE_DIR
from dotenv import load_dotenv


load_dotenv(os.path.join(BASE_DIR, '.env'))

DATABASE_URL = os.getenv('DATABASE_URL')
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
STORAGE = os.getenv('STORAGE')
