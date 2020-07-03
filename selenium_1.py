#包含商品图片、名称、价格、购买人数、店铺名称、店铺所在地
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import time
from pyquery import PyQuery as pq
import requests
import re
from requests.exceptions import RequestException
import csv

browser = webdriver.Chrome()
wait=WebDriverWait(browser, 10)
keyword = "ipad"
url = 'https://s.taobao.com/search?q=' + quote(keyword)
GROUP_START = 1
GROUP_END = 10

def login(url):
    browser.get(url)
    browser.maximize_window()
    browser.find_element_by_id('fm-login-id').send_keys('**********')
    browser.find_element_by_id('fm-login-password').send_keys('**********')
    sleep(2)
    source=browser.find_element_by_xpath("//*[@id='nc_1_n1z']")  
    ActionChains(browser).drag_and_drop_by_offset(source,280,0).perform()
    browser.find_element_by_xpath(".//*[@type='submit']").click()

def index_page(page):
    try: 
        if page > 1:
            browser.find_element_by_css_selector('li.item.next').click()
    except TimeoutException:
        index_page(page)

def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    # 使用 CSS 选择器获取商品信息列表，匹配的是整个页面的每个商品，匹配结果有多个
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'title':item.find('.row.row-2.title').text(),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        write_to_csvRows(product)

def write_to_csvField(fieldname):
    with open("ipad.csv",'a',encoding = 'utf-8', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
    
#内容写入csv
def write_to_csvRows(product):
    with open("ipad.csv",'a',encoding = 'utf-8', newline = '') as f:
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writerow(product)
        f.close()

def main():
    login(url)
    for i in range(GROUP_START, GROUP_END):
        index_page(i)
        get_products()
        sleep(2)

if __name__ == '__main__':
    fieldnames = ["title", "price", "deal", "shop", "location"]
    write_to_csvField(fieldnames)
    main()
