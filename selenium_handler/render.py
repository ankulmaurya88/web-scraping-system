# Selenium rendering logic
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def render_with_selenium(url):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)  # Wait for JS to load
    html = driver.page_source
    driver.quit()
    return html
