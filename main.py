from fastapi import FastAPI
from pydantic import BaseModel
from tasks import sum_task, test_sum
from settings.conf import FILES_DIR


app = FastAPI()


class File(BaseModel):
    name: str


@app.post('/get_name/')
async def get_name(file: File) -> dict:
    task = sum_task.delay((file.name,))
    return {'task_id': task.id}


@app.get('/task_count/')
async def task_count() -> dict:
    return {'task_count': 0}


@app.post('/test/')
async def get_name(file: File) -> dict:
    task = await test_sum(file.name)
    return {'task_id': task}
