def add(a, b, plus=0): # parameters
    x = a + b + plus
    return x

c = add(3, 5) # arguments
print(c)
d = add(3, 5, 2) # arguments
print(d)

c1 = add(b=5, a=3) # keyword arguments
print(c1)