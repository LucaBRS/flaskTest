import json
import logging

from flask import redirect
from sqlalchemy.orm import Session

from main.dao.gas_prices_dao import GasPriceDao

logger = logging.getLogger(__name__)


class GasPriceService:

    @classmethod
    def get_all_gas_prices(cls):
        return GasPriceDao.get_all_gas_prices()

    @classmethod
    def post_gas_prices(cls, contents):
        contents = json.loads(contents)
        gas_prices: list = []
        for content in contents['results']:

            _id = int(content['id'])
            name = content['name']
            lat = float(content['location']['lat'])
            lng = float(content['location']['lng'])
            gas = -1
            diesel = -1

            for fuel in content['fuels']:
                if fuel['fuelId'] == 1 and fuel['isSelf'] == True:
                    gas = float(fuel['price'])
                elif fuel['fuelId'] == 2 and fuel['isSelf'] == True:
                    diesel = float(fuel['price'])

            GasPriceDao.add_gas_price(_id, name, lat, lng, gas, diesel)

            gas_prices.append({
                "id": _id,
                "name": name,
                "lat": lat,
                "lng": lng,
                "gas": gas,
                "diesel": diesel
            })

        logger.debug(gas_prices)

    @classmethod
    def delete_all_gas_prices(cls):
        GasPriceDao.delete_all_gas_prices()
