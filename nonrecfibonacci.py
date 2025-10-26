"""
File: nonrecfibonacci.py
Description: Group Project 1, Non-recursive fibonacci program
"""

import time

#Non recursively iterates over 
def main():
    start = time.time()  

    a, b = 0, 1
    for i in range(40):
        #print(a)
        a, b = b, a + b

    end = time.time()  

    runtime = (end - start) * 1000
    
    f = open("fibOutput.txt", "w")
    f.write("Non-recursive fibonacci Runtime:\n")
    f.write(runtime)
    f.close()


main()
