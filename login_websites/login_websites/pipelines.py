from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


# 澎湃，与豆瓣的写法，基本一致。
class PengpaiPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for u in item["image_urls"]:
            yield Request(u)

    def file_path(self, request, response=None, info=None, *, item=None):
        image_name = ''.join(request.url.split("/")[-3:])
        return image_name


class ZhihuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for u in item["image_urls"]:
            yield Request(u)

    def file_path(self, request, response=None, info=None, *, item=None):
        image_name = request.url.split("/")[-1]
        return image_name


# 豆瓣 + 知乎， 使用同样的 Pipeline。知乎，不必新建了。???
class DoubanPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for u in item["image_urls"]:
            yield Request(u)

    def file_path(self, request, response=None, info=None, *, item=None):
        image_name = request.url.split("/")[-1]
        return image_name


class SohuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for u in item["image_urls"]:
            yield Request(u)

    def file_path(self, request, response=None, info=None, *, item=None):
        # 即便是我想把描述文字也加入到图片的名称上，但是文件描述的过程中，有很多的非法字符串。
        image_name = request.url.split("/")[-1].split('.')[0] + '.jpg'
        return image_name


# class NeteaseMusicItem(scrapy.Item):
#     singer = scrapy.Field()
#     album = scrapy.Field()
#     img_url = scrapy.Field()

class NeteaseMusicPipeline(ImagesPipeline):
    # 保存规则 singer_name + album_name + origin.jpg
    pass

