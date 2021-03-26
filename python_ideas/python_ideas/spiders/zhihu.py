# -*- coding: utf-8 -*-
# Author:       fanchuang
# DateTime:     2021/3/25 0025 13:46 
# Contact:      baogebuxuele@163.com
# Github:       https://github.com/buxuele 
# About:

import json
import scrapy
from scrapy import Request
from python_ideas.items import PythonIdeasItem


"""
通过对 api 的解析，试着去理解知乎这个网站在【数据结构上的设计】:
1. 比如问题与答案的关系。
2. 以及与用户的关系。
"""


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    base = 'https://www.zhihu.com'
    allowed_domains = ['zhihu.com']

    # 构造 api-url 每页10篇内容。起始 url offset=0
    def start_requests(self):
        #          python爬虫    Python 编程  Python 开发  Python
        topic_id = ['20086364', '20052039', '19710602', '19552832']
        for i in topic_id:
            u = f'https://www.zhihu.com/api/v4/topics/{i}/feeds/timeline_activity?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Canswer_type%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.paid_info%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=10&offset=0'
            yield Request(u, callback=self.parse_json)

    # 找到文章，或是某个回答。实际上找到的是 问题以及回答。
    def parse_json(self, response, **kwargs):
        cnt = 0     # 对一个话题爬取的数量做下限定。
        people_base = 'https://www.zhihu.com/people/'
        item = PythonIdeasItem()

        resp = json.loads(response.text)
        junk = resp['data']
        for j in junk:
            # j['type'] == 'question' 说明是没有人回答的问题。
            if j['target']['type'] == 'answer':
                item['title'] = j['target']['question']['title']

                # 得到的是      http://www.zhihu.com/api/v4/questions/372436672
                # 实际网页 url  https://www.zhihu.com/question/372436672
                # 只需要去掉 api字段，作者链接也是一样的。
                item['link'] = j['target']['question']['url']
                item['author'] = j['target']['author']['name']
                item['author_home'] = people_base + j['target']['author']['url_token']
                item['publish_time'] = j['target']['updated_time']  # 1616399111
                yield item

        next_page = resp['paging']['next']
        if next_page and cnt < 20:
            cnt += 1
            yield Request(next_page, callback=self.parse_json)



