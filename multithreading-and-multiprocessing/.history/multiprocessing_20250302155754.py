import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square : {i*i}")
        
        
def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube : {i*i*i}")
        
        
## create 2 processes


p1 = multiprocessing.Process(target=square_numbers) 
p2 = multiprocessing.Process(target=cube_numbers)

## start the process
p1.start()
p2.start()        


## wait for the process to finish
p1.join()
p2.join()

       

