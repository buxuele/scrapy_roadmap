BOT_NAME = 'wallpaper'

SPIDER_MODULES = ['wallpaper.spiders']
NEWSPIDER_MODULE = 'wallpaper.spiders'

ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False    # 可以防止被ban

DOWNLOAD_DELAY = 0
CONCURRENT_REQUESTS = 100
CONCURRENT_REQUESTS_PER_DOMAIN = 100
CONCURRENT_REQUESTS_PER_IP = 100

# 以下需要手动修改。
IMAGES_STORE = 'E:\Work_500'

ITEM_PIPELINES = {
   'wallpaper.pipelines.WallpaperPipeline': 300,
}

DOWNLOADER_MIDDLEWARES = {
   'wallpaper.middlewares.WallpaperDownloaderMiddleware': 543,
}


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
