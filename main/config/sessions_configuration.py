import logging
import os

import toml

from main.config.database_creation import DatabaseCreation
from main.model.gas_station_model import GasStation
from main.model.person_model import Person
from main.model.task_model import Task

logger = logging.getLogger(__name__)

config_from_env = os.environ.get('CONFIG')

if config_from_env is not None:
    logger.info("CONFIG_FILE argument provided:", config_from_env)
else:
    logger.info("CONFIG_FILE argument not provided. Setting to default config.")
    config_from_env = 'config.toml'

# absolute path to  app.py
current_dir = os.path.dirname(os.path.abspath(__file__))

#  up two directories
flaskTest_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))

# Construct the path to the configuration file
config_file_path = os.path.join(flaskTest_dir, config_from_env)
logger.debug('path for the config: ' + config_file_path)
# Load
config = toml.load(config_file_path)

# Create the SQLite session
sqlite_session = DatabaseCreation(config['flask']['sql_lite_database_uri'], [GasStation, Person, Task]).get_session()
