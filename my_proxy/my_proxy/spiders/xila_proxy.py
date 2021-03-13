# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/3/13 0013 19:42 
# contact: fanchuangwater@gmail.com
# about:

import json
import scrapy
from bs4 import BeautifulSoup
from my_proxy.items import MyProxyItem


# 不稳定，响应慢！
class HuanProxySpider(scrapy.Spider):
    name = 'xila'
    allowed_domains = ['xiladaili.com']
    start_urls = ['http://www.xiladaili.com/gaoni/']

    custom_settings = {
        'CLOSESPIDER_ITEMCOUNT': '500',
        'DOWNLOAD_DELAY': 5,
    }

    def parse(self, response, **kwargs):
        item = MyProxyItem()
        soup = BeautifulSoup(response.text, 'lxml')
        tbody = soup.find('tbody').find_all('tr')
        for tr in tbody:
            data = [td.text for td in tr.find_all("td")][:2]
            item['ip'] = data[0].split(':')[0]
            item['port'] = data[0].split(':')[1]
            if data[0][1].startswith("HTTPS"):
                item['protocol'] = "https"
            else:
                item['protocol'] = "http"
            item['is_china'] = True
            yield item

        next_page = soup.find_all('a', attrs={'class': 'page-link'})[-1].get('href')
        base = "http://www.xiladaili.com"
        if next_page:
            yield scrapy.Request(url=base+next_page, callback=self.parse)