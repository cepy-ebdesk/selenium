import time

from selenium import webdriver
from flask import abort, Flask
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class API(Flask):
    def __init__(self, import_name: str):
        super().__init__(import_name)
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument("start-maximized")  # open Browser in maximized mode
        self.options.add_argument("disable-infobars")  # disabling infobars
        self.options.add_argument("--disable-extensions")  # disabling extensions
        self.options.add_argument("--disable-gpu")  # applicable to windows os only
        self.options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        self.options.add_argument("--no-sandbox")  # Bypass OS security model

    def html(self, url):
        try:
            driver = webdriver.Chrome(chrome_options=self.options)
            driver.get(url)
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.latest-featured')))
            html = driver.page_source
            driver.close()
            return html
        except Exception as e:
            print(e)
            abort(500)
