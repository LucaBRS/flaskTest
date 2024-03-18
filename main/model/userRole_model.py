from sqlalchemy import Column, Integer, ForeignKey, Table

from main.model.base_auth import Base


# UserRole = Table('user_role', Base.metadata, Column('user_id', ForeignKey('user.id'), primary_key=True),
#                  Column('role_id', ForeignKey('role.id'), primary_key=True)
#                  )

class UserRole(Base):
    __tablename__ = 'user_role'

    id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('user.id'))
    role_id = Column('role_id', Integer(), ForeignKey('role.id'))
