# Written by Lauren Smith

import time
# pos (position) just represents what current n we are calculating in the fibonacci sequence  
pos = -1
runtime = 0 
executionTime = 0

# takes in a positive integer n and applies recursive fibonacci, returning the fibonacci for each n and the number of additions a(n) performed on n 
def recurFibonacci(n):
    runtime = 0 
    # basecase scenerios for fib(0) and fib(1)
    if n == 0 or n == 1:
        return 1, 0
    else: 
        fib1, an1 = recurFibonacci(n-1)
        fib2, an2 = recurFibonacci(n-2)
        runtime = an1 + an2 + 1 
        return(fib1 + fib2, runtime) 

# opens the file for outputting our data and prepares a column with names 
f = open("fibOutput.txt", "w")
f.write("Pos  Fibonacci  Runtime\n")

# calculates fibonacci for input 0-50, and displays the position(n), the fibonacci, and the runtime for each n 
for n in range(51):
    pos = pos + 1
    if n == 40:
        # finds execution time of n = 40 and outputs it
        start = time.time()
        fibValue, runtime = recurFibonacci(n)
        end = time.time()
        executionTime = (end - start) * 1000
        f.write(f"Execution time for n={pos}: {executionTime} milliseconds\n")
    else: 
        fibValue, runtime = recurFibonacci(n)
    f.write(f"{pos:4}  {fibValue:9}  {runtime:7}\n")

# closing file for writing, we are done writing 
f.close()

# reopen the file for reading only, read it, then output the file contents to the console 
f = open("fibOutput.txt", "r")
print(f.read())
f.close()