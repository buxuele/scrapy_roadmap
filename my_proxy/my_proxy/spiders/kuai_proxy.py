# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/3/1 0001 17:13 
# contact: fanchuangwater@gmail.com
# about:


import scrapy
from bs4 import BeautifulSoup
from my_proxy.items import MyProxyItem


class SmallProxySpider(scrapy.Spider):
    name = 'p2'
    allowed_domains = ['kuaidaili.com']
    # inha 这里全是国内的代理
    start_urls = [f'https://www.kuaidaili.com/free/inha/{x}' for x in range(1, 11)]

    def parse(self, response):
        item = MyProxyItem()
        resp = BeautifulSoup(response.text, 'lxml')

        tb = resp.find('tbody').find_all('tr')
        for t in tb:
            item['ip'] = t.find('td', attrs={"data-title": "IP"}).text
            item['port'] = t.find('td', attrs={"data-title": "PORT"}).text
            item['protocol'] = t.find('td', attrs={"data-title": "类型"}).text
            item['is_china'] = True
            yield item



