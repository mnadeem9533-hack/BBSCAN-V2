												# reports/html_report.py
import os

class HTMLReport:
    def __init__(self, filename="report"):
        self.filename = filename
        self.issues = []

    def add_issue(self, issue_type, url, param):
        self.issues.append((issue_type, url, param))

    def generate(self):
        os.makedirs("reports", exist_ok=True)
        path = f"reports/{self.filename}.html"
        html = "<h1>BBScan Report</h1><table border=1>"
        html += "<tr><th>Type</th><th>URL</th><th>Parameter</th></tr>"
        for i in self.issues:
            html += f"<tr><td>{i[0]}</td><td>{i[1]}</td><td>{i[2]}</td></tr>"
        html += "</table>"
        with open(path, "w") as f:
            f.write(html)
        print(f"[+] HTML Report saved: {path}")
