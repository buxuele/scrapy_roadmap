# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/3/1 0001 20:23 
# contact: fanchuangwater@gmail.com
# about: 运行此文件 = 下载代理 + 校验代理。

from check import CheckProxy
from my_proxy.spiders.fate0_proxy import SecondProxy

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def special():
    s = SecondProxy()  # github/fate0  这个代理的质量也是很好的。而且数量稍微多一些。
    s.run()


def get_raw():
    settings = get_project_settings()
    crawler = CrawlerProcess(settings)
    crawler.crawl('small')      # 数量虽然少的，但是质量很高。都是能用的，没有虚假的。

    # crawler.crawl('xila')     # 响应慢。
    # crawler.crawl('huan')     # 我怀疑这个是坏掉的。
    # crawler.crawl('kuai')     # 我怀疑这个是坏掉的。
    crawler.start()

    special()


# 校验
def happy():
    ck = CheckProxy()
    ck.run()


if __name__ == '__main__':
    # get_raw()   # 下载
    happy()     # 校验。如果只想校验，那么就注释掉上面一行。 todo 我还想再深度校验一下。看看到底是什么情况。
