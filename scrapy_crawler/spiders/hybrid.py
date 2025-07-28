import scrapy
from scrapy_crawler.items import ScrapyCrawlerItem
from w3lib.html import remove_tags
from bs4 import BeautifulSoup

class HybridSpider(scrapy.Spider):
    name = 'hybrid'
    
    def __init__(self, url=None, *args, **kwargs):
        super(HybridSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]

    def parse(self, response):
        item = ScrapyCrawlerItem()
        item['url'] = response.url
        item['title'] = response.xpath('//title/text()').get()
        item['meta_description'] = response.xpath('//meta[@name="description"]/@content').get()

        # Raw HTML of the page
        item['full_html'] = response.text

        # Extract visible text using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        for script_or_style in soup(['script', 'style', 'noscript']):
            script_or_style.decompose()  # remove unwanted tags

        visible_text = soup.get_text(separator=' ', strip=True)
        item['visible_text'] = visible_text

        # Extract all headings
        headings = []
        for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            headings.extend([h.get_text(strip=True) for h in soup.find_all(tag)])
        item['headings'] = headings

        yield item
