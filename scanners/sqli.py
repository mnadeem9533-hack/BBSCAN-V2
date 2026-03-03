# scanners/sqli.py
from scanners.base import Scanner

class SQLiScanner(Scanner):
    ERRORS = ["sql", "mysql", "syntax", "warning"]

    def __init__(self, payloads):
        self.payloads = payloads

    def scan(self, engine, url, param):
        for payload in self.payloads:
            resp = engine.post(url, {param: payload})
            if resp and any(err in resp.text.lower() for err in self.ERRORS):
                return True
        return False
