from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base

from laserfocus.utils.database import DatabaseHandler
from laserfocus.utils.logger import logger

import os

Base = declarative_base()

class Template(Base):
    """Template table"""
    __tablename__ = 'template'
    id = Column(String, primary_key=True)
    name = Column(String)

logger.announcement('Initializing Database Service', 'info')

db_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'template.db')
db_url = f'sqlite:///{db_path}'

engine = create_engine(db_url)

db = DatabaseHandler(base=Base, engine=engine, type='sqlite')

logger.announcement('Successfully initialized Template Service', 'success')