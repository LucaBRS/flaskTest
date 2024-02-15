import json
import logging

from flask import redirect
from sqlalchemy.orm import Session

from main.dao.gas_prices_dao import GasPriceDao

logger = logging.getLogger(__name__)


class GasPriceService:
    def __init__(self,session:Session):
        self.gas_price_dao = GasPriceDao(session)
    def get_all_gas_prices(self):
        return self.gas_price_dao.get_all_gas_prices()


    def post_gas_prices(self, contents):
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

            self.gas_price_dao.add_gas_price(_id, name, lat, lng, gas, diesel)

            gas_prices.append({
                "id": _id,
                "name": name,
                "lat": lat,
                "lng": lng,
                "gas": gas,
                "diesel": diesel
            })

        logger.debug(gas_prices)

    def delete_all_gas_prices(self=None):
        self.gas_price_dao.delete_all_gas_prices()

