# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/3/2 0002 18:38 
# contact: fanchuangwater@gmail.com
# about: 小幻代理。及其不稳定。

import json
import scrapy
from bs4 import BeautifulSoup
from my_proxy.items import MyProxyItem


class HuanProxySpider(scrapy.Spider):
    name = 'huan'
    allowed_domains = ['ip.ihuan.me']

    #  国内的代理，最好是请求这个地址。不确定是否会修改。如果需要大量的国内代理可以选这个。
    #  https://ip.ihuan.me/address/5Lit5Zu9.html
    start_urls = ['https://ip.ihuan.me/']

    # 限定爬虫
    custom_settings = {
        'CLOSESPIDER_ITEMCOUNT': '500',
    }

    def parse(self, response, **kwargs):
        item = MyProxyItem()
        soup = BeautifulSoup(response.text, 'lxml')
        tbody = soup.find('tbody').find_all('tr')
        for tr in tbody:
            data = [td.text for td in tr.find_all("td")]
            item['ip'] = data[0]
            item['port'] = data[1]
            if data[4] == "支持":
                item['protocol'] = "https"
            else:
                item['protocol'] = "http"
            if data[2].startswith("中国"):
                item['is_china'] = True
            else:
                item['is_china'] = False
            yield item

        next_page = soup.find('a', attrs={'aria-label': 'Next'}).get("href")
        base = "https://ip.ihuan.me/"
        if next_page:
            yield scrapy.Request(url=base+next_page, callback=self.parse)




