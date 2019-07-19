#!/usr/bin/env python

import threading


def thread_func(arg):
    for i in range(10):
        print("{}.{}".format(i,arg))


if __name__ == "__main__":
    t1 = threading.Thread(target=thread_func, args=("First Thread",))
    t2 = threading.Thread(target=thread_func, args=("Second Thread",))
    

    t1.start()
    t2.start()

    t1.join()
    t2.join()
