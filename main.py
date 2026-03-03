# main.py
import argparse
from core.engine import RequestEngine
from core.crawler import Crawler
from core.payload_manager import PayloadManager
from scanners.sqli import SQLiScanner
from scanners.xss import XSSScanner
from intelligence.waf_detector import detect_waf
from intelligence.tech_detector import detect_technology
from reports.html_report import HTMLReport

def main():
    parser = argparse.ArgumentParser(description="BBScan - Professional Bug Bounty Scanner (Educational Use Only)")
    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--threads", type=int, default=5, help="Thread count")
    parser.add_argument("--deep", type=int, default=2, help="Crawl depth")
    parser.add_argument("--report", default="report", help="Report name")
    args = parser.parse_args()

    engine = RequestEngine()
    crawler = Crawler(engine, args.deep)
    pm = PayloadManager()
    sqli_scanner = SQLiScanner(pm.load_payloads("sqli.txt"))
    xss_scanner = XSSScanner(pm.load_payloads("xss.txt"))
    report = HTMLReport(args.report)

    print("[*] Detecting WAF...")
    print("WAF:", detect_waf(engine, args.url))
    server, powered = detect_technology(engine, args.url)
    print("Server:", server, "| X-Powered-By:", powered)

    print("[*] Crawling URLs...")
    urls = crawler.crawl(args.url)
    urls.append(args.url)
    print(f"[+] URLs discovered: {len(urls)}")

    for url in urls:
        # Discover parameters
        from core.payload_manager import PayloadManager
        from urllib.parse import urlparse, parse_qs
        params = list(parse_qs(urlparse(url).query).keys())
        if not params:
            continue
        for param in params:
            if sqli_scanner.scan(engine, url, param):
                report.add_issue("SQLi", url, param)
            if xss_scanner.scan(engine, url, param):
                report.add_issue("XSS", url, param)

    report.generate()
    print("[+] Scan Completed.")

if __name__ == "__main__":
    main()
