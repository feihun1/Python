from scrapy import signals
import scrapy
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.http import HtmlResponse
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 

class BytedanceDownloaderMiddleware:
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def __del__(self):
        self.driver.close()

    def process_request(self, request, spider):

        offset = request.meta.get('offset', 1)
        self.driver.get(request.url)
        time.sleep(1)
        if offset > 1:
            self.driver.find_element_by_xpath('.//*[@class="anticon"]').click()
        #html = self.driver.page_source
        #self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        return scrapy.http.HtmlResponse(url = request.url, body = self.driver.page_source.encode('utf-8'), encoding = 'utf-8', request = request, status = 200)# Called for each request that goes through the downloader
