# todo pytest ()
# todo transazioni di sqlalchemy
# todo vedere come aggiungiere openAPI

import logging
import toml
from flask import Flask, render_template, url_for, request, redirect

#l+ SQLAlchemy provides a set of tools and utilities for working with databases from flask_sqlalchemy import SQLAlchemy from datetime import datetime
from src.main.model.task_model import db, TaskModule  # Import db from the model module
from src.main.controller.task_controller import TaskController

config = toml.load('config.toml')

#l+ creating a Flask application instance named app __name__ parameter is a special variable that represents the name of the current module
app = Flask(__name__)
app.template_folder = config['flask']["template_folder"]
app.static_folder = config['flask']["static_folder"]
app.instance_path=config['flask']["instance_path"]
#l+ configuring Flask application to use a SQLite database named task.db app.config: This is a dictionary-like object provided by Flask to store configuration settings for your application ['SQLALCHEMY_DATABASE_URI']: This accesses a specific configuration option within the app.config dictionary 'sqlite:///task.db': This is the database URI that specifies the connection details for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = config['flask']["database_uri"]
#l+  explicitly associate the db instance with your Flask application by calling db.init_app(app). This allows Flask-SQLAlchemy to work within the context of your Flask application.
db.init_app(app)
logging.basicConfig(level=logging.DEBUG)
logger = app.logger

@app.route('/', methods=['GET'])
def get_task_index():
    return TaskController.get_tasks()

@app.route('/', methods=['POST'])
def add_task_index():
    return TaskController.post_task()


@app.route('/delete/<int:id>')
def delete_index(id):
    return TaskController.delete_task(id)

@app.route('/update/<int:id>',methods=['GET'])
def get_update_task_index(id):
    return TaskController.get_update_task(id)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    return TaskController.post_update_task(id)



if __name__ == '__main__':
    app.run(debug=True)
