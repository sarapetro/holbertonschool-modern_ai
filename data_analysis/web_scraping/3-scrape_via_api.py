#!/usr/bin/env python3
"""Retrieve quotes from every page of the quotes API."""

import json

fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """Return quote text, author names, and tags from all API pages."""
    quotes = []
    page = 1
    while True:
        url = '{}/api/quotes?page={}'.format(base_url.rstrip('/'), page)
        data = json.loads(fetch_html(url))
        for quote in data['quotes']:
            quotes.append({
                'text': quote['text'],
                'author': quote['author']['name'],
                'tags': quote['tags']
            })
        if not data['has_next']:
            break
        page += 1
    return quotes
