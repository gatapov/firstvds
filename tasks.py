import os
import logging
import csv
from settings.conf import LOG_DIR, FILES_DIR
from celery.signals import after_setup_logger
from settings.celery import celery_app


logger = logging.getLogger(__name__)


@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filehandler = logging.FileHandler(os.path.join(LOG_DIR, 'celery.log'))
    filehandler.setLevel(logging.DEBUG)
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)


@celery_app.task
def sum_task(file_name: str):
    with open(os.path.join(FILES_DIR, f'{file_name}.csv'), 'r') as file:
        file_reader = csv.reader(file, delimiter=",")
    return True


async def test_sum(file_name: str):
    with open(os.path.join(FILES_DIR, f'{file_name}.csv'), 'r') as file:
        file_reader = csv.reader(file, delimiter=",")
        for line in file_reader:
            print(line)

    return 1
