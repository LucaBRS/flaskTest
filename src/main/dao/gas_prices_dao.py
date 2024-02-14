from main.config.sqllite_config import  Session_sqlite
from main.model.gas_station_model import GasStation

class GasPriceDao:
    @staticmethod
    def get_all_gas_prices():
        session = Session_sqlite()
        gas_prices = session.query(GasStation).all()
        session.close()
        return gas_prices

    @classmethod
    def add_gas_price(cls, _id, name, lat, lng, gas, diesel):
        session = Session_sqlite()
        new_gas_station = GasStation(name=name, latitude=lat, longitude=lng, gas_price=gas, diesel_price=diesel)
        session.add(new_gas_station)
        session.commit()
        session.close()

    @classmethod
    def delete_all_gas_prices(cls):
        session = Session_sqlite()
        session.query(GasStation).delete()
        session.commit()
        session.close()