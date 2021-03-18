# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/3/12 0012 4:13 
# contact: fanchuangwater@gmail.com
# about:  爬取搜狐上 赵孟頫的书法图片。


import re
import json
import scrapy
from scrapy import Request
from bs4 import BeautifulSoup
from login_websites.items import SouhuItem
from utils.secret import sohu_cookies

"""
从任意一篇文章入手，获取作者 id， 进而构造api-url, 进而获取全部内容
"""


class SohuSpider(scrapy.Spider):
    name = 'hu'
    allowed_domains = ['sohu.com']

    url = 'https://www.sohu.com/a/453502899_584699?spm=smpc.author.fd-d.32.1615601091157zDkhATv'  # 书法
    str_cookies = sohu_cookies
    @staticmethod
    def make_cookies(str_cookies):
        # 目前还是写一个解析的函数。
        # todo 这里最好是能写一个中间件，单独来处理这些 cookies  整个项目都需要使用这些 cookies
        ret = {}
        for i in str_cookies.split('; '):
            idx = i.find('=')
            left = i[:idx]
            right = i[idx + 1:]
            ret[left] = right
        print(ret)
        return ret

    def start_requests(self):
        cookies = self.make_cookies(self.str_cookies)
        t = re.findall(r'\d+', self.url)[1]    # 根据传入的 网页url 来构造 实际请求 api的url
        for i in range(1, 20):  # 200
            u = f'https://v2.sohu.com/author-page-api/author-articles/pc/{t}?pNo={i}'
            yield Request(u, cookies=cookies, callback=self.parse_json)

    def parse_json(self, response, **kwargs):
        resp = json.loads(response.text)
        junk = resp['data']['pcArticleVOS']
        for j in junk:
            url = 'https://' + j['link']
            yield Request(url, callback=self.parse_img)

    def parse_img(self, response, **kwargs):
        item = SouhuItem()
        soup = BeautifulSoup(response.text, 'lxml')

        article = soup.find('article', attrs={'id': 'mp-editor'})
        item['image_urls'] = [x.get('src') for x in article.find_all('img')]
        yield item


