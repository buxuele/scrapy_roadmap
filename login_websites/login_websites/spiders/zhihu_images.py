# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/3/15 0015 7:38 
# contact: fanchuangwater@gmail.com
# about:  爬取知乎。

import re
import json
import scrapy
from scrapy import Request
from login_websites.items import ZhihuItem
from utils.secret import zhihu_cookies as st_cookies


# 1. 爬取一个用户的全部图片。
# 2. 爬取一个问题下的全部图片。
# 3. 爬取一个话题下的全部图片。
class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    # url = 'https://www.zhihu.com/people/mike-leaf'     #  叶修著有《学习的逻辑》《深度思维》，研究中学生高效学习策略
    url = 'https://www.zhihu.com/people/fan-fan-85-56-77'    #  扮猫骑老虎工程师

    """
    # 从个人主页进来就是 xhr,  且 api 没什么具体规则。而且从的别处发送了请求数据。
    """

    @staticmethod
    def make_cookies(str_cookies):
        ret = {}
        for i in str_cookies.split('; '):
            idx = i.find('=')
            left = i[:idx]
            right = i[idx + 1:]
            ret[left] = right
        return ret

    # todo 知乎这个暂时写不了。因为有点难度。有时间的话， 看看别人是怎么写的。
    # def start_requests(self):
    #     cookies = self.make_cookies(st_cookies)
    #     #  # 根据传入的 网页url 来构造 实际请求 api的url
    #     t = re.findall(r'\d+', self.url)[0]
    #     yield Request(self.url, cookies=cookies, callback=self.parse)
    #
    # def parse(self, response, **kwargs):
    #     item = ZhihuItem()
    #     resp = json.loads(response.text)
    #     for i in resp['items']:
    #         item['title'] = i['target']['status']['text'].replace('\r\n', '')
    #         item['image_url'] = i['target']['status']['images'][0]['large']['url']     # 这里简化处理了。只要一张图片
    #         yield item
