# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# """
# __author__ = "Ashiquzzaman Khan"
# __version__ = "0.0.1"
# __email__ = "dreadlordn@gmail.com"
# __status__ = "Production"
# __license__ = "GPL-3"
# __copyright__ = "Copyright 2020, PandorAstrum"
# __date__ = 8/25/2020
# __desc__ = "Database Model (Spider Table, Data Table)"
# """
from datetime import datetime
# from flask_serialize import FlaskSerializeMixin
#
# FlaskSerializeMixin.db = db
#
#
# class Spider(db.Model, FlaskSerializeMixin):
#     """
#     A database model for spiders
#     """
#     __tablename__ = 'spider-model'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), index=True, nullable=False)
#
#     def __repr__(self):
#         return '<Spider %r>' % self.name
#
#
# class Data(db.Model, FlaskSerializeMixin):
#     """
#     A database model for scraped Data
#     """
#     __tablename__ = 'data-model'
#     id = db.Column(db.Integer, primary_key=True)
#     # spider = db.Column(db.String(100), db.ForeignKey('Spider.name'), nullable=False)
#     runs_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
#     website = db.Column(db.String(256), nullable=False)
#     terms_url = db.Column(db.Text)
#     privacy_url = db.Column(db.Text)
#     cookie_url = db.Column(db.Text)
#     error = db.Column(db.Text)
#
#     def __repr__(self):
#         return '<Data %r>' % self.website
