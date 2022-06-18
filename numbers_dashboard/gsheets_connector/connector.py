import json
from typing import Iterable

import httplib2

import apiclient
from oauth2client.service_account import ServiceAccountCredentials

from gsheets_connector.parser import Parser
from numbers_dashboard.settings import API_NAME
from numbers_dashboard.settings import API_VERSION
from numbers_dashboard.settings import DIMENSION
from numbers_dashboard.settings import PATH_TO_CREDENTIALS_FILE
from numbers_dashboard.settings import SPREADSHEET_ID
from numbers_dashboard.settings import SCOPES
from numbers_dashboard.settings import TABLE_RANGE


class SheetsApiConnector:

    def __init__(self):
        self.path = PATH_TO_CREDENTIALS_FILE
        self.spreadsheet_id = SPREADSHEET_ID
        self.scopes = SCOPES
        self.table_range = TABLE_RANGE
        self.dimension = DIMENSION
        self.api_name = API_NAME
        self.api_version = API_VERSION

        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.path,
            self.scopes,
        )
        self.http_auth = self.credentials.authorize(httplib2.Http())
        self.service = apiclient.discovery.build(
            self.api_name,
            self.api_version,
            http=self.http_auth,
        )

    def get_row_data(self) -> Iterable:
        values = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range=self.table_range,
            majorDimension=self.dimension,
        ).execute()
        for row in values['values'][1:]:
            yield row


def _write_to_json(content: dict, file_name: str) -> None:
    with open(f'{file_name}.json', 'w', encoding='utf-8', ) as f_obj:
        f_obj.write(json.dumps(content))


if __name__ == '__main__':
    conn = SheetsApiConnector()
    parser = Parser()
    for row in conn.get_row_data():
        print(parser.get_entry(row))
