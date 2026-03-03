# core/engine.py
import requests

TIMEOUT = 8

class RequestEngine:
    def __init__(self):
        self.session = requests.Session()

    def get(self, url, headers=None):
        try:
            return self.session.get(url, headers=headers, timeout=TIMEOUT)
        except requests.RequestException:
            return None

    def post(self, url, data=None, headers=None):
        try:
            return self.session.post(url, data=data, headers=headers, timeout=TIMEOUT)
        except requests.RequestException:
            return None
