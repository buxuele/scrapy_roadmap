# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/3/1 0001 21:48 
# contact: fanchuangwater@gmail.com
# about: 校验代理。

import requests
from pymongo import MongoClient
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED


"""
1. 校验全部的代理
2. 提供简洁的接口， 给其他的项目。
3. 考虑另一种可能性: 直接在旧的数据上进行修改。
   即， 把失败的给删除掉。那么剩下的就是好用的。以后每次可以随时校验。
4. 这里的方式不对。 
5. 已经尝试过 aiohttp, multiprocessing.dummy.pool，目前都不合适。 再次回到多线程上来。
"""


class CheckProxy:
    def __init__(self):
        self.real_ip = self.find_myself()
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['proxies_db']
        # self.coll = self.db['proxies_coll']
        self.coll_name = 'proxies_coll'
        self.good = []       # 在内存中置换。

    @staticmethod
    def find_myself():
        target = 'http://httpbin.org/ip'
        resp = requests.get(target)
        return resp.json()["origin"]

    def check_status(self, dic):
        url = "http://httpbin.org/ip"
        p = {f'{dic["protocol"].lower()}': f'{dic["protocol"].lower()}://{dic["ip"]}:{dic["port"]}'}

        resp = requests.get(url, proxies=p, timeout=1)
        # 当前使用的代理 != 真实的ip: 代理是有效的。
        if resp.status_code == 200 and resp.json()["origin"] != self.real_ip:
            self.good.append(dic)

    def run(self):
        t1 = self.db[self.coll_name].count_documents({})
        raw_data = self.db[self.coll_name].find()
        with ThreadPoolExecutor(max_workers=50) as executor:
            future_tasks = [executor.submit(self.check_status, p) for p in raw_data]
            wait(future_tasks, return_when=ALL_COMPLETED)

        print("Origin proxy nums: ", t1)

        # delete old + add new.  Same coll name!
        print("Good proxy nums: ", len(self.good))
        self.db.drop_collection(self.coll_name)
        self.db[self.coll_name].insert_many(self.good)

        self.china()
        self.double_check()

    def double_check(self):
        k = self.db[self.coll_name].count_documents({})
        f = self.db["china"].count_documents({})
        c = self.db["world"].count_documents({})
        print("all: ", k)
        print("china: ", f)
        print("world: ", c)

    """
    这里索性再进一步，中外代理分类。 那么访问的话，直接就是:
    1. 如果需要国内的代理，就是直接访问 MongoClient('localhost', 27017)['proxies_db']['china']
    2. 如果需要国外的代理，就是直接访问 MongoClient('localhost', 27017)['proxies_db']['world']
    3. 如果需要全部的代理，就是直接访问 MongoClient('localhost', 27017)['proxies_db']['proxies_coll']
    4. 拼接  {f'{dic["protocol"].lower()}': f'{dic["protocol"].lower()}://{dic["ip"]}:{dic["port"]}'}
      
    或者是直接照抄下面的一小段代码 (也可以根据自己的情况来简化。):
    
    from pymongo import MongoClient
    data = MongoClient('localhost', 27017)['proxies_db']['china'].find()
    for dic in data:
        print({f'{dic["protocol"].lower()}': f'{dic["protocol"].lower()}://{dic["ip"]}:{dic["port"]}'})
    
    """
    def china(self):
        cn = []
        other = []
        if "china" in self.db.list_collection_names():
            self.db.drop_collection("china")
        if "world" in self.db.list_collection_names():
            self.db.drop_collection("world")

        for dic in self.db[self.coll_name].find():
            if dic['is_china']:
                cn.append(dic)
            else:
                other.append(dic)
        self.db['china'].insert_many(cn)
        self.db['world'].insert_many(other)

    # 临时测试用的。
    def drop_data(self):
        if "world" in self.db.list_collection_names():
            self.db.drop_collection("world")
            self.db.drop_collection("china")
            self.db.drop_collection("proxies_coll")


if __name__ == '__main__':
    s = CheckProxy()
    s.drop_data()


