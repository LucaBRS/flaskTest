from main.model.gas_station_model import GasStation
from sqlalchemy.orm import Session

class GasPriceDao:
    def __init__(self, session):
        self.session = session

    def get_all_gas_prices(self):
        gas_prices = self.session.query(GasStation).all()
        self.session.close()
        return gas_prices

    def add_gas_price(self, _id, name, lat, lng, gas, diesel):
        new_gas_station = GasStation(name=name, latitude=lat, longitude=lng, gas_price=gas, diesel_price=diesel)
        self.session.add(new_gas_station)
        self.session.commit()
        self.session.close()

    def delete_all_gas_prices(self):
        self.session.query(GasStation).delete()
        self.session.commit()
        self.session.close()
