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
__desc__ = "Configuration for flask"
"""
import os


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(Config):
    """Config for production"""
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    """Config for development"""
    BASEDIR = os.path.abspath(os.path.dirname(__file__))  # root directory
    FLASK_DIR = os.path.join(BASEDIR, "App")  # flask app dir
    SCRAPER_DIR = os.path.join(BASEDIR, "scraper")  # flask app dir
    OUTPUT_DIR = os.path.join(SCRAPER_DIR, "output") # scraper output dir
    FLASK_DEBUG = False  # app environment
    FLASK_ENV = "development"
    DEBUG = False


class TestingConfig(Config):
    """App testing env"""
    TESTING = True



