import time
BOT_NAME = 'book'

SPIDER_MODULES = ['book.spiders']
NEWSPIDER_MODULE = 'book.spiders'

ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False
FEED_EXPORT_ENCODING = 'utf-8'

ITEM_PIPELINES = {
   'book.pipelines.BookPipeline': 300,
}


DOWNLOADER_MIDDLEWARES = {
   'book.middlewares.BookDownloaderMiddleware': 543,
   'book.proxy_middleware.ProxyMiddleware': 125,
}

DOWNLOAD_DELAY = 0
CONCURRENT_REQUESTS = 2
CONCURRENT_REQUESTS_PER_IP = 2
CONCURRENT_REQUESTS_PER_DOMAIN = 2

# 异常状态码的处理
RETRY_TIMES = 2
RETRY_HTTP_CODES = [403, 500, 502, 503, 504, 522, 524, 408, 429, 520]

DEFAULT_REQUEST_HEADERS = {
  'Accept': '*/*',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'accept-encoding': 'utf8',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
}


HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 日志 log  调试的时候，最好还是不要用log 文件。
# LOG_FILE = f"{str(int(time.time()))}.log"
# LOG_ENABLED = True
# LOG_LEVEL = 'INFO'          # Default: 'DEBUG'
