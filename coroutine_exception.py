#!/usr/bin/python
# -*- coding: utf-8 -*-


class DemoException(Exception):
    pass


def demo_exc_handling():
    print("coroutine started.")
    while True:
        try:
            x = yield

        except DemoException:
            print("DemoException captured, continuing")

        else:
            print("coroutine received {!r}.".format(x))

    raise RuntimeError("This line should never run.")


if __name__ == "__main__":
    gen = demo_exc_handling()
    next(gen)
    gen.send(10)
    gen.send(20)
    gen.throw(DemoException)
    gen.send(30)
    gen.throw(ZeroDivisionError)
    gen.send(40)
    gen.close()

