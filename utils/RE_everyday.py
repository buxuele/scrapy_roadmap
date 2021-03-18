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
        print(p)
        with open("ret.txt", 'a') as g:
            g.write(p + ',')
            g.write('\n')


# 去除重复的域名。
# 1. 从自己的 pac 配置选项中选择全部的域名，复制到 ret.txt
# 2. 运行此文件，得到没有重复的域名。
def remove_dup():
    ret = set()
    with open('ret.txt', 'r') as f:
        data = f.read()
        print("初始域名个数: ", len(data.split("\n")))
        for i in data.split('\n'):
            if i not in ret:
                ret.add(i)

    print("不重复的域名个数: ", len(ret))
    print(ret)
    with open('ret.txt', 'w') as g:
        for x in list(ret):
            g.write(x + '\n')


if __name__ == '__main__':
    f = 'x.html'
    html_url(html_file=f)

    # u = "http://pb.7mla.xyz/2048/read.php?tid-3185463-fpage-2.html"
    # html_url(url=u)

    # remove_dup()


