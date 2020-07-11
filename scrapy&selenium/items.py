import scrapy

class ScrapyuniversalItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    text = scrapy.Field()
    datatime = scrapy.Field()
    source = scrapy.Field()
    website = scrapy.Field()
