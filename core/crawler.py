# core/crawler.py
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class Crawler:
    def __init__(self, engine, depth=2):
        self.engine = engine
        self.visited = set()
        self.depth = depth

    def crawl(self, url, level=0):
        if level > self.depth or url in self.visited:
            return []

        self.visited.add(url)
        urls = []

        r = self.engine.get(url)
        if r:
            soup = BeautifulSoup(r.text, "html.parser")
            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link['href'])
                if urlparse(full_url).netloc == urlparse(url).netloc:
                    urls.append(full_url)
                    urls += self.crawl(full_url, level + 1)
        return list(set(urls))
