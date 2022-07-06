from dotenv import dotenv_values
from requests import Session

BASE_URL = dotenv_values()["API_BASE_URL"]


class RequestsManager:
    def __init__(self):
        self.session = Session()

    def set_headers(self, headers):
        self.session.headers.update(headers)

    def get(self, url, *args, **kwargs):
        full_url = BASE_URL + url

        return self.session.get(full_url, *args, **kwargs)

    def post(self, url, data, *args, **kwargs):
        full_url = BASE_URL + url

        return self.session.post(full_url, data)


session = RequestsManager()
