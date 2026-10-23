#!/usr/bin/env python3
"""Module for fetching HTML content."""

import requests


def fetch_html(url, headers=None, timeout=10):
    """Fetch HTML from a URL, raising an error for failed HTTP requests."""
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.text
