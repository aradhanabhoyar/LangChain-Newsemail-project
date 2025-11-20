# ======================================================
#      SCORE ARTICLES + CONTENT QUALITY FILTER
# ======================================================

def score_article(article: dict) -> float:
    """
    Basic scoring: higher score = more important
    """
    important = ["tech", "security", "ai", "cloud", "startup"]

    cat = article.get("category", "").lower()
    score = 1

    if cat in important:
        score += 5

    # Keyword bonus
    text = (article.get("title", "") + article.get("content", "")).lower()
    for k in ["ai", "machine learning", "cloud"]:
        if k in text:
            score += 2

    return score


def filter_low_quality(articles, threshold=5.0):
    """
    Filters out articles below a relevance score.
    """
    return [a for a in articles if a["score"] >= threshold]
