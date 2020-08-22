from scrapy import Spider


class DefaultSpider(Spider):
    name = 'default'
    allowed_domains = ['google.com']
    start_urls = ['http://google.com/']

    def parse(self, response):
        pass
