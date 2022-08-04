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

Build and start docker 
```
docker-compose build
docker-compose up -d
```

There are 3 endpoints:

http://localhost:8000/get_name/ -  получает по HTTP имя CSV-файла в хранилище и
суммирует каждый 10й столбец

http://localhost:8000/task_count/ - показывает количество задач на вычисление, которые на текущий момент в работе

http://localhost:8000/task_result/ -принимает ID задачи из п.1 и отображает результат в JSON-формате


OpenApi
http://localhost:8000/docs
