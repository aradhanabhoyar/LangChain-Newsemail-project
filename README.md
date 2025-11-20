# LangChain Email Newsletter Writer

Automated newsletter generator that curates articles (RSS + scraping), categorizes and scores content, summarizes using LangChain (with fallback), and builds professional HTML newsletters. Includes A/B subject generation, caching, analytics, and optional PDF export

## Features

- RSS feed integration & web scraping
- Content categorization & relevance scoring
- LangChain summarization with local fallback
- Personalized newsletters per subscriber preferences
- Template library (modern, minimal, corporate)
- A/B subject line generation
- Simple analytics logging
- Optional HTML → PDF export (requires `wkhtmltopdf`)

## Setup (Fresher-Friendly)

1. Clone the repo
git clone https://github.com/yourusername/langchain-newsletter.git
cd langchain-newsletter

2. Create a virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Add OpenAI key
setx OPENAI_API_KEY "sk-..."

5. Run the project
python main.py

6. View output
Fetching RSS articles...
Found 15 feed entries (raw).
Scraping: https://techcrunch.com/2025/11/18/poes-ai-app-now-supports-group-chats-across-ai-models
Article: Poe’s AI app now supports group chats across AI models... | Category: Tech | Score: 8
Scraping: https://techcrunch.com/2025/11/18/our-funds-are-20-years-old-a-look-inside-the-liquidity-crisis-reshaping-venture-capital
Article: ‘Our funds are 20 years old’: liquidity crisis... | Category: General | Score: 1
Scraping: https://techcrunch.com/2025/11/18/a16z-leads-21m-series-a-into-tax-compliance-platform-sphere
Article: a16z leads $21M Series A into AI-native tax compliance... | Category: Tech | Score: 8
Scraping: https://www.theverge.com/news/822035/microsoft-agent-365-businesses-control-security
Article: Microsoft Agent 365 lets businesses manage AI agents... | Category: Tech | Score: 8
Scraping: https://www.theverge.com/news/822789/microsoft-copilot-chat-outlook-word-excel-powerpoint
Article: Microsoft’s Office apps are getting even more features... | Category: Tech | Score: 8
Scraping: https://www.bbc.com/news/articles/c8drzv37z4jo?at_medium=RSS&at_campaign=rss
Article: Don't blindly trust what AI tells you, says Google... | Category: Tech | Score: 8
Prepared 6 articles after filtering & summarizing.

=== GENERATING NEWSLETTERS ===
Generating newsletter for Araya...
Generated: ['./samples\\Araya_newsletter.html']
Generating newsletter for Bhavana...
Generated: ['./samples\\Bhavana_newsletter.html']
Generating newsletter for Kiran...
Generated: ['./samples\\Kiran_newsletter.html']
Generating newsletter for Ravi...
Generated: ['./samples\\Ravi_newsletter.html']
Generating newsletter for Sonia...
Generated: ['./samples\\Sonia_newsletter.html']
All newsletters generated: ['./samples\\Araya_newsletter.html', './samples\\Bhavana_newsletter.html', './samples\\Kiran_newsletter.html', './samples\\Ravi_newsletter.html', './samples\\Sonia_newsletter.html']



