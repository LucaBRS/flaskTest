from unittest.mock import Mock

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main.dao.gas_prices_dao import GasPriceDao
from main.model.gas_station_model import GasStation

mock_engine = create_engine("sqlite:///:memory:")
MockSession = sessionmaker(bind=mock_engine)()
mock_session = Mock(spec=MockSession)


@pytest.fixture
def mock_session():
    return mock_session


@pytest.fixture
def gas_price_dao(mock_session):
    return GasPriceDao(mock_session)


def test_get_all_gas_prices(mock_session, gas_price_dao):
    mock_session.query.return_value.all.return_value = [
        GasStation(id=1, name="Station 1", latitude=0, longitude=0, gas_price=2.5, diesel_price=2.0)
    ]

    gas_prices = gas_price_dao.get_all_gas_prices()

    assert len(gas_prices) == 1
    assert isinstance(gas_prices[0], GasStation)
    assert gas_prices[0].id == 1
    assert gas_prices[0].name == "Station 1"
    assert gas_prices[0].latitude == 0
    assert gas_prices[0].longitude == 0
    assert gas_prices[0].gas_price == 2.5
    assert gas_prices[0].diesel_price == 2.0
