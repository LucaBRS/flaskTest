# todo pytest ()
# todo transazioni di sqlalchemy e COME GESTIRLE se sono aouto commit (pernsare di creare un decorator transactional e wrapper con rallback) apertura a lviello service
# todo vedere come aggiungiere openAPI (censire endpoint) e file yml dove esporre serv. REST  # todo SISTEMARE END-POINT IN MODO DA IMPORTARLI DA ESTERNO
# TODO separare le classi (tavole) trovare soluzione per eriditare da Base IMPORTANTE
# TODO alembic (migrazioni) (importante vedere per i roll back e capire le versioni...)
# todo docker per la chiamate al gov

import logging

from flask_login import LoginManager

# ùù if u do not specify the log file name, it will print on the console!!
logging.basicConfig(filename='', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s - [%(name)s] %(levelname)s %(message)s')
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


import toml
from flask import Flask
from main.blueprint.todo_list_routing import todo_list_bp
from main.blueprint.auth import auth_bp,login_manager

config = toml.load('config.toml')

# l+ creating a Flask application instance named app __name__ parameter is a special variable that represents the name of the current module
app = Flask(__name__)

app.template_folder = config['flask']["template_folder"]
app.static_folder = config['flask']["static_folder"]
app.instance_path = config['flask']["instance_path"]

app.config['SECRET_KEY'] = 'dsfsgdfvdfgh'  # never share!
#


# ll here search for the primary key automatically!

app.register_blueprint(todo_list_bp, url_prefix="/")
app.register_blueprint(auth_bp, url_prefix="/")

login_manager.init_app(app)  # ll tell log in manager which app we are using!

if __name__ == '__main__':
    app.run(debug=True)
