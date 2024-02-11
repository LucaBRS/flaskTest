from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# This creates an instance of the SQLAlchemy class and binds it to your Flask application (app)
db = SQLAlchemy()


class TaskModule(db.Model):
    __bind_key__ = "sqlite_task"
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    # this is going to be set automatically!
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    # This method defines how instances of the T odo class are represented as strings when printed or converted to a string
    def __repr__(self):
        return "<Task %r>" % self.id


class Person(db.Model):
    __bind_key__ = "sqlite_person"
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    # this is going to be set automatically!
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return "<Task %r>" % self.id


class GasStation(db.Model):
    __bind_key__ = "sqlite_gas_station"
    __tablename__ = 'gas_station'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    gas_price = db.Column(db.Float, nullable=False)
    diesel_price = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return "<Task %r>" % self.id