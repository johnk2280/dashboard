from datetime import datetime
import decimal
from typing import Iterable, List

from numbers_dashboard.settings import CURRENCY
from .currency_converter import CurrencyConverter


class Parser:

    def __init__(self):
        # self.data = data
        self.converter = CurrencyConverter()
        self.currency = CURRENCY

    def _get_date(self, dt: str) -> datetime.date:
        try:
            return datetime.strptime(dt, '%d.%m.%Y').date()
        except ValueError:
            print(f'Time data {dt} does not match format "%d.%m.%Y".')
            raise

    def get_entry(self, row: List[str]) -> Iterable:
        print('Еще одна запись')
        return {
                'order_id': int(row[1]),
                'usd_price': decimal.Decimal(row[2]),
                'rur_price': decimal.Decimal(
                    str(round(float(row[2]) * self.converter.get_currency_rate_to_rur(self.currency), 2))
                ),
                'delivery_date': self._get_date(row[-1]),
            }
