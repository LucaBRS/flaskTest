# import logging
# from flask import redirect, url_for, request, Blueprint, session, render_template, flash
# from functools import wraps
#
# logger = logging.getLogger(__name__)
#
#
# # Define roles
# ROLES = {
#     'admin': ['admin'],
#     'user': ['user']
# }
#
# #  decorator
# def role_required(required_roles):
#     def decorator(view_func):
#         @wraps(view_func)
#         def wrapper(*args, **kwargs):
#             logger.debug('inside role required wrapper!')
#             #  user role from your user management system
#             user_role = get_user_role(request)
#             if user_role in required_roles:
#                 return view_func(*args, **kwargs)
#             else:
#                 # Handle unauthorized access here (e.g., redirect to login)
#                 return redirect(url_for('login.login'))#ll here goes the blueprint name plus the routing
#         return wrapper
#     return decorator
#
# # Mock function  (need to replace with actual implementation ?????)
# def get_user_role(request):
#     # Retrieve user role from request (e.g., session, token, database)
#     #  mock user role
#     return 'user'
#
# #  Blueprint for login routes
# login_bp = Blueprint('login', __name__)
#
#
# # Example views within login Blueprint
# @login_bp.route('/admin', methods=['GET'])
# @role_required(ROLES['admin'])
# def admin_panel():
#     return 'Admin Panel'
#
# @login_bp.route('/user', methods=['GET'])
# @role_required(ROLES['user'])
# def user_dashboard():
#     return 'User Dashboard'
#
#
#
# @login_bp.route('/login', methods=['GET'])
# def show_login_form():
#     # Render the login page
#     return render_template('login.html')
#
#
# @login_bp.route('/login', methods=['POST'])
# def login():
#     username = request.form.get('username')
#     password = request.form.get('password')
#     if username == 'admin' and password == 'admin':
#         logger.debug(username + ' is logged in')
#         session['logged_in'] = True
#         session['username'] = username
#         session['role'] = 'admin'  # Set the role upon successful login
#         return redirect(url_for('login.admin_panel'))  # Redirect to admin panel upon login
#     elif username == 'user' and password == 'user':
#         logger.debug(username + ' is logged in')
#         session['logged_in'] = True
#         session['username'] = username
#         session['role'] = 'user'  # Set the role upon successful login
#         return redirect(url_for('login.user_dashboard'))  # Redirect to user dashboard upon login
#     else:
#         flash('Invalid username or password', 'error')
#         return render_template('login.html')