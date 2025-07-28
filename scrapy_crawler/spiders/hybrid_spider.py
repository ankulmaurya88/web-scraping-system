# # # Spider implementation goes here
# # import scrapy
# # from selenium_handler.render import render_with_selenium
# # from bs_parser.parser import parse_with_bs
# # from validation.validator import validate
# # from ingestion.store import store

# # class HybridSpider(scrapy.Spider):
# #     name = "hybrid"
# #     start_urls = ['https://example.com']  # Replace with real URLs

# #     def parse(self, response):
# #         # Try using Scrapy selectors
# #         data = {'title': response.css('title::text').get()}

# #         if not data['title']:
# #             # Use Selenium rendering if data not found
# #             html = render_with_selenium(response.url)
# #             data = parse_with_bs(html)

# #         if validate(data):
# #             store(data)




# import scrapy
# from selenium_handler.render import render_with_selenium
# from bs_parser.parser import parse_with_bs
# from validation.validator import validate
# from ingestion.store import store

# class HybridSpider(scrapy.Spider):
#     name = 'hybrid_spider'

#     def __init__(self, start_url=None, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.start_urls = [start_url]

#     def parse(self, response):
#         url = response.url
#         html = render_with_selenium(url)
#         data = parse_with_bs(html)
#         if validate(data):
#             store(data)



# scrapy_crawler/hybrid_spider.py
import scrapy
from scrapy.crawler import CrawlerProcess
import json

class SimpleSpider(scrapy.Spider):
    name = 'simple'
    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url]

    def parse(self, response):
        yield {
            'title': response.xpath('//title/text()').get(),
            'links': response.css('a::attr(href)').getall()
        }

def run_scrapy_spider(url):
    process = CrawlerProcess(settings={
        "FEEDS": {"output.json": {"format": "json"}}
    })
    process.crawl(SimpleSpider, url=url)
    process.start()
