import threading
import time


def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number : {i}")
        

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter : {letter}")
        
   
t = time.time()
print_numbers()
print_letter()   
finished_time = time.time() - t
print(finished_time)             
        
        
        
        