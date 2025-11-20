"""
generator/builder.py

Provides `generate_newsletter(...)` used by main.py.

Features:
- Ensures templates/modern.html and templates/classic.html exist (writes simple defaults if missing).
- Renders articles + subscriber context using Jinja2.
- Writes files into OUTPUT_DIR (falls back to ./samples).
- Returns list of generated file paths.
"""

import os
from typing import List, Dict, Any
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from datetime import datetime

try:
    from config import OUTPUT_DIR
except Exception:
    OUTPUT_DIR = "samples"  # fallback if config doesn't define it


# --- Default templates to write if missing ---
_DEFAULT_CLASSIC = """<!doctype html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>{{ subscriber.name }}'s Newsletter — {{ date }}</title>
  <style>
    body { font-family: Arial, Helvetica, sans-serif; margin: 20px; line-height: 1.5; color: #222; }
    header { border-bottom: 1px solid #eee; margin-bottom: 20px; padding-bottom: 10px; }
    h1 { margin: 0; font-size: 24px; }
    .article { margin-bottom: 18px; padding-bottom: 12px; border-bottom: 1px dashed #eee; }
    .article a { color: #1a73e8; text-decoration: none; }
    .meta { color: #666; font-size: 12px; }
  </style>
</head>
<body>
  <header>
    <h1>{{ subscriber.name }} — Curated News</h1>
    <p class="meta">Topics: {{ subscriber.topics | join(', ') }} · Tone: {{ subscriber.tone }}</p>
    <p class="meta">Generated: {{ date }}</p>
  </header>

  {% for art in articles %}
  <div class="article">
    <h2><a href="{{ art.link }}" target="_blank" rel="noopener">{{ art.title }}</a></h2>
    <p class="meta">{{ art.category }} · Score: {{ art.score }}</p>
    <p>{{ art.content }}</p>
  </div>
  {% endfor %}

  <footer style="margin-top:30px; color:#777; font-size:12px;">
    <p>You're receiving this because you subscribed to curated updates.</p>
  </footer>
</body>
</html>
"""

_DEFAULT_MODERN = """<!doctype html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>{{ subscriber.name }} — Weekly Brief</title>
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <style>
    body { font-family: 'Segoe UI', Roboto, Arial, sans-serif; background:#f7f9fb; color:#222; padding:20px; }
    .card { background:white; border-radius:12px; padding:22px; box-shadow: 0 6px 18px rgba(0,0,0,0.06); max-width:800px; margin:auto; }
    header h1 { margin:0; font-size:22px; }
    .meta { color:#667; font-size:13px; margin-top:6px; }
    .grid { display:grid; gap:16px; margin-top:18px; }
    .item { padding:14px; border-radius:8px; background:linear-gradient(180deg, rgba(255,255,255,1), rgba(250,250,250,1)); }
    .item h3 { margin:0 0 6px 0; font-size:16px; }
    .item p { margin:0; color:#444; }
    .item a { color: #0b63d6; text-decoration:none; }
  </style>
</head>
<body>
  <div class="card">
    <header>
      <h1>{{ subscriber.name }}'s Brief</h1>
      <div class="meta">Topics: {{ subscriber.topics | join(', ') }} · Tone: {{ subscriber.tone }} · {{ date }}</div>
    </header>

    <div class="grid">
      {% for art in articles %}
      <article class="item">
        <h3><a href="{{ art.link }}" target="_blank" rel="noopener">{{ art.title }}</a></h3>
        <div class="meta">{{ art.category }} · Score: {{ art.score }}</div>
        <p>{{ art.content }}</p>
      </article>
      {% endfor %}
    </div>

    <footer style="margin-top:18px; color:#7a7a7a; font-size:13px;">
      <p>Thank you for reading — curated automatically.</p>
    </footer>
  </div>
</body>
</html>
"""


def _ensure_templates_dir(templates_dir: str):
    """Create templates dir & default templates if missing."""
    os.makedirs(templates_dir, exist_ok=True)
    classic_path = os.path.join(templates_dir, "classic.html")
    modern_path = os.path.join(templates_dir, "modern.html")

    if not os.path.exists(classic_path):
        with open(classic_path, "w", encoding="utf-8") as f:
            f.write(_DEFAULT_CLASSIC)

    if not os.path.exists(modern_path):
        with open(modern_path, "w", encoding="utf-8") as f:
            f.write(_DEFAULT_MODERN)


def generate_newsletter(
    articles: List[Dict[str, Any]],
    subscriber: Dict[str, Any],
    template_name: str = "classic.html",
    translate: bool = False,
    output_formats: List[str] = None,
) -> List[str]:
    """
    Generate newsletter files for a single subscriber.
    Returns list of generated file paths.

    Parameters mirror how main.py calls the function.
    """
    if output_formats is None:
        output_formats = ["html"]

    # ensure output dir
    out_dir = OUTPUT_DIR or "samples"
    os.makedirs(out_dir, exist_ok=True)

    # templates folder relative to project root
    templates_dir = os.path.join(os.getcwd(), "templates")
    _ensure_templates_dir(templates_dir)

    # Setup Jinja env
    env = Environment(loader=FileSystemLoader(templates_dir), autoescape=True)

    # Try requested template, fallback to classic.html
    chosen_template = template_name or "classic.html"
    try:
        template = env.get_template(chosen_template)
    except TemplateNotFound:
        # try fallback
        try:
            template = env.get_template("classic.html")
        except TemplateNotFound:
            # As last resort, create a Template from the default string
            template = env.from_string(_DEFAULT_CLASSIC)

    # prepare context
    ctx = {
        "subscriber": subscriber,
        "articles": articles,
        "date": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        "translate": translate,
    }

    generated_paths: List[str] = []

    # HTML output
    if "html" in output_formats:
        # safe filename
        name = subscriber.get("name", "subscriber").strip().replace(" ", "_")
        filename = f"{name}_newsletter.html"
        out_path = os.path.join(out_dir, filename)

        rendered = template.render(**ctx)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(rendered)

        generated_paths.append(out_path)

    # (Optional) future formats like text/pdf could be added here

    return generated_paths


# If run directly, a tiny smoke test
if __name__ == "__main__":
    sample_articles = [
        {"title": "Test Article", "content": "Short summary", "category": "General", "score": 5, "link": "https://example.com"}
    ]
    sample_sub = {"name": "Demo", "topics": ["Tech"], "tone": "casual"}
    print(generate_newsletter(sample_articles, sample_sub))
