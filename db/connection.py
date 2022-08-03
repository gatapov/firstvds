from sqlalchemy import create_engine
from dotenv import load_dotenv
from settings.conf import BASE_DIR
import os
from sqlalchemy.orm import sessionmaker


load_dotenv(os.path.join(BASE_DIR, '.env'))

engine = create_engine(os.getenv('DATABASE_URL'))
Session = sessionmaker(bind=engine)
session = Session()

