from logger import logging

def add(a, b):
    logging.debug("The adding operation if taking place")
    return a + b


logging.debug("This addition function is called")
add(10, 15)