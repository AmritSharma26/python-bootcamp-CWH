# Part 1
def increment():
    counter = 0
    counter += 1
    print(counter)

increment()
increment()

# Part 2
def multiply(a, b):
    '''
    This function mutiply two numbers
    arguments: 
        a (int or float): first number.
        b (int or float): second number.
    returns: 
        int or float: product of a and b
    '''
    return a*b

print(multiply(5, 3))
help(multiply)