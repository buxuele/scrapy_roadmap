import scrapy


class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    image_url = scrapy.Field()


class SouhuItem(scrapy.Item):
    image_urls = scrapy.Field()
