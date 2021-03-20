import scrapy


class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    image_urls = scrapy.Field()


class SouhuItem(scrapy.Item):
    image_urls = scrapy.Field()


# class NeteaseMusicItem(scrapy.Item):
#     singer = scrapy.Field()
#     album = scrapy.Field()
#     img_url = scrapy.Field()


class JianShuItem(scrapy.Item):
    author = scrapy.Field()
    author_url = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()


class ZhihuItem(scrapy.Item):
    author = scrapy.Field()
    author_url = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()


