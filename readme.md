###   Scrapy 小项目
- 大胆去写，无情修改。

#### 项目1:  wallpaper, 下载 unsplash.com 的图片。
1. 学习如何下载并保存图片， 使用内建的 ImagesPipeline.
2. 根据网页提供的选项，构造 api url. 
3. 如何停止一个爬虫，并且下次启动的时候，从上次停下的地方继续爬取。
```python
# Ctrl + C, 可以停止，下次在运行的时候会继续。
class SplashSpider(scrapy.Spider):
    name = 'x'
    allowed_domains = ['x.com']
    custom_settings = {"JOBDIR": "spider_name_01"}  # 添加这这一行。
```
4. 增加错误处理，把失败的 url 记录下来。

#### 项目2: book, 借助 selenium 来获取 js 处理过的页面
1. 武侠：从下载一本书, 到下载一个类目的图书，再到下载全站的图书。
2. 99藏书网: 由于原始 html 里面是加盐的，因此需要借助 selenium 来获取 js 处理过的页面。
3. 努努书坊: 书的内容还是很齐全的。

#### 项目3: my_proxy, 使用 MongoDB 保存数据。  
1. 爬取代理，并校验。 我写一个 [一篇文章](https://www.jianshu.com/p/51f83c6579f7) 介绍这个项目的思路，以及用法。
2. 代理这一块，不能花太多时间，因为别人用的都是付费代理，那肯定是一个爽啊。
3. 目前正在使用 v2ray，感觉很流畅，至于自己这些代理，似乎是没必要了。 

#### 项目4：login_websites, 大型网站，小小尝试。
1. 尝试登陆，但是点击验证码，滑动窗口验证码，以及手机验证码，所以还是使用网页自带的 cookies 来登录。
2. douban_explore.py 从一个豆瓣话题的主页开始，下载该话题下全部的图片。待完善。
3. souhu_images.py  给出任意一篇搜狐文章的url, 作为入口，下载该用户全部的图片。
4. jianshu, 随机游走。
5. 

#### Todo
1. 如果图片太小，则不下载。