#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__version__ = "0.0.1"
__email__ = "dreadlordn@gmail.com"
__status__ = "Production"
__license__ = "GPL-3"
__copyright__ = "Copyright 2019, PandorAstrum"
__date__ = 8/25/2020
__desc__ = "Description about this file and what it does"
"""
from flask import Flask
from flask_cors import CORS

from bson.json_util import dumps, loads
from scraper.scraper import Scraper
from config import DevelopmentConfig

# create the database object


# scraper object
scraper = Scraper()


# this function is the application factory
def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())
    CORS(app, resources={r'/*': {'origins': '*'}})

    from App import db
    from .routes import api
    app.register_blueprint(api, url_prefix='/api/v1')  # blueprints for api
    _spiders = scraper.get_all_spiders()

    if len(_spiders) > 0:
        _spider_col = loads(dumps(db.spider_collection.find()))
        new_spider = [s for s in _spiders if not any(_s['name'] in s for _s in _spider_col)]
        if len(new_spider) > 0:
            for n in new_spider:
                db.spider_collection.insert_one({"name": n})

    return app












