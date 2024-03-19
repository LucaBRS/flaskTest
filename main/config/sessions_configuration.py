import logging
import os

import toml

from main.config.database_creation import DatabaseCreation
from main.model.gas_station_model import GasStation
from main.model.person_model import Person
from main.model.task_model import Task
from main.model.user_model import User
from main.model.role_model import Role
from main.model.userRole_model import UserRole
from main.model.base_auth import Base_Auth
from main.model.base import Base

logger = logging.getLogger(__name__)

config_from_env = os.environ.get('CONFIG')

config = toml.load('config.toml')

# Create the SQLite session
sqlite_session_user = DatabaseCreation(config['flask']['sql_lite_database_user'], [User, Role, UserRole],Base_Auth).get_session()

sqlite_session = DatabaseCreation(config['flask']['sql_lite_database_uri'], [GasStation, Person, Task],Base).get_session()
