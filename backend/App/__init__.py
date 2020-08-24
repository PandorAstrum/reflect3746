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
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# create the database object
from scraper.scraper import Scraper

db = SQLAlchemy()


# this function is the application factory
def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    with app.app_context():
        CORS(app, resources={r'/*': {'origins': '*'}})          # enable CORS

        db.create_all(app=app)                                  # create tables only once

        from .routes import api
        app.register_blueprint(api, url_prefix='/api/v1')  # blueprints for api
        scraper = Scraper()
        print(scraper.get_all_spiders())
        # get list of spider from scrapy
        # commit to database with their name
        return app





