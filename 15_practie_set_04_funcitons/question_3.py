# Part 1

add = lambda num1, num2: num1+num2
print(add(5, 3))

# Part 2

my_list = [1, 2, 3, 4, 5]
square = lambda nums: nums**2
sq_square = list(map(square, my_list))
print(sq_square)