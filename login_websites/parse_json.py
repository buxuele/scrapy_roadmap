# -*- coding: utf-8 -*-
# Author:       fanchuang
# DateTime:     2021/3/23 0023 12:04 
# Contact:      baogebuxuele@163.com
# Github:       https://github.com/buxuele 
# About:


import json


with open('../data/jianshu_ret_5W.json', 'r', encoding='utf-8') as f:
    raw = f.read()
    dic = json.loads(raw)
    s_author = set()
    articles = set()
    print(len(dic))
    for x in dic:
        # print(x)
        s_author.add(x['author'])
        articles.add(x['url'])

    print(len(s_author))
    print(len(articles))





