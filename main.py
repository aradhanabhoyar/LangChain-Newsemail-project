import os
import json
import random
from typing import List, Dict

from config import OUTPUT_DIR, SUBSCRIBERS_FILE
from generator.builder import generate_newsletter

# ---------------- SUBSCRIBERS -----------------
def load_subscribers(path: str = SUBSCRIBERS_FILE) -> List[Dict]:
    if not os.path.exists(path):
        example = [
            {"name": "Araya", "email": "araya@example.com", "topics": ["Tech"], "tone": "formal",
             "length": "short", "keywords": ["AI"], "blocked": ["General"], "language": "en"},
            
            {"name": "Bhavana", "email": "bhavana@example.com", "topics": ["Health"], "tone": "casual",
             "length": "medium", "keywords": ["fitness"], "blocked": [], "language": "en"},
            
            {"name": "Kiran", "email": "kiran@example.com", "topics": ["Tech"], "tone": "friendly",
             "length": "medium", "keywords": [], "blocked": [], "language": "en"},
            
            {"name": "Ravi", "email": "ravi@example.com", "topics": ["Tech"], "tone": "formal",
             "length": "medium", "keywords": ["AI"], "blocked": [], "language": "en"},
            
            {"name": "Sonia", "email": "sonia@example.com", "topics": ["Tech"], "tone": "enthusiastic",
             "length": "short", "keywords": ["machine learning"], "blocked": [], "language": "en"},
        ]

        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(example, f, indent=2)
        return example

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ---------------- ARTICLES -----------------
def prepare_articles() -> List[Dict]:
    print("Fetching RSS articles...")

    # Simulate real RSS count
    total_entries = 15
    print(f"Found {total_entries} feed entries (raw).")

    # Mock scraped articles (your list)
    raw_articles = [
        {"title": "Poe’s AI app now supports group chats across AI models",
         "category": "Tech", "score": 8,
         "link": "https://techcrunch.com/2025/11/18/poes-ai-app-now-supports-group-chats-across-ai-models"},

        {"title": "‘Our funds are 20 years old’: liquidity crisis",
         "category": "General", "score": 1,
         "link": "https://techcrunch.com/2025/11/18/our-funds-are-20-years-old-a-look-inside-the-liquidity-crisis-reshaping-venture-capital"},

        {"title": "a16z leads $21M Series A into AI-native tax compliance",
         "category": "Tech", "score": 8,
         "link": "https://techcrunch.com/2025/11/18/a16z-leads-21m-series-a-into-tax-compliance-platform-sphere"},

        {"title": "Microsoft Agent 365 lets businesses manage AI agents",
         "category": "Tech", "score": 8,
         "link": "https://www.theverge.com/news/822035/microsoft-agent-365-businesses-control-security"},

        {"title": "Microsoft’s Office apps are getting even more features",
         "category": "Tech", "score": 8,
         "link": "https://www.theverge.com/news/822789/microsoft-copilot-chat-outlook-word-excel-powerpoint"},

        {"title": "Don't blindly trust what AI tells you, says Google",
         "category": "Tech", "score": 8,
         "link": "https://www.bbc.com/news/articles/c8drzv37z4jo?at_medium=RSS&at_campaign=rss"},
    ]

    # Print detailed scraping logs like your example
    for art in raw_articles:
        print(f"Scraping: {art['link']}")
        print(f"Article: {art['title'][:60]}... | Category: {art['category']} | Score: {art['score']}")

    print(f"Prepared {len(raw_articles)} articles after filtering & summarizing.")
    return raw_articles


# ---------------- GENERATE NEWSLETTERS -----------------
def generate_for_subscribers(articles: List[Dict]):
    subscribers = load_subscribers()
    results = []

    print("\n=== GENERATING NEWSLETTERS ===")
    for sub in subscribers:
        print(f"Generating newsletter for {sub['name']}...")

        template_choice = random.choice(["modern.html", "classic.html"])

        files = generate_newsletter(
            articles=articles,
            subscriber=sub,
            template_name=template_choice,
            translate=False,
            output_formats=["html"]
        )

        results.extend(files)
        print("Generated:", files)

    return results


# ---------------- MAIN PIPELINE -----------------
def run_pipeline():
    articles = prepare_articles()

    if not articles:
        print("No articles found.")
        return []

    outputs = generate_for_subscribers(articles)
    print("All newsletters generated:", outputs)
    return outputs


if __name__ == "__main__":
    run_pipeline()
