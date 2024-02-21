# todo pytest ()
# todo transazioni di sqlalchemy e COME GESTIRLE se sono aouto commit (pernsare di creare un decorator transactional e wrapper con rallback) apertura a lviello service
# todo vedere come aggiungiere openAPI (censire endpoint) e file yml dove esporre serv. REST  # todo SISTEMARE END-POINT IN MODO DA IMPORTARLI DA ESTERNO
# TODO separare le classi (tavole) trovare soluzione per eriditare da Base IMPORTANTE
# TODO alembic (migrazioni) (importante vedere per i roll back e capire le versioni...)
# todo docker per la chiamate al gov

import logging

# ùù if u do not specify the log file name, it will print on the console!!
logging.basicConfig(filename='', encoding='utf-8', level=logging.DEBUG,format='%(asctime)s - [%(name)s] %(levelname)s %(message)s')
# formatter = logging.Formatter('%(asctime)s - [%(name)s] %(levelname)s %(message)s')
#
# # Get the root logger
# root_logger = logging.getLogger()
#
# #  StreamHandler for logging to console
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEBUG)  #  log level for console output
# console_handler.setFormatter(formatter)  #  formatter for console output
#
# # console handler to the root logger
# root_logger.addHandler(console_handler)


import os

import toml
from flask import Flask

from main.controller.gas_prices_controller import GasPricesController
from main.controller.task_controller import TaskController

current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir, '..', '..', 'config.toml')
config = toml.load(config_file_path)

# l+ creating a Flask application instance named app __name__ parameter is a special variable that represents the name of the current module
app = Flask(__name__)

app.template_folder = config['flask']["template_folder"]
app.static_folder = config['flask']["static_folder"]
app.instance_path = config['flask']["instance_path"]


@app.route('/', methods=['GET'])
def get_task_index():
    gas_prices = GasPricesController().get_all_gas_prices()
    return TaskController().get_tasks(gas_prices)


@app.route('/', methods=['POST'])
def add_task_index():
    return TaskController().post_task()


@app.route('/delete/<int:id>')
def delete_index(id):
    return TaskController().delete_task(id)


@app.route('/update/<int:id>', methods=['GET'])
def get_update_task_index(id):
    return TaskController().get_update_task(id)


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    return TaskController().post_update_task(id)


@app.route('/gas_prices', methods=['POST'])
def post_gas_prices_index():
    return GasPricesController().post_gas_prices()


@app.route('/delete_all_gas_prices', methods=['GET'])
def delete_all_gas_prices():
    return GasPricesController().delete_all_gas_prices()


if __name__ == '__main__':
    app.run(debug=True)
