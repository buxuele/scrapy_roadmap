from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
import logging

#  这个日志文件名称，会被全局的日志系统覆盖。但是要记录的内容会被记录下来。
logger = logging.getLogger(__name__)


class WallpaperSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        spider.logger.error(exception)
        spider.logger.error(response.url)


    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class WallpaperDownloaderMiddleware:
    def process_request(self, request, spider):
        referer = request.url
        if referer:
            request.headers['referer'] = referer

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        spider.logger.error(exception)
        spider.logger.error(request.url)

    def spider_opened(self, spider):
        spider.logger.info('开始下载: %s' % spider.name)
