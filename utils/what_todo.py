# -*- coding: utf-8 -*-
# author: fanchuang
# DateTime:2021/2/17 0017 18:28 
# contact: fanchuangwater@gmail.com
# about:

import os
import time
import shutil
from datetime import datetime
from openpyxl import load_workbook

# !以后需要更新这个文件 todo
"""  待办清单


1. 自动生成每天的固定任务。随时可以添加临时任务。 
2. 最好是能定时执行，比如开机5分钟后，执行。
3. 写个文件来自动生成每日的todo任务。保存到桌面。格式最好是 excel.
4. 如果我已经有了一个文件模板，那么我直接在这个模板文件中新建一个工作表即可。
"""


def make_name():
    a = datetime.date(datetime.now())
    # print(str(a))
    return str(a)


def parse_text():
    raw_data = """温习笔记，也可以适当整理。比如每天背单词。
阅读源码, 目前定为每天半个小时。
完成之前的Todo。每天5条。尽力而为吧。
尽量少抽烟。每半个小时一根烟。目前是这样的。
每天花办小时来整理房间。
每天晚上临睡前读书
远离B站，远离美剧。使用知乎来代替原来的消遣。
每周或是每2周，出一趟远门，开阔一下视野，刺激一下野心。"""
    return raw_data.split('\n')


# 这部分我觉得不需要了。shutil 这一块还是需要再看看的。很强大啊。
def move_file(filename):
    start = os.path.abspath(filename)
    end = r"C:\Users\Administrator\Desktop" + '\\' + filename
    # shutil.move(start, end)
    # 如果目的地存在同名文件，怎么办呢。删除原文件吗。应该是始终更新同一个文件。
    shutil.copyfile(start, end)


def generate_tasks():
    # 1. 准备工作，打开关闭等  始终更新同一个文件。

    excel_name = r'C:\Users\Administrator\Desktop\Small_Plan.xlsx'
    sheet_name = make_name()

    wb = load_workbook(excel_name)
    if sheet_name not in wb.sheetnames:
        working_sheet = wb.create_sheet(sheet_name, 0)  # 添加到开头，很机智啊。
    else:
        working_sheet = wb[sheet_name]

    # 2. 写入文件, 表头不用管了，因为我到时候会写一个模板出来的。
    data = parse_text()

    # box = working_sheet['A'][1:]  # 此时的 box 是空的。

    for index, things in enumerate(data):
        print(things)
        # working_sheet[f'A{index+10}'] = index+1   # 序号
        # working_sheet[f'B{index+10}'] = str(datetime.now()).split(".")[0]  # 时间
        working_sheet[f'C{index + 10}'] = things

    wb.save(excel_name)


# todo 这一块确实是做不了。因为我怀疑是这个模板本身有问题的。
# todo 除非是能生成数据，然后把对应的格式都套上去。这一块以后再看看吧。
def copy_sheet():
    template_excel = r'E:\mm.xlsx'
    final_excel = f'C:\\Users\Administrator\Desktop\\{make_name()}.xlsx'
    shutil.copyfile(template_excel, final_excel)

    """
    1. 复制一个工作表，打开文件后总是报错
    2. 直接复制一个文件呢。然后在文件的基础上进行修改。粗暴，其实是退而求其次。
    """
    data = parse_text()

    wb = load_workbook(final_excel)
    working_sheet = wb['To Do List 模板']

    for index, things in enumerate(data):
        # working_sheet[f'A{index + 10}'] = index + 1  # 序号
        # working_sheet[f'B{index + 10}'] = str(datetime.now()).split(".")[0]  # 时间
        pos = f'C{index + 6}'
        working_sheet[pos] = things.strip()

    wb.save(final_excel)


if __name__ == '__main__':
    generate_tasks()
    # copy_sheet()
