import scrapy

class ScrapyCrawlerItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    full_html = scrapy.Field()
    visible_text = scrapy.Field()
    meta_description = scrapy.Field()
    headings = scrapy.Field()
