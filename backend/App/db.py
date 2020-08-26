#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__version__ = "0.0.1"
__email__ = "dreadlordn@gmail.com"
__status__ = "Production"
__license__ = "GPL-3"
__copyright__ = "Copyright 2020, PandorAstrum"
__date__ = 8/26/2020
__desc__ = "MongoDB atlas utilities"
"""
import json
import datetime
from bson import ObjectId
from flask_pymongo import pymongo
from pymongo import uri_parser

CONNECTION_STRING = "mongodb+srv://mongo_admin:starwars0@cluster0.zbsaw.mongodb.net/reflect3746?retryWrites=true&w=majority"


class DB(object):
    def __init__(self):
        self.client = None
        self.db = None
        self.db_name = None
        self.node_list = None
        self.username = None
        self.error = None
        self.connect()
        self.connect_db()

    def connect(self):
        try:
            self.client = pymongo.MongoClient(CONNECTION_STRING)
        except pymongo.errors.ConnectionFailure as e:
            self.client = None
            self.error = f"Could not connect to MongoDB: {e}"
        except pymongo.errors.ServerSelectionTimeoutError as e:
            self.client = None
            self.error = f"Mongodb server not responding: {e}"
        except pymongo.errors.ExecutionTimeout as e:
            self.client = None
            self.error = f"Execution took too long: {e}"
        except pymongo.errors.InvalidURI as e:
            self.client = None
            self.error = f"Invalid database URI: {e}"
        except pymongo.errors.NetworkTimeout as e:
            self.client = None
            self.error = f"Network Error: {e}"
        except pymongo.errors.OperationFailure as e:
            self.client = None
            self.error = f"Bad Operations: {e}"
        except pymongo.errors.ConfigurationError as e:
            self.client = None
            self.error = f"Configuration Error: {e}"

    def connect_db(self, dbname="reflect3746"):
        if self.client is not None:
            self.db = self.client.get_database(dbname)
            parsed = uri_parser.parse_uri(CONNECTION_STRING)
            self.db_name = parsed['database']
            self.node_list = parsed['nodelist']
            self.username = parsed['username']
            return self.db
        return None

    def get_collection(self, collection_name):
        if self.client is not None and self.db is not None:
            return pymongo.collection.Collection(self.db, collection_name)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, datetime.datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)


json_encoder = JSONEncoder()
mongoatlas = DB()
spider_col = mongoatlas.get_collection('spiders')
scraped_col = mongoatlas.get_collection('scraped')
logs_col = mongoatlas.get_collection('logs')


