#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import functools


def timeit(fun):
    @functools.wraps(fun)  # copy the property from fun to timeit
    def inner_fun(*args, **kwargs):
        """
        function
        :param args:
        :param kwargs:
        :return:
        """
        t0 = time.time()
        res = fun(*args, **kwargs)
        t1 = time.time()
        print("time_consumed: %s, args: %s" % ((t1 - t0), args))
        return res
    return inner_fun  # 返回内部函数，取代被装饰的函数


@timeit
def sleep(seconds):
    time.sleep(seconds)


def sleep_1(seconds):
    time.sleep(seconds)


if __name__ == "__main__":
    sleep(1)

    # this is a equivalence type of @ grammar
    sleep_1 = timeit(sleep_1)  # decorator accept a function as arg
    print(type(sleep_1))
    sleep_1(1)
