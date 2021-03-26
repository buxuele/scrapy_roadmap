# -*- coding: utf-8 -*-
# Author:       fanchuang
# DateTime:     2021/3/21 0021 17:43 
# Contact:      baogebuxuele@163.com
# Github:       https://github.com/buxuele 
# About:

import re
import scrapy
from bs4 import BeautifulSoup
from book.items import BookItem


#  真是搞笑啊。 难怪我总是觉得不对劲，原来是是这个网站本身的内容就是错的。真是搞笑啊。
class KankanSpider(scrapy.Spider):
    name = 'shici'
    # allowed_domains = ['shicimingju.com']
    base = 'https://www.shicimingju.com'
    start_urls = ['https://www.shicimingju.com/book/']  # 我国古代书籍，古典文学书，历史书
    custom_settings = {
        'COOKIES_ENABLED': False,
    }

    # 每本书的首页
    def parse(self, response, **kwargs):
        soup = BeautifulSoup(response.text, "lxml")
        chunk = soup.find_all('a', href=re.compile('/book/\w+\.html'))
        for a in chunk:
            yield scrapy.Request(self.base + a.get('href'), callback=self.parse_book)

    # 每本书的第一章, 传递书名。
    def parse_book(self, response, **kwargs):
        soup = BeautifulSoup(response.text, "lxml")
        first_chap = soup.find('a', href=re.compile('^/book/\w+/1\.html'))
        book_name = soup.find('h1').text
        yield scrapy.Request(self.base + first_chap.get('href'), callback=self.parse_content, cb_kwargs={"book_name": book_name})

    # 每一章的 标题，内容
    def parse_content(self, response, **kwargs):
        item = BookItem()
        soup = BeautifulSoup(response.text, "lxml")
        same_name = response.cb_kwargs.get('book_name')

        item['book_name'] = same_name
        item['chapter_title'] = soup.find('h1').text
        item['chapter_content'] = soup.find('div', attrs={'class': 'chapter_content'}).text
        # yield item

        next_page = [x for x in soup.find_all('a') if x.text == '下一章']
        if next_page:
            print(self.base + next_page[0].get('href'))
            yield scrapy.Request(self.base + next_page[0].get('href'), callback=self.parse_content, cb_kwargs={"book_name": same_name})
        else:
            print("working on: ", response.url)
            print()
