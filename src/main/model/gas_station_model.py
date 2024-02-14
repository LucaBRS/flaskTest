from datetime import datetime

from sqlite_tables_models import Base
from sqlalchemy import ForeignKey, Column, Integer, DateTime, Float, create_engine, String
from sqlalchemy.orm import Mapped, mapped_column


class GasStation1(Base):
    __tablename__ = 'gas_station1'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    gas_price: Mapped[float] = mapped_column(Float, nullable=False)
    diesel_price: Mapped[float] = mapped_column(Float, nullable=False)
    date_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<GasStation {self.id}>"
