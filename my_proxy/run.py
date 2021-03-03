# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/3/1 0001 20:23
# contact: fanchuangwater@gmail.com
# about: 运行此文件 = 下载代理 + 校验代理。

from check import CheckProxy
from my_proxy.spiders.fate0_proxy import SecondProxy

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# todo 目前有4个爬虫网站可以用，以后再发现其他的，再添加

""" 运行结果:
Origin proxy nums:  800
Good proxy nums:  231
all:  231
china:  96
world:  135
"""


def get_raw():
    settings = get_project_settings()
    crawler = CrawlerProcess(settings)

    crawler.crawl('p1')
    crawler.crawl('p2')
    crawler.crawl('p3')
    crawler.start()
    
    s = SecondProxy()
    s.run()


# 下载完成之后，立马校验就行了啊。
def happy():
    ck = CheckProxy()
    ck.run()


if __name__ == '__main__':
    # get_raw()   # 下载
    happy()     # 校验。如果只想校验，那么就注释掉上面一行。 todo 我还想再深度校验一下。看看到底是什么情况。
