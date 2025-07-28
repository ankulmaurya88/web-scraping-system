# Scrapy settings


# settings.py

BOT_NAME = 'scrapy_crawler'

SPIDER_MODULES = ['scrapy_crawler.spiders']
NEWSPIDER_MODULE = 'scrapy_crawler.spiders'

# Obey robots.txt rules (optional, you can disable it for more aggressive crawling)
ROBOTSTXT_OBEY = True

# Configure item pipelines
ITEM_PIPELINES = {
    'scrapy_crawler.pipelines.SaveToSQLitePipeline': 300,
}

# Other common settings you may want to set:
DOWNLOAD_DELAY = 1  # Delay between requests to the same website

# User-Agent (optional, can customize if needed)
# USER_AGENT = 'scrapy_crawler (+http://www.yourdomain.com)'

# Logging
LOG_LEVEL = 'INFO'

