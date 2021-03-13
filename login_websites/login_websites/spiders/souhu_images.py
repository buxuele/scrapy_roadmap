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

"""
关于 article-url 与 api-url 之间有2点需要注意:
1. 从作者的主页（目前）还无法直接获取这个作者的id, 但是随便从作者的一个一篇文章入手，则可以获取该作者的 id.
   因此需要传入作者的任意一篇文章的 url,即可。
2. api-url 这里的secretStr，这里开始吓我一跳，实际上不加上也没事的，一样能取到数据。
3. 另外听说搜狐限定只能从 api 中取出 1000 条数据，待验证。
"""


class SohuSpider(scrapy.Spider):
    name = 'hu'
    allowed_domains = ['sohu.com']

    url = 'https://www.sohu.com/a/453502899_584699?spm=smpc.author.fd-d.32.1615601091157zDkhATv'  # 书法
    str_cookies = 'SUV=1599150263935ncd246; gidinf=x099980109ee12100ee2de45a0006b576830a79ffbea; _muid_=1609058969178956; OUTFOX_SEARCH_USER_ID_NCOO=1531278692.9789631; IPLOC=CN3101; t=1615588161292; reqtype=pc'

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


