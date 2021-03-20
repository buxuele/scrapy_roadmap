# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/3/19 0019 15:17 
# contact: fanchuangwater@gmail.com
# about: 爬取简书的文章标题，随机漫步，不做过多的限定，只是练习。


import re
import json
import scrapy
from scrapy import Request
from bs4 import BeautifulSoup
from login_websites.items import JianShuItem
from utils.secret import jianshu_cookies as str_cookies


"""
1. 从首页入手，抓取首页的文章 list_A。
2. 然后依次访问 list_A, 每遇到新的文章，加入 list_A. 这里涉及去重。
3. 如果总访问页面达到了 1000， 则停止。
4. 结果保存为 json，别忘了设置 FEED_EXPORT_ENCODING = 'utf-8'，不然结果很难看。
"""


class SohuSpider(scrapy.Spider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    home = 'https://www.jianshu.com'
    custom_settings = {
        'CLOSESPIDER_ITEMCOUNT': '1000',
        'ITEM_PIPELINES': None,     # 直接命令行保存数据，json
    }

    @staticmethod
    def make_cookies(str_cookies):
        ret = {}
        for i in str_cookies.split('; '):
            idx = i.find('=')
            left = i[:idx]
            right = i[idx + 1:]
            ret[left] = right
        # print(ret)
        return ret

    # 首页
    def start_requests(self):
        cookies = self.make_cookies(str_cookies)
        yield Request(self.home, cookies=cookies, callback=self.parse_post)

    # 首页下的每一页
    def parse_post(self, response, **kwargs):
        soup = BeautifulSoup(response.text, 'lxml')
        urls = soup.find_all('a', attrs={'class': 'title'})
        for u in urls:
            yield response.follow(u.get("href"), callback=self.parse_data)

    # 每一页以及下面的推荐。
    def parse_data(self, response, **kwargs):
        """本来是想在正文中查找作者信息的，但是找不到。那么就换一种思路好了。"""
        item = JianShuItem()
        soup = BeautifulSoup(response.text, 'lxml')

        sec = soup.find('ul', attrs={'class': '_1iTR78'})
        if sec:
            more_stuff = sec.find_all('li', attrs={'class': '_11jppn'})
            for junk in more_stuff:
                item['author'] = junk.find('span', attrs={'class': '_3tPsL6'}).text
                item['author_url'] = self.home + junk.find('a', attrs={'class': '_3IWz1q _1OhGeD'}).get('href')
                item['title'] = junk.find('div', attrs={'class': 'em6wEs'}).text
                new_url = junk.find('a', attrs={'class': '_2voXH8 _1OhGeD'}).get('href')
                item['url'] = self.home + new_url
                yield item
                yield response.follow(new_url, callback=self.parse_data)




