import scrapy
from scrapy import Request, Spider
from urllib.parse import quote
from bytedance.items import BytedanceItem


class ByteSpider(scrapy.Spider):

    name = 'Byte'
    allowed_domains = ['job.bytedance.com']
    url = "https://job.bytedance.com/society/position?current="
    offset = 1
    start_urls = [url + str(offset)]

    def start_requests(self):
        for offset in range(1, 10):
            url = self.url + str(offset)
            yield Request(url = url, callback = self.parse, meta = {'offset': offset}, dont_filter = True)

    def parse(self, response):
        item = BytedanceItem()
        node_list = response.xpath('//div[@class="positionItem__1giWi positionItem"]')
        for node in node_list:       
            item['PositionName'] = node.xpath('.//span[@class="positionItem-title-text"]//text()').extract()
            item['WorkLocation'] = node.xpath('.//div[@class="subTitle__3sRa3 positionItem-subTitle"]//text()[1]').extract()
            item['PositionType'] = node.xpath('.//div[@class="subTitle__3sRa3 positionItem-subTitle"]//text()[2]').extract()
            item['PositionInfo'] = node.xpath('normalize-space(.//div[@class="jobDesc__3ZDgU positionItem-jobDesc"]//text())').extract()
            yield item
