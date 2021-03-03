# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


"""
总体设计: 代理一定要分中外。不然没法分开用。
1. 第一步，首先是不分类，全部添加进来再说、
2. 
"""


class MyProxyItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()

    protocol = scrapy.Field()
    is_china = scrapy.Field()

