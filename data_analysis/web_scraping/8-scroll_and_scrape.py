#!/usr/bin/env python3
"""Scroll through an infinite page and scrape unique products."""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll and extract unique products from an infinite-scroll page."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    products = []
    seen = set()

    try:
        driver.get(url)
        time.sleep(scroll_pause)

        last_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight)"
            )
            time.sleep(scroll_pause)

            new_height = driver.execute_script(
                "return document.body.scrollHeight"
            )

            if new_height == last_height:
                break

            last_height = new_height

        cards = driver.find_elements("css selector", "div.thumbnail")

        for card in cards:
            title_element = card.find_element(
                "css selector", "a.title"
            )
            title = title_element.get_attribute("title")

            price = card.find_element(
                "css selector", "h4.price"
            ).text

            key = (title, price)

            if key in seen:
                continue

            seen.add(key)

            description = card.find_element(
                "css selector", "p.description"
            ).text

            stars = card.find_elements(
                "css selector", ".ratings p.ws-icon.ws-icon-star"
            )

            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": len(stars)
            })

    finally:
        driver.quit()

    return products
