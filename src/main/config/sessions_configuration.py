import os

import toml
from main.model.gas_station_model import GasStation
from main.model.person_model import Person
from main.model.task_model import Task
from config.database_creation import DatabaseCreation

#TODO evitare classe e "scrivere diretto"

current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir,'..', '..', '..', 'config.toml')
config = toml.load(config_file_path)

sqlite_session = DatabaseCreation(config['flask']['sql_lite_database_uri'],[GasStation,Person,Task]).get_session()



