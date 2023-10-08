from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
DATABASE_URL = os.getenv('IOT_DATABASE_URL')

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind = engine) # autocommit=False, autoflush=False

Base = declarative_base()
