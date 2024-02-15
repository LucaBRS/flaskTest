import requests
from flask import redirect, render_template

from main.service.gas_prices_service import GasPriceService


class GasPricesController:
    def __init__(self,sessions:dict):
        self.gas_price_service = GasPriceService(sessions['sqlite_session'])
    def get_all_gas_prices(self):
        gas_prices = self.gas_price_service.get_all_gas_prices()
        return  gas_prices

    def post_gas_prices(self):
        url = "http://localhost:8000/get_json"
        response = requests.get(url)
        if response.status_code == 200:
            self.gas_price_service.post_gas_prices(response.content)
            return redirect('/')
        else:
            raise Exception("Error posting GasPrices")

    def delete_all_gas_prices(self):
        self.gas_price_service.delete_all_gas_prices()
        return redirect('/')
        pass
