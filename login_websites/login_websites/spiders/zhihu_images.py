# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/3/15 0015 7:38 
# contact: fanchuangwater@gmail.com
# about:  爬取知乎。

import re
import json
import time
import scrapy
from scrapy import Request
from login_websites.items import ZhihuItem
from bs4 import BeautifulSoup


# todo
#  1. 切换用户的时候，失败，原因未知。
#  2. 自动生成 session_id

# 1. 爬取一个用户的全部图片。目前是只写这一个，另外2个搁置。
# 2. 爬取一个问题下的全部图片。
# 3. 爬取一个话题下的全部图片。
class ZhihuSpider(scrapy.Spider):
    url = 'https://www.zhihu.com/people/qun-jiao-wei-wei'
    # url = 'https://www.zhihu.com/people/maidaren888'

    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    custom_settings = {
        'CLOSESPIDER_ITEMCOUNT': '5000',
        'IMAGES_STORE': f'E:\爬虫结果\图片\知乎用户_{url.split("/")[-1]}',
        'ITEM_PIPELINES': {'login_websites.pipelines.ZhihuPipeline': 300},     # 因为 Pipeline 的写法与豆瓣一样。
    }

    @staticmethod
    def make_api_url(home_url):
        """
        1. 传入用户主页的地址，返回 api-url.
        2. 另外如何找到初始的第一页还需要再测试一下。我怀疑自己找的第一页是不准确的。
        """
        nickname = home_url.split('/')[-1]
        time_str = str(time.time()).split('.')[0]

        # 这个 session_id，我怀疑是包含了用户信息，所以使用浏览器无痕模式下生成一个。而且这个值自动生成比较安全。写一个辅助函数，随机增值。
        session_id = '1359178678597910528'  # 1359178678597910528
        ret = f'https://www.zhihu.com/api/v3/moments/{nickname}/activities?limit=7&session_id={session_id}&after_id={time_str}&desktop=true'
        return ret

    def start_requests(self):
        # 从网页传入url，构造 api-url
        u = self.make_api_url(self.url)
        yield Request(u, callback=self.parse)

    def parse(self, response, **kwargs):
        resp = json.loads(response.text)
        junk = resp['data']
        content_url = ''
        flag = ''

        # 这里只要此用户原创的内容: 发布的文章 + 回答。 收藏，赞同都不要。
        # 这里使用一个 cb_args 告诉下级解析函数，往哪里去找图片。
        for j in junk:
            if j['verb'] == 'ANSWER_CREATE':
                flag = "ans"
                ques = j['target']['question']['url'].split('/')[-1]
                ans = j['target']['url'].split('/')[-1]
                content_url = f'https://www.zhihu.com/question/{ques}/answer/{ans}'

            elif j['verb'] == 'MEMBER_CREATE_ARTICLE':
                flag = 'zhuanlan'
                content_url = j['target']['url']
            else:
                pass
            yield Request(content_url, callback=self.parse_img, cb_kwargs={'flag': flag})

        next_page = resp['paging']['next']
        if next_page:
            yield Request(next_page, callback=self.parse)

    def parse_img(self, response, **kwargs):
        item = ZhihuItem()
        soup = BeautifulSoup(response.text, 'lxml')

        if response.cb_kwargs['flag'] == 'ans':
            box = soup.find('div', attrs={'class': 'QuestionAnswer-content'})
        else:
            box = soup.find('article')
        img_urls = box.find_all('img', src=re.compile(r'https://pic[1-9]?\.zhimg.*\?'))
        item['image_urls'] = [i.get('src').split('?')[0] for i in img_urls]
        yield item


