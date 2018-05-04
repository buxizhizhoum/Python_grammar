#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import itertools
import sys


# @asyncio.coroutine
async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for ch in itertools.cycle("-\|/"):
        status = ch + " " + msg
        write(status)
        flush()
        write("\x08" * len(status))
        # if add this line, there will be the effect that cursor goes back to the start of line and blink
        # flush()
        asyncio.sleep(0.1)
        # time.sleep(0.1)  # will block
        try:
            # yield from asyncio.sleep(.1)
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    # write(" " * len(status) + "\x08" * len(status))


# @asyncio.coroutine
async def slow_func():
    # yield from asyncio.sleep(3)
    await asyncio.sleep(3)
    return 1


# @asyncio.coroutine
async def supervisor():
    # spinner = asyncio.async(spin("running..."))
    spinner = asyncio.ensure_future(spin("running..."))
    print("spin: {}", spinner)
    # result = yield from slow_func()
    result = await slow_func()
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print("Answer:", result)


if __name__ == "__main__":
    # spin("test")
    main()

