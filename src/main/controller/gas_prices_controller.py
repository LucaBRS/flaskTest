import requests
from flask import redirect, render_template

from main.service.gas_prices_service import GasPriceService


class GasPricesController:

    @staticmethod
    def get_all_gas_prices():
        gas_prices = GasPriceService().get_all_gas_prices()
        return  gas_prices

    @classmethod
    def post_gas_prices(cls):
        url = "http://localhost:8000/get_json"
        response = requests.get(url)
        if response.status_code == 200:
            GasPriceService.post_gas_prices(response.content)
            return redirect('/')
        else:
            raise Exception("Error posting GasPrices")

    @staticmethod
    def delete_all_gas_prices():
        GasPriceService.delete_all_gas_prices()
        return redirect('/')
        pass
