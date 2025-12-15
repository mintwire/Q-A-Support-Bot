import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited_urls = set()

def crawl_website(start_url, max_pages=5):
    pages = []
    base_domain = urlparse(start_url).netloc

    def crawl(url):
        if url in visited_urls or len(visited_urls) >= max_pages:
            return

        visited_urls.add(url)

        try:
            response = requests.get(url, timeout=10)
        except Exception:
            return

        pages.append({
            "url": url,
            "html": response.text
        })

        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a", href=True):
            next_url = urljoin(url, link["href"])
            if urlparse(next_url).netloc == base_domain:
                crawl(next_url)

    crawl(start_url)
    return pages
