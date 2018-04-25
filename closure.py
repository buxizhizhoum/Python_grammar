#!/usr/bin/python
# -*- coding: utf-8 -*-


def make_averager():
    """
    version for python 2
    :return:
    """
    # 如果sum_all是数字等不可变对象，在内层函数sum_all进行更新时
    # 实际上会创建一个新的局部变量然后赋值，这个时候sum_all就不是自由变量了，
    # 内层函数也就无法访问，count同理
    sum_all = [0]
    count = [0]

    def averager(new_value):
        sum_all[0] += new_value
        count[0] += 1
        return sum_all[0]/count[0]
    return averager


def make_averager_1():
    """
    version for python 3
    :return:
    """
    sum_all = 0
    count = 0

    def averager(new_value):
        # nonlocal关键字指明sum_all和count不是局部变量，
        # 将其标记为自由变量，这样就可以在内层函数中进行更新。
        nonlocal sum_all, count
        sum_all += new_value
        count += 1
        return sum_all/count
    return averager


if __name__ == "__main__":
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))

    avg1 = make_averager_1()
    print(avg1(10))
    print(avg1(11))
    print(avg1(12))
