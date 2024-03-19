# todo pytest ()
# todo transazioni di sqlalchemy e COME GESTIRLE se sono aouto commit (pernsare di creare un decorator transactional e wrapper con rallback) apertura a lviello service
# todo vedere come aggiungiere openAPI (censire endpoint) e file yml dove esporre serv. REST  # todo SISTEMARE END-POINT IN MODO DA IMPORTARLI DA ESTERNO
# TODO separare le classi (tavole) trovare soluzione per eriditare da Base IMPORTANTE
# TODO alembic (migrazioni) (importante vedere per i roll back e capire le versioni...)
# todo docker per la chiamate al gov

import logging
import os

from flask_login import LoginManager
from flask_security import hash_password

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
# from main.blueprint.todo_list_routing import todo_list_bp
from main.blueprint.auth import auth_bp,login_manager,security,session_user

config = toml.load('config.toml')

# l+ creating a Flask application instance named app __name__ parameter is a special variable that represents the name of the current module
app = Flask(__name__)

app.template_folder = config['flask']["template_folder"]
app.static_folder = config['flask']["static_folder"]
app.instance_path = config['flask']["instance_path"]

# Generate a nice key using secrets.token_urlsafe()
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", 'pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw')
# Bcrypt is set as default SECURITY_PASSWORD_HASH, which requires a salt
# Generate a good salt using: secrets.SystemRandom().getrandbits(128)
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT", '146585145368132386173505678016728509634')
# Don't worry if email has findable domain
app.config["SECURITY_EMAIL_VALIDATOR_ARGS"] = {"check_deliverability": False}


# ll here search for the primary key automatically!

# app.register_blueprint(todo_list_bp, url_prefix="/")
app.register_blueprint(auth_bp, url_prefix="/")

login_manager.init_app(app)  # ll tell log in manager which app we are using!
security.init_app(app)

app.security = security


# one time setup
# with app.app_context():
#
#     # Create a user and role to test with
#     app.security.datastore.find_or_create_role(
#         name="admin", permissions={"user-read", "user-write", "admin_modify"}
#     )
#     session_user.commit()
#     if not app.security.datastore.find_user(email="admin@me.com"):
#         app.security.datastore.create_user(email="admin@me.com",
#         password=hash_password("admin"), roles=["admin"])
#     session_user.commit()


if __name__ == '__main__':
    app.run(debug=True)
