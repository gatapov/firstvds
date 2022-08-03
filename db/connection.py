from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings.env import DATABASE_URL


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

