def sum(a, b):
    print("Hey I a summing")
    c = a + b
    global z # Please modify global z
    z = 0
    return c

z = 3
print(sum(3, 12))
print(z)