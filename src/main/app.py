# todo pytest ()
# todo transazioni di sqlalchemy e COME GESTIRLE se sono aouto commit (pernsare di creare un decorator transactional e wrapper con rallback) apertura a lviello service
# todo vedere come aggiungiere openAPI (censire endpoint) e file yml dove esporre serv. REST  # todo SISTEMARE END-POINT IN MODO DA IMPORTARLI DA ESTERNO
# TODO separare le classi (tavole) trovare soluzione per eriditare da Base IMPORTANTE
# TODO alembic (migrazioni) (importante vedere per i roll back e capire le versioni...)
# todo docker per la chiamate al gov

import logging

import toml
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main.controller.gas_prices_controller import GasPricesController
from main.controller.task_controller import TaskController
from main.model.sqlite_tables_models import Base

# l+ SQLAlchemy provides a set of tools and utilities for working with databases from flask_sqlalchemy import  SQLAlchemy from datetime import datetime



config = toml.load('src/main/config/config.toml')

# l+ creating a Flask application instance named app __name__ parameter is a special variable that represents the name of the current module
app = Flask(__name__)
app.template_folder = config['flask']["template_folder"]
app.static_folder = config['flask']["static_folder"]
app.instance_path = config['flask']["instance_path"]
# l+ configuring Flask application to use a SQLite database named task.db app.config: This is a dictionary-like object provided by Flask to store configuration settings for your application ['SQLALCHEMY_DATABASE_URI']: This accesses a specific configuration option within the app.config dictionary 'sqlite:///task.db': This is the database URI that specifies the connection details for the SQLite database


# l+  explicitly associate the db instance with your Flask application by calling db.init_app(app). This allows Flask-SQLAlchemy to work within the context of your Flask application.
logging.basicConfig(level=logging.DEBUG)
logger = app.logger


@app.route('/', methods=['GET'])
def get_task_index():
    gas_prices = GasPricesController.get_all_gas_prices()
    return TaskController.get_tasks(gas_prices)


@app.route('/', methods=['POST'])
def add_task_index():
    return TaskController.post_task()


@app.route('/delete/<int:id>')
def delete_index(id):
    return TaskController.delete_task(id)


@app.route('/update/<int:id>', methods=['GET'])
def get_update_task_index(id):
    return TaskController.get_update_task(id)


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    return TaskController.post_update_task(id)


# @app.route('/', methods=['GET'])
# def get_all_gas_prices():
#     return GasPricesController.get_all_gas_prices()


@app.route('/gas_prices', methods=['POST'])
def post_gas_prices_index():
    return GasPricesController.post_gas_prices()

@app.route('/delete_all_gas_prices', methods=['GET'])
def delete_all_gas_prices():
    return GasPricesController.delete_all_gas_prices()

if __name__ == '__main__':
    app.run(debug=True)
