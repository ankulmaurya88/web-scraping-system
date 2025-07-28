# Custom middlewares

class SeleniumMiddleware:
    def process_request(self, request, spider):
        driver = webdriver.Chrome()
        driver.get(request.url)
        body = driver.page_source
        driver.quit()
        return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)

