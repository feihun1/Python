# -*- coding: utf-8 -*-
import scrapy
from scrapy_news.items import ScrapyNewsItem

class SunSpiderSpider(scrapy.Spider):
    name = 'sun_spider'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?id=1&page='
    offset = 1
    start_urls = [url + str(offset)]

    def parse(self, response):
        links = response.xpath('/html/body/div[2]/div[3]/ul[2]/li/span[3]/a/@href').extract()
        for link in links:
            link = response.urljoin(link)
            yield scrapy.Request(link, callback = self.parse_item)
        if self.offset<=10:
            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset), callback = self.parse)

    def parse_item(self, response):
        item = ScrapyNewsItem()
        item['title'] = response.xpath('/html/body/div[3]/div[2]/div[2]/p/text()').extract()
        item['date'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[2]/text()').extract()
        state = response.xpath('normalize-space(/html/body/div[3]/div[2]/div[2]/div[1]/span[3]/text())').extract()
        item['state'] = state
        item['number'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[4]/text()').extract()
        item['content'] = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract()
        item['url'] = response.url
        yield item
