from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TaskModule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    #this is going to be set automatically!
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

# This method defines how instances of the T odo class are represented as strings when printed or converted to a string
    def __repr__(self):
        return "<Task %r>" % self.id