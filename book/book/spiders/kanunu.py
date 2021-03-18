# -*- coding: utf-8 -*-
import re
import scrapy
from bs4 import BeautifulSoup
from book.items import BookItem


# 其实，质量还是很不错的。只是书的种类我不喜欢。
class KankanSpider(scrapy.Spider):
    name = 'k1'
    allowed_domains = ['kanunu8.com']
    start_urls = ['https://www.kanunu8.com/files/16.html']  # 诺贝尔文学奖这个类别。

    # 每本书的首页
    def parse(self, response, **kwargs):
        soup = BeautifulSoup(response.text, "lxml")
        chunk = soup.find_all('a', href=re.compile('/book[0-9]?/\w+/'))
        for a in chunk:
            yield response.follow(a.get('href'), callback=self.parse_book)

    # 每本书的第一章, 传递书名。
    def parse_book(self, response, **kwargs):
        soup = BeautifulSoup(response.text, "lxml")
        first_chap = soup.find('a', href=re.compile('^\d+\.html'))
        book_name = soup.find('h1').text
        yield response.follow(first_chap.get('href'), callback=self.parse_content, cb_kwargs={"book_name": book_name})

    # 每一章的 标题，内容
    def parse_content(self, response, **kwargs):
        item = BookItem()
        soup = BeautifulSoup(response.text, "lxml")
        same_name = response.cb_kwargs.get('book_name')
        item['book_name'] = same_name
        item['chapter_title'] = soup.find('font', attrs={'size': '4'}).text
        item['chapter_content'] = soup.find('td', attrs={'width': '820'}).text
        yield item

        next_page = soup.find('td', attrs={'width': '28%'}).find('a')
        if next_page:
            yield response.follow(next_page.get('href'), callback=self.parse_content, cb_kwargs={"book_name": same_name})








