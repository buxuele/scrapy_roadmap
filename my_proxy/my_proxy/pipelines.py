# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


# todo  也许这种写法有点繁琐，但是目前还是这样吧，以后再看看怎么修改
# 使用框架的话， 难免有些地方是固定的。
class MongoPipeline:
    collection = 'proxies_coll'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    # 这里不放在初始化的原因，应该是为了能改写设置中的2个常量。？？？？
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close(self, spider):
        self.client.close()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
        )

    def process_item(self, item, spider):
        coll = self.db[self.collection]         # 就是最初的 collection = 'raw_proxies'
        data = dict(item)
        coll.insert_one(data)
        return item









