from scrapy import spiderloader

from scraper.scraper.spiders.default import DefaultSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os


class Scraper:
    def __init__(self):
        settings_file_path = 'scraper.scraper.settings' # The path seen from root, ie. from main.py
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        self.process = CrawlerProcess(get_project_settings())
        # self.spider = QuotesSpider # The spider you want to crawl

        self.spider_list = []
        self._project_settings = get_project_settings()
        self.spider_loader = spiderloader.SpiderLoader.from_settings(self._project_settings)
        self._spiders = self.spider_loader.list()
        self._spider_classes = [self.spider_loader.load(name) for name in self._spiders]

    def get_all_spiders(self):
        _temp = []
        for self._spider in self._spider_classes:
            _temp.append(self._spider.name)

        return _temp

    # def run_spiders(self):
    #     self.process.crawl(self.spider)
    #     self.process.start()  # the script will block here until the crawling is finished