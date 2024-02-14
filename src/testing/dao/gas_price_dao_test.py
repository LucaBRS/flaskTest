import unittest

import pytest

from main.dao.gas_prices_dao import GasPriceDao, Session
from main.model.gas_station_model import GasStation

test_gas_station = {
    'name': 'Test Gas Station',
    'latitude': 0.0,
    'longitude': 0.0,
    'gas_price': 1.0,
    'diesel_price': 2.0
}


class GasPriceDaoTest(unittest.TestCase):

    def test_get_all_gas_prices(self):
        test_station = GasStation(**test_gas_station)
        Session.add(test_station)

        gas_stations = GasPriceDao.get_all_gas_prices()

        assert len(gas_stations) == 1
        assert gas_stations[0].name == 'Test Gas Station'


    def test_add_gas_price(self):
        GasPriceDao.add_gas_price(**test_gas_station)

        gas_station = Session.query(GasStation).filter_by(name='Test Gas Station').first()

        assert gas_station is not None
        assert gas_station.latitude == 0.0

    def test_delete_all_gas_prices(self):
        test_station = GasStation(**test_gas_station)
        Session.add(test_station)
        Session.commit()

        GasPriceDao.delete_all_gas_prices()

        gas_stations = Session.query(GasStation).all()
        assert len(gas_stations) == 0
