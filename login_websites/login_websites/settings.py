BOT_NAME = 'login_websites'

SPIDER_MODULES = ['login_websites.spiders']
NEWSPIDER_MODULE = 'login_websites.spiders'

ROBOTSTXT_OBEY = False
COOKIES_ENABLED = True
# FEED_EXPORT_ENCODING = 'utf-8'

DOWNLOAD_DELAY = 0
CONCURRENT_REQUESTS = 20
CONCURRENT_REQUESTS_PER_DOMAIN = 20
CONCURRENT_REQUESTS_PER_IP = 20

# 异常状态码的处理
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429, 520]

DEFAULT_REQUEST_HEADERS = {
  'Accept': '*/*',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'accept-encoding': 'gzip, deflate, br',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
}

# IMAGES_STORE = f'E:\爬虫结果\\豆瓣话题_露台植物记'
IMAGES_STORE = f'E:\爬虫结果\\搜狐图片_书法2'

SPIDER_MIDDLEWARES = {
   'login_websites.middlewares.LoginWebsitesSpiderMiddleware': 543,
}

DOWNLOADER_MIDDLEWARES = {
   'login_websites.middlewares.LoginWebsitesDownloaderMiddleware': 543,
}


ITEM_PIPELINES = {
   # 'login_websites.pipelines.DoubanPipeline': 300,
   'login_websites.pipelines.SohuPipeline': 300,
}

