#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))
appdir = os.path.join(basedir, "App")
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')           # database path
SQLALCHEMY_TRACK_MODIFICATIONS = False                                                  # dont use
SQLALCHEMY_ECHO = False
