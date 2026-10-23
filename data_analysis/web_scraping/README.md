# Web Scraping

Python exercises for fetching HTML and extracting structured data.

- `0-fetch_html.py`: Fetch HTML content from a URL.
- `1-scrape_basic.py`: Use BeautifulSoup and `fetch_html()` to extract quote
  text, authors, and tags from the first page of Quotes to Scrape.
- `3-scrape_via_api.py`: Fetch every quotes API page and return quote text,
  author names, and tags using `scrape_via_api(base_url)`.

`scrape_basic(url)` returns a list of dictionaries with `text`, `author`,
and `tags` keys. It does not follow pagination links.
