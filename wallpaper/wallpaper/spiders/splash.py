import scrapy
import json
from wallpaper.items import WallpaperItem
from wallpaper.settings import IMAGES_STORE
from pprint import pp


class SplashSpider(scrapy.Spider):
    name = 'hi'
    allowed_domains = ['unsplash.com']

    # 直接筛选出横向的图片，适合做桌面壁纸。 todo art,  book,  coffee, shark
    start_urls = [f'https://unsplash.com/napi/search/photos?query=bedroom&per_page=20&page={x}&orientation=landscape&xp=feedback-loop-v2%3Acontrol' for x in range(1, 21)]

    def parse(self, response):
        item = WallpaperItem()
        resp = json.loads(response.body)    # 此时是一个字典。

        # 这里可以直接返回一个 url列表然后交给 pipeline 来处理。
        temp_urls = [i["urls"]["raw"] for i in resp['results']]
        item['pic_urls'] = temp_urls
        yield item

        # 这里如果直接修改 start_urls ？？？
        # cnt = 2
        # next_page = f'https://unsplash.com/napi/topics/wallpapers/photos?page={cnt}&per_page=10'
        # if next_page is not None:
        #     cnt += 1
        #     yield scrapy.Request(next_page, callback=self.parse)







