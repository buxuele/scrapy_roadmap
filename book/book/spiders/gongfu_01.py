# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/2/25 0025 18:23 
# contact: fanchuangwater@gmail.com
# about: 下载武侠小说、  http://www.jinyongwang.com/ntian/


import re
import scrapy
from bs4 import BeautifulSoup
from book.items import BookItem

# todo 再找点好的网站试试看。
# 这个网站的文字排版与问题，读天龙八部的时候，错别字以及杂乱的标点令人很痛苦。
# 第一个版本 尝试自己来自写，看看如何下载一本书、
class SongSpider(scrapy.Spider):
    name = 'g1'
    allowed_domains = ['book.sbkk8.com']
    start_urls = ['http://book.sbkk8.com/xiandai/jinyong/shediaoyingxiongchuan/200826.html']

    # 1. 这里解析的是第一层级的 urls articleH1
    def parse(self, response):
        item = BookItem()
        soup = BeautifulSoup(response.text, "lxml")

        chapter_title = soup.find('h1').text
        book_content = soup.find('div', attrs={'id': 'content'}).text
        item['chapter_title'] = chapter_title
        item['chapter_content'] = book_content
        yield item

        next_page = soup.find_all('a', attrs={'class': 'pagedaohang'})[1].get('href')
        if next_page:
            next_page_url = 'http://book.sbkk8.com' + next_page
            yield scrapy.Request(next_page_url, callback=self.parse)
