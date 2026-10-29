#!/usr/bin/env python3
"""Scrape product information using Selenium."""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_products(url):
    """Extract product details from a static category page."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    products = []

    try:
        driver.get(url)
        time.sleep(2)

        items = driver.find_elements(By.CSS_SELECTOR, ".thumbnail")

        for item in items:
            title_element = item.find_element(
                By.CSS_SELECTOR, "a.title"
            )
            price_element = item.find_element(
                By.CSS_SELECTOR, "h4.price"
            )
            description_element = item.find_element(
                By.CSS_SELECTOR, "p.description"
            )
            rating_element = item.find_element(
                By.CSS_SELECTOR, ".ratings p[data-rating]"
            )

            products.append({
                "title": title_element.get_attribute("title"),
                "price": price_element.text,
                "description": description_element.text,
                "rating": int(
                    rating_element.get_attribute("data-rating")
                )
            })

    finally:
        driver.quit()

    return products
