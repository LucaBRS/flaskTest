from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String(200))
    date_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def __init__(self, content: str):
        self.content = str(content)

    def __repr__(self):
        return "<Task %r>" % self.id
