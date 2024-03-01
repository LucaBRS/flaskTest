import logging
from functools import wraps

from flask import Blueprint, abort, redirect, url_for
from flask_login import login_required,current_user
from sqlalchemy import Null

from main.controller.gas_prices_controller import GasPricesController
from main.controller.task_controller import TaskController

logger = logging.getLogger(__name__)

todo_list_bp = Blueprint('todo_list_bp', __name__)

def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.is_authenticated:
                if role == 'viewer':
                    if current_user.role in ['viewer', 'maintainer', 'admin']:
                        return func(*args, **kwargs)
                elif role == 'maintainer':
                    if current_user.role in ['maintainer', 'admin']:
                        return func(*args, **kwargs)
                elif role == 'admin':
                    if current_user.role == 'admin':
                        return func(*args, **kwargs)
                # If the user's role does not match the required role, handle accordingly
                abort(403)  # Forbidden
            else:
                abort(401)  # Unauthorized
        return wrapper
    return decorator

@todo_list_bp.route('/', methods=['GET'])
@login_required
@role_required('viewer')
def get_task_index():
    username = current_user
    # gas_prices = GasPricesController().get_all_gas_prices()
    gas_prices = Null
    return TaskController().get_tasks(gas_prices)


@todo_list_bp.route('/', methods=['POST'])
@login_required
@role_required('maintainer')
def add_task_index():
    return TaskController().post_task()


@todo_list_bp.route('/delete/<int:id>')
@login_required
@role_required('maintainer')
def delete_index(id):
    return TaskController().delete_task(id)


@todo_list_bp.route('/update/<int:id>', methods=['GET'])
@login_required
@role_required('maintainer')
def get_update_task_index(id):
    return TaskController().get_update_task(id)


@todo_list_bp.route('/update/<int:id>', methods=['POST'])
@login_required
@role_required('maintainer')
def update(id):
    return TaskController().post_update_task(id)

# @todo_list_bp.route('/gas_prices', methods=['POST'])
# def post_gas_prices_index():
#     return GasPricesController().post_gas_prices()


# @todo_list_bp.route('/delete_all_gas_prices', methods=['GET'])
# def delete_all_gas_prices():
#     return GasPricesController().delete_all_gas_prices()


