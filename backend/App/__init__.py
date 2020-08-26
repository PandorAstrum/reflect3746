#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__version__ = "0.0.1"
__email__ = "dreadlordn@gmail.com"
__status__ = "Production"
__license__ = "GPL-3"
__copyright__ = "Copyright 2020, PandorAstrum"
__date__ = 8/25/2020
__desc__ = "Flask app factory"
"""
from flask import Flask
from flask_cors import CORS
from config import DevelopmentConfig

from scraper.scraper import Scraper

_scraper = Scraper()


# this function is the application factory
def create_app():
    global _scraper

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())
    CORS(app, resources={r'/*': {'origins': '*'}})

    from App import db
    from bson.json_util import dumps, loads

    from .routes import api
    app.register_blueprint(api, url_prefix='/api/v1')           # blueprints for api
    _spiders = _scraper.get_all_spiders()                        # get list of all spiders
    if db.mongoatlas.client is not None:
        _spider_col = loads(dumps(db.spider_col.find()))     # db queries

        if len(_spiders) > 0:                                       # ensuring correct spider on database
            new_spider = [s for s in _spiders if not any(_s['name'] in s for _s in _spider_col)]    # filter
            if len(new_spider) > 0:
                for n in new_spider:
                    db.spider_col.insert_one({"name": n})    # adding new if not exist on database
    return app












