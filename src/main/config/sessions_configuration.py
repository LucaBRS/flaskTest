import os
import sys

import toml
from main.model.gas_station_model import GasStation
from main.model.person_model import Person
from main.model.task_model import Task
from config.database_creation import DatabaseCreation


def parse_arguments(args):
    config_file = None
    for arg in args:
        if arg.startswith('CONFIG_FILE='):
            config_file = arg.split('=')[1]
    return config_file

config_file = parse_arguments(sys.argv[1:])

if config_file:
    print("CONFIG_FILE argument provided:", config_file)
else:
    print("CONFIG_FILE argument not provided. Setting to default config.")
    config_file = 'config.toml'

current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir,'..', '..', '..', 'config.toml')
config = toml.load(config_file_path)

sqlite_session = DatabaseCreation(config['flask']['sql_lite_database_uri'],[GasStation,Person,Task]).get_session()



