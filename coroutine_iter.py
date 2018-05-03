#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
learning codes when read book "fluent python" by Luciano Ramalho.
"""
from functools import wraps
from inspect import getgeneratorstate


def coroutine(func):
    @wraps(func)  # keep the info of original function
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


def coroutine_0():
    print("started")
    x = yield
    print("received: {}".format(x))
    y = yield
    print("received: {}".format(y))


def coroutine_1(a):
    print("started: {}".format(a))
    x = yield a
    print("received: {}".format(x))
    y = yield a + x
    print("received: {}".format(y))


@coroutine
def coroutine_2(a):
    print("started: {}".format(a))
    x = yield a
    print("received: {}".format(x))
    y = yield a + x
    print("received: {}".format(y))


if __name__ == "__main__":
    gen = coroutine_0()
    next(gen)
    gen.send(10)
    # gen.send(20)
    # gen.send(30)
    print("-" * 60)
    gen_1 = coroutine_1(1)
    print("generator status: {}".format(getgeneratorstate(gen_1)))
    next(gen_1)
    print("generator status: {}".format(getgeneratorstate(gen_1)))
    gen_1.send(11)
    print("generator status: {}".format(getgeneratorstate(gen_1)))
    # gen_1.send(12)
    # print("generator status: {}".format(getgeneratorstate(gen_1)))

    print("-" * 60)
    gen_2 = coroutine_2(10)
    gen_2.send(20)
    gen_2.send(30)
