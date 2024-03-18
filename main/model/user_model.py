from datetime import datetime

from flask_login import UserMixin

from sqlalchemy import String, Column, Integer, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base, backref
from main.model.userRole_model import UserRole
from main.model.base_auth import Base


class User(UserMixin, Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    first_name = Column(String(80))
    password = Column(String(80), nullable=False)

    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())
    fs_uniquifier = Column(String(64), unique=True, nullable=False)
    confirmed_at = Column(DateTime())

    roles = relationship('Role', secondary='user_role',
                         backref=backref('users', lazy='dynamic'))
