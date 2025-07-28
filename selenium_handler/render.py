# # Selenium rendering logic
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time

# def render_with_selenium(url):
#     options = Options()
#     options.add_argument('--headless')
#     driver = webdriver.Chrome(options=options)
#     driver.get(url)
#     time.sleep(2)  # Wait for JS to load
#     html = driver.page_source
#     driver.quit()
#     return html



# selenium_handler/render.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def render_with_selenium(url):
    options = Options()
    options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)  # Wait for JavaScript to render

    html = driver.page_source
    # print(html)
    driver.quit()
    return html

