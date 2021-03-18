import scrapy
import json
from wallpaper.items import WallpaperItem
from wallpaper.settings import IMAGES_STORE, TAG_NAME
from pprint import pp


class SplashSpider(scrapy.Spider):
    name = 'hi'
    allowed_domains = ['unsplash.com']
    custom_settings = {
        "JOBDIR": "spider_name_01"
    }
    # 直接筛选出横向的图片，适合做桌面壁纸。
    start_urls = [f'https://unsplash.com/napi/search/photos?query={TAG_NAME}&per_page=20&page={x}&orientation=landscape&xp=feedback-loop-v2%3Acontrol' for x in range(1, 21)]

    def parse(self, response, **kws):
        item = WallpaperItem()
        resp = json.loads(response.body)    # 此时是一个字典。
        item['pic_urls'] = [i["urls"]["raw"] for i in resp['results']]
        yield item






