import logging
import os

import toml
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.gas_station_model import GasStation
from model.person_model import Person
from model.task_model import TaskModule

logger = logging.getLogger(__name__)
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir, '..', 'config', 'config.toml')
config = toml.load(config_file_path)



engine = create_engine(config['flask']['sql_lite_database_uri'])
TaskModule.metadata.create_all(bind=engine)
Person.metadata.create_all(bind=engine)
GasStation.metadata.create_all(bind=engine)

Session_sqlite = sessionmaker(bind=engine)
