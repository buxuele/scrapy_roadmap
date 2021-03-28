# -*- coding: utf-8 -*-
# Author:       fanchuang
# DateTime:     2021/3/26 0026 18:00 
# Contact:      baogebuxuele@163.com
# Github:       https://github.com/buxuele 
# About:        爬网易号，某个用户的全部图片。与搜狐很类似。

import re
import json
import scrapy
from scrapy import Request
from bs4 import BeautifulSoup
from login_websites.items import SouhuItem
from utils.secret import sohu_cookies


# todo 我其实不是很喜欢这个网站，基本上没有原创的东西，而且图片的质量太差了。
class NeteaseSpider(scrapy.Spider):
    name = 'netease'
    allowed_domains = ['163.com']
