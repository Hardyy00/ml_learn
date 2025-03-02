## Multithreading with thread pool executor


from concurrent.futures import ThreadPoolExecutor
import time


def print_number(number):
    time.sleep(1)