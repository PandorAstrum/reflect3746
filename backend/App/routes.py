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
from flask import Blueprint, jsonify, make_response, request
from .models import Spider
from . import db

api = Blueprint('api', __name__, template_folder='templates')


@api.route('/server_status', methods=["GET"])
def server_status():
    """Ping Server to check if it is running"""
    return jsonify("ok")


@api.route('/database_status', methods=["GET"])
def database_status():
    """Check if database table exist and connection established"""
    try:
        # connect database path
        # check database connection
        # check database table
        pass
    except:
        pass
    return jsonify("not okay")


@api.route('/spider', methods=["GET", "POST"])
def spider():
    """Query Spider or Create one"""
    if request.method == "POST":
        """Create a spider via query string parameters."""
        name = request.args.get('name')
        new_spider = ''
        if name:
            new_spider = Spider(name=name)
            db.session.add(new_spider)  # Adds new User record to database
            db.session.commit()  # Commits all changes
        return Spider.get_delete_put_post(new_spider)
    else:
        return Spider.get_delete_put_post()


@api.route('/run', methods=["POST"])
def spider_run():
    # check if the website is previously scraped if so return pointer to database
    # if not start scraping and dump data
    pass