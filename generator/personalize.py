# generator/personalize.py
from typing import Optional

def apply_personalization(text: str, tone: str = "formal", length: str = "medium") -> str:
    """
    Lightweight personalization wrapper:
    - tone: 'formal','friendly','concise'
    - length: 'short','medium','long'
    This uses prompt templates for your LLM if you want; currently it will
    shorten or slightly rephrase locally as a fallback to keep offline-friendly.
    """
    # local fallback summarizer/trimmer
    lines_map = {"short": 2, "medium": 4, "long": 8}
    max_sentences = lines_map.get(length, 4)

    # naive sentence split
    import re
    sents = re.split(r'(?<=[.!?])\s+', (text or "").strip())
    s = " ".join(sents[:max_sentences]).strip()
    if not s:
        return "[No content]"

    # Simple tone tweak (local)
    if tone == "friendly":
        # append friendly sign-off if short enough
        if len(s) < 240:
            s = s + " — Quick note: hope you find this useful!"
    elif tone == "concise":
        # shorten further
        s = " ".join(s.split()[:60])
        if len(s) > 200:
            s = s[:200].rsplit(" ", 1)[0] + "..."
    # formal leaves as-is

    return s
