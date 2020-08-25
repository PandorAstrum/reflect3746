#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scraper.scraper import Scraper


scraper = Scraper()
spider_settings = {
'LOG_LEVEL': "INFO",
}
spider_kwargs = {
    'domain': 'stackoverflow.com',
    'url': 'https://stackoverflow.com/'
}
scraper.run_spiders(spider_name="LeadGrabber", spider_settings=spider_settings, spider_kwargs=spider_kwargs)