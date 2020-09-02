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
__desc__ = "API routes"
"""
import crochet
import json
import tldextract
from datetime import datetime

from flask import Blueprint, jsonify, request, make_response
from bson.json_util import dumps, loads
from bson.objectid import ObjectId
from pymongo import ReturnDocument
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from App import db
from scraper.scraper import Scraper

crochet.setup()                                             # initialize crochet
urls_list = []                                              # temp store urls
current_inserted = None                                     # new inserted doc in mongo
exact_domain = ""                                           # domain name from url
scrape_in_progress = False                                  # progress flag
scrape_complete = False                                     # complete flag
_selected_spider = None                                     # Selected Spider
_scraper = Scraper()
_crawl_runner = CrawlerRunner(_scraper.get_settings())    # requires the Twisted reactor to run

api = Blueprint('api', __name__, template_folder='templates')   # Blueprints

# END POINTS ====================================================================================
@api.route('/server_status', methods=["GET"])
def server_status():
    """Ping Server to check if it is running"""
    return jsonify({'host': request.host, 'Status': 200})


@api.route('/database_status', methods=["GET"])
def database_status():
    """Check if database table exist and connection established"""
    db.mongoatlas.connect()
    if db.mongoatlas.client is not None:
        db.mongoatlas.connect_db()
        db_name = db.mongoatlas.db_name
        username = db.mongoatlas.username
        nodes = db.mongoatlas.node_list[0]
        return jsonify({
            "Status": 200,
            "database": db_name,
            "nodes": nodes,
            "username": username
        })
    else:

        error_message = db.mongoatlas.error
        return jsonify({
            "Status": 404,
            "error": error_message
        })


@api.route('/spider', methods=["GET", "POST"])
def spider():
    """Query Spider or Create one"""
    if request.method == "POST":
        """Create a spider via query string parameters."""
        # get name and parameter from FORM
        # db collection add
        return
    if db.mongoatlas.client is not None:
        _spiders_col = loads(dumps(db.spider_col.find()))
        return db.json_encoder.encode(_spiders_col)
    return jsonify({"Status": 404, "msg": "Not Connected"})


@api.route('/run', methods=["POST"])
def spider_run():
    """start crawling"""
    global exact_domain
    global _selected_spider
    if request.method == "POST":
        params = request.get_json()                                 # get form
        spider_kwargs = params["spider_kwargs"]                     # get spider arguments
        _selected_spider = spider_kwargs['spider_name']
        spider_settings = params["spider_settings"]                 # get spider settings
        exact_domain = tldextract.extract(spider_kwargs["baseurl"]).registered_domain
        if db.scraped_col.count_documents({'domain': exact_domain}, limit=1) != 0:   # if already exist
            existed_content = [loads(dumps(db.scraped_col.find_one({'domain': exact_domain})))]
            return db.json_encoder.encode(existed_content)
        else:
            global scrape_in_progress
            global scrape_complete
            global urls_list
            if not scrape_in_progress:
                urls_list = []
                scrape_in_progress = True
                print(spider_settings)
                # build params for spider
                _spider_kwargs = {
                    "base_url": spider_kwargs['baseurl'],
                    "domain": exact_domain,
                    "spider_settings": spider_settings
                }

                scrape_with_crochet(_spider=_scraper.get_spider(_selected_spider),
                                    _kwargs=_spider_kwargs,
                                    _list_output=urls_list)                  # run spider
                return jsonify({"msg": "Scraping started"})
            elif scrape_complete:
                return jsonify({"msg": "Scraping Completed"})
            return jsonify({"msg": "Scraping in Progress"})


@api.route('/results', methods=["GET"])
def get_results():
    """
    Get the results only if a spider has results
    """
    global current_inserted
    global scrape_complete
    global scrape_in_progress
    if scrape_complete:
        if len(urls_list) > 0:
            return jsonify({"Status": 200, "msg": "Scraping Complete", "urls": urls_list,
                            "_id": str(current_inserted.inserted_id)})

    if scrape_in_progress:
        return jsonify({"Status": 102, "msg": "Scraping in progress"})
    return jsonify({"Status": 404, "msg": "Scraping Not Started"})


@api.route('/results/<result_id>', methods=["GET"])
def get_results_for(result_id):
    """
    Get the results of a single item
    """
    if db.mongoatlas.client is not None:
        returned_obj = [loads(dumps(db.scraped_col.find_one({"_id": ObjectId(result_id)})))]

        return db.json_encoder.encode(returned_obj)


@api.route('/all', methods=["GET"])
def all_results():
    """fetch all results from database"""
    if db.mongoatlas.client is not None:
        returned_obj = loads(dumps(db.scraped_col.find()))
        return db.json_encoder.encode(returned_obj)


@api.route('/logs', methods=["GET"])
def get_logs():
    """
    Get history of scraping from database
    """
    if db.mongoatlas.client is not None:
        all_logs = loads(dumps(db.logs_col.find()))
        return db.json_encoder.encode(all_logs)
    return jsonify({"Status": 200, "error": "Cant do it"})


@api.route('/mutations', methods=["POST"])
def mutate_entry():
    """Edit the urls edit or delete"""
    if request.method == "POST":
        params = request.get_json()                                                 # get form
        ids = params["_id"]                                                         # get doc id
        index = params["index"]                                                # get index of element
        url_modified = params["modified_entry"]                                     # new value

        if db.mongoatlas.client is not None:
            captured_doc = [loads(dumps(db.scraped_col.find_one_and_update(
                {'_id': ObjectId(ids)},
                {"$set": {f"urls.{index}": url_modified}},
                return_document=ReturnDocument.AFTER
            )))]
            return db.json_encoder.encode(captured_doc)


@api.route('/deletion', methods=["POST"])
def delete_entry():
    """Delete the urls edit or delete"""
    if request.method == "POST":
        params = request.get_json()                                                 # get form
        ids = params["_id"]                                                         # get doc id
        value = params['value']                                                     # get the value to be deleted

        if db.mongoatlas.client is not None:
            captured_doc = [loads(dumps(db.scraped_col.find_one_and_update(
                {'_id': ObjectId(ids)},
                {'$pull': {"urls": value}},
                return_document=ReturnDocument.AFTER
            )))]
            return db.json_encoder.encode(captured_doc)

# NECESSARY METHODS TO CALL =====================================================================
@crochet.run_in_reactor
def scrape_with_crochet(_spider, _kwargs, _list_output):
    global _crawl_runner
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    eventual = _crawl_runner.crawl(_spider, kwargs=_kwargs, urls_list=_list_output)
    eventual.addCallback(finished_scrape)


def finished_scrape(null):
    """
    A callback that is fired after the scrape has completed.
    Set a flag to allow display the results from /results
    """
    global scrape_complete
    global scrape_in_progress
    global urls_list
    global current_inserted
    global exact_domain
    global _selected_spider
    scrape_complete = True
    scrape_in_progress = False

    if len(urls_list) > 0:
        # build data model to insert into mongodb
        scraped = {
            "domain": exact_domain,
            "urls": urls_list,
        }
        current_inserted = db.scraped_col.insert_one(scraped)
        logs = {
            "spidername": _selected_spider,
            "domain": exact_domain,
            "found_urls": len(urls_list),
            "timestamp": datetime.now(),
            "job_id": current_inserted.inserted_id
        }
        returned_id_2 = db.logs_col.insert_one(logs)
