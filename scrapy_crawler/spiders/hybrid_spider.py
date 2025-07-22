# Spider implementation goes here
import scrapy
from selenium_handler.render import render_with_selenium
from bs_parser.parser import parse_with_bs
from validation.validator import validate
from ingestion.store import store

class HybridSpider(scrapy.Spider):
    name = "hybrid"
    start_urls = ['https://example.com']  # Replace with real URLs

    def parse(self, response):
        # Try using Scrapy selectors
        data = {'title': response.css('title::text').get()}

        if not data['title']:
            # Use Selenium rendering if data not found
            html = render_with_selenium(response.url)
            data = parse_with_bs(html)

        if validate(data):
            store(data)
