# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/3/15 0015 7:38 
# contact: fanchuangwater@gmail.com
# about:  爬取知乎。

import re
import json
import scrapy
from scrapy import Request
from login_websites.items import DoubanItem


# 1. 爬取一个用户的全部图片。
# 2. 爬取一个问题下的全部图片。
# 3. 爬取一个话题下的全部图片。
class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['douban.com']
    url = 'https://www.douban.com/gallery/topic/152905/?from=discussing'    # 露台植物记
    str_cookies = 'bid=q0zgvBVOcKI; douban-fav-remind=1; ll="108296"; _vwo_uuid_v2=DF0F7918D61BB7233A9D20A9B94314FDE|1132a421078a81034f2ee1b44e1287ac; gr_user_id=dc6e1a0e-662b-44e6-9544-3ad551b4b502; ct=y; viewed="10738023_4881639_5915365_1083428_2097249"; dbcl2="161289377:k8VtynNhjSo"; push_doumail_num=0; push_noty_num=0; ps=y; __utmv=30149280.16128; __utma=30149280.159925537.1599147897.1615317945.1615320310.26; __utmz=30149280.1615320310.26.23.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/channel/30168716/; ck=q0bA; ap_v=0,6.0; frodotk="8b6951657bf23140a23bf43073d693c0"'

    # @staticmethod
    # def make_cookies(str_cookies):
    #     ret = {}
    #     for i in str_cookies.split('; '):
    #         idx = i.find('=')
    #         left = i[:idx]
    #         right = i[idx + 1:]
    #         ret[left] = right
    #     return ret
    #
    # def start_requests(self):
    #     cookies = self.make_cookies(self.str_cookies)
    #     t = re.findall(r'\d+', self.url)[0]    # 根据传入的 网页url 来构造 实际请求 api的url
    #     for i in range(50):
    #         u = f'https://m.douban.com/rexxar/api/v2/gallery/topic/{t}/items?from_web=1&sort=hot&start={i*20}&count=20&status_full_text=1&guest_only=0&ck=q0bA'
    #         yield Request(u, cookies=cookies, callback=self.parse)
    #
    # def parse(self, response, **kwargs):
    #     item = DoubanItem()
    #     resp = json.loads(response.text)
    #     for i in resp['items']:
    #         # todo 其实不必了。我本身不在意数据的完整性，只是想多看几张图片而已。以后再说吧。另外，真正的大图是在每位用户的主页里面。
    #         # 这里的 json 解析其实还是有点问题的，因为原始的 json 文件是不完全规则的，需要加上条件判断，目前没必要处理了。
    #         item['title'] = i['target']['status']['text'].replace('\r\n', '')
    #         item['image_url'] = i['target']['status']['images'][0]['large']['url']     # 这里简化处理了。只要一张图片
    #         yield item
