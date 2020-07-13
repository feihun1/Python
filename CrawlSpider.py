import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qstest.items import QstestItem

class QstSpider(CrawlSpider):
    name = 'qst'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/8hr/page/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        links = response.xpath('//*[@id="content"]/div/div[2]/div/ul/li/a/@href').extract()
        for link in links:
            link = response.urljoin(link)
            yield scrapy.Request(link, callback = self.parse_content, dont_filter = True)

    def parse_content(self, response):
        item = QstestItem()
        item['title'] = response.xpath('normalize-space(//*[@id="content"]/div/div[2]/h1/text())').extract()[0]
        item['author'] = response.xpath('//*[@id="articleSideLeft"]/a/div[1]/span[1]/text()').extract()[0]
        yield item
