from selenium import webdriver
from flask import abort, Flask
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


class API(Flask):
    def __init__(self, import_name):
        super(API, self).__init__(import_name)
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')

    def html(self, url):
        try:
            driver = webdriver.Chrome(chrome_options=self.options)
            driver.get(url)
            WebDriverWait(driver, 5)
            html = driver.page_source
            driver.close()
            return html
        except Exception as e:
            print(e)
            abort(500)
