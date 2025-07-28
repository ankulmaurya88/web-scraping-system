# main.py

import sys
import requests

from bs_parser.parser import parse_with_bs
from selenium_handler.render import render_with_selenium
from scrapy_crawler.spiders.hybrid_spider import run_scrapy_spider
# from output_handler.save import save_output

from output_handler.save import OutputSaver

def should_use_selenium(url):
    """
    Determine if the website is JavaScript-heavy and needs Selenium.
    """
    try:
        resp = requests.get(url, timeout=5)
        if len(resp.text) < 1000:
            return True  # Possibly JS-heavy
        if "Flipkart" not in resp.text and "<script" in resp.text:
            return True
        return False
    except Exception:
        return True

def should_use_scrapy(url):
    """
    Determine if the website structure indicates deep crawling is required.
    """
    keywords = ["category", "search", "page", "filter"]
    return any(kw in url.lower() for kw in keywords)

def main():
    """
    Entry point: Accepts a URL and chooses the scraping strategy.
    """
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        return

    url = sys.argv[1]

    if should_use_selenium(url):
        print("[+] Using Selenium...")
        html = render_with_selenium(url)
        data = parse_with_bs(html)
    elif should_use_scrapy(url):
        print("[+] Using Scrapy...")
        run_scrapy_spider(url)
        return
    else:
        print("[+] Using BeautifulSoup...")
        html = requests.get(url).text
        data = parse_with_bs(html)

    # Save data to all formats (Word, Excel, PDF)



    saver = OutputSaver(data)
    saver.save_all_formats()
    
    # save_output(data)
    print("[✓] Scraping Completed.")

if __name__ == "__main__":
    main()
