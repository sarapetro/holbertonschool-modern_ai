#!/usr/bin/env python3
"""Extract quotes, authors, and tags from a quotes listing page."""

from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html


def scrape_basic(url):
    """Return quote dictionaries from the first page at the given URL."""
    soup = BeautifulSoup(fetch_html(url), 'html.parser')
    quotes = []
    for quote in soup.select('div.quote'):
        quotes.append({
            'text': quote.select_one('span.text').get_text(),
            'author': quote.select_one('small.author').get_text(),
            'tags': [tag.get_text() for tag in quote.select('.tags a.tag')]
        })
    return quotes
