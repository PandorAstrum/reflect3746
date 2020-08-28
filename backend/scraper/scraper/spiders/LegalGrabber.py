import random
import re

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import ScraperItem


class LegalGrabberSpider(CrawlSpider):
    name = 'LegalGrabber'

    def __init__(self, **kwargs):
        super(LegalGrabberSpider, self).__init__(**kwargs)
        self._kwargs = kwargs.get('kwargs')
        self.allowed_domains = [self._kwargs['domain']]
        self.myBaseUrl = self._kwargs['base_url']
        self.start_urls.append(self.myBaseUrl)
        self.headers_pool = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.3",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0",
            "Mozilla/5.0 (X11; Linux i586; rv:63.0) Gecko/20100101 Firefox/63.0",
            "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
        ]
        # r'/(?:\b(?:terms|privacy?\w+|cookie|tos|policy|legal)\b)/gi'
        self.header = random.choice(self.headers_pool)
        self._rules = [Rule
                       (LinkExtractor
                        (allow_domains=[self._kwargs['domain']],
                         allow=['terms', 'tos', 'privacy', 'privacypolicy', 'legal']
                         ),
                        callback=self.parse_link,
                        follow=False)
                       ]
        self.custom_settings = kwargs.get('spider_settings')

    def parse_link(self, response):
        _scraperItem = ScraperItem()
        _scraperItem["urls"] = response.url
        self.urls_list.append({
            'urls': response.url})
        yield _scraperItem
