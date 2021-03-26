BOT_NAME = 'python_ideas'

SPIDER_MODULES = ['python_ideas.spiders']
NEWSPIDER_MODULE = 'python_ideas.spiders'


DEFAULT_REQUEST_HEADERS = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
  'accept-encoding': 'gzip, deflate, br',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
}

COOKIES_ENABLED = False		# 可以防止被ban
ROBOTSTXT_OBEY = False
FEED_EXPORT_ENCODING = 'utf-8'

MONGO_URI = 'mongodb://localhost:27017'
MONGO_DB = 'python_daily'

# 线程，网速
DOWNLOAD_DELAY = 0          # 调整爬虫速度
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

#SPIDER_MIDDLEWARES = {
#    'python_ideas.middlewares.PythonIdeasSpiderMiddleware': 543,
#}

ITEM_PIPELINES = {
   'python_ideas.pipelines.MongoPipeline': 200,
}

