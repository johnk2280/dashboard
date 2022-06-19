import datetime

from django.shortcuts import render
from django.views.generic import View

from .models import Order
from gsheets_connector.connector import SheetsApiConnector
from gsheets_connector.parser import Parser
from gsheets_connector.message import TelegramMessage


class IndexView(View):
    connector = SheetsApiConnector()
    parser = Parser()
    message = TelegramMessage()

    def _check_date(self, dtm: datetime.date) -> bool:
        return dtm < datetime.date.today()

    def get(self, request):
        usd_total = 0
        rur_total = 0
        expired_orders = []
        entries = tuple(map(
            self.parser.get_entry,
            self.connector.get_row_data(),
        ))
        for obj in entries:
            usd_total += obj['usd_price']
            rur_total += obj['rur_price']
            expired = self._check_date(obj['delivery_date'])
            if expired:
                expired_orders.append(obj["order_id"])

            Order.objects.update_or_create(
                defaults=obj,
                order_id=obj['order_id'],
            )

        if expired_orders:
            self.message.send(expired_orders)

        context = {
            'usd_total': usd_total,
            'rur_total': rur_total,
            'entries': entries,
        }
        return render(request, 'mainapp/orders.html', context)
