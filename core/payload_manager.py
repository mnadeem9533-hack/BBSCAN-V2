# core/payload_manager.py
import os

class PayloadManager:
    def __init__(self, base_path="payloads"):
        self.base_path = base_path

    def load_payloads(self, filename):
        path = os.path.join(self.base_path, filename)
        if os.path.exists(path):
            with open(path, "r") as f:
                return [line.strip() for line in f if line.strip()]
        return []
