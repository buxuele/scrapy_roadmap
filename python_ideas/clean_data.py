# -*- coding: utf-8 -*-
# Author:       fanchuang
# DateTime:     2021/3/26 0026 15:08 
# Contact:      baogebuxuele@163.com
# Github:       https://github.com/buxuele 
# About:

# 尝试简单的数据清理工作。

import datetime
from pymongo import MongoClient
from pprint import pprint


class Mongo:
    def __init__(self, db, collections):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[db]
        self.coll = self.db[collections]

    @property
    def all_data(self):
        return self.coll.find()

    # 'https://blog.csdn.net/hihell/article/details/115204870'
    def show_data(self):
        """
        Mongo("python_daily", "python_ideas3")
        all data is:  5811
        csdn:  510
        zhihu:  3801
        juejin:  1500
        """
        csdn = 0
        zhihu = 0
        juejin = 0
        for x in self.coll.find():
            # pprint(x['link'])

            if x['link'].startswith('https://blog.csdn.net'):
                csdn += 1
                # pprint(x)
            elif x['link'].startswith('http://www.zhihu.com'):
                zhihu += 1
                # pprint(x)
            else:
                juejin += 1
                # pprint(x)

        print("all data is: ", self.coll.count_documents({}))
        print("csdn: ", csdn)
        print("zhihu: ", zhihu)
        print("juejin: ", juejin)

    def check_repeat(self):
        unique = set()
        shit = set()
        for x in self.coll.find():
            if x["link"] not in unique:
                unique.add(x["link"])
            else:
                shit.add(x["link"])
        print("以下内容有重复！ 个数: ", len(shit))
        return shit

    def show_db(self):
        # 显示数据库，数据集的名称.
        db = self.client.list_database_names()
        print(db)
        for d in db:
            c = self.client[d].list_collection_names()
            print(d, "--->", c)

        # 临时删除一个数据库
        # self.client.drop_database("some_db")


if __name__ == '__main__':
    m = Mongo("python_daily", "python_ideas3")
    m.show_data()
    # m.get_unique(show=True)
