###   Scrapy 小项目
- 大胆去写，无情修改。
- 爬东爬西，无所适从。

#### 项目1: wallpaper, 下载 unsplash.com 的图片。
1. 学习如何下载并保存图片， 使用内建的 ImagesPipeline.
2. 根据网页提供的选项，构造 api url. 
3. 增加错误处理，把失败的 url 记录下来。
4. 如何停止一个爬虫，并且下次启动的时候，从上次停下的地方继续爬取。
```python
# Ctrl + C, 可以停止，下次在运行的时候会继续。
class SplashSpider(scrapy.Spider):
    name = 'x'
    allowed_domains = ['x.com']
    custom_settings = {"JOBDIR": "spider_name_01"}  # 添加这这一行。
```


#### 项目2: book, 爬几个电子书网站
1. 武侠：从下载一本书, 到下载一个类目的图书，再到下载全站的图书。
2. 99藏书网: 由于原始 html 里面是加盐的，因此需要借助 selenium 来获取 js 处理过的页面。
3. 努努书坊: 每本书的内容还是很完整的，只是大部分类型我不喜欢。


#### 项目3: my_proxy, 自建代理池， 多方采集 + 校验。
1. 爬取代理，并校验。 我写一个 [一篇文章](https://www.jianshu.com/p/51f83c6579f7) 介绍这个项目的思路，以及用法。
2. 代理这一块，不能花太多时间，因为别人用的都是付费代理，那肯定是一个爽啊。
3. 使用 MongoDB 保存数据。  
4. 目前正在使用 v2ray，感觉很流畅，至于自己这些代理，似乎是没必要了。 



#### 项目4: login_websites, 大型网站，小小尝试。
1. 尝试登陆，但是点击验证码，滑动窗口验证码，以及手机验证码，所以还是使用网页自带的 cookies 来登录。
2. 豆瓣，从一个豆瓣话题的主页开始，下载该话题下全部的图片。待完善。
3. 简书, 随机游走。
4. 知乎, 爬取某个用户的原创图片。
5. 搜狐，给出任意一篇搜狐文章的url, 作为入口，下载该用户全部的图片。
6. 澎湃, 艺术评论类目下的图片。



#### 项目5: python_ideas, 爬取与 python 有关的文章， 整合到一起。
1. 知乎，按照话题爬问题。看看大家提出了哪些问题，比较关注哪些问题。
2. csdn， 基本上同上。
3. 掘金, 其实的掘金的插件，整合的已经是很好了。另外，这个网站的爬取也是最有意思的。POST --> api, 需要改写一段 base64 加密的请求信息。
4. 也许以后可以添加其他的数据源。
5. 尝试简单的数据清洗。clean_data.py


#### 项目5: shopping,  爬一些商城的数据
1. 一批威客， 实时【任务】监控，看看是否有合适单子可以接。
2. 


#### Todo
1. 如果图片太小，则不下载。
2. 爬一下商城网站
3. 


#### 运行环境
- Windows 10 
- Anaconda env
- Scrapy 2.4.1
- requirements.txt 
