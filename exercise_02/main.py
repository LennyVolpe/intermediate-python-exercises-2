"""Sources: https://www.geeksforgeeks.org/python-program-for-n-th-fibonacci-number
            https://pynative.com/python-get-execution-time-of-program/ """
import random
import time

n = random.randint(15,35)

def fib(n):
    start = time.time()
    if n == 0:
        return 0
    elif n== 1:        
        return 1
    elif n ==2:
        
        return 1
    else:
        n = fib(n-1) + fib (n-2)
        
        return n

start = time.time()
print("fib("+ str(n) +") = " + str(fib(n)))   
print("fib("+ str(n) +") = " + str(time.time() - start) + " seconds") 