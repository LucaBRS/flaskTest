from datetime import datetime

from flask_login import UserMixin

from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship, declarative_base
from main.model.userRole_model import UserRole
from main.model.base_auth import Base



class User(UserMixin, Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    first_name = Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)
    roles = relationship('Role',secondary=UserRole)
