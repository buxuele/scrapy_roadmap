import scrapy


class BookItem(scrapy.Item):

    book_name = scrapy.Field()
    # chapter_url = scrapy.Field()
    # first_chapter_url = scrapy.Field()

    # 这里2个变量对应是方法 1
    chapter_title = scrapy.Field()
    chapter_content = scrapy.Field()
