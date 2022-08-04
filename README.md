# FirstVDS test

Test for FirstVDS

## Getting started

Create project folder and clone:

```
mkdir fvds && cd fvds
git clone https://github.com/gatapov/firstvds.git .

```

Create files and logs folders:

```
mkdir files
mkdir logs

```

Create .env file:

```
nano .env

DATABASE_URL=postgresql+psycopg2://postgres:gv@db:5432/fvds
CELERY_BROKER_URL=redis://redis:6379/0
STORAGE=local

```

Put a datafile (data.csv) into files folder

Start with docker compose:
```
docker-compose build
docker-compose up -d
```

Start without docker compose:

create virtualenv (python 3.9) and activate it
```
python3 -m venv env
source env/bin/activate
```

Create db and db user

Create .env file:

```
nano .env

DATABASE_URL=postgresql+psycopg2://user:password@host:5432/fvds
CELERY_BROKER_URL=localhost://redis:6379/0
STORAGE=local

```
install requirements
```
pip install -r requiremets.txt
```

Run project

```
uvicorn main:app --reload
```


There are 3 endpoints:

http://localhost:8000/get_name/ -  получает по HTTP имя CSV-файла в хранилище и
суммирует каждый 10й столбец

http://localhost:8000/task_count/ - показывает количество задач на вычисление, которые на текущий момент в работе

http://localhost:8000/task_result/ -принимает ID задачи из п.1 и отображает результат в JSON-формате


OpenApi
http://localhost:8000/docs
