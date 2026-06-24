'''
fibonacci series:   0 1 1 2 3 5 8 13 ...
index:              0 1 2 3 4 5 6 7  ...

fib(0) = 0
fib(1) = 1
fib(2) = fib(1) + fib(0) = 1
fib(3) = fib(2) + fib(1) = 1
fib(4) = fib(3) + fib(2) = 1
fib(n) = fib(n-1) + fib(n-2)
'''

def fib(n):
    # base case of recursion
    if(n==0 or n==1):
        return n
    return fib(n-1) + fib(n-2)

print(fib(6))
