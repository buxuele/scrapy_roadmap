BOT_NAME = 'wallpaper'

SPIDER_MODULES = ['wallpaper.spiders']
NEWSPIDER_MODULE = 'wallpaper.spiders'

ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False    # 可以防止被ban

DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS = 10
CONCURRENT_REQUESTS_PER_DOMAIN = 10
CONCURRENT_REQUESTS_PER_IP = 10

TAG_NAME = "cat"       # book, shark library dog, todo cat  city, lake, mall, music, park, china,
# 以下需要手动修改。
IMAGES_STORE = f'E:\爬虫结果\\{TAG_NAME.capitalize()}400'

ITEM_PIPELINES = {
   'wallpaper.pipelines.WallpaperPipeline': 300,
}

DOWNLOADER_MIDDLEWARES = {
   'wallpaper.middlewares.WallpaperDownloaderMiddleware': 543,
}

# 异常状态码的处理
RETRY_TIMES = 5
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429, 520]

DEFAULT_REQUEST_HEADERS = {
  'Accept': '*/*',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'accept-encoding': 'gzip, deflate, br',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
}

# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# 开启这几项缓存 加快了本地调试速度，也减轻了 网站的压力
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
