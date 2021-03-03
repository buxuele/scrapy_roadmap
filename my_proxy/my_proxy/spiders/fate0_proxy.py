# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/2/28 0028 17:03
# contact: fanchuangwater@gmail.com
# about:    


import os
import time
import shutil
import zipfile
import json
import requests
from pymongo import MongoClient

"""
# {'port': 80, 'country': 'SA', 'host': '77.232.100.132', 'export_address': ['77.232.100.132'], 
# 'from': 'freeproxylist', 'anonymity': 'high_anonymous', 'response_time': 1.6, 'type': 'http'}
# 这个文件不使用 scrapy 但是我也放到这里， 因为在功能上保持一致性！
# 这里只是获取批量的代理，解析的话，在别的地方，统一执行。
"""


class SecondProxy:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client["proxies_db"]
        self.coll = self.db["proxies_coll"]

    # 完成任务后，删除用过的临时文件，防止下次出错。
    @staticmethod
    def clear_space():
        # 也许可以留下备份，也许没必要了。
        temp_dir = r"E:\爬虫结果\temp"
        temp_zip = "temp_file.zip"
        if temp_zip in os.listdir(temp_dir):
            os.remove(f"{temp_dir}\\{temp_zip}")
        if 'proxylist-master' in os.listdir(temp_dir):
            shutil.rmtree(os.path.normpath(f"{temp_dir}\\proxylist-master"))

    def clone_zip(self):
        temp_dir = r"E:\爬虫结果\temp"
        temp_zip = r"E:\爬虫结果\temp\temp_file.zip"

        # 1. 下载
        url = "https://github.com/fate0/proxylist/archive/master.zip"
        h = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
             'accept-encoding': 'gzip, deflate, br',
             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
             }
        ret = requests.get(url, headers=h)
        if ret.status_code == 200:
            with open(temp_zip, "wb") as f:
                f.write(ret.content)
        else:
            print("Internet broken!")
        time.sleep(0.2)

        # 2. 解压
        if "temp_file.zip" in os.listdir(temp_dir):
            with zipfile.ZipFile(temp_zip, 'r') as zzz:
                zzz.extractall(path=temp_dir)       # 解压全部文件，并保存到当前文件目录

        # 3. 读取，解析这批代理文件
        ret_file = f'{temp_dir}\\proxylist-master\\proxy.list'
        with open(ret_file, 'r') as g:
            for d in g.readlines():
                food = {}
                proxy = json.loads(d)
                food['ip'] = proxy['host']
                food['port'] = str(proxy['port'])
                food['protocol'] = proxy['type']
                if proxy['country'] == 'CN':
                    food['is_china'] = True
                else:
                    food['is_china'] = False
                # print(food)
                self.coll.insert_one(food)

    def run(self):
        self.clear_space()
        self.clone_zip()
        time.sleep(5)
        self.clear_space()


if __name__ == '__main__':
    s = SecondProxy()
    s.run()




































