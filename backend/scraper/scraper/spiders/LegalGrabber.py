import re
import random
from scrapy.spiders import CrawlSpider, Rule
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from ..items import ScraperItem


class LeadGrabberSpider(CrawlSpider):
    name = 'LeadGrabber'
    allowed_domains = ['unity3d.com']

    def __init__(self, **kwargs):
        super(LeadGrabberSpider, self).__init__(**kwargs)
        self._scraperItem = ScraperItem()
        self._kwargs = kwargs.get('kwargs')
        self.allowed_domains = [self._kwargs['domain']]
        self.myBaseUrl = self._kwargs['url']
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
            "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0"]
        self.header = random.choice(self.headers_pool)
        self._rules = [Rule
                       (LinkExtractor
                        (allow_domains=self._kwargs['domain'],
                         restrict_text=["Terms", "Legal", "Privacy", "Cookies"]),
                        callback=self.parse_link,
                        follow=True)
                       ]

    def parse_link(self, response):
        terms = "N/A"
        policy = "N/A"
        cookie = "N/A"

        print(response.url)
        # try to find terms
        # try:
        #     terms = response.xpath(f"//a[contains(text(), 'Terms')]/@href").extract_first()
        # except AttributeError:
        #     pass
        # # try to find privacy
        # try:
        #     terms = response.xpath(f"//a[contains(text(), 'Privacy')]/@href").extract_first()
        # except AttributeError:
        #     pass
        # # try to find cookie
        # try:
        #     terms = response.xpath(f"//a[contains(text(), 'Cookie')]/@href").extract_first()
        # except AttributeError:
        #     pass
        # putt data to scraper item
        # self._scraperItem["Terms_url"] = terms
        # self._scraperItem["Privacy_url"] = policy
        # self._scraperItem["Cookie_url"] = cookie
