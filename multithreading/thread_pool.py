#!/usr/bin/env python

import threading
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
import time
import logging


class Task:
    def __init__(self, num):
        self.num = num

    def __call__(self):
        logging.warning("Start {}".format(self.num))
        time.sleep(0.1)
        self.square = self.num * self.num
        logging.warning("Done {}".format(self.num))
    def __str__(self):
        return "num={}, square={}".format(self.num,self.square)

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%H:%M:%S')

    executor = ThreadPoolExecutor()
    tasks = []
    for i in range(100):
        logging.info("{}".format(i))
        t = Task(i)
        tasks.append(t)
        t.future = executor.submit(t)
    for t in tasks:
        t.future.result()
        logging.warning(t)
    logging.warning("All done")
