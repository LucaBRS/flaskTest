import logging
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.gas_station_model import GasStation
from model.person_model import Person
from model.task_model import TaskModule

logger = logging.getLogger(__name__)

class SqliteConfig():
    def __init__(self,db_path):
        logger.debug("starting config for sqlite database")
        engine = create_engine(db_path)
        tables= [TaskModule,Person,GasStation]
        for table in tables:
            table.metadata.create_all(bind=engine)
        self.session_sqlite = sessionmaker(bind=engine)()

    def get_session(self):
        return self.session_sqlite
