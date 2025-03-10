from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
import os

from laserfocus.utils.database import DatabaseHandler
from laserfocus.utils.logger import logger

class Database:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            logger.announcement('Initializing Database Service', 'info')
            
            self.db_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'template.db')
            self.db_url = f'sqlite:///{self.db_path}'
            self.engine = create_engine(self.db_url)
            
            self.Base = declarative_base()
            self._setup_models()
            self.db = DatabaseHandler(base=self.Base, engine=self.engine, type='sqlite')
            
            logger.announcement('Successfully initialized Database Service', 'success')
            self._initialized = True

    def _setup_models(self):
        class Template(self.Base):
            """Template table"""
            __tablename__ = 'template'
            id = Column(String, primary_key=True)
            name = Column(String)
            updated = Column(String)
            created = Column(String)

        # Store model classes as attributes of the instance
        self.Template = Template

# Create a single instance that can be imported and used throughout the application
db = Database().db