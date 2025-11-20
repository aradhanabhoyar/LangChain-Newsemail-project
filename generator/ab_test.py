
# generator/ab_test.py
import os
import re
from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY, LLM_TEMPERATURE

# simple offline fallback for subject lines
def _simple_subjects_fallback(topic: str):
    topic = (topic or "News").strip()
    s1 = f"Top stories: {topic}"
    s2 = f"Today in {topic} — quick read"
    return [s1, s2]

def generate_subjects(topic: str):
    topic = (topic or "News").strip()
    try:
        llm = ChatOpenAI(api_key=os.environ.get("OPENAI_API_KEY", ""), model="gpt-3.5-turbo", temperature=LLM_TEMPERATURE)
        prompt = (
            f"Create two short, catchy email subject lines for a newsletter about: {topic}. "
            "Label them A and B (but output just the lines)."
        )
        response = llm.invoke(prompt)
        out = getattr(response, "content", None) or str(response)
        # parse 2 lines
        lines = [l.strip(" -•:") for l in re.split(r'\n+', out) if l.strip()]
        # common fallback parsing: pick two non-empty short lines
        subjects = [l for l in lines if len(l) > 3]
        if len(subjects) >= 2:
            return subjects[:2]
        return _simple_subjects_fallback(topic)
    except Exception as e:
        msg = str(e).lower()
        if "quota" in msg or "rate" in msg or "429" in msg:
            return _simple_subjects_fallback(topic)
        return _simple_subjects_fallback(topic)
