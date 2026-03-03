# scanners/xss.py
from scanners.base import Scanner

class XSSScanner(Scanner):
    def __init__(self, payloads):
        self.payloads = payloads

    def scan(self, engine, url, param):
        for payload in self.payloads:
            resp = engine.post(url, {param: payload})
            if resp and payload in resp.text:
                return True
        return False
