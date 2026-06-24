# Part 1

def fibonacchi(n, curr=0, next=1, count=0):
    if n-count == 0:
        print()
        return
    print(curr, end=" ")
    fibonacchi(n, next, curr+next, count+1)

# def print_fib(n):
#     def fib(n):
#         if n==0 or n==1:
#             return n
#         return fib(n-1) + fib(n-2)
#     res = " ".join(str(fib(i)) for i in range(n))
#     print(res)

fibonacchi(10)
# print_fib(10)

# Part 2

def safe_devide(a, b):
    if (b == 0):
        return f"Denominator can not be zero!!"
    return a/b

print(safe_devide(10, 0))
print(safe_devide(10, 2))

# Part 3 

from my_utils import is_even
num = -2
if(is_even(num)):
    print(f"{num} is a even number.")
else: 
    print(f"{num} is not a even number")