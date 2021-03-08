# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/2/27 0027 0:52
# contact: fanchuangwater@gmail.com
# about:

import re
import warnings
import scrapy
from bs4 import BeautifulSoup
from pprint import pprint
from book.items import BookItem


# 在 04 的基础上，下载某个专题内全部的书。就是在原来的基础上再加一层。 yes!
class SongSpider(scrapy.Spider):
    name = 'g3'
    allowed_domains = ['book.sbkk8.com']
    # start_urls = ['http://book.sbkk8.com/xiandai/']       # 现代
    start_urls = ['http://book.sbkk8.com/gudai/tangshi/']   # 唐诗
    base_url = 'http://book.sbkk8.com'

    # 解析首页，找到每本书的主页
    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        all_book_urls = soup.find_all('a', attrs={'class': "ablum"})
        for i in all_book_urls:
            book_home = self.base_url + i.get("href")

            # 其实这里也可以传递 类别，比如像 现代2个字。方便按照文件夹来分类。
            yield scrapy.Request(book_home, callback=self.pase_book)

    # 解析每一本书的首页，找到 书名 + 第一章的url
    def pase_book(self, response):
        base = 'http://book.sbkk8.com'
        soup = BeautifulSoup(response.text, "lxml")
        this_book_name = soup.find('h1', attrs={'class': "listH11"}).text
        first_chapter = base + soup.find('div', attrs={'class': "mulu"}).find('a').get("href")
        yield scrapy.Request(first_chapter, callback=self.parse_text, meta={'book_name': this_book_name})

    # 根据第一章的url 来查找下一章，并保存。
    def parse_text(self, response):
        item = BookItem()
        soup = BeautifulSoup(response.text, "lxml")

        item['chapter_title'] = soup.find('h1').text
        item['chapter_content'] = soup.find('div', attrs={'id': 'content'}).text

        # 我猜测: 这个meta 第一个从 parse 传递过来的时候是有值的， 但是当进入到自身的递归时，这个meta是None，
        # 所以呢，在自身的递归中，也是要带上这同一个 meta.
        same_book_name = response.meta.get('book_name')
        item['book_name'] = same_book_name
        yield item

        next_page = soup.find_all('a', attrs={'class': 'pagedaohang'})[1].get('href')
        if next_page:
            next_page_url = 'http://book.sbkk8.com' + next_page
            yield scrapy.Request(next_page_url, callback=self.parse_text, meta={'book_name': same_book_name})


