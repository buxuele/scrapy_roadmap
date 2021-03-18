# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/3/15 0015 7:38 
# contact: fanchuangwater@gmail.com
# about:  爬取知乎。

import re
import json
import scrapy
from scrapy import Request
from login_websites.items import DoubanItem
from utils.secret import zhihu_cookies


# 1. 爬取一个用户的全部图片。
# 2. 爬取一个问题下的全部图片。
# 3. 爬取一个话题下的全部图片。
class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['douban.com']
    url = 'https://www.douban.com/gallery/topic/152905/?from=discussing'    # 露台植物记

    # @staticmethod
    # def make_cookies(str_cookies):
    #     ret = {}
    #     for i in str_cookies.split('; '):
    #         idx = i.find('=')
    #         left = i[:idx]
    #         right = i[idx + 1:]
    #         ret[left] = right
    #     return ret
    #
    # def start_requests(self):
    #     cookies = self.make_cookies(self.str_cookies)
    #     t = re.findall(r'\d+', self.url)[0]    # 根据传入的 网页url 来构造 实际请求 api的url
    #     for i in range(50):
    #         u = f'https://m.douban.com/rexxar/api/v2/gallery/topic/{t}/items?from_web=1&sort=hot&start={i*20}&count=20&status_full_text=1&guest_only=0&ck=q0bA'
    #         yield Request(u, cookies=cookies, callback=self.parse)
    #
    # def parse(self, response, **kwargs):
    #     item = DoubanItem()
    #     resp = json.loads(response.text)
    #     for i in resp['items']:
    #         # todo 其实不必了。我本身不在意数据的完整性，只是想多看几张图片而已。以后再说吧。另外，真正的大图是在每位用户的主页里面。
    #         # 这里的 json 解析其实还是有点问题的，因为原始的 json 文件是不完全规则的，需要加上条件判断，目前没必要处理了。
    #         item['title'] = i['target']['status']['text'].replace('\r\n', '')
    #         item['image_url'] = i['target']['status']['images'][0]['large']['url']     # 这里简化处理了。只要一张图片
    #         yield item
