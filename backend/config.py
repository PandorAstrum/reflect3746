#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    FLASKDIR = os.path.join(BASEDIR, "App")  # flask app dir
    FLASK_DEBUG = False  # app environment
    DEBUG = False
    MONGO_URI = 'mongodb+srv://mongo_admin:starwars0@cluster0.zbsaw.mongodb.net/reflect3746?retryWrites=true&w=majority'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'database.db')  # database path
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # sqlite3 dont use
    SQLALCHEMY_ECHO = False


class TestingConfig(Config):
    """App testing env"""
    TESTING = True



