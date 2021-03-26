# -*- coding: utf-8 -*-
# Author:       fanchuang
# DateTime:     2021/3/25 0025 16:14 
# Contact:      baogebuxuele@163.com
# Github:       https://github.com/buxuele 
# About:


import json
import time
import scrapy
from scrapy import Request
from python_ideas.items import PythonIdeasItem


"""
针对 csdn 这个网站
1. 一定要把 cookies 打开。因为请求api的url是不变的，那么实际请求的信息中，变化的的那一部分一定是在 cookies里面。
"""


class CSDNSpider(scrapy.Spider):
    name = 'csdn'
    base = 'https://www.csdn.net'
    allowed_domains = ['csdn.net']
    custom_settings = {
        'COOKIES_ENABLED': True,
        'CLOSESPIDER_ITEMCOUNT': '1000',
    }

    # 构造 api-url.
    def start_requests(self):
        u = 'https://www.csdn.net/api/articles?type=more&category=python&shown_offset=0'
        yield Request(u, callback=self.parse_json, dont_filter=True)

    # 找到文章
    def parse_json(self, response, **kwargs):
        cnt = 0
        item = PythonIdeasItem()
        resp = json.loads(response.text)
        # print(resp)

        junk = resp['articles']
        for j in junk:
            item['title'] = j['title']
            item['link'] = j['url']
            item['author'] = j['user_name']
            item['author_home'] =j['user_url']
            item['publish_time'] = j['shown_time']  # 1616663622
            # print(item)
            yield item

        if cnt < 50:
            time.sleep(1)   # 没法加快了。不然返回的是重复内容。
            u = 'https://www.csdn.net/api/articles?type=more&category=python&shown_offset=0'
            yield Request(u, callback=self.parse_json, dont_filter=True)


