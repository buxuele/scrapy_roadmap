import scrapy


class BookItem(scrapy.Item):
    book_name = scrapy.Field()
    chapter_title = scrapy.Field()
    chapter_content = scrapy.Field()
