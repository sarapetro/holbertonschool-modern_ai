#!/usr/bin/env python3
"""Log in to a website and scrape protected quotes."""

import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Log in and extract quotes from the protected page."""
    session = requests.Session()

    response = session.get(login_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    csrf_token = soup.find("input", {"name": "csrf_token"})["value"]

    credentials = {
        "username": user,
        "password": pwd,
        "csrf_token": csrf_token
    }

    session.post(login_url, data=credentials).raise_for_status()

    quotes_url = "https://quotes.toscrape.com/"
    response = session.get(quotes_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []

    for quote in soup.select("div.quote"):
        text = quote.select_one("span.text").get_text(strip=True)
        author = quote.select_one("small.author").get_text(strip=True)
        tags = [
            tag.get_text(strip=True)
            for tag in quote.select("a.tag")
        ]

        quotes.append({
            "text": text,
            "author": author,
            "tags": tags
        })

    return quotes
