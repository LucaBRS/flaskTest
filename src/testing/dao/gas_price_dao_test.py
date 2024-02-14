import unittest

import pytest

from main.dao.gas_prices_dao import GasPriceDao
from model.sqlite_tables_models import Session_sqlite, GasStation

test_gas_station = {
    'name': 'Test Gas Station',
    'latitude': 0.0,
    'longitude': 0.0,
    'gas_price': 1.0,
    'diesel_price': 2.0
}

class GasPriceDaoTest(unittest.TestCase):


    # Fixture to set up and tear down the test database
    @pytest.fixture
    def setup_teardown_test_db(self):
        session = Session_sqlite()
        yield session
        session.close()

    # Test case for get_all_gas_prices method
    def test_get_all_gas_prices(self,setup_teardown_test_db):
        # Add test data
        test_station = GasStation(**test_gas_station)
        setup_teardown_test_db.add(test_station)
        setup_teardown_test_db.commit()

        # Call the method to be tested
        gas_stations = GasPriceDao.get_all_gas_prices()

        # Assert the result
        assert len(gas_stations) == 1
        assert gas_stations[0].name == 'Test Gas Station'

    # Test case for add_gas_price method
    def test_add_gas_price(self,setup_teardown_test_db):
        # Call the method to add test data
        GasPriceDao.add_gas_price(**test_gas_station)

        # Retrieve the added data from the test database
        gas_station = setup_teardown_test_db.query(GasStation).filter_by(name='Test Gas Station').first()

        # Assert the result
        assert gas_station is not None
        assert gas_station.latitude == 0.0

    # Test case for delete_all_gas_prices method
    def test_delete_all_gas_prices(self,setup_teardown_test_db):
        # Add test data to the test database
        test_station = GasStation(**test_gas_station)
        setup_teardown_test_db.add(test_station)
        setup_teardown_test_db.commit()

        # Call the method to be tested
        GasPriceDao.delete_all_gas_prices()

        # Retrieve data from the test database and assert that it has been deleted
        gas_stations = setup_teardown_test_db.query(GasStation).all()
        assert len(gas_stations) == 0