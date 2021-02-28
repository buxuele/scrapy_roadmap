BOT_NAME = 'book'

SPIDER_MODULES = ['book.spiders']
NEWSPIDER_MODULE = 'book.spiders'

ROBOTSTXT_OBEY = False


ITEM_PIPELINES = {
   'book.pipelines.BookPipeline': 300,
}

DOWNLOADER_MIDDLEWARES = {
   'book.middlewares.BookDownloaderMiddleware': 543,
}

# 这里修改为1 是不是就能顺序执行了 ？？？？ 貌似并不会啊。
CONCURRENT_REQUESTS = 1


DOWNLOAD_DELAY = 0
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1

COOKIES_ENABLED = False




HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
