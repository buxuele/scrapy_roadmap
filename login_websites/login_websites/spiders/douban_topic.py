# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/3/10 0010 2:49 
# contact: fanchuangwater@gmail.com
# about:

# 豆瓣话题，有很多原创的高质量图片
# 尝试登陆。直接使用 cookies

import re
import json
import scrapy
from scrapy import Request
from login_websites.items import DoubanItem
from utils.secret import douban_cookies


class DoubanSpider(scrapy.Spider):
    name = 'dou'
    allowed_domains = ['douban.com']
    url = 'https://www.douban.com/gallery/topic/166889/'    # 收集有趣的商品陈列方式
    custom_settings = {
        'ITEM_PIPELINES': {'login_websites.pipelines.SohuPipeline': 300,},
        'IMAGES_STORE': f'E:\爬虫结果\图片\豆瓣话题_收集有趣的商品陈列方式3',
    }

    @staticmethod
    def make_cookies(str_cookies):
        ret = {}
        for i in str_cookies.split('; '):
            idx = i.find('=')
            left = i[:idx]
            right = i[idx + 1:]
            ret[left] = right
        return ret

    # 根据传入的 网页url 来构造 实际请求 api的url
    def start_requests(self):
        cookies = self.make_cookies(douban_cookies)
        t = re.findall(r'\d+', self.url)[0]
        for i in range(2):
            u = f'https://m.douban.com/rexxar/api/v2/gallery/topic/{t}/items?from_web=1&sort=hot&start={i*20}&count=20&status_full_text=1&guest_only=0&ck=q0bA'
            yield Request(u, cookies=cookies, callback=self.parse)

    def parse(self, response, **kwargs):
        item = DoubanItem()
        resp = json.loads(response.text)
        for i in resp['items']:
            item['title'] = i['target']['status']['text'].replace('\r\n', '')
            item['image_urls'] = [x['large']['url'] for x in i['target']['status']['images']]
            yield item












