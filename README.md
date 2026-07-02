# shopify-multi-store-scraper
A Python web scraper that extracts product data from multiple Shopify stores with pagination support, error handling, and CSV export.

## Features
- Scrapes product data from multiple Shopify stores sequentially
- Handles pagination (automatically fetches all pages)
- Extracts product title, type, variant name, price, and image URL
- Saves each store's data as a separate CSV file
- Error handling for network issues and missing data fields
- Safe extraction using `.get()` to prevent crashes

## Requirements
- Python 3.x
- `requests` library

## Installation

1. Clone or download this repository
2. Install required library:
```bash
pip install requests
