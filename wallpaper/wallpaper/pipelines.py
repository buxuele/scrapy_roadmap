from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class WallpaperPipeline(ImagesPipeline):
    # 这里看看是如何修改默认的处理方式的.
    # 这里也可以用很原始的写法: with open ...
    # def process_item(self, item, spider):
    #     return item

    def get_media_requests(self, item, info):
        for u in item["pic_urls"]:
            yield Request(u)

    def file_path(self, request, response=None, info=None, *, item=None):
        image_name = request.url.split('?')[0].split("/")[-1] + '.jpg'
        return image_name
