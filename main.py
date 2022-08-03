import os
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from tasks import sum_task      # test_sum
from utils import check_file_exist
from settings.conf import STORAGE
from fastapi_sqlalchemy import DBSessionMiddleware
from dotenv import load_dotenv
from settings.conf import BASE_DIR
import json
from db.connection import session
from db.model import Task


load_dotenv(os.path.join(BASE_DIR, '.env'))
app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.getenv('DATABASE_URL'))


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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'File {file.name} not found')


@app.get('/task_count/')
async def task_count() -> dict:
    return {'task_count': 0}


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

