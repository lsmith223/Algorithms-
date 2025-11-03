"""
File:CombinedFib.py
Desc: Combined file with both methods of Fibonacci calculation
Authors: DAA Group 7
"""
import time

# Non recursively iterates over
def nonRecurFib(n):

    runtime=0

    if n == 0 or n == 1:
        return 1, 0

    a, b = 0, 1
    for i in range(n):
        #print(a)
        a, b = b, a+b

    runtime=b-1 #This is the additions needed to find the answer

    return b, runtime



def nonRecurFib_Main():
    # pos (position) just represents what current n we are calculating in the fibonacci sequence
    pos = -1
    # runtime represents a(n)
    runtime = 0
    # execution time represents how long our method takes to run, in milliseconds
    executionTime = 0

    # opens the file for outputting our data and prepares a column with names
    f = open("Non_recursive_fibOutput.txt", "w")
    f.write("Pos  Fibonacci  Runtime\n")
    # calculates fibonacci for input n = 0-50, and displays the position(n), the fibonacci, and the runtime for each n
    for n in range(51):
        pos = pos + 1
        if n == 40:
            # finds execution time of n = 40 only and outputs it
            start = time.time()
            fibValue, runtime = nonRecurFib(n)
            end = time.time()
            executionTime = (end - start) * 1000
            f.write(f"Execution time for n={pos}: {executionTime} milliseconds\n")
        else:
            fibValue, runtime = nonRecurFib(n)
        f.write(f"{pos:4}  {fibValue:9}  {runtime:7}\n")  # the :num afterward creates spaces between the numbers

    # closing file for writing, we are done writing
    f.close()

    # reopen the file for reading only, read it, then output the file contents to the console & re-close file
    f = open("Non_recursive_fibOutput.txt","r")
    print(f.read())

    f.close()











# takes in a positive integer n and applies recursive fibonacci, returning the fibonacci for each n and the number of additions a(n) performed on n 
def recurFibonacci(n):
    runtime = 0 
    # basecase scenerios for fib(0) and fib(1)
    if n == 0 or n == 1:
        return 1, 0
    else: #fib1 and fib2 broken up to make the program more efficient when returning the runtime 
        fib1, an1 = recurFibonacci(n-1)
        fib2, an2 = recurFibonacci(n-2)
        runtime = an1 + an2 + 1 # equivalent to a(n) = n+1 (a(n) = (n/2 + n/2 + 1)) --> we know 1/2 + 1/2 = 1, so = n
        return(fib1 + fib2, runtime) #equiv to recurFibonacci(n-1) + recurFibonacci(n-2), a(n)


def recurFib_Main():
    # pos (position) just represents what current n we are calculating in the fibonacci sequence
    pos = -1
    # runtime represents a(n)
    runtime = 0
    # execution time represents how long our method takes to run, in milliseconds
    executionTime = 0

    # opens the file for outputting our data and prepares a column with names
    f = open("fibOutput.txt", "w")
    f.write("Pos  Fibonacci  Runtime\n")
    # calculates fibonacci for input n = 0-50, and displays the position(n), the fibonacci, and the runtime for each n
    for n in range(51):
        pos = pos + 1
        if n == 40:
            # finds execution time of n = 40 only and outputs it
            start = time.time()
            fibValue, runtime = recurFibonacci(n)
            end = time.time()
            executionTime = (end - start) * 1000
            f.write(f"Execution time for n={pos}: {executionTime} milliseconds\n")
        else:
            fibValue, runtime = recurFibonacci(n)
        f.write(f"{pos:4}  {fibValue:9}  {runtime:7}\n") # the :num afterward creates spaces between the numbers

    # closing file for writing, we are done writing
    f.close()

    # reopen the file for reading only, read it, then output the file contents to the console & re-close file
    f = open("fibOutput.txt", "r")
    print(f.read())

    f.close()

nonRecurFib_Main()
#print(nonRecurFib(10))
recurFib_Main()
