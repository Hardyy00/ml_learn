from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    
    time.sleep(1)
    return f"Square : {number * number}"


with ProcessPoolExecutor(max_workers=3) as executor:
    
    