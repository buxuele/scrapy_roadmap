# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/2/27 0027 0:24 
# contact: fanchuangwater@gmail.com
# about:

import re
import warnings
import scrapy
from bs4 import BeautifulSoup
from pprint import pprint
from book.items import BookItem

# yes!
# 这样就做到了： 下载多本书 + 同时保证章节是按顺序的。
# 注意递归的过程中传递同样的书名。不然会找不到书名。
class SongSpider(scrapy.Spider):
    name = 'g2'
    allowed_domains = ['book.sbkk8.com']
    start_urls = ['http://book.sbkk8.com/xiandai/jinyong/shediaoyingxiongchuan/',
                  'http://book.sbkk8.com/xiandai/jinyong/shendiaoxialv/',
                  'http://book.sbkk8.com/xiandai/jinyong/tianlongbabu/',
                  ]

    def parse(self, response):
        base = 'http://book.sbkk8.com'
        soup = BeautifulSoup(response.text, "lxml")
        this_book_name = soup.find('h1', attrs={'class': "listH11"}).text
        first_chapter = base + soup.find('div', attrs={'class': "mulu"}).find('a').get("href")
        yield scrapy.Request(first_chapter, callback=self.parse_text, meta={'book_name': this_book_name})

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
            # warnings.warn("next page url is ", next_page_url)
            yield scrapy.Request(next_page_url, callback=self.parse_text, meta={'book_name': same_book_name})

