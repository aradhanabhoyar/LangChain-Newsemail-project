def render_template(template_name, subscriber, grouped_articles):
    """
    Generate a fully styled HTML newsletter.
    template_name: string (not used right now but needed for builder compatibility)
    subscriber: dict with user information
    grouped_articles: dict with categories and list of articles
    """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Newsletter for {subscriber.get('name','User')}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 20px;
                line-height: 1.6;
                color: #333;
            }}
            h1 {{
                color: #222;
            }}
            h2 {{
                color: #0077cc;
                border-bottom: 2px solid #0077cc;
                padding-bottom: 5px;
                margin-top: 30px;
            }}
            .news-card {{
                background: #fff;
                padding: 15px;
                margin: 10px 0;
                border-radius: 8px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }}
            .cta-button {{
                display: inline-block;
                background-color: #0077cc;
                color: white;
                padding: 8px 12px;
                border-radius: 5px;
                text-decoration: none;
                margin-top: 10px;
            }}
            .cta-button:hover {{
                background-color: #005fa3;
            }}
        </style>
    </head>
    <body>
        <h1>Hello {subscriber.get('name','User')}, here’s your personalized newsletter!</h1>
    """

    # CATEGORY GROUPING
    for category in sorted(grouped_articles.keys()):
        html += f"<h2>{category}</h2>"

        sorted_articles = sorted(
            grouped_articles[category],
            key=lambda x: x.get("score", 0),
            reverse=True
        )

        for article in sorted_articles:
            html += f"""
            <div class="news-card">
                <h3>{article['title']}</h3>
                <p>{article['summary']}</p>
                <a href="{article.get('url','')}" class="cta-button" target="_blank">Read More</a>
            </div>
            """

    html += """
    </body>
    </html>
    """

    return html
