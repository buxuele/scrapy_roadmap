import datetime
from pymongo import MongoClient
from pprint import pprint



class Mongo2:
    """
    # 如果是想避免数据库名称有重复，可以按照下面的写法继续写下去。
    # 就单纯地初始化一个 MongoClient， 就有很多东西可以写。
    # 进行初始化，这里是最安全的地方。
    """
    def __init__(self, db, coll):
        self.client = MongoClient('localhost', 27017)

        # if db in self.client.list_databases():
        self.db = self.client[db]

        if coll in self.db.list_collection_names():
            # warnings.warn(f"*** {coll} *** already exits! Please give me a new one!")     # 没执行！！！
            self.db.drop_collection(coll)
        self.coll = self.db[coll]

    def __str__(self):
        return f'{self.coll}'


class Mongo:
    def __init__(self, db, collections):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[db]
        self.coll = self.db[collections]

    @staticmethod
    def read_raw_data():
        good = []

        urls = [{"url": u.rstrip()} for u in good]
        return urls

    def add_to_db(self, data):
        self.coll.insert_one(data)

    # 插入多个值。 这个 仅仅 是本地临时调试用的。
    def insert_temp_data(self):
        data = self.read_raw_data()
        self.coll.insert_many(data)

    # 插入多个值专为 爬虫准备过程中准备的。
    def insert_bulk_data(self, list_data):
        self.coll.insert_many([{"url": u} for u in list_data])

    def get_data(self):
        return self.coll.find()

    def show_data(self):
        for x in self.coll.find():
            pprint(x)
        print("all data is: ", self.coll.count_documents({}))

    # check_repeat
    # get_unique
    # 这里写的简直就是狗屎一样。
    def check_repeat(self):
        unique = set()
        shit = set()
        for x in self.coll.find():
            if x["url"] not in unique:
                unique.add(x["url"])
            else:
                shit.add(x["url"])
        print("以下内容有重复！ 个数: ", len(shit))
        return shit

    def get_unique(self, show=False):
        unique = []
        for x in self.coll.find():
            if x["url"] not in unique:
                unique.append(x["url"])

        if show:
            pprint(unique)
        print("唯一的个数是： ", len(unique))
        return unique

    def show_db(self):
        # 正确 显示数据库名称，与数据集合的名称.这里也可以逐个检测每个数据集的大小。用于筛选。
        db = self.client.list_database_names()
        print(db)
        print()

        for d in db:
            c = self.client[d].list_collection_names()
            print(d, "--->", c)

        # 删除一个  数据库
        # self.client.drop_database("china")


if __name__ == '__main__':
    # m = Mongo("china", "y7")
    m = Mongo("proxies_db", "proxies_coll")               # 17231
    # m = Mongo('github', 'a1')

    m.show_data()
    # m.get_unique(show=True)
