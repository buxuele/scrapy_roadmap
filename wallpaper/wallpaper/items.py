# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WallpaperItem(scrapy.Item):
    pic_urls = scrapy.Field()

