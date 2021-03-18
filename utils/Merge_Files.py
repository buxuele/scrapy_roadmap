# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/2/28 0028 15:57 
# contact: fanchuangwater@gmail.com
# about: 把一些图片合并到同一个文件夹


import os
import shutil
import pathlib


origin_path = 'E:\爬虫结果\图片\RTX_2070'
target_path = 'E:\爬虫结果\图片\\000'


def move_files():
    for folder in os.listdir(origin_path):
        child_path = os.path.join(origin_path, folder)
        for img in os.listdir(child_path):
            img_path = os.path.join(child_path, img)
            shutil.copyfile(img_path, f'{target_path}/{img}')


# 把一个文件夹中的文件全部重命名, 新旧文件路径都使用绝对路径，都使用 os.path.join() 最安全。
def rename_folder():
    t = 0
    for i in os.listdir(origin_path):
        old_path = os.path.join(origin_path, i)
        new_path = os.path.join(origin_path, str(t))
        print(old_path)
        print(new_path)
        print()
        os.rename(old_path, new_path)
        t += 1

# rename_folder()
move_files()




