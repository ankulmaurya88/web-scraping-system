import scrapy

class HybridSpider(scrapy.Spider):
    name = "hybrid"

    def __init__(self, start_url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [start_url] if start_url else []

    def parse(self, response):
        yield {
            "url": response.url,
            "title": response.css("title::text").get()
        }
