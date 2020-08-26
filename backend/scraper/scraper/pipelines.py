# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from scrapy.exceptions import DropItem
from App import db
from itemadapter import ItemAdapter


class MongoPipeline:

    def __init__(self):
        self.mongo_collection = db.scraped_col

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            if "_id" in item:
                _id = item.pop("_id")
                self.mongo_collection.update_one({"_id": _id}, {"$set": item})
            # self.mongo_collection.insert(dict(item))
        return item

