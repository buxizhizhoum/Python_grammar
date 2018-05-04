#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
yield from 的主要功能是打开双向通道， 把最外层的调用方与最内层
的子生成器连接起来， 这样二者可以直接发送和产出值， 还可以直接传
入异常， 而不用在位于中间的协程中添加大量处理异常的样板代码。 有
了这个结构， 协程可以通过以前不可能的方式委托职责。
"""

# def gen_0():
#     for ch in "ABC":
#         yield ch
#
#     for item in range(10):
#         yield item
#
#
# def gen_1():
#     yield from "ABC"
#
#     yield from range(10)


from collections import namedtuple
Result = namedtuple('Result', 'count average')


# 子生成器
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)


# 委派生成器
def grouper(results, key):
    while True:
        # print("while loop")
        # 这个yield from 打通了子生成器averager和调用方group
        # 在此处，调用者可以直接把值发给子生成器，子生成器再将产出值发给调用者
        # 子生成器返回后，解释器会抛出StopIteration，并把返回值附加到异常对象
        # 上，此时委派生成器会恢复。
        results[key] = yield from averager()
        # print("results[key]: {}".format(results[key]))


# 客户端代码， 即调用方
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)  # 重要！
    print(results)  # 如果要调试， 去掉注释
    report(results)


# 输出报告
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(
              result.count, group, result.average, unit))


data = {
    'girls;kg': [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m': [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46]
}


if __name__ == "__main__":
    # gen = gen_0()
    # print(list(gen))
    #
    # gen_1 = gen_1()
    # print(list(gen_1))

# if __name__ == '__main__':
    main(data)
