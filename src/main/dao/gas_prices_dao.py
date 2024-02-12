from main.model.sqlite_tables_models import  Session,GasStation

class GasPriceDao:
    @staticmethod
    def get_all_gas_prices():
        session = Session()
        gas_prices = session.query(GasStation).all()
        session.close()
        return gas_prices

    @classmethod
    def add_gas_price(cls, _id, name, lat, lng, gas, diesel):
        session = Session()
        new_gas_station = GasStation(name=name, latitude=lat, longitude=lng, gas_price=gas, diesel_price=diesel)
        session.add(new_gas_station)
        session.commit()
        session.close()

    @classmethod
    def delete_all_gas_prices(cls):
        session = Session()
        session.query(GasStation).delete()
        session.commit()
        session.close()