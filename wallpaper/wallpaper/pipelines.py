from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

from contextlib import suppress
from itemadapter import ItemAdapter
import logging

#  这个日志文件名称，会被全局的日志系统覆盖。但是要记录的内容会被记录下来。
logger = logging.getLogger(__file__)


class WallpaperPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for u in item["pic_urls"]:
            yield Request(u)

    def file_path(self, request, response=None, info=None, *, item=None):
        image_name = request.url.split('?')[0].split("/")[-1] + '.jpg'
        return image_name

    # 修改默认的错误处理函数，把下载失败的 itme 记录下来。
    def item_completed(self, results, item, info):
        for ok, x in results:
            if not ok:
                logger.error(logging.ERROR, x)
                logger.error(logging.ERROR, ok)
                logger.error(logging.ERROR, info)

        return item
