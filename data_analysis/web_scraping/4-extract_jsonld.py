#!/usr/bin/env python3
"""Extract quotes from JSON-LD structured data."""

import json
from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """Extract quotes, authors, and tags from JSON-LD."""
    html = fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")
    quotes = []

    for script in soup.select('script[type="application/ld+json"]'):
        data = json.loads(script.string or script.get_text())

        if isinstance(data, dict):
            data = [data]

        for item in data:
            if item.get("@type") == "Quote":
                tags = item.get("keywords", [])

                if isinstance(tags, str):
                    tags = [tag.strip() for tag in tags.split(",")]

                quotes.append({
                    "text": item.get("text"),
                    "author": item.get("author", {}).get("name"),
                    "tags": tags
                })

    return quotes
