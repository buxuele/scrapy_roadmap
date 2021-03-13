from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class DoubanPipeline(ImagesPipeline):
    # cookies 如何传进来呢？？？？？？？？？
    # 这里不需要了。因为设置里面已经打开了   COOKIES_ENABLED = True

    def get_media_requests(self, item, info):
        u = item["image_url"]
        yield Request(u)

    def file_path(self, request, response=None, info=None, *, item=None):
        # 即便是我想把描述文字也加入到图片的名称上，但是文件描述的过程中，有很多的非法字符串。
        image_name = request.url.split("/")[-1]
        return image_name


class SohuPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for u in item["image_urls"]:
            yield Request(u)

    def file_path(self, request, response=None, info=None, *, item=None):
        # 即便是我想把描述文字也加入到图片的名称上，但是文件描述的过程中，有很多的非法字符串。
        image_name = request.url.split("/")[-1]
        return image_name
