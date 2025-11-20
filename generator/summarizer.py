import re
import os
from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY, LLM_TEMPERATURE

if OPENAI_API_KEY:
    os.environ.setdefault("OPENAI_API_KEY", OPENAI_API_KEY)

# Map lengths to bullet points
SUMMARY_LENGTH_MAP = {
    "short": 3,
    "medium": 5,
    "long": 8
}

# Tone descriptions for LLM
TONE_MAP = {
    "formal": "professional and factual",
    "casual": "friendly and relaxed",
    "enthusiastic": "energetic and engaging"
}

# =====================================================
#              LOCAL FALLBACK SUMMARY
# =====================================================

def _simple_local_summary(text: str, lines: int = 3) -> str:
    """
    Simple fallback summary: takes first N sentences
    """
    if not text:
        return "[No content]"
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    out = " ".join(sentences[:lines])
    return out[:600] + "..." if len(out) > 600 else out

# =====================================================
#              SUMMARY GENERATION
# =====================================================

def generate_summary(text: str, length: str = "medium", tone: str = "formal", lines: int = None) -> str:
    """
    Generate a bullet-point summary of text.
    :param text: Article content
    :param length: short, medium, long (ignored if lines provided)
    :param tone: formal, casual, enthusiastic
    :param lines: Number of bullet points (overrides length)
    :return: Summary string
    """
    text = (text or "").strip()
    if not text:
        return "[No content extracted]"

    # Determine bullet count
    if lines is None:
        lines = SUMMARY_LENGTH_MAP.get(length, 5)

    tone_desc = TONE_MAP.get(tone, TONE_MAP["formal"])

    try:
        llm = ChatOpenAI(
            api_key=os.environ.get("OPENAI_API_KEY", ""),
            model="gpt-4o-mini",
            temperature=LLM_TEMPERATURE
        )

        prompt = f"""
Summarize the following article in {lines} bullet points.
The tone should be {tone_desc}.
Output must be bullet points only, no paragraphs.

Article:
{text}

Summary:
"""
        response = llm.invoke(prompt)
        return getattr(response, "content", str(response)).strip()

    except Exception:
        # Fallback
        return _simple_local_summary(text, lines)
