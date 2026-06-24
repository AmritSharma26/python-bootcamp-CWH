def sum(a, b):
    # a and b are local variables
    c = a + b
    # print(z)
    z = 1 # creates a local variable called z, which destoryed after this function returns
    return c

def greet():
    z = 32 # Local variable
    print("Hello")

z = 8 # z is a global variable
print(sum(4, 6))
