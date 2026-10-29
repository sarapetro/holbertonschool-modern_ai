#!/usr/bin/env python3
"""Scrape the details of a single product using Selenium."""

import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """Extract the title, price, description, and rating of a product."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(delay)

        caption = driver.find_element("css selector", ".caption")
        title = caption.find_elements("css selector", "h4")[1].text

        price = driver.find_element(
            "css selector", "h4.price"
        ).text

        description = driver.find_element(
            "css selector", "p.description"
        ).text

        stars = driver.find_elements(
        "css selector", ".ratings .ws-icon-star"
        ) 

        return {
            "title": title,
            "price": price,
            "description": description,
            "rating": len(stars)
        }

    finally:
        driver.quit()
