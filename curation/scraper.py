# simple scraper: fetch paragraph text from a URL
import requests
from bs4 import BeautifulSoup

def extract_article_text(url: str, char_limit: int = 4000) -> str:
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=8)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "lxml")

        # prefer article tag, fallback to paragraphs
        article = soup.find("article")
        blocks = article.find_all("p") if article else soup.find_all("p")
        text = " ".join(p.get_text(strip=True) for p in blocks)
        return text[:char_limit]
    except Exception:
        return ""
