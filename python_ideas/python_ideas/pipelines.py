from itemadapter import ItemAdapter
import pymongo

# class PythonIdeasPipeline:
#     def process_item(self, item, spider):
#         return item


class MongoPipeline:
    collection = 'python_ideas3'

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
        coll = self.db[self.collection]
        data = dict(item)
        coll.insert_one(data)
        return item
