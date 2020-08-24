# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    Website = scrapy.Field()
    Privacy_url = scrapy.Field()
    Terms_url = scrapy.Field()
    Cookie_url = scrapy.Field()
