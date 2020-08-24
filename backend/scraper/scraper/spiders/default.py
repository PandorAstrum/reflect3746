import scrapy


class DefaultSpider(scrapy.Spider):
    name = 'default'
    allowed_domains = ['google.com']
    start_urls = ['http://google.com/']

    def parse(self, response):
        pass
