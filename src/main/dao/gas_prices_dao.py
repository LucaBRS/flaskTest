from main.model.sqlite_tables_models import GasStation, db


class GasPriceDao:

    @staticmethod
    def get_all_gas_prices():
        return GasStation.query.all()

    @classmethod
    def add_gas_price(cls, _id, name, lat, lng, gas, diesel):
        new_gas_station = GasStation(name=name, latitude=lat, longitude=lng, gas_price=gas, diesel_price=diesel)
        db.session.add(new_gas_station)
        db.session.commit()

    @classmethod
    def delete_all_gas_prices(cls):
        db.session.query(GasStation).delete()
        db.session.commit()
