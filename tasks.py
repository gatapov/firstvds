import os
import logging
import pandas as pd
import json
from settings.conf import LOG_DIR
from celery.signals import after_setup_logger
from settings.celery import celery_app
from storage import get_file_link
from settings.env import STORAGE
from db.model import Task


logger = logging.getLogger(__name__)


@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filehandler = logging.FileHandler(os.path.join(LOG_DIR, 'celery.log'))
    filehandler.setLevel(logging.DEBUG)
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)


@celery_app.task(bind=True)
def sum_task(self, file_name: str):
    file_name = file_name[0]
    file_link = get_file_link(file_name, STORAGE)
    df = pd.read_csv(file_link, delimiter=',')
    cols_list = list(df.columns.values)[0].split(',')[1::10]
    cols_list = list(map(lambda i: i.replace('"', ''), cols_list))
    sum_dict = {}
    for name, data in df.iterrows():
        row = list(data)[0].split(',')[1::10]
        row = list(map(lambda i: float(i.replace('"', '')) if i.replace('"', '') != '' else None, row))
        row_dict = dict(zip(cols_list, row))
        for key in row_dict:
            if key in sum_dict and row_dict[key] is not None:
                sum_dict[key] = sum_dict[key] + row_dict[key]
            elif row_dict[key] is not None:
                sum_dict.update({key: row_dict[key]})

    task = Task(celery_id=self.request.id, data=json.dumps(sum_dict))
    task.save()


