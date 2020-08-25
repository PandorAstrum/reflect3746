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

from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://mongo_admin:starwars0@cluster0.zbsaw.mongodb.net/reflect3746?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('reflect3746')
spider_collection = pymongo.collection.Collection(db, 'spiders')
scraped_collection = pymongo.collection.Collection(db, 'scraped')
