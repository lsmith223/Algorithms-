"""
File: nonrecfibonacci.py
Description: Group Project 1, Non-recursive fibonacci program
"""

import time

#Non recursively iterates over 
def nonRecFib(n): 
    a, b = 0, 1
    for i in range(n):
        #print(a)
        a, b = b, a + b
    return a 

start = time.time() 
nonRecFib(40)
end = time.time()
runtime = (end - start) * 1000
f = open("fibOutput.txt", "w")
f.write(f"Non-recursive fibonacci Runtime:\n")
f.write(f"runtime = {runtime} milliseconds")
f.close()

