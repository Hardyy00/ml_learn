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


logger = logging.
