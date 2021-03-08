# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/3/2 0002 21:12 
# contact: fanchuangwater@gmail.com
# about:


import re
import scrapy
from bs4 import BeautifulSoup
from book.items import BookItem


"""
1. 九九藏书网 https://www.99csw.com./index.php
2. ！！！！其实这个网站是有点意思的。因为每一个内容页，源码里面隐藏了一些 [脏东西]， 所以需要想办法来解除它。这里还没解决。！！！！
3. 
"""


class CSWSpider(scrapy.Spider):
    name = 'c1'
    allowed_domains = ['99csw.com']

    # 爱丽丝门罗
    # start_urls = ['https://www.99csw.com/book/search.php?type=author&keyword=%E8%89%BE%E4%B8%BD%E4%B8%9D%C2%B7%E9%97%A8%E7%BD%97']

    # 诺贝尔文学奖
    start_urls = ['https://www.99csw.com/book/search.php?s=13139900387823019677&type=%E7%AB%99%E5%86%85&q=%E8%AF%BA%E8%B4%9D%E5%B0%94%E6%96%87%E5%AD%A6%E5%A5%96']

    def parse(self, response, **kwargs):
        base = 'https://www.99csw.com'
        soup = BeautifulSoup(response.text, "lxml")
        junk = soup.find_all("a", attrs={"class": "Aimg"})
        for a in junk:
            u = a.get("href")
            yield scrapy.Request(base+u, callback=self.parse_book)

        next_page = soup.find('a', attrs={'class': 'other next'})
        if next_page:
            next_url = base + next_page.get('href')
            yield scrapy.Request(next_url, callback=self.parse)

    # 找到每一本书的第一章链接。
    def parse_book(self, response):
        base = 'https://www.99csw.com'
        soup = BeautifulSoup(response.text, "lxml")
        name = soup.find('h2').text.strip()
        chapter = soup.find('dl', attrs={"id": 'dir'}).find('a').get('href')
        yield scrapy.Request(base+chapter, callback=self.parse_content, meta={'book_name': name})

    # 进入并解析第一章。并递归地找到下一章。
    def parse_content(self, response):
        base = 'https://www.99csw.com'
        item = BookItem()
        soup = BeautifulSoup(response.text, "lxml")

        same_book_name = response.meta.get('book_name')
        item['book_name'] = same_book_name
        item['chapter_title'] = soup.find('h2').text
        item['chapter_content'] = soup.find('div', attrs={"id": "content"}).text
        yield item

        next_page = soup.find('a', attrs={'id': 'next'})
        if next_page:
            next_url = base + next_page.get('href')
            yield scrapy.Request(next_url, callback=self.parse_content, meta={'book_name': same_book_name})


