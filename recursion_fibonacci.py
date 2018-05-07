#!/usr/bin/python
# -*- coding: utf-8 -*-
import functools
import time
from decorator import timeit


@timeit
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# this decorator will cache the least recently used result
@functools.lru_cache()  # least recently used cache
@timeit
def fibonacci_1(n):
    if n < 2:
        return n
    else:
        return fibonacci_1(n-1) + fibonacci_1(n-2)


def fibonacci_2():
    """
    from fluent python, chapter iterator
    :return:
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    # tmp = fibonacci(10)
    t0 = time.time()
    print(fibonacci(10))
    t1 = time.time()
    print(fibonacci_1(10))
    t2 = time.time()

    print("time no cache consumed: %s" % (t1 - t0))
    print("time cache consumed: %s" % (t2 - t1))

    fib = fibonacci_2()
    for i in range(10):
        print(next(fib))
