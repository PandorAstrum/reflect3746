
import os
from scrapy import spiderloader
from scrapy.utils.project import get_project_settings


class Scraper:
    def __init__(self):
        settings_file_path = 'scraper.scraper.settings'     # The path seen from root, ie. from main.py
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        self._project_settings = get_project_settings()
        self.spider_loader = spiderloader.SpiderLoader.from_settings(self._project_settings)
        self._spiders = self.spider_loader.list()
        self._spider_classes = [self.spider_loader.load(name) for name in self._spiders]

    def get_all_spiders(self):
        """get a list of all spiders"""
        _temp = []
        for _s in self._spider_classes:
            _temp.append(_s.name)
        return _temp

    def get_spider(self, _name):
        """Get exact spider class"""
        for _s in self._spider_classes:
            if _name == _s.name:
                return _s

    def get_settings(self):
        """get scrapy project settings"""
        return self._project_settings
