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
