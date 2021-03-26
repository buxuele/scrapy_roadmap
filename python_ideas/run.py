# from scrapy import cmdline

# cmdline.execute("scrapy crawl zhihu".split())
# cmdline.execute("scrapy crawl csdn".split())
# cmdline.execute("scrapy crawl juejin".split())

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def run():
    settings = get_project_settings()
    crawler = CrawlerProcess(settings)
    crawler.crawl('zhihu')
    crawler.crawl('csdn')
    crawler.crawl('juejin')
    crawler.start()


if __name__ == '__main__':
    run()