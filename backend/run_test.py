#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__version__ = "0.0.1"
__email__ = "dreadlordn@gmail.com"
__status__ = "Production"
__license__ = "GPL-3"
__copyright__ = "Copyright 2019, PandorAstrum"
__date__ = 8/26/2020
__desc__ = "Description about this file and what it does"
"""
import time

from scraper.scraper import Scraper

s = Scraper()

params = {
"base_url": "https://stackoverflow.com/",
'domain': "stackoverflow.com"
}

s.run_spiders(spider_name="LeadGrabber", spider_settings={"LOG_LEVEL": "DEBUG"}, spider_kwargs=params)
print(s.output_data)