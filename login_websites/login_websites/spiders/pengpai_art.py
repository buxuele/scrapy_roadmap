# -*- coding: utf-8 -*-
# Author:       fanchuang
# DateTime:     2021/3/26 0026 20:39 
# Contact:      baogebuxuele@163.com
# Github:       https://github.com/buxuele 
# About:        爬取澎湃官网--艺术评论类目下的图片。https://www.thepaper.cn/list_25455
# todo:         以后也可以试试爬其他类目的东西，比如翻书党: https://www.thepaper.cn/list_80623


import re
import json
import time
import scrapy
from scrapy import Request
from bs4 import BeautifulSoup
from login_websites.items import PengpaiItem


class PengpaiSpider(scrapy.Spider):
    name = 'pengpai'
    home_url = 'https://www.thepaper.cn/'
    allowed_domains = ['thepaper.cn']
    custom_settings = {
        # 'CLOSESPIDER_ITEMCOUNT': '500',
        'ITEM_PIPELINES': {'login_websites.pipelines.PengpaiPipeline': 290},
        'IMAGES_STORE': f'E:\爬虫结果\图片\澎湃艺术评论_{time.strftime("%Y-%m-%d_%H-%M-%S")}',
    }

    # 数量还是需要稍微控制一下的。
    def start_requests(self):
        for i in range(1, 5):
            u = f'https://www.thepaper.cn/load_index.jsp?nodeids=25455&topCids=,11810886,11677312,11765395,11746075&pageidx={i}&isList=true&lastTime=1615263560979'
            yield Request(u, callback=self.parse_json)

    def parse_json(self, response, **kwargs):
        resp = BeautifulSoup(response.text, 'lxml')
        junk = resp.find_all('a', attrs={'class': 'tiptitleImg'})
        for j in junk:
            u = self.home_url + j.get('href')
            yield Request(u, callback=self.parse_img)

    def parse_img(self, response, **kwargs):
        item = PengpaiItem()
        soup = BeautifulSoup(response.text, 'lxml')

        article = soup.find('div', attrs={'class': 'news_txt'})
        item['image_urls'] = [x.get('src') for x in article.find_all('img')]
        yield item
