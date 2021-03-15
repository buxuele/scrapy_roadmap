# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/3/14 0014 15:13 
# contact: fanchuangwater@gmail.com
# about: 正则表达式，必须多练，必须熟练。

import re
import requests
from pprint import pp


# 从一个 html 源码中，找出全部的 url，然后提取全部的 域名。
def html_url(url=None, html_file=None):
    st = set()
    if url:
        resp = requests.get(url)
        resp.encoding = 'utf-8'
        text = resp.text
    elif html_file:
        text = open(html_file, 'r', encoding='utf-8').read()
    else:
        print("请给出一个文件啊，老哥！")
        return

    # ret = re.findall('"((http|https)://.*?)"', html, re.M)    # tuple
    ret = re.findall('"[a-z]+://\S+"', text, re.M)              # 我觉得这种写法是最好的。
    for s in ret:
        temp = s[1:-1].split("/")[2].split("?")[0].split(":")[0]        # 这一步其实也可以用正则的。
        if temp not in st:
            st.add(temp)

    for p in list(st):
        with open("ret.txt", 'a') as g:
            g.write(p + ',')
            g.write('\n')
    return list(st)


if __name__ == '__main__':
    f = 'x.html'
    html_url(html_file=f)

    # u = "http://pb.7mla.xyz/2048/read.php?tid-3185463-fpage-2.html"
    # html_url(url=u)


