import logging

# logging settings

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name) -%(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
    
)


logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a +b
    logger.debug(f"Adding {a} + {b}", result)
    return result

def subtract(a, b):
    result = a-b
    logger.debug(f"Subtracting {a} - {b}", result)
    return result

def multiply(a, b):
    result = a-b
    logger.debug(f"Multiply {a} - {b}", result)
    return result


    
