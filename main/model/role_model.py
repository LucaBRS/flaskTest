from flask_authorize import AllowancesMixin
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

from main.model.base_auth import Base


class Role(Base, AllowancesMixin):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    user = relationship('UserRole', back_populates='role')
