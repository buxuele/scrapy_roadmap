# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/3/15 0015 4:14 
# contact: fanchuangwater@gmail.com
# about: 单独处理网页的字符编码问题

import requests
from bs4 import BeautifulSoup


def csw():
    a = 'https://www.99csw.com/book/search.php?s=13139900387823019677&type=%E7%AB%99%E5%86%85&q=%E8%AF%BA%E8%B4%9D%E5%B0%94%E6%96%87%E5%AD%A6%E5%A5%96'

    ret = requests.get(a)
    print(ret.status_code)
    print(ret.encoding)
    print(ret.text[:500])
    ret.encoding = 'utf-8'
    print()
    print()
    print(ret.text[:500])


def parse():
    text = open('a.html', 'r', encoding='utf-8').read()
    # soup = BeautifulSoup(text, 'lxml')
    print(text)


# parse()
csw()



