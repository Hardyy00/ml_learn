'''
Real-World Example : Multiprocessing for CPU-bound Tasks

Scenario : Factorial Calculation

Factorial Calculation especially for large numbers, involve significant computational work. Multiprocessing can be used to distribute the workload across multiple CPU cores, improving performance

'''


import multiprocessing
import math
import sys
import time

## increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)


## function to compute factorial of a given number

def compute_factorial(number):
    print(f"Computing Factorial of {number}")
    result = math.factorial(number)
    p


