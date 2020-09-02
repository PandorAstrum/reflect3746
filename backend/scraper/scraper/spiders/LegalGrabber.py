import random
from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor
from scrapy.http import HtmlResponse
from scrapy_splash import SplashRequest, SplashJsonResponse, SplashTextResponse
from ..items import ScraperItem


class LegalGrabberSpider(CrawlSpider):
    name = 'LegalGrabber'

    def __init__(self, **kwargs):
        super(LegalGrabberSpider, self).__init__(**kwargs)
        self._kwargs = kwargs.get('kwargs')
        self.allowed_domains = [self._kwargs['domain']]
        self.myBaseUrl = self._kwargs['base_url']
        self.start_urls.append(self.myBaseUrl)
        self._dynamic = self._kwargs['dynamic']

        self._user_agent_pool = [
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
        self._user_agent = random.choice(self._user_agent_pool)

        if not self._dynamic:
            self._rules = [Rule(LinkExtractor
                                (allow=['terms', 'tos', 'privacy', 'privacypolicy', 'legal'], deny=['photos']),
                                callback=self.parse_link,
                                follow=False)
                           ]
        else:
            self._rules = [Rule(LinkExtractor
                                (allow=['terms', 'tos', 'privacy', 'privacypolicy', 'legal'], deny=['photos']),
                                callback=self.parse_link,
                                process_request=self.process_with_dynamic,
                                follow=False)
                           ]

    def start_requests(self):
        """generic start request"""
        for url in self.start_urls:
            if not self._dynamic:
                yield Request(url, headers={'User-Agent': self._user_agent})
            else:
                yield SplashRequest(url, args={'wait': 15}, meta={'real_url': url})

    def process_with_dynamic(self, request):
        """Use of splash to render js"""
        request.meta['splash'] = {
            'endpoint': 'render.html',
            'args': {
                'wait': 15,
            }
        }
        return request

    def _requests_to_follow(self, response):
        if not isinstance(
                response,
                (HtmlResponse, SplashJsonResponse, SplashTextResponse)):
            return
        seen = set()
        for n, rule in enumerate(self._rules):
            links = [lnk for lnk in rule.link_extractor.extract_links(response)
                     if lnk not in seen]
            if links and rule.process_links:
                links = rule.process_links(links)
            for link in links:
                seen.add(link)
                r = self._build_request(n, link)
                yield rule.process_request(r, response)

    def parse_link(self, response):
        """Final response link to scrap and dump"""
        _scraperItem = ScraperItem()
        _scraperItem["urls"] = response.url
        self.urls_list.append(response.url)
        yield _scraperItem
