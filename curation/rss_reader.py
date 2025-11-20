# fetch simple RSS entries
import feedparser
from typing import List, Dict

def fetch_rss_articles(feed_urls: List[str], max_per_feed: int = 8) -> List[Dict]:
    all_articles = []
    for url in feed_urls:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:max_per_feed]:
                all_articles.append({
                    "title": entry.get("title", "").strip(),
                    "link": entry.get("link", "").strip(),
                    "published": entry.get("published", "")
                })
        except Exception:
            # skip feeds that fail
            continue
    return all_articles
