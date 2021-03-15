import time


# 这个是常用的时间显示方式
def chinese_time():
    # print(datetime.now())         # 2020-12-31 19:40:58.431721

    pretty_time = time.strftime("%Y-%m-%d %H:%M:%S")
    # print(pretty_time)          # 2020-12-31 19:40:58
    return pretty_time


# 参考 ： https://blog.csdn.net/qq_40438165/article/details/107208086
def timer(func):
    def func_wrapper(*args, **kwargs):
        t1 = time.time()
        ret = func(*args, **kwargs)
        cost = time.time() - t1
        print(f"Cost: {cost} seconds on: {func.__name__}")
        return ret
    return func_wrapper


@timer
def print_nums():
    for x in range(1000000):
        print(x + 1)


if __name__ == '__main__':
    print_nums()        # Cost: 3.04231333732605 seconds on print_nums

