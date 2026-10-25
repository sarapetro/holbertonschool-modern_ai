#!/usr/bin/env python3
"""Scrape quotes from all pages by following Next links."""

from bs4 import BeautifulSoup
import time
from urllib import parse


fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """Follow the next links until there are none left."""
    all_quotes = []
    url = base_url

    while url:
        all_quotes.extend(scrape_basic(url))

        soup = BeautifulSoup(fetch_html(url), "html.parser")

        next_link = soup.select_one("li.next a")

        url = parse.urljoin(
            url, next_link["href"]
        ) if next_link else None

        if url:
            time.sleep(1)

    return all_quotes
