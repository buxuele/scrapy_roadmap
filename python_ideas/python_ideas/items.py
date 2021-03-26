# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy import Field, Item


# 我只关注 python 有什么新的动向。
# 所有重点是: title
class PythonIdeasItem(Item):
    title = Field()
    link = Field()
    author = Field()
    author_home = Field()
    publish_time = Field()
