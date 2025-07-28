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
# import scrapy
# from scrapy.crawler import CrawlerProcess
# import json

# class SimpleSpider(scrapy.Spider):
#     name = 'simple'
    
#     def __init__(self, url=None, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.start_urls = [url]

#     def parse(self, response):
#         yield {
#             'title': response.xpath('//title/text()').get(),
#             'links': response.css('a::attr(href)').getall()
#         }

# def run_scrapy_spider(url):
#     process = CrawlerProcess(settings={
#         "FEEDS": {"output.json": {"format": "json"}}
#     })
#     process.crawl(SimpleSpider, url=url)
#     process.start()



# import os
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from scrapy_crawler.spiders.hybrid import HybridSpider

# import scrapy

# class HybridSpider(scrapy.Spider):
#     name = "hybrid"

#     def __init__(self, start_url=None, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.start_urls = [start_url] if start_url else []

#     def parse(self, response):
#         yield {
#             "url": response.url,
#             "title": response.css("title::text").get()
#         }




# def run_scrapy_spider(url):
#     output_dir = "based_output"
#     os.makedirs(output_dir, exist_ok=True)
    
#     output_file = os.path.join(output_dir, "output.json")

#     settings = get_project_settings()
#     settings.set("FEEDS", {
#         output_file: {"format": "json", "overwrite": True}
#     })

#     process = CrawlerProcess(settings)
#     process.crawl(HybridSpider, start_url=url)
#     process.start()


# import os
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from scrapy_crawler.spiders.hybrid import HybridSpider

# def run_scrapy_spider(url):
#     output_dir = "based_output"
#     os.makedirs(output_dir, exist_ok=True)
    
#     output_file = os.path.join(output_dir, "output.json")

#     settings = get_project_settings()
#     settings.set("FEEDS", {
#         output_file: {"format": "json", "overwrite": True}
#     })

#     process = CrawlerProcess(settings)
#     process.crawl(HybridSpider, start_url=url)
#     process.start()


import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_crawler.spiders.hybrid import HybridSpider

def run_scrapy_spider(url):
    output_dir = "based_output"
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, "output.json")

    settings = get_project_settings()
    settings.set("FEEDS", {
        output_file: {"format": "json", "overwrite": True}
    })

    process = CrawlerProcess(settings)
    process.crawl(HybridSpider, url=url)
    process.start()
