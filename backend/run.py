#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import jsonify
# @crochet.run_in_reactor
# def scrape_with_crochet(baseURL):
#     # This will connect to the dispatcher that will kind of loop the code between these two functions.
#     dispatcher.connect(_crawler_result, signal=signals.item_scraped)
#     # This will connect to the ReviewspiderSpider function in our scrapy file and after each yield will pass to the crawler_result function.
#     eventual = crawl_runner.crawl(DefaultSpider, _url=baseURL)
#     return eventual
#
#
# # This will append the data to the output data list.
# def _crawler_result(item, response, spider):
#     output_data.append(dict(item))


# @app.route('/api/v1.0/run', methods=['POST'])
# def submit():
#     if request.method == 'POST':
#         s = request.form['url']  # Getting the Input Amazon Product URL
#         global baseURL
#         baseURL = s
#
#         # This will remove any existing file with the same name so that the scrapy will not append the data to any previous file.
#         if os.path.exists("<path_to_outputfile.json>"):
#             os.remove("<path_to_outputfile.json>")
#
#         return redirect(url_for('scrape'))  # Passing to the Scrape function
#
#
# @app.route('/api/v1.0/scrape', methods=['GET'])
# def scrape():
#     scrape_with_crochet(baseURL=baseURL)  # Passing that URL to our Scraping Function
#
#     time.sleep(20)  # Pause the function while the scrapy spider is running
#
#     return jsonify(output_data)  # Returns the scraped data after being running for 20 seconds.


# @app.route('/api/v1.0/getscraper', methods=['GET'])
# def getscraper():
#     # get scrapper list
#     _project_settings = get_project_settings()
#     spider_loader = spiderloader.SpiderLoader.from_settings(_project_settings)
#     _spiders = spider_loader.list()
#     _spider_classes = [spider_loader.load(name) for name in _spiders]
#     # post run scrapper
#     return jsonify({"spiders":_spider_classes})

