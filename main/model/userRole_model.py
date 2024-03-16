from sqlalchemy import Column, Integer, ForeignKey, Table

from main.model.base_auth import Base

UserRole = Table('user_role', Base.metadata, Column('user_id', ForeignKey('user.id'), primary_key=True),
                 Column('role_id', ForeignKey('role.id'), primary_key=True)
                 )

# class UserRole(Base):
#     __tablename__ = 'user_role'
#
#     user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
#     role_id = Column(Integer, ForeignKey('role.id'), primary_key=True)
#
#     # Define relationships with User and Role
#     user = relationship('User', back_populates='roles')
#     role = relationship('Role', back_populates='users')
#
#
# User.roles = relationship('UserRole', back_populates='user')
# Role.users = relationship('UserRole', back_populates='role')
