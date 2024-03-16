import logging

from flask import Blueprint, render_template, request, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from main.config.sessions_configuration import sqlite_session_user
from main.model.user_model import User
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from flask_authorize import Authorize

from main.model.permission_model import Permission

auth_bp = Blueprint('auth', __name__)
logger = logging.getLogger(__name__)

session_user = sqlite_session_user

ROLES_PERMISSIONS = {
    'admin': ['create_task', 'modify_task', 'delete_task'],
    'user': ['create_task']
}


login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # where u should redirect if the no user is not logged in


@login_manager.user_loader  # ll this tell flask how we load user and what user we are looking for
def load_user(user_id):
    return session_user.query(User).get(int(user_id))


@auth_bp.route('/update-user', methods=['GET', 'POST'])
@login_required
def update_users():
    if request.method == 'POST':
        if current_user.role != 'admin':
            flash('you are not an admin', category='error')
            return redirect(url_for('auth.update_user'))
        update_user_id = request.form.get('update_user')
        update_user: User = session_user.query(User).get(int(update_user_id))
        if not update_user:
            flash('User not found.', category='error')
            return redirect(url_for('auth.update_user'))
        else:
            update_user.first_name = request.form.get(f'first_name_{update_user_id}')
            update_user.password = generate_password_hash(request.form.get(f'password_{update_user_id}'),
                                                          method='sha256')
            update_user.role = request.form.get(f'role_{update_user_id}')
            session_user.commit()
            flash('User updated!', category='success')

    users = session_user.query(User).all()
    return render_template('update_user.html', users=users, user=current_user)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    logger.debug("Inside login")
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = session_user.query(User).filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                logger.debug('Logged in successfully!')
                login_user(user, remember=True)
                return redirect(url_for('todo_list_bp.get_task_index'))
            else:
                flash('incorrect password,try again', category='error')
        else:
            flash('email does not exist', category='error')

    return render_template('login.html', user=current_user)


@auth_bp.route('/logout')
@login_required  # decorator that does not able you to log out if u are not log in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth_bp.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    logger.debug("Inside sign_up")
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = session_user.query(User).filter_by(email=email).first()
        if user:
            flash('already registered', category='error')

        elif len(email) < 4:
            flash('email must be grater then 4 characters',
                  category='error')  # built in of flask, this wil flash in case the email is less then 4 char and
            # the category will tell if is success or error its just a name but have to be meaningfull
        elif len(first_name) < 2:
            flash('first name must be grater then 3 characters',
                  category='error')
            pass
        elif password1 != password2:
            flash('password dont match',
                  category='error')
            pass
        elif len(password1) < 7:
            flash('password must be grater then 7 characters',
                  category='error')
            pass
        else:
            # add user to db
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password1, method='sha256'))
            session_user.add(new_user)
            session_user.commit()
            flash('Account created!', category='success')
            logger.debug('Account created!')
            return redirect(url_for('todo_list_bp.get_task_index'))

    return render_template('sign_up.html', user=current_user)
