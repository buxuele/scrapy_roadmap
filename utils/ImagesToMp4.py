# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/2/18 0018 15:14 
# contact: fanchuangwater@gmail.com
# about:
# 1. 练习并使用 shutil 来进行常用的文件操作
# 2. 把图片合集转为 .mp4 文件

import os
import time
import shutil
from datetime import datetime
from PIL import Image

image_prefix = "zoo"


def delete_stuff(path, file_size):
    os.chdir(path)
    ret = os.listdir()
    print("Origin files nums are: ", len(ret))

    for x in ret:
        if not os.path.isdir(x):
            size = os.path.getsize(x) // 1024  # 单位是 kb
            if size < file_size:
                os.remove(x)
    print("This is end, and file nums are:  ", len(os.listdir()))


def make_group(folder):
    # 新建同级文件夹 把原始文件夹分成2个文件夹。按照图片尺寸分为 宽屏，竖屏。
    os.chdir(folder)
    if 'mobile_size' not in os.listdir():
        os.mkdir("mobile_size")  # 可能也不需要了
    if 'pc_size' not in os.listdir():
        os.mkdir("pc_size")  # 可能也不需要了

    abspath = os.path.abspath(folder)
    os.chdir(abspath)

    for img in os.listdir():
        if not os.path.isdir(img):
            try:
                with Image.open(img) as im:
                    width, height = im.size
                    if width <= height:
                        shutil.move(img, './mobile_size/')
                    else:
                        shutil.move(img, './pc_size/')
            except IOError:
                os.remove(img)  # 如果出现损坏的文件，就删除这个文件
                continue


def rename_img(your_path):
    os.chdir(your_path)
    if f"{image_prefix}0.jpg" in os.listdir():
        return
    else:
        start = 0
        for i in os.listdir():
            os.rename(i, image_prefix + str(start) + ".jpg")
            start += 1


def convert(your_path, resolution, output_name):
    # -f image2            指定输入输出文件的格式，这里为图片文件指定了 image2。一般来说 FFmpeg 会自动推断文件类型，这个选项可以忽略。
    # -framerate 1         设置视频流的帧率（frames per second），这里为每秒 1 张图。
    cmd = f"ffmpeg -f image2 -framerate 0.3 -i {image_prefix}%d.jpg -c:v libx264 -pix_fmt yuv420p -s  {resolution} {output_name}"
    os.system(cmd)
    time.sleep(.1)
    now = str(datetime.date(datetime.now()))
    shutil.copyfile(output_name, f'../{now}{output_name}')


def work(folder):
    rename_img(folder)
    os.chdir(folder)
    convert(folder, '2000*3000', "1_dream.mp4")


def run(p):
    # 顺序： 粗略去除小文件， 分组，命名，转化，合并。
    delete_stuff(p, 50)
    make_group(p)

    rename_img('./pc_size')
    convert('./pc_size', '3000*2000', "pc.mp4")
    os.chdir('../')

    time.sleep(2)   # 稍作停歇。
    rename_img('./mobile_size')
    convert('./mobile_size', '2000*3000', "phone.mp4")


if __name__ == '__main__':
    """ 使用：
    1. [必选] 传入文件路径
    2. [可选] 修改图片的前缀，在此文件的顶部。
    3. [可选] 进入文件路径查看视频
    """

    p = r'E:\爬虫结果\douban\豆瓣话题_你理想的工作间是什么样子的'

    # run(p)   # 1. 对一个文件夹按照长宽分类，然后处理
    work(p)  # 2. 只是想对已经已经处理好的文件夹进行合成











