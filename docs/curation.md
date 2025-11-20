# Curation Documentation

## Sources
Feeds used:
- TechCrunch: https://techcrunch.com/feed/
- The Verge: https://www.theverge.com/rss/index.xml
- BBC Tech: https://www.bbc.com/news/technology/rss.xml

## Scraping
- `curation/scraper.py` extracts article text from the article URL.
- If article body cannot be scraped, the RSS summary/title is used.

## Categorization
- `curation/categorizer.py` uses keyword mapping to assign categories:
  - Tech: AI, GPU, Intel, Startup, Software
  - Gadgets: SSD, Steam Deck, Camera, Ring
  - Security: Data breach, Hacker, Privacy, Cyber
  - General: default

## Scoring
- `score_article()` computes relevance using:
  - category weight
  - keyword frequency in title & content
  - content length bonus
- Scores are stored in the article dict as `score` and used to sort descending.

## Personalization
- `generator/personalize.py` controls tone and length:
  - tone: 'formal', 'friendly', 'concise'
  - length: 'short', 'medium', 'long'
- Summaries are personalized per subscriber during newsletter generation.

## Templates
- Templates located in `/templates`:
  - `template_modern.html`
  - `template_classic.html`
  - `template_minimal.html`

## Analytics
- `generator/analytics.py` logs run metadata to `analytics.json`.
- Links include UTM parameters for external analytics.

## How to run
1. Populate `data/subscribers.json`.
2. Install dependencies and (optional) `pdfkit`.
3. Run `python main.py`.
4. Outputs saved to `./samples/` and `analytics.json`.

