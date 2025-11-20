def categorize_article(article: dict) -> str:
    categories = {
        "Tech": ["AI", "GPU", "Intel", "Startup", "Software"],
        "Gadgets": ["SSD", "Steam Deck", "Camera", "Ring"],
        "Security": ["Data breach", "Hacker", "Privacy", "Cyber"],
    }
    text = article.get("title","") + " " + article.get("content","")
    for category, keywords in categories.items():
        if any(keyword.lower() in text.lower() for keyword in keywords):
            return category
    return "General"

# curation/categorizer.py

def score_article(article: dict) -> float:
    """
    Improved relevance scoring:
    - Category importance
    - Keyword frequency in title + content
    - Article length bonus
    """
    category_weights = {
        "Tech": 5,
        "Gadgets": 4,
        "Security": 5,
        "Business": 3,
        "General": 1
    }

    keywords = {
        "AI": 3, "GPU": 2, "Intel": 2, "Startup": 3,
        "SSD": 2, "Camera": 2, "Ring": 2, "Data breach": 3,
        "Fintech": 2, "Google": 2, "Apple": 2
    }

    text = (article.get("title", "") + " " + article.get("content", "")).lower()

    # Base score from category
    score = category_weights.get(article.get("category", "General"), 1)

    # Add keyword frequency weight
    for kw, w in keywords.items():
        score += text.count(kw.lower()) * w

    # Boost longer articles (optional, e.g., more than 200 words)
    if len(text.split()) > 200:
        score += 2

    return float(score)
