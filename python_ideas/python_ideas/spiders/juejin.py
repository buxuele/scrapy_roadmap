# -*- coding: utf-8 -*-
# Author:       fanchuang
# DateTime:     2021/3/25 0025 17:49 
# Contact:      baogebuxuele@163.com
# Github:       https://github.com/buxuele 
# About:

import json
import time
import base64
import scrapy
from scrapy import Request
from python_ideas.items import PythonIdeasItem

"""
 掘金  https://juejin.cn/backend/Python
1. 注意是 POST 请求
2. 同理，一定要把 cookies 打开。# 也许不必了，待测试。
3. post data 里面有一个东西被加密了，base64 天天见。
4. 
"""


class JuejinSpider(scrapy.Spider):
    name = 'juejin'
    allowed_domains = ['juejin.cn']
    u = 'https://api.juejin.cn/recommend_api/v1/article/recommend_cate_tag_feed'
    payload = {"id_type": 2, "sort_type": 200, "cate_id": "6809637769959178254", "tag_id": "6809640448827588622",
               "limit": 20}

    custom_settings = {
        'COOKIES_ENABLED': True,
        'CLOSESPIDER_ITEMCOUNT': '2000',
        'DEFAULT_REQUEST_HEADERS': {
            'content-type': 'application/json',  # 这一行是必不可少的。
            'cookie': 'MONITOR_WEB_ID=6dff4ae8-490d-4ea0-b3d2-c150ddf0daf2; _ga=GA1.2.1778178177.1608561846',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
        }
    }

    # 构造 api-url. 这里需要 post 一个字典。
    def start_requests(self):
        yield Request(self.u, method="POST", body=json.dumps(self.payload), callback=self.parse_json, dont_filter=True)

    # 找到文章 author_user_info https://juejin.cn/user/2400989125030840
    def parse_json(self, response, **kwargs):
        item = PythonIdeasItem()
        resp = json.loads(response.text)
        # print(resp['data'])

        junk = resp['data']
        for j in junk:
            item['title'] = j['article_info']['title']
            item['link'] = 'https://juejin.cn/post/' + j['article_id']
            item['author'] = j['author_user_info']['user_name']
            item['author_home'] = 'https://juejin.cn/user/' + j['author_user_info']['user_id']
            item['publish_time'] = j['article_info']['mtime']
            print(item)
            yield item

        new_payload = {"id_type": 2, "sort_type": 200, "cate_id": "6809637769959178254",
                       "tag_id": "6809640448827588622",
                       "limit": 20}
        for i in range(1, 101):
            # time.sleep(1)
            temp_dic = {"v": "6943765223379566599", "i": i * 20}
            new_dic = {"cursor": self.b64encode_dict(temp_dic)}
            new_payload.update(new_dic)
            yield Request(self.u, method="POST", body=json.dumps(new_payload), callback=self.parse_json,
                          dont_filter=True)

    @staticmethod
    def b64encode_dict(dic):
        dic_bytes = bytes(json.dumps(dic), encoding='utf-8')  # 必须指定 encoding
        bb = base64.b64encode(dic_bytes)  # 只接受 bytes 类型。
        # print(bb.decode('utf-8'))
        return bb.decode('utf-8')
