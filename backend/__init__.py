#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, url_for
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy

import crochet
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
from scraper.scraper.spiders.default import DefaultSpider

# Initialize app
app = Flask(__name__)
app.config.from_object('config')


# configuration
DEBUG = True                                                # debug
CORS(app, resources={r'/*': {'origins': '*'}})              # enable CORS
db = SQLAlchemy(app)                                        # Use SQLAlchemy with this app

# crotchet setup
crochet.setup()
output_data = []
crawl_runner = CrawlerRunner()