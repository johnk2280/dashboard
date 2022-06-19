import requests

from numbers_dashboard.settings import BOT_CHAT_ID
from numbers_dashboard.settings import BOT_TOKEN
from numbers_dashboard.settings import MESSAGE_URL


class TelegramMessage:

    def __init__(self):
        self.token = BOT_TOKEN
        self.chat_id = BOT_CHAT_ID
        self.url = MESSAGE_URL

    def send(self, text: str) -> bool:
        url = self.url.format(self.token, self.chat_id, text)
        resp = requests.get(url)
        return resp.ok

