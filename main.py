from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from tasks import sum_task
from utils import check_file_exist
from settings.env import STORAGE
import json
from db.connection import session
from db.model import Task
from settings.celery import celery_app


app = FastAPI()


class File(BaseModel):
    name: str


class Result(BaseModel):
    task_id: str


@app.post('/get_name/')
async def get_name(file: File) -> dict:
    file_exist = await check_file_exist(file.name, STORAGE)
    if file_exist:
        task = sum_task.delay((file.name,))
        return {'task_id': task.id}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'File {file.name}.csv not found')


@app.get('/task_count/')
async def task_count() -> dict:
    i = celery_app.control.inspect()
    keys = list(i.active().keys())
    task_list = i.active()[keys[0]]
    task_list = list(filter(lambda item: item['name'] == 'tasks.sum_task', task_list))

    return {'task_count': len(task_list)}


@app.post('/task_result/')
async def task_result(result: Result):
    query_data = session.query(Task).filter(Task.celery_id == result.task_id)
    response = {}
    for row in query_data:
        response['id'] = row.celery_id
        response['data'] = json.loads(row.data)

    if 'data' in response:
        return response
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Task {result.task_id} not found')
