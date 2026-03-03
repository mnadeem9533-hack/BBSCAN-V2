# reports/json_report.py
import os
import json

class JSONReport:
    def __init__(self, filename="report"):
        self.filename = filename
        self.issues = []

    def add_issue(self, issue_type, url, param):
        self.issues.append({"type": issue_type, "url": url, "param": param})

    def generate(self):
        os.makedirs("reports", exist_ok=True)
        path = f"reports/{self.filename}.json"
        with open(path, "w") as f:
            json.dump(self.issues, f, indent=4)
        print(f"[+] JSON Report saved: {path}")
