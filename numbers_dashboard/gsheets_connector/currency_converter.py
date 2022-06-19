import requests

from numbers_dashboard.settings import EXCHANGE_RATES_URL


class CurrencyRate:

    def __init__(self):
        self.url = EXCHANGE_RATES_URL
        self.rates = self._get_rates()

    def _get_response(self) -> dict:
        response = requests.get(self.url)
        return response.json()

    def _get_rates(self) -> dict:
        rates = self._get_response()['Valute']
        return rates

    def get_rate_to_rur(self, currency: str) -> float:
        currency_rate = self.rates[currency]['Value']
        return currency_rate




