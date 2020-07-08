# -*- coding: utf-8 -*-
import scrapy
from Itcast.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    #爬虫名：启动爬虫时必须的参数（必选）
    name = 'itcast'
    #爬取域范围，允许爬虫在这个域名下进行爬取（可选）
    allowed_domains = ['itcast.cn']
    #起始url列表，爬虫执行后第一批请求，将从这个列表中获取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        node_list = response.xpath("//div[@class = 'li_txt']")
        for node in node_list:
            item = ItcastItem()
            item['name'] = node.xpath('./h3/text()').extract()[0]
            item['title'] = node.xpath('./h4/text()').extract()[0]
            item['info'] = node.xpath('./p/text()').extract()[0]
            yield item

