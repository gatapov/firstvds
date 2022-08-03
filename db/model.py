from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, JSON
from db.connection import session


Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    celery_id = Column(String)
    data = Column(JSON)

    def save(self):
        session.add(self)
        session.commit()


tasks = Task.__table__
