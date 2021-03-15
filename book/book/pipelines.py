# useful for handling different item types with a single interface
from itemadapter import ItemAdapter # todo
from scrapy.pipelines.files import FilesPipeline
from scrapy import Request


# 尝试在这里保存文本信息。也许还有一些其他内建的方法，但是我目前不需要了，因为我想自定义一下试试看。
# class BookPipeline(FilesPipeline):
class BookPipeline:
    def process_item(self, item, spider):
        # 1. 尝试按照每个章节，单独写入一个文件。 yes!
        # with open(f"{item['chapter_title']}.txt", 'w', encoding='utf-8') as f:
        #     f.write(item['book_content'])
        # return item

        # 2. 整体写入一个文件。yes! 这里的
        # with open("射雕英雄传3.txt", 'a', encoding='utf-8') as f:
        #     f.write(item['chapter_title'].strip())
        #     f.write('\n'*2)
        #     f.write(item['chapter_content'].strip())
        #     f.write('\n'*5)
        # return item

        # 3. 书名也需要作为一个变量传递进来。 这个更改 文件存储目录也是很方便的。
        # store_path = r'E:\爬虫结果\99藏书网\爱丽丝门罗'
        store_path = r'E:\爬虫结果\电子书\努努书坊_诺贝尔文学奖'
        b_name = item['book_name'] + '.txt'
        file_name = f'{store_path}\\{b_name}'
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(item['chapter_title'].strip())
            f.write('\n' * 2)
            f.write(item['chapter_content'].strip())
            f.write('\n' * 5)
        return item

    # todo 这里有点行不通了。先搁置。
    # 3. 看看别人是怎么写的，以及内建的方法是怎么写的。
    # 这里其实也只是尝试而已。
    # 如果按照这种写法，那么必须新建一个文件，每一本书，返回全部的章节urls
    # def get_media_requests(self, item, info):
    #     for a_url in item["chapter_urls"]:
    #         yield Request(a_url, meta={"chapter_name": item['chapter_name']})
    #
    # 这里保存的类型是 BytesIO(response.body) ？？我估计是不能用的。
    # def file_downloaded(self, response, request, info, *, item=None):

    #
    # def file_path(self, request, response=None, info=None, *, item=None):
    #     filename = item['book_name'] + '.txt'
    #     return filename

