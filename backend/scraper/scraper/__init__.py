from scrapy import spiderloader
from scrapy.crawler import CrawlerProcess

from scrapy.utils.project import get_project_settings
import os


class Scraper:
    def __init__(self):
        settings_file_path = 'scraper.scraper.settings' # The path seen from root, ie. from main.py
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)

        # self.spider = QuotesSpider # The spider you want to crawl
        self.spider_list = []
        self._project_settings = get_project_settings()
        self.spider_loader = spiderloader.SpiderLoader.from_settings(self._project_settings)
        self._spiders = self.spider_loader.list()
        self._spider_classes = [self.spider_loader.load(name) for name in self._spiders]
        self._process = CrawlerProcess(self._project_settings)

    def get_all_spiders(self):
        """get a list of all spiders"""
        _temp = []
        for self._spider in self._spider_classes:
            _temp.append(self._spider.name)

        return _temp

    def add_scraper(self, domain):
        """create a spider"""
        pass

    def run_spiders(self, spider_name, spider_settings, spider_kwargs):
        """run a spider"""
        for _spider in self._spider_classes:
            if spider_name == _spider.name:
                self._process.settings.update(spider_settings)
                    # 'LOG_LEVEL': "INFO",
                    # 'FEED_URI': output,
                    # 'FEED_FORMAT': 'csv'
                self._process.crawl(_spider, kwargs=spider_kwargs)
        self._process.start()  # the script will block here until the crawling is finished

        # self.process.crawl(self.spider)
        # self.process.start()  # the script will block here until the crawling is finished

    def stop_spiders(self, spider_name):
        """stop the running spider"""
        pass



