# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from book.items import BookItem


"""
todo 再写几个别的图书网站的爬虫 也放在这里。
这个网站我只想下载特定类目下的图书。比如诺贝尔文学奖这个类别。

"""


# todo 网速很差劲。
class KankanSpider(scrapy.Spider):
    name = 'k1'
    allowed_domains = ['kanunu8.com']
    start_urls = ['https://www.kanunu8.com/files/16.html']  # 诺贝尔文学奖这个类别。

    def parse(self, response, **kwargs):
        item = BookItem()
        soup = BeautifulSoup(response.text, "lxml")

        chunk = soup.find('td').find_all('a')
        for a in chunk:
            print(a)


