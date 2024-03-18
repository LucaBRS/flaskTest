from datetime import datetime

from sqlalchemy import DateTime,  String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import declarative_base

from main.model.base import Base


class Person(Base):
    __tablename__ = 'person'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    surname: Mapped[str] = mapped_column(String(30), nullable=False)

    # Define the many-to-many relationship with TaskModule
    task_id: Mapped['int'] = mapped_column(Integer)

    date_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Person id=%r, name='%s', surname='%s'>" % (self.id, self.name, self.surname)
