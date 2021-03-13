# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/2/27 0027 18:57 
# contact: fanchuangwater@gmail.com
# about:

import json
import scrapy
from my_proxy.items import MyProxyItem

"""
{'unique_id': '47b45f2ab72bf799bd4acb3f6d4c9903', 
 'ip': '116.117.134.134', 'port': '8828',
 'country': '中国', 'ip_address': '中国 内蒙古 呼和浩特市', 'anonymity': 2,
 'protocol': 'http',
 'isp': '联通', 'speed': 48, 'validated_at': '2021-03-01 17:35:06',
 'created_at': '2021-02-28 22:42:26', 
 'updated_at': '2021-03-01 17:35:06'}
"""


class SmallProxySpider(scrapy.Spider):
    # 这里打算多搞几个代理的网站，最后整合到一起。todo
    name = 'small'
    allowed_domains = ['ip.jiangxianli.com']

    # 这里还是使用直接请求api的形式。
    def start_requests(self):
        base_url = 'https://ip.jiangxianli.com/api/proxy_ips'
        payloads = [{"page": c, "country": "中国", "order_by": "speed"} for c in range(1, 6)]
        for p in payloads:
            yield scrapy.Request(base_url, body=json.dumps(p))

    def parse(self, response):
        item = MyProxyItem()
        junk = json.loads(response.body)
        if junk:
            all_data = junk['data']['data']
            for a in all_data:
                item['ip'] = a['ip']
                item['port'] = a['port']
                item['protocol'] = a['protocol']
                if a['country'] == '中国':
                    item['is_china'] = True
                else:
                    item['is_china'] = False
                yield item

