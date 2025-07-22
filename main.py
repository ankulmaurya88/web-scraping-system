# Entry point to run Scrapy spider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl('hybrid')  # spider name from hybrid_spider.py
    process.start()

if __name__ == "__main__":
    run_spider()
