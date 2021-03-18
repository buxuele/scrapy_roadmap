import os


def delete_stuff(path, file_size):
    os.chdir(path)
    ret = os.listdir()
    print("Origin files nums are: ", len(ret))
    for x in ret:
        size = os.path.getsize(x) // 1024  # 单位是 kb
        if size < file_size:
            os.remove(x)
    print("This is end, and file nums are:  ", len(os.listdir()))


if __name__ == '__main__':
    my_path = r"E:\爬虫结果\图片\000"
    delete_stuff(my_path, 200)    # 传入文件路径，文件大小的阈值 单位是 kb
