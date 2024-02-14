# import logging
# from datetime import datetime
#
# import toml
# from sqlalchemy import ForeignKey, Column, Integer, DateTime, Float, create_engine, String
# from sqlalchemy.orm import Mapped, mapped_column
#
# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy.orm import relationship
#
# config = toml.load('../main/config/config.toml')
#
# logger = logging.getLogger(__name__)
#
# Base = declarative_base()
#
#
# class TaskModule(Base):
#     __tablename__ = 'task'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     content: Mapped[str] = mapped_column(String(200))
#     date_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#
#     def __init__(self, content: str):
#         self.content = str(content)
#
#     def __repr__(self):
#         return "<Task %r>" % self.id
#
#
# class Person(Base):
#     __tablename__ = 'person'
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30), nullable=False)
#     surname: Mapped[str] = mapped_column(String(30), nullable=False)
#
#     # Define the many-to-many relationship with TaskModule
#     task_id: Mapped['int'] = mapped_column(Integer)
#
#     date_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return "<Person id=%r, name='%s', surname='%s'>" % (self.id, self.name, self.surname)
#
#
# class GasStation(Base):
#     __tablename__ = 'gas_station'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30), nullable=False)
#     latitude: Mapped[float] = mapped_column(Float, nullable=False)
#     longitude: Mapped[float] = mapped_column(Float, nullable=False)
#     gas_price: Mapped[float] = mapped_column(Float, nullable=False)
#     diesel_price: Mapped[float] = mapped_column(Float, nullable=False)
#     date_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return f"<GasStation {self.id}>"
#
#
# logger.debug(config['flask']['sql_lite_database_uri'])
# engine = create_engine(config['flask']['sql_lite_database_uri'])
# Base.metadata.create_all(bind=engine)
#
# Session_sqlite = sessionmaker(bind=engine)
