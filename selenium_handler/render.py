



# selenium_handler/render.py
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time

# def render_with_selenium(url):
#     options = Options()
#     options.headless = True
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")

#     driver = webdriver.Chrome(options=options)
#     driver.get(url)
#     time.sleep(5)  # Wait for JavaScript to render

#     html = driver.page_source
#     # print(html)
#     driver.quit()
#     return html



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def render_with_selenium(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html
