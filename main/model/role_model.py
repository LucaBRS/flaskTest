from flask_security import RoleMixin, AsaList
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import declarative_base, relationship

from main.model.base_auth import Base_Auth


class Role(Base_Auth, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255))

    permissions = Column(MutableList.as_mutable(AsaList()), nullable=True)
