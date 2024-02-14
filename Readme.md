# LUCA BARSOTTINI

## Solutions to problems:
- Run `pip list --format=freeze > requirements.txt` to avoid the weird output of "pip freeze".
- When installing the database:
  - Start Python, then run `from app import app`. Since you need to work within the application context, use `with app.app_context():` and perform other operations inside it.
- If you change the name of the database model, you should track these changes in the database. You can either delete and recreate it or rename it (follow the steps mentioned above).
- To separate the database, it's best to initialize it.
- FOR DOCKER: If you put the volume in the docker-compose.yml file, the ./app directory from your host machine will be mounted into the /app directory. Therefore, if you have a COPY command in the Dockerfile to the same directory, everything will be overwritten.

## Problems or Todos
- Structure the project into "modules": model, DAO, service (or business logic), controller (or route), utils, config.


`main/
|-- config/
|   |-- config.toml
|-- dao/
|   |-- __init__.py
|   |-- task_dao.py
|   |-- person_dao.py
|   |-- gas_station_dao.py
|-- model/
|   |-- __init__.py
|   |-- task_module.py
|   |-- person.py
|   |-- gas_station.py
|-- service/
|   |-- __init__.py
|   |-- task_service.py
|   |-- person_service.py
|   |-- gas_station_service.py
|-- controller/
|   |-- __init__.py
|   |-- gas_prices_controller.py
|   |-- task_controller.py
|-- app.py`