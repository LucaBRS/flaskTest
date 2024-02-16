from main.model.gas_station_model import GasStation
from main.config.sessions_configuration import sqlite_session


class GasPriceDao:

    @classmethod
    def get_all_gas_prices(cls):
        session = sqlite_session
        gas_prices = session.query(GasStation).all()
        session.close()
        return gas_prices

    @classmethod
    def add_gas_price(cls, _id, name, lat, lng, gas, diesel):
        session = sqlite_session

        new_gas_station = GasStation(name=name, latitude=lat, longitude=lng, gas_price=gas, diesel_price=diesel)

        session.add(new_gas_station)
        session.commit()
        session.close()

    @classmethod
    def delete_all_gas_prices(cls):
        session = sqlite_session

        session.query(GasStation).delete()
        session.commit()
        session.close()
