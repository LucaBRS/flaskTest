import logging

from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_security import hash_password, Security, SQLAlchemySessionUserDatastore, roles_required, auth_required, \
    permissions_accepted
from werkzeug.security import generate_password_hash, check_password_hash

from main.config.sessions_configuration import sqlite_session_user
from main.model.user_model import User
from main.model.role_model import Role
from flask_login import login_user, logout_user, login_required, current_user, LoginManager

# from model import user_model

auth_bp = Blueprint('auth', __name__)
logger = logging.getLogger(__name__)

session_user = sqlite_session_user

login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # where u should redirect if no user is not logged in
user_datastore = SQLAlchemySessionUserDatastore(session_user, User, Role)
security = Security(datastore=user_datastore)



@login_manager.user_loader  # ll this tell flask how we load user and what user we are looking for
def load_user(user_id):
    logger.debug("Loading user {}".format(user_id))
    return security.datastore.find_user(id=user_id)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = security.datastore.find_user(email=email)

        if user.password == password:
            # Assuming you have a method to check password
            login_user(user, remember=True)
            user_datastore.commit()
            return redirect(url_for('auth.dashboard'))  # Redirect to dashboard or wherever you want
        else:
            error = 'Invalid username or password'
            logger.warning(error)
            return render_template('login_test.html', error=error)
    return render_template('login_test.html')


@auth_bp.route('/dashboard', methods=['GET'])
@login_required
@permissions_accepted('user-read')
def dashboard():
    return render_template('dashboard.html')


# @auth_bp.route('/login', methods=['GET', 'POST'])
# def login():
#     logger.debug("Inside login")
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')
#         user = session_user.query(User).filter_by(email=email).first()
#         if user:
#             if check_password_hash(user.password, password):
#                 flash('Logged in successfully!', category='success')
#                 logger.debug('Logged in successfully!')
#                 login_user(user, remember=True)
#                 return redirect(url_for('todo_list_bp.get_task_index'))
#             else:
#                 flash('incorrect password,try again', category='error')
#         else:
#             flash('email does not exist', category='error')
#
#     return render_template('login.html', user=current_user)
#
#
# @auth_bp.route('/logout')
# @login_required  # decorator that does not able you to log out if u are not log in
# def logout():
#     logout_user()
#     return redirect(url_for('auth.login'))

#
# @auth_bp.route('/sign-up', methods=['GET', 'POST'])
# def sign_up():
#     logger.debug("Inside sign_up")
#     if request.method == 'POST':
#         email = request.form.get('email')
#         first_name = request.form.get('firstName')
#         password1 = request.form.get('password1')
#         password2 = request.form.get('password2')
#
#         user = session_user.query(User).filter_by(email=email).first()
#         if user:
#             flash('already registered', category='error')
#
#         elif len(email) < 4:
#             flash('email must be grater then 4 characters',
#                   category='error')  # built in of flask, this wil flash in case the email is less then 4 char and
#             # the category will tell if is success or error its just a name but have to be meaningfull
#         elif len(first_name) < 2:
#             flash('first name must be grater then 3 characters',
#                   category='error')
#             pass
#         elif password1 != password2:
#             flash('password dont match',
#                   category='error')
#             pass
#         elif len(password1) < 7:
#             flash('password must be grater then 7 characters',
#                   category='error')
#             pass
#         else:
#             # add user to db
#             new_user = User(email=email, first_name=first_name,
#                             password=generate_password_hash(password1, method='sha256'))
#             session_user.add(new_user)
#             session_user.commit()
#             flash('Account created!', category='success')
#             logger.debug('Account created!')
#             return redirect(url_for('todo_list_bp.get_task_index'))
#
#     return render_template('sign_up.html', user=current_user)
#
#
# @auth_bp.route('/update-user', methods=['GET', 'POST'])
# @login_required
# def update_users():
#     if request.method == 'POST':
#         if current_user.role != 'admin':
#             flash('you are not an admin', category='error')
#             return redirect(url_for('auth.update_user'))
#         update_user_id = request.form.get('update_user')
#         update_user: User = session_user.query(User).get(int(update_user_id))
#         if not update_user:
#             flash('User not found.', category='error')
#             return redirect(url_for('auth.update_user'))
#         else:
#             update_user.first_name = request.form.get(f'first_name_{update_user_id}')
#             update_user.password = generate_password_hash(request.form.get(f'password_{update_user_id}'),
#                                                           method='sha256')
#             update_user.role = request.form.get(f'role_{update_user_id}')
#             session_user.commit()
#             flash('User updated!', category='success')
#
#     users = session_user.query(User).all()
#     return render_template('update_user.html', users=users, user=current_user)
#
# # one time setup
#
#
# Login route and view function

@auth_bp.route('/modify_users')
@login_required
@roles_required('admin_modify')
def modify_users():
    # Retrieve all users from the database
    all_users = User.query.all()
    return render_template('modify_users.html', users=all_users)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if the username or email already exists
        existing_user = security.datastore.find_user(username=username) or user_datastore.find_user(email=email)
        if existing_user:
            error = 'Username or email already exists. Please choose another.'
            return render_template('signup_test.html', error=error)

        # Create a new user and add the "user" role to them
        new_user = user_datastore.create_user(username=username, email=email, password=hash_password(password))
        user_datastore.add_role_to_user(new_user, "user")

        # Commit changes to the database
        user_datastore.commit()

        # Log in the new user
        login_user(new_user)

        # Redirect to the dashboard or any other page
        return redirect(url_for('dashboard'))

    return render_template('signup_test.html')
