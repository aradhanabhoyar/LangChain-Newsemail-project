import os

# -----------------------------
# RSS Feeds (News Sources)
# -----------------------------
RSS_FEEDS = [
    "https://techcrunch.com/feed/",
    "https://www.theverge.com/rss/index.xml",
    "https://www.bbc.com/news/technology/rss.xml"
]

# -----------------------------
# API & LLM Settings
# -----------------------------
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
LLM_TEMPERATURE = 0.2

# Summary default lines used by summarizer.py
DEFAULT_SUMMARY_LINES = 4

# -----------------------------
# Output Paths
# -----------------------------
OUTPUT_DIR = "./samples"
SUBSCRIBERS_FILE = "./data/subscribers.json"

# Enable/disable PDF export
ENABLE_PDF_EXPORT = True

# -----------------------------
# Templates
# -----------------------------
DEFAULT_TEMPLATE = "modern.html"

TEMPLATE_LIBRARY = [
    "modern.html",
    "classic.html"
]

# -----------------------------
# Personalization Defaults
# -----------------------------
DEFAULT_TONE = "formal"
DEFAULT_LENGTH = "medium"   # short=2 | medium=4 | long=6

# -----------------------------
# Scoring Keywords
# -----------------------------
KEYWORDS = [
    "ai", "cloud", "software", "startup", "market",
    "machine learning", "security", "data", "research"
]
