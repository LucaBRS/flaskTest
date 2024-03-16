from flask_authorize import PermissionsMixin
from main.model.base_auth import Base

class Permission(Base, PermissionsMixin):
    __permissions__ = {
        'admin': ['read', 'update', 'delete','add'],
        'normal': ['read', 'update','delete'],
        'read_only': ['read']
    }